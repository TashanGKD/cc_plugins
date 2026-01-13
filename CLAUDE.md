# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

他山团队 (Tashan) Claude Code 研究插件集合，基于 Scispark 方法的结构化研究想法生成工作流。

## 开发命令

### 文档构建

```bash
# 构建文档并验证渲染
mkdocs build --clean

# 本地预览文档（实时刷新）
mkdocs serve

# 验证插件配置格式
claude plugin validate .claude-plugin/marketplace.json
```

### Pre-commit 验证

```bash
# 安装 pre-commit hooks
pip install pre-commit && pre-commit install

# 手动运行验证
pre-commit run --all-files
```

**Pre-commit 钩子功能**：
- 提交信息规范检查（Conventional Commits）
- `marketplace.json` 和 `plugin.json` 格式验证
- README 表格自动更新
- 文档自动同步到 `docs/` 目录
- JSON/YAML 语法检查

### 项目依赖管理

```bash
# 使用 uv 管理依赖
uv sync

# 安装开发依赖
uv pip install -e .
```

**核心依赖**（`pyproject.toml`）：
- `mkdocs-material>=9.7.1` - 文档主题
- `mkdocs-git-revision-date-localized-plugin>=1.5.0` - Git 版本日期

### 工作流命令

项目提供多个开发工作流命令，通过 `/命令名` 调用：

| 命令 | 用途 | 触发时机 |
|------|------|----------|
| `/tdd` | 测试驱动开发 | 功能开发 |
| `/bdd` | 行为驱动开发 | 验收测试 |
| `/squash` | Commit 历史整理 | TDD 循环完成后 |
| `/docs` | 活文档维护 | 代码变更后 |
| `/gh` | GitHub CLI 指南 | Git/GitHub 操作 |

**工作流命令特点**：
- 支持会话状态管理（如 TDD 会话恢复）
- 智能分析代码变更（如 `/docs` 自动更新文档）
- 集成 Git 工作流（如 `/squash` 安全检查）

## 核心架构

### 项目结构

```
cc_plugins/
├── .claude/                   # Claude Code 工作流命令
│   └── commands/             # 全局工作流命令（/tdd、/bdd 等）
├── .claude-plugin/           # 插件市场配置
│   └── marketplace.json      # 插件注册表
├── plugins/                  # 核心插件目录
│   ├── scispark/            # 研究想法生成工作流
│   └── manim-creator/       # 数学动画创建工具
├── docs/                    # MkDocs 文档站点
│   ├── tutorial/            # 教程文档
│   ├── plugins/             # 插件文档
│   └── development/         # 开发指南
├── scripts/                 # 自动化脚本
│   ├── sync-docs.sh        # 同步 README 到 docs
│   └── generate_readme_tables.py  # 自动更新表格
└── .github/workflows/       # CI/CD 工作流
```

### 插件架构模式

每个插件遵循标准结构：

```
plugins/<plugin-name>/
├── agents/                   # 编排智能体（完整工作流和状态管理）
├── commands/                 # 用户命令接口
├── skills/                   # 独立技能模块
├── templates/                # 输出模板
├── tools/.mcp.json          # MCP 服务器依赖配置
└── plugin.json              # 插件元数据
```

### Scispark 工作流插件 (`plugins/scispark/`)

**7 阶段结构化研究想法生成系统**：

```
阶段1: 事实提取 → 阶段2: 假设生成 → 阶段3: 初始想法
→ 阶段4: 技术优化+Review → 阶段5: MoA优化+Review
→ 阶段6: 人机协作+Review → (可选) 阶段7: 幻灯片生成
```

**关键设计模式**：

1. **状态管理**：通过 `scispark-state.json` 跟踪每个阶段的执行状态、输出文件和文献统计

2. **文献追踪**：`literature.csv` 累积记录所有文献及其使用情况，stage 和 usage 字段支持分号分隔的多值追加

3. **Review 循环**：阶段 4-6 集成评审机制，每次评审包含：当前版本评估 → 专家系统视角 → 改进计划（生成问题 ID：S{阶段}-P{序号}）

4. **专家系统**：在阶段 1 前、4 前、5 前、6 前调用不同类型专家，输出保存在 `experts/` 目录

5. **分级阈值**：根据全文文献数量自适应执行模式：
   - ≥50 篇：理想执行（深度分析）
   - ≥30 篇：标准执行
   - ≥15 篇：降级执行（+局限说明）
   - <15 篇：错误终止

6. **技能模块**：7 个独立技能，每个对应一个阶段，使用不同的 Temperature 参数

### Manim Creator 插件 (`plugins/manim-creator/`)

**数学动画一键生成工具**：

- **技能模块**：`manim-generator`（代码生成）、`manim-builder`（编译渲染）、`manim-tools`（工具函数库）
- **输出**：1080p 高清 MP4 视频

## MCP 依赖管理

### 必需 MCP 服务器

