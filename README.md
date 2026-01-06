# 他山团队 (Tashan) Claude Code 插件集合

他山团队 (Tashan) 开发的 Claude Code 插件集合，为学术研究提供专业的工作流支持。

## 📦 已包含插件
| 插件名称 | 版本 | 类别 | 描述 |
|---------|------|------|------|
| [scispark](./plugins/scispark/) | 0.1.0 | workflow | Scispark 结构化研究想法生成工作流，通过7阶段流程将关键词转化为高质量、可验证的研究想法，包... |
| [manim-creator](./plugins/manim-creator/) | 0.1.0 | visualization | Manim 数学动画创建插件，提供代码生成、工具函数库和编译渲染功能。支持函数可视化、几何图形、动画... |

## 📋 可用命令
| 命令 | 版本 | 类型 | 标签 | 描述 |
|------|------|------|------|------|
| `/tdd` | 0.0.4 | 项目命令 | testing, tdd, workflow... | 测试驱动开发（TDD）流程助手，支持会话状态管理 |
| `/gh` | 0.0.2 | 项目命令 | git, github, cli... | GitHub CLI 专家助手，提供 gh 命令的场景化指导 |
| `/bdd` | 0.0.2 | 项目命令 | bdd, testing, acceptance... | 行为驱动开发（BDD）流程助手，支持 Gherkin 语法 |
| `/docs` | 0.0.4 | 项目命令 | documentation, maintenance... | 活文档维护，智能分析代码更新文档 |
| `/squash` | 0.0.2 | 项目命令 | git, rebase, commit... | Commit 历史整理与合并，TDD 后清理提交 |
| `/scispark` | 0.1.0 | 插件 (scispark) | research, workflow, academic... | Execute the 7-stage Scispark workflow to... |
| `/manim` | 0.1.0 | 插件 (manim-creator) | visualization, animation, math... | Manim 一键动画生成命令，输入自然语言描述，自动输出 1080p 高清数学动... |

## 📖 命令使用

### 命令系统工作原理

```
用户输入 /command → 读取 .md 定义 → 解析 YAML frontmatter → 执行工作流 → 返回结果
```

### 命令文件结构

```markdown
---
name: command-name
description: 命令描述
version: 0.0.1
tags: [tag1, tag2]
dependencies:
  tool: "version"
---

# 命令说明
详细内容...
```

### 命令示例

```bash
# 工作流命令
/tdd               # 测试驱动开发
/bdd               # 行为驱动开发
/squash            # 整理 commit 历史
/docs              # 维护文档

# 插件命令：研究工作流
/scispark "杂交物种形成"

# 项目命令：GitHub 操作
/gh
```

### 命令选项速查

| 命令 | 选项 | 说明 |
|------|------|------|
| `/scispark` | `--skip-slides` | 跳过幻灯片生成 |
| `/scispark` | `--min-papers <n>` | 设置最低文献阈值 |
| `/scispark` | `--quick-mode` | 快速模式 |
| `/scispark` | `--target <stage>` | 停留在指定阶段 (1-6) |
| `/manim` | `--quality low/medium/high/4k` | 设置视频质量 |
| `/manim` | `--format mp4/gif/png` | 设置输出格式 |
| `/manim` | `--code-only` | 只生成代码不编译 |

## 🛠️ 开发指南

```bash
# 安装 pre-commit（自动验证和更新 README）
pip install pre-commit && pre-commit install
```

### 添加插件/命令

**插件**: 在 `plugins/` 创建目录 → 在 `marketplace.json` 添加条目 → README 自动更新

**命令**: 在 `.claude/commands/` 或 `plugins/*/commands/` 创建 `.md` 文件（需包含 YAML frontmatter）

## 📁 项目结构

```
cc_plugins/
├── .claude-plugin/
│   └── marketplace.json          # 插件市场配置
├── .claude/commands/              # 项目级命令
│   ├── tdd.md                    # 测试驱动开发
│   ├── gh.md                     # GitHub CLI 指南
│   ├── bdd.md                    # 行为驱动开发
│   ├── docs.md                   # 活文档维护
│   └── squash.md                 # Commit 整理
├── plugins/
│   ├── scispark/                 # 研究工作流插件
│   │   ├── commands/             # /scispark 命令
│   │   ├── agents/ skills/ templates/
│   │   └── tools/.mcp.json       # MCP 依赖
│   └── manim-creator/            # 数学动画插件
│       ├── commands/             # /manim 命令
│       └── agents/ skills/
├── scripts/
│   └── generate_readme_tables.py # README 表格生成器
├── .pre-commit-config.yaml
└── README.md
```

## 📋 许可证

MIT License - 详见 [LICENSE](LICENSE)

## 👤 作者

**他山团队 (Tashan)** - 科研工具开发团队

- 📧 Email: qingyuge@foxmail.com
- 🔗 GitHub: [@gqy20](https://github.com/gqy20)

---

⭐ 如果这个项目对你有帮助，请给我们一个 Star！
