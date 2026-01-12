# Manim Creator

Manim 数学动画创建插件，提供代码生成、工具函数库和编译渲染功能。

## 功能

- **manim-generator**: 将自然语言描述转换为 Manim 代码
- **manim-tools**: 可复用的 Python 工具函数库
- **manim-builder**: 编译和渲染 Manim 场景

## 安装

### 前置要求

```bash
# 安装 Manim
pip install manim

# 安装 LaTeX（可选，用于数学公式）
sudo apt-get install texlive-full  # Ubuntu/Debian
brew install mactex                 # macOS
```

### 安装插件

将此插件放置在 `plugins/manim-creator/` 目录下。

## 使用

### 快速开始

```
/manim create 绘制一个正弦函数图像
```

### 查看工具函数

```
/manim tools circle
```

### 编译场景

```
/manim build scene.py --quality high
```

## 文件管理

### 输出文件位置

使用插件时产生的文件位置：

```
项目根目录/
└── manim_outputs/               # 结构化输出目录
    └── <scene_name>_<timestamp>/
        ├── scene.py             # 场景源代码
        ├── config.json          # 生成配置
        ├── output/
        │   └── <quality>/       # 按质量分目录
        │       └── <SceneName>.mp4
        ├── logs/
        │   └── build.log        # 编译日志
        └── README.md            # 输出说明
```

### 文件类型说明

| 文件 | 位置 | 说明 | 清理 |
|------|------|------|------|
| 输出目录 | `项目根目录/manim_outputs/` | 所有编译输出 | 整体管理 |
| 场景代码 | `manim_outputs/*/scene.py` | 场景源代码 | 保留用于编辑 |
| 视频文件 | `manim_outputs/*/output/*/*.mp4` | 生成的视频 | 主要输出 |
| 配置文件 | `manim_outputs/*/config.json` | 生成配置 | 记录信息 |
| 编译日志 | `manim_outputs/*/logs/build.log` | 编译日志 | 调试用 |

### 清理命令

```bash
# 清理所有输出
rm -rf manim_outputs/

# 清理特定场景的输出
rm -rf manim_outputs/<scene_name>_*/

# 只清理视频文件（保留代码和配置）
find manim_outputs/ -name "*.mp4" -delete

# 清理日志文件
find manim_outputs/ -name "build.log" -delete
```

### 工作流产生的文件

完整工作流中产生的文件：

```
输入: /manim 绘制正弦函数
  ↓
[1] 生成代码
  → manim_outputs/sine_wave_scene_<timestamp>/
  ↓
[2] 编译渲染
  → scene.py                     # 场景源代码
  → config.json                  # 生成配置
  → output/high/SineWaveScene.mp4 # 最终视频
  → logs/build.log               # 编译日志
  → README.md                    # 输出说明
```

### 建议的文件组织

```
项目根目录/
├── manim_outputs/             # 输出目录（加入 .gitignore）
│   └── <scene_name>_<timestamp>/
└── plugins/manim-creator/      # 插件文件
```

### .gitignore 配置

建议在项目 `.gitignore` 中添加：

```gitignore
# Manim 输出
/manim_outputs/
```

## 目录结构

```
manim-creator/
├── README.md
├── agents/
│   └── manim-orchestrator.md     # 主编排智能体
├── commands/
│   └── manim.md                  # /manim 命令定义
├── skills/
│   ├── manim-generator/          # 代码生成 Skill
│   │   ├── SKILL.md
│   │   └── references/
│   │       └── patterns.md
│   ├── manim-tools/              # 工具函数库 Skill
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   │   └── tools.py          # 可复用工具函数
│   │   └── references/
│   │       └── api.md
│   └── manim-builder/            # 编译渲染 Skill
│       ├── SKILL.md
│       ├── scripts/
│       │   └── build.py          # 编译脚本
│       └── references/
│           └── options.md
├── templates/                    # 预留：代码模板
└── tools/
    └── .mcp.json                 # MCP 依赖配置
```

## 工具函数示例

```python
from tools.tools import *

class MyScene(Scene):
    def construct(self):
        # 创建几何图形
        circle = create_circle(radius=1, color=BLUE)
        square = create_square(side_length=2, color=RED)

        # 绘制函数
        sine = plot_sine(x_range=(-PI, PI), color=GREEN)

        # 使用预定义动画
        self.play(fade_in_transform(circle))
        self.play(morph_transform(circle, square))
```

## 命令参考

| 命令 | 说明 |
|------|------|
| `/manim create <描述>` | 创建动画 |
| `/manim tools [关键词]` | 查看工具 |
| `/manim build <文件>` | 编译场景 |
| `/manim help` | 帮助信息 |

## 质量选项

| 选项 | 分辨率 | 用途 |
|------|--------|------|
| `--quality low` | 480p | 快速预览 |
| `--quality medium` | 720p | 标准输出 |
| `--quality high` | 1080p | 高质量 |
| `--quality 4k` | 2160p | 超高清 |

## 依赖

- Python 3.8+
- manim
- numpy
- ffmpeg（用于 GIF 转换）

## 版本

0.1.0

## 作者

gqy20 <qingyuge@foxmail.com>
