# Manim 渲染选项参考

完整的 Manim 渲染质量、格式和配置选项说明。

## 质量设置

### 预设质量级别

| 级别 | 分辨率 | 帧率 | 像素数 | 用途 |
|------|--------|------|--------|------|
| **low** (`-ql`) | 854x480 | 15 fps | ~410K | 快速预览、测试 |
| **medium** (`-qm`) | 1280x720 | 30 fps | ~920K | 标准输出 |
| **high** (`-qh`) | 1920x1080 | 30 fps | ~2.1M | 高质量视频 |
| **4k** (`-qk`) | 3840x2160 | 60 fps | ~8.3M | 超高清输出 |

### 使用建议

- **开发/调试**: 使用 `low` 质量，快速迭代
- **日常使用**: 使用 `medium` 质量，平衡质量和速度
- **最终输出**: 使用 `high` 或 `4k` 质量

### 自定义质量

在代码中自定义配置:

```python
from manim import *

config.quality = "medium_quality"
config.pixel_height = 720
config.pixel_width = 1280
config.frame_rate = 30

class MyScene(Scene):
    def construct(self):
        # ...
```

或使用 `config.dict()`:

```python
config.background_color = WHITE
config.max_files_cached = 100
```

## 输出格式

### MP4 视频（默认）

**优点**: 压缩率高、兼容性好、支持透明度

```bash
manim -qm scene.py MyScene
```

输出: `manim_outputs/scene_<timestamp>/output/medium/MyScene.mp4`

### GIF 动图

**优点**: 无需播放器、适合社交媒体

**缺点**: 文件大、色彩有限（256 色）

```bash
# 方法 1: 直接导出
manim -qm scene.py MyScene --format gif

# 方法 2: 使用 ffmpeg 转换
ffmpeg -i MyScene.mp4 MyScene.gif
```

### PNG 序列

**优点**: 无损质量、便于后期处理

```bash
manim -qm scene.py MyScene --format png
```

输出: `manim_outputs/scene_<timestamp>/output/medium/MyScene/*.png`

## 输出目录结构

```
manim_outputs/
└── <scene_name>_<timestamp>/
    ├── scene.py                   # 场景源代码
    ├── config.json                # 生成配置
    ├── output/
    │   └── <quality>/             # 按质量分目录
    │       └── <SceneName>.mp4
    ├── logs/
    │   └── build.log              # 编译日志
    ├── thumbnails/                # GIF 缩略图
    └── README.md                  # 输出说明
```

## 渲染选项

### 命令行选项

```bash
manim [OPTIONS] INPUT_FILE SCENE_NAME
```

| 选项 | 说明 |
|------|------|
| `-ql`, `-qm`, `-qh`, `-qk` | 质量级别 |
| `-o`, `--output_file` | 指定输出文件名 |
| `--output_dir` | 指定输出目录 |
| `--format` | 输出格式 (mp4, gif, png) |
| `-s`, `--save_last_frame` | 只保存最后一帧 |
| `--transparent` | 透明背景 |
| `--background_color` | 背景颜色 |
| `-v`, `--version` | 版本信息 |
| `-h`, `--help` | 帮助信息 |

### 代码内配置

```python
from manim import *

# 全局配置
config.quality = "high_quality"
config.background_color = WHITE
config.frame_rate = 60

class MyScene(Scene):
    def construct(self):
        # 场景级配置
        self.camera.background_color = BLACK
        # ...
```

## 性能优化

### 加速渲染

1. **降低质量预览**
```bash
manim -ql scene.py MyScene  # 快速测试
```

2. **限制场景长度**
```python
class MyScene(Scene):
    def construct(self):
        # 开发时只渲染前几秒
        self.wait(1)  # 预览时渲染 1 秒
```

3. **禁用缓存清理**
```python
config.max_files_cached = 999  # 保留更多缓存
```

4. **并行渲染**
```bash
# 渲染多个场景
manim -qm scene.py Scene1 Scene2 Scene3
```

### 减小文件大小

1. **使用较低质量**
```bash
manim -ql scene.py MyScene  # smallest file
```

2. **限制帧率**
```python
config.frame_rate = 15  # 降低帧率
```

3. **使用压缩**
```bash
# 使用 ffmpeg 二次编码
ffmpeg -i input.mp4 -crf 28 output.mp4
```

## 故障排除

### 常见错误

#### 错误 1: `NameError: name 'np' is not defined`

**原因**: 未导入 numpy

**解决**:
```python
import numpy as np
```

#### 错误 2: LaTeX 渲染失败

**原因**: LaTeX 未安装或路径不正确

**解决**:
```bash
# Ubuntu/Debian
sudo apt-get install texlive-full

# macOS
brew install mactex

# 检查安装
latex --version
```

#### 错误 3: 内存不足

**原因**: 高质量渲染消耗大量内存

**解决**:
```bash
# 使用较低质量
manim -qm scene.py MyScene

# 或在代码中简化场景
config.max_files_cached = 10
```

#### 错误 4: 渲染卡住

**原因**: 无限循环或复杂计算

**解决**:
```python
# 添加超时或限制
class MyScene(Scene):
    def construct(self):
        # 使用 run_time 限制动画时长
        self.play(Create(obj), run_time=2)
```

### 调试技巧

1. **使用 `-s` 只保存最后一帧**
```bash
manim -qm -s scene.py MyScene
```

2. **从最简场景开始**
```python
class TestScene(Scene):
    def construct(self):
        self.add(Text("Hello"))  # 先测试基础功能
```

3. **检查 Manim 版本**
```bash
manim --version
```

4. **清理缓存**
```bash
rm -rf manim_outputs/
```
