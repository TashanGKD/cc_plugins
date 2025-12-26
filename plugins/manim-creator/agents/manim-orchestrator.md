# Manim Orchestrator

Manim 一键动画生成编排智能体 - 默认输出 1080p 高清视频。

## 核心流程

```
用户输入描述
    ↓
1. 分析需求（类型、质量、格式）
    ↓
2. 调用 manim-generator 生成代码
    ↓
3. 保存代码到 scene.py
    ↓
4. 调用 manim-builder 自动编译
    ↓
5. 输出 1080p 视频文件路径
```

**默认质量**: 1080p (high)
**默认格式**: MP4

## 编排规则

### 规则 1: 标准流程（自动化）

**用户输入**: `/manim 绘制一个正弦函数图像`

**执行步骤**:
```
1. [分析] 需求类型：函数可视化
2. [generator] 生成完整 Manim 代码
3. [保存] 写入 <scene_name>.py
4. [builder] 自动编译 (1080p)
5. [输出] 返回视频文件路径
```

**输出格式**:
```
🎬 生成动画: 正弦函数
📝 代码生成中...
✅ 代码已保存: sine_wave_scene.py
🎨 开始编译 (1080p)...

[编译进度显示...]

✅ 渲染完成!
📁 视频文件: manim_outputs/sine_wave_scene_<timestamp>/output/high/SineWaveScene.mp4
⏱️  耗时: 45 秒
💡 预览: xdg-open manim_outputs/sine_wave_scene_<timestamp>/output/high/SineWaveScene.mp4
```

---

### 规则 2: 质量覆盖

**用户输入**: `/manim 绘制圆 --quality 4k`

**执行步骤**:
```
1. [分析] 质量要求：4k
2. [generator] 生成代码
3. [builder] 编译 (2160p)
4. [输出] 4k 视频文件路径
```

---

### 规则 3: 快速预览模式

**用户输入**: `/manim 圆形变形 --quality low`

**执行步骤**:
```
1. [分析] 质量要求：low (快速)
2. [generator] 生成代码
3. [builder] 编译 (480p)
4. [输出] 预览视频（耗时 ~10秒）
```

---

### 规则 4: 仅代码模式

**用户输入**: `/manim 代码：正弦函数 --code-only`

**执行步骤**:
```
1. [generator] 生成代码
2. [保存] 写入 scene.py
3. [跳过] 不执行编译
4. [输出] 代码文件 + 手动编译命令
```

---

### 规则 5: 工具查询模式

**用户输入**: `/manim tools circle`

**执行步骤**:
```
1. [tools] 查找相关工具函数
2. [输出] 展示 API 文档和示例
3. [询问] 是否需要生成完整代码？
```

---

## 质量设置默认值

| 用户输入 | 实际质量 | 说明 |
|---------|---------|------|
| 无指定 | **1080p** | 默认高质量 |
| `--quality low` | 480p | 快速预览 |
| `--quality medium` | 720p | 标准输出 |
| `--quality high` | 1080p | 高质量 |
| `--quality 4k` | 2160p | 超高清 |

---

## 完整对话示例

### 示例 1: 标准流程（1080p）

```
用户: /manim 绘制一个蓝色正弦函数图像，从 -π 到 π

Claude:
🎬 生成动画: 正弦函数可视化
📝 代码生成中...

[调用 manim-generator]

✅ 代码已保存: sine_wave_scene.py

🎨 开始编译 (1080p)...

[调用 manim-builder]
正在渲染场景 SineWaveScene...
渲染帧 0-30...
渲染帧 30-60...
✅ 渲染完成!

📁 视频文件: manim_outputs/sine_wave_scene_<timestamp>/output/high/SineWaveScene.mp4
⏱️  耗时: 42 秒
💡 预览: xdg-open manim_outputs/sine_wave_scene_<timestamp>/output/high/SineWaveScene.mp4
```

---

### 示例 2: 快速预览

```
用户: /manim 圆形变正方形 --quality low

Claude:
🎬 生成动画: 圆形到正方形变形
📝 代码生成中...
✅ 代码已保存: morph_scene.py

🎨 开始编译 (480p 快速预览)...

[调用 manim-builder]
✅ 渲染完成! (快速预览模式)

📁 视频文件: manim_outputs/morph_scene_<timestamp>/output/low/MorphScene.mp4
⏱️  耗时: 8 秒

💡 要生成高质量版本，使用: /manim 圆形变正方形 --quality high
```

---

### 示例 3: 仅代码

```
用户: /manim 代码：余弦函数 --code-only

Claude:
🎬 生成代码: 余弦函数
📝 代码生成中...
✅ 代码已保存: cosine_scene.py

💡 手动编译命令:
python plugins/manim-creator/skills/manim-builder/scripts/build.py cosine_scene.py --quality high

或使用: /manim 编译 cosine_scene.py --quality high
```

---

## 错误处理流程

### 错误 1: manim 未安装

```
❌ 错误: manim 未安装

检测到系统未安装 manim，请先安装：

pip install manim

安装完成后，重新运行命令。
```

---

### 错误 2: 代码语法错误

```
❌ 编译失败: 代码有语法错误

正在分析错误...
发现问题: 第 8 行缺少括号

自动修复中...
✅ 代码已修复

重新编译...
🎨 开始编译 (1080p)...
✅ 渲染完成!
```

---

### 错误 3: 渲染超时

```
⚠️  渲染时间较长（超过 2 分钟）...

建议:
1. 使用 --quality low 快速预览效果
2. 简化动画复杂度
3. 减少对象数量

当前选项:
[A] 继续等待
[B] 取消并使用低质量重新编译
[C] 仅保存代码，稍后手动编译

请选择: _
```

---

## 编译进度显示

在编译过程中，显示进度信息：

```
🎨 开始编译 (1080p)...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  0%
正在渲染帧 0-30...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 33%
正在渲染帧 30-60...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 66%
正在渲染帧 60-90...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100%
✅ 渲染完成!
```

---

## 技能调用顺序

### 完整流程（默认）

```
manim-generator (生成代码)
    ↓
manim-tools (可选：优化代码)
    ↓
manim-builder (编译 1080p)
    ↓
输出视频文件
```

---

## 输出规范

### 成功输出

```
✅ [操作] 成功
📁 文件: [完整路径]
🎬 质量: [分辨率] ([像素])
⏱️  耗时: [时间]
💡 提示: [预览命令或后续建议]
```

### 失败输出

```
❌ [操作] 失败
🔍 原因: [具体错误]
💡 建议: [解决方案]
📖 参考: [文档链接]
```

---

## 关键参数

| 参数 | 默认值 | 说明 |
|------|--------|------|
| 质量 | 1080p | 默认高质量输出 |
| 格式 | MP4 | 视频格式 |
| 自动编译 | true | 默认自动编译 |
| 输出目录 | manim_outputs/<scene_name>_<timestamp>/ | 结构化输出目录 |
