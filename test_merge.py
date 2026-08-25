# -*- coding: utf-8 -*-
"""merge.py 最小自测：不联网，验证去重、保序、格式渲染与文件输出。"""
import os
import tempfile

import merge


def test_clean_lines():
    assert merge.clean_lines("  a\r\n\n  b  \n") == ["a", "b"], "应去除空白并丢弃空行"


def test_dedupe_keeps_order():
    assert merge.dedupe(["b", "a", "b", "c", "a"]) == ["b", "a", "c"], "应保序去重"


def test_render_formats():
    items = ["udp://a", "https://b"]
    assert merge.render(items, "default") == "udp://a\nhttps://b"
    assert merge.render(items, "line") == "udp://a\n\nhttps://b"
    assert merge.render(items, "aria2") == "udp://a,https://b"


def test_build_list_and_output():
    # 伪造上游与本地数据，避免网络
    fake = {
        merge.SOURCES["xiu2"]: "udp://x1\nudp://x2\n",
        merge.SOURCES["xiu2_best"]: "udp://x1\n",
        merge.SOURCES["itzmx"]: "udp://i1\nudp://i1\n",  # 含重复，应被去重
        merge.SOURCES["anime"]: "udp://a1\n",
        merge.SOURCES["anime_best"]: "udp://a1\nudp://a2\n",
    }
    merge.fetch = lambda url: fake[url]
    merge.read_local = lambda path: "udp://local\n"

    all_list = merge.build_list(False)
    best_list = merge.build_list(True)
    assert all_list == ["udp://x1", "udp://x2", "udp://i1", "udp://a1", "udp://local"], all_list
    assert best_list == ["udp://x1", "udp://i1", "udp://a1", "udp://a2", "udp://local"], best_list

    # 用临时目录模拟输出
    tmp = tempfile.mkdtemp()
    old_outputs = merge.OUTPUTS
    old_cwd = os.getcwd()
    try:
        os.chdir(tmp)
        merge.OUTPUTS = [
            ("default", "./default_all.txt", "all"),
            ("line", "./spaceline.txt", "best"),
            ("aria2", "./aria2.txt", "all"),
        ]
        merge.main()
        with open("./default_all.txt", encoding="utf-8") as f:
            assert f.read() == "udp://x1\nudp://x2\nudp://i1\nudp://a1\nudp://local"
        with open("./spaceline.txt", encoding="utf-8") as f:
            assert f.read() == "udp://x1\n\nudp://i1\n\nudp://a1\n\nudp://a2\n\nudp://local"
        with open("./aria2.txt", encoding="utf-8") as f:
            assert f.read() == "udp://x1,udp://x2,udp://i1,udp://a1,udp://local"
    finally:
        merge.OUTPUTS = old_outputs
        os.chdir(old_cwd)


if __name__ == "__main__":
    test_clean_lines()
    test_dedupe_keeps_order()
    test_render_formats()
    test_build_list_and_output()
    print("test_merge.py: all tests passed")