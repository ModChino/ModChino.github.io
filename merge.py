# -*- coding: utf-8 -*-
"""合并多个上游 Tracker 列表，生成多种格式的发布文件。

原版问题修复：
- write_file 末尾判断误用 len(all)，best 文件会多出尾部分隔符 -> 改为按数据本身长度判断
- set() 去重打乱顺序 -> 改为保序去重
- 依赖 wget 下载 -> 统一用 requests
- 不再残留 all.txt / best.txt / AT_*.txt / tracker.txt 临时文件
"""
import os

import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
}

SOURCES = {
    "xiu2": "https://raw.githubusercontent.com/XIU2/TrackersListCollection/master/all.txt",
    "xiu2_best": "https://raw.githubusercontent.com/XIU2/TrackersListCollection/master/best.txt",
    "itzmx": "http://github.itzmx.com/1265578519/OpenTracker/master/tracker.txt",
    "anime": "https://raw.githubusercontent.com/DeSireFire/animeTrackerList/master/AT_all.txt",
    "anime_best": "https://raw.githubusercontent.com/DeSireFire/animeTrackerList/master/AT_best.txt",
}

LOCAL_FILES = ["sukebei.txt", "PBH-BTN_Trunker.txt"]

# (格式, 输出路径, 用全量还是 best)
OUTPUTS = [
    ("default", "./default_all.txt", "all"),
    ("default", "./best/best_default_all.txt", "best"),
    ("line", "./SpaceLine_All.txt", "all"),
    ("line", "./best/Best_SpaceLine_All.txt", "best"),
    ("aria2", "./aria2_all.txt", "all"),
    ("aria2", "./best/best_aria2_all.txt", "best"),
]


def fetch(url):
    resp = requests.get(url, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    return resp.text


def read_local(path):
    with open(path, "r", encoding="utf-8") as fp:
        return fp.read()


def clean_lines(text):
    """按行去除首尾空白，丢弃空行。"""
    return [line.strip() for line in text.splitlines() if line.strip()]


def dedupe(items):
    """保序去重。"""
    seen = set()
    out = []
    for item in items:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out


def build_list(use_best):
    data = []
    data += clean_lines(fetch(SOURCES["xiu2_best" if use_best else "xiu2"]))
    data += clean_lines(fetch(SOURCES["itzmx"]))
    data += clean_lines(fetch(SOURCES["anime_best" if use_best else "anime"]))
    for path in LOCAL_FILES:
        data += clean_lines(read_local(path))
    return dedupe(data)


def render(items, fmt):
    if fmt == "default":
        return "\n".join(items)
    if fmt == "line":
        return "\n\n".join(items)
    if fmt == "aria2":
        return ",".join(items)
    raise ValueError(f"unknown format: {fmt}")


def main():
    all_list = build_list(False)
    best_list = build_list(True)

    for fmt, path, which in OUTPUTS:
        items = all_list if which == "all" else best_list
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(render(items, fmt))
        print(f"wrote {path}: {len(items)} trackers")


if __name__ == "__main__":
    main()
