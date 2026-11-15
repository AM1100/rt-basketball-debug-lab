# 篮球追踪故障排查练习

对应《技术选型与原型》任务三。项目读取视频，生成带标记的视频和逐帧 CSV。篮球完全不可见后，程序仍把最后一次检测到的位置标成当前位置。请复现、定位并修复，再检查正常可见和重新出现阶段。

## 复现

在 Ubuntu 或 WSL 的仓库根目录执行以下命令。使用 Python 3.10–3.13。

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m basketball --demo --output-dir runs/before
```

`--demo` 生成的合成视频含 96 帧，0–31 帧可见，32–63 帧完全遮挡，64–95 帧重新出现。正式验收统一使用[飞书培训文档中任务二的实拍视频](https://gcnhkq914dqv.feishu.cn/wiki/FRLKwEGQmiAteqkJHLUc8nU2ncd#doxcnpqrTZQIZU7CzLTJQpk3Ypg)。篮球短暂完全出画，随后重新进入画面。下载为 `samples/basketball.mp4` 后运行：

```bash
python -m basketball --input samples/basketball.mp4 --output-dir runs/before
```

`tracking.csv` 记录帧号（从 0 开始）、视频时间（秒）、追踪状态、中心坐标和半径。`annotated.mp4` 便于核对画面。可见时应标出当前球的位置，丢失时应让使用者分辨当前位置不可用。

在自己的仓库分支完成修复。用同一段视频复测，把修复后输出写到 `runs/after`，保留两个目录用于对照。按飞书文档的任务三要求提交分支链接、复现证据、定位依据和复测结果。
