# ModChino Tracker 合并发布站

一个由 GitHub Actions 每日自动运行的 BitTorrent Tracker 合并去重发布站，托管于 GitHub Pages。

## 简介

本项目将多个上游 Tracker 列表聚合、去重，并发布为多种格式的文件，供 BT 下载客户端（qBittorrent、aria2、transmission 等）直接订阅使用。

**内置上游来源（自动同步）：**

- [XIU2/TrackersListCollection](https://github.com/XIU2/TrackersListCollection)
- [itzmx OpenTracker](http://github.itzmx.com/1265578519/OpenTracker/master/tracker.txt)
- [DeSireFire/animeTrackerList](https://github.com/DeSireFire/animeTrackerList)
- 本地补充列表：`sukebei.txt`、`PBH-BTN_Trunker.txt`

**更新机制：** 每日 **14:00 UTC** 由 GitHub Actions 自动触发合并脚本（`merge.py`），对上表来源进行拉取、合并与去重，随后发布到本项目域名下。

## 全部产物下载

**ALL 链接（完整列表）：**

| 格式 | 链接 |
| --- | --- |
| 默认（每行一个） | https://modchino.github.io/default_all.txt |
| aria2 用（逗号分隔） | https://modchino.github.io/aria2_all.txt |
| 空行切割方式 | https://modchino.github.io/SpaceLine_All.txt |

**Best 链接（精选列表）：**

| 格式 | 链接 |
| --- | --- |
| 默认（每行一个） | https://modchino.github.io/best/best_default_all.txt |
| aria2 用（逗号分隔） | https://modchino.github.io/best/best_aria2_all.txt |
| 空行切割方式 | https://modchino.github.io/best/Best_SpaceLine_All.txt |

## 备用地址

主站不可用时，可使用备用地址：

- https://trackers.chino.one/

## 开发与自测

本地重新生成产物：

```bash
pip install -r requirements.txt
python merge.py
```

运行自测：

```bash
python test_merge.py
```

## 致谢

向以下上游项目与维护者致谢，本项目仅做聚合去重，Tracker 数据版权归相应来源所有：

- [XIU2/TrackersListCollection](https://github.com/XIU2/TrackersListCollection)
- [itzmx OpenTracker](http://github.itzmx.com/1265578519/OpenTracker/master/tracker.txt)
- [DeSireFire/animeTrackerList](https://github.com/DeSireFire/animeTrackerList)

## 免责声明

本项目仅提供 BT Tracker 聚合服务，不包含任何版权内容。请依法合规使用。