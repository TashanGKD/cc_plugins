# 他山团队 (Tashan) Claude Code 插件集合

他山团队 (Tashan) 开发的 Claude Code 插件集合，为学术研究提供专业的工作流支持。

## 📦 已包含插件

| 插件名称 | 版本 | 类别 | 描述 |
|---------|------|------|------|
| [scispark](./plugins/scispark/) | 0.1.0 | workflow | 结构化研究想法生成工作流 |
| [manim-creator](./plugins/manim-creator/) | 0.1.0 | visualization | Manim 数学动画创建插件 |

## ✨ 插件特性

### Scispark 工作流

- **🔄 7阶段结构化流程** - 事实提取 → 假设生成 → 初始想法 → 技术优化 → MoA优化 → 人机协作 → 幻灯片生成
- **🔍 Review 评审机制** - 阶段4-6集成评审循环
- **🧠 专家系统整合** - 4次专家调用支持各阶段
- **📊 分级文献阈值** - 理想(≥50)/标准(≥30)/最低(≥15)自适应
- **📝 学术规范** - Nature 格式引用，严格的学术标准检查

### Manim Creator

- **🎬 一键动画生成** - 自然语言描述 → 1080p 高清视频
- **🛠️ 三大技能模块** - 代码生成、工具函数库、编译渲染
- **📦 结构化输出** - 带时间戳的输出目录，包含源码、配置、日志

## 🚀 快速开始

### 1. 安装 Claude Code CLI

```bash
curl -fsSL https://claude.ai/install.sh | sh
```

### 2. 安装 MCP 依赖

```bash
# 学术文献检索 (必需)
claude mcp add article-mcp uvx article-mcp server

# 结构化思考分析 (必需)
claude mcp add sequentialthinking npx -y @modelcontextprotocol/server-sequential-thinking@latest

# 可选依赖
claude mcp add mediawiki-mcp-server npx @professional-wiki/mediawiki-mcp-server@latest
claude mcp add playwright npx @playwright/mcp@latest --browser chrome --headless

# Manim 编译渲染（使用 manim-creator 插件时需要）
pip install manim
```

### 3. 配置环境变量 (可选)

```bash
# 本地文献库根目录
export COURSE_ROOT=/path/to/course/directory

# 期刊质量评估 API（可选）
export EASYSCHOLAR_SECRET_KEY="your_api_key_here"
```

### 4. 验证安装

```bash
# 验证 marketplace 配置
claude plugin validate .claude-plugin/marketplace.json
```

## 📖 使用方法

### Scispark 研究工作流

```
/scispark "杂交物种形成"
/scispark "CRISPR基因编辑"
/scispark "climate adaptation" "hybrid zones"
```

### Manim 动画创建

```
/manim 绘制一个正弦函数图像
/manim 创建一个圆变形成正方形的动画 --quality 4k
/manim 展示 E=mc^2 公式动画
```

### 高级选项

#### Scispark 选项
```
/scispark "关键词" --skip-slides       # 跳过幻灯片生成
/scispark "关键词" --min-papers 20     # 设置最低文献阈值
/scispark "关键词" --quick-mode        # 快速模式
/scispark "关键词" --target 4          # 停留在阶段4
```

#### Manim 选项
```
/manim "描述" --quality high          # 1080p 高质量（默认）
/manim "描述" --quality low           # 480p 快速预览
/manim "描述" --format gif            # 导出 GIF 格式
/manim "描述" --code-only             # 只生成代码不编译
```

## 🛠️ 开发指南

### 安装 Pre-commit Hooks

```bash
# 安装 pre-commit
pip install pre-commit

# 安装 hooks
pre-commit install
```

Pre-commit 会在 `marketplace.json` 变更时自动验证配置。

### 日常开发流程

1. **修改插件文件** - 编辑相应的 agents、skills 或配置文件
2. **暂存更改** - `git add .`
3. **提交代码** - `git commit -m "feat: 添加新功能"`
   - Pre-commit hook 会自动验证配置
   - 如果验证失败，请修复错误后重新提交
4. **推送代码** - `git push`

### 手动验证

```bash
# 验证 marketplace 配置
claude plugin validate .claude-plugin/marketplace.json

# 运行 pre-commit 手动检查
pre-commit run --all-files

# 跳过验证 (不推荐)
git commit --no-verify
```

## 📁 项目结构

```
cc_plugins/
├── .claude-plugin/
│   └── marketplace.json          # 插件市场配置
├── plugins/
│   ├── scispark/                 # Scispark 工作流插件
│   │   ├── README.md
│   │   ├── commands/
│   │   ├── agents/
│   │   ├── skills/
│   │   ├── templates/
│   │   └── tools/
│   └── manim-creator/            # Manim 动画创建插件
│       ├── README.md
│       ├── commands/
│       ├── agents/
│       ├── skills/
│       └── tools/
├── .pre-commit-config.yaml       # Pre-commit 配置
└── README.md                     # 本文件
```

## 🔧 配置标准

本项目遵循严格的配置标准：

- **插件配置** - 符合 Claude Code 官方 marketplace 格式
- **文件结构** - 标准化的目录结构和命名规范
- **质量控制** - Pre-commit 自动验证
- **文档标准** - 完整的 README 和技能文档

## 📋 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

## 👤 作者

**他山团队 (Tashan)** - 科研工具开发团队

- 📧 Email: qingyuge@foxmail.com
- 🔗 GitHub: [@gqy20](https://github.com/gqy20)

## 🙏 致谢

- Claude Code 团队提供的优秀开发平台
- 所有贡献者和用户的支持
- 开源社区的灵感和工具

---

⭐ 如果这个项目对你有帮助，请给我们一个 Star！