```bash
# 文献解析（Scispark 依赖）
claude mcp add article-mcp uvx article-mcp server

# 顺序推理（Scispark 依赖）
claude mcp add sequentialthinking npx -y @modelcontextprotocol/server-sequential-thinking@latest
```

### 可选 MCP 服务器

```bash
# MediaWiki 支持
claude mcp add mediawiki-mcp-server npx @professional-wiki/mediawiki-mcp-server@latest

# Playwright 浏览器自动化
claude mcp add playwright npx @playwright/mcp@latest --browser chrome --headless
```

**MCP 配置文件**：每个插件在 `tools/.mcp.json` 中声明 MCP 依赖

## 添加新插件

1. 在 `plugins/` 创建新目录
2. 创建标准的子目录结构：`commands/`, `agents/`, `skills/`, `templates/`
3. 创建 `plugin.json` 元数据文件
4. 在 `.claude-plugin/marketplace.json` 的 `plugins` 数组中添加条目
5. 更新主 README.md 的插件列表
6. 提交信息遵循 `.gitmessage` 格式规范

## 修改现有插件

- **Agent 修改**：更新对应的 `.md` 文件，同步更新技能调用流程
- **技能修改**：更新 `skills/` 下的对应文件
- **配置修改**：更新 `marketplace.json` 或 `plugin.json` 后 pre-commit 会自动验证
- **版本更新**：同步更新 `marketplace.json` 中的版本号和插件 README

## 提交信息规范

遵循 Conventional Commits 格式（详见 `.gitmessage`）：

```
<type>(<scope>): <subject>

## Summary
<简要描述>

## Changes Made
### <Component> Updates
<具体变更>

## Impact
<影响说明>

Co-authored-by: Claude <noreply@anthropic.com>
```

**类型（type）**：feat / fix / docs / style / refactor / test / chore

**作用域（scope）**：
- 插件开发：agent / skill / command / template / config
- 项目级：docs / workflow
- 工作流命令：`workflow`（修改 `/tdd` 等命令）、`command`（修改 `.claude/commands/*.md`）

## 文档编写规范

### Markdown 语法规范

1. **中文标点与 Markdown 语法**：避免紧邻，用空格或换行分隔
   - ❌ 错误：`**描述**：内容`
   - ✅ 正确：`描述：**内容**`

2. **MkDocs 兼容性**：
   - 使用标准 CommonMarkdown 语法
   - 避免嵌套过深（最多 3 层）
   - 代码块必须指定语言：```bash 而非 ```

3. **链接格式**：
   - 文档内链接使用相对路径：`[文本](path/to/file.md)`
   - 外部链接使用完整 URL

4. **表格格式**：
   - 表头和内容间用 `|` 分隔
   - 对齐方式：`:---`（左对齐）、`:---:`（居中）、`---:`（右对齐）

5. **文档去冗余原则**：
   - 避免使用独立的 `!!!` 块展示简单链接，将链接整合到标题或正文中
   - 删除单独显示的完整 URL 行，将其改为可点击的锚文本
   - 简短提示使用引用块 `>` 而非独立的 info/tip/warning 块
   - 仅在需要强调的重要警告或复杂说明时使用 admonition 块
   - 优先使用内联格式（如 `### [标题](链接)`）替代分离的标题和链接

### 文档验证

```bash
# 构建检查（避免缓存问题）
mkdocs build --clean

# 本地预览（实时刷新）
mkdocs serve
```

### 文档同步机制

Pre-commit 钩子自动执行以下同步操作：

1. **README 同步**：`scripts/sync-docs.sh` 将项目 README 同步到 `docs/`
2. **表格更新**：`scripts/generate_readme_tables.py` 自动更新命令和插件表格

## 质量保证机制

### Pre-commit Hooks

1. 提交信息规范检查
2. `marketplace.json` 格式验证
3. `plugin.json` 格式验证（author 类型、category 禁用、entry_points 禁用）
4. README 表格自动更新
5. 文档同步到 `docs/` 目录
6. JSON/YAML 格式检查
7. 大文件检查（最大 100KB）

### GitHub Actions

- **`plugin-validation.yml`**：插件配置验证
- **`docs.yml`**：文档自动部署到 GitHub Pages

## 分支命名规范

- `feat/` - 新功能
- `fix/` - Bug 修复
- `docs/` - 文档更新
- `refactor/` - 代码重构
- `test/` - 测试相关
- `chore/` - 构建/工具

## 开发最佳实践

1. **遵循插件结构**：严格按照 agents/skills/commands/templates 组织
2. **使用 MCP 协议**：通过 `.mcp.json` 声明依赖
3. **维护文档同步**：依赖 pre-commit 自动化
4. **遵循提交规范**：使用 `.gitmessage` 模板
5. **验证配置**：提交前运行 `pre-commit run --all-files`
6. **测试文档渲染**：运行 `mkdocs build --clean` 检查文档
