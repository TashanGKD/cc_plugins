# Skills 使用教程

Skills 是 Claude Code 中扩展 Claude 能力的强大方式。与斜杠命令不同，Skills 由 Claude 自动发现并调用，无需手动输入命令。

## 一、什么是 Skills

### Skills 的核心特点

| 特点 | 说明 |
|------|------|
| 自动发现 | Claude 根据你的请求自动选择合适的 Skill |
| 模型调用 | 由 Claude 决定何时使用，无需手动触发 |
| 多文件支持 | 可以包含参考文档、脚本、模板等资源 |
| 渐进式披露 | 主文件简洁，详细信息按需加载 |

!!! info "版本变更：Claude Code 2.1+"
    在 Claude Code 2.1 版本中，slash commands 和 Skills 被统一合并到 `Skill` 工具中。

    变更内容 ：
    - Skills 现在默认出现在斜杠命令菜单中
    - 可以通过 `/skill-name` 直接手动调用 Skills
    - 之前的 `SlashCommand` 工具被移除，统一使用 `Skill` 工具

    这意味着 Skills 兼具两种触发方式 ：
    - 自动触发 ：Claude 根据上下文自动选择
    - 手动调用 ：像斜杠命令一样通过 `/skill-name` 调用

### Skills 与其他扩展方式的对比

| 类型 | 触发方式 | 适用场景 | 复杂度 |
|------|----------|----------|--------|
| Skills | Claude 自动选择 `/skill-name` 手动调用 | 复杂工作流、团队标准、需要多文件的知识 | 高 |
| 传统斜杠命令 | 手动输入 `/command` | 频繁使用的简单提示 | 低 |
| CLAUDE.md | 每次对话自动加载 | 项目范围的指导 | 中 |
| MCP 服务器 | Claude 按需调用 | 连接外部工具和数据源 | 高 |

### Skills 的两种调用方式

方式一 ：自动触发（2.1 之前的核心特性）
- 你只需说 "审查这段代码"
- Claude 根据请求自动匹配相关 Skill
- 适合复杂的多步骤流程、需要详细指导的任务

方式二 ：手动调用（2.1 新增）
- 直接输入 `/your-skill-name` 触发
- 像传统斜杠命令一样使用
- 适合需要明确控制的场景

## 二、Skills 存放位置

Skills 的存储位置决定了谁可以使用它：

| 位置 | 路径 | 适用范围 |
|------|------|----------|
| 个人 | `~/.claude/skills/` | 仅你，跨所有项目 |
| 项目 | `.claude/skills/` | 该仓库的所有协作者 |
| 插件 | 插件目录的 `skills/` | 安装该插件的任何人 |

### 优先级规则

如果多个位置有同名 Skill，按以下优先级：

个人 > 项目 > 插件

## 三、创建你的第一个 Skill

### Skill 文件结构

最简单的 Skill 只需要一个 `SKILL.md` 文件：

```
.claude/skills/
└── my-skill/
    └── SKILL.md
```

### SKILL.md 基本格式

`SKILL.md` 文件由两部分组成：

1. YAML 前置元数据（`---` 标记之间的部分）
2. Markdown 说明（告诉 Claude 如何使用 Skill）

```markdown
---
name: your-skill-name
description: 简要描述 Skill 的功能和使用场景
---

# Your Skill Name

## Instructions
提供清晰的分步指导。

## Examples
展示具体使用示例。
```

### 元数据字段说明

| 字段 | 必需 | 说明 |
|------|------|------|
| `name` | 是 | Skill 名称，只能用小写字母、数字和连字符（最多 64 字符） |
| `description` | 是 | 功能描述和使用场景（最多 1024 字符），Claude 用它来决定何时使用 |
| `allowed-tools` | 否 | Skill 活跃时无需权限即可使用的工具 |
| `model` | 否 | Skill 使用的特定模型 |
| `context` | 否 | 设置为 `fork` 在独立子代理上下文中运行 |
| `agent` | 否 | 指定 `context: fork` 时使用的代理类型 |
| `hooks` | 否 | Skill 生命周期期间运行的钩子 |
| `user-invocable` | 否 | 是否在斜杠命令菜单中显示（默认 `true`） |

### 简单 Skill 示例

创建一个帮助生成提交消息的 Skill：

```bash
# 创建 Skill 目录
mkdir -p .claude/skills/commit-helper

# 创建 SKILL.md
cat > .claude/skills/commit-helper/SKILL.md << 'EOF'
---
name: generating-commit-messages
description: 从 git diff 生成清晰的提交消息。在编写提交消息或审查暂存更改时使用。
---

# 生成提交消息

## 指令

1. 运行 `git diff --staged` 查看更改
2. 建议包含以下内容的提交消息：
   - 50 字符以内的摘要
   - 详细描述
   - 受影响的组件

## 最佳实践

- 使用现在时态
- 说明做了什么和为什么，而不是怎么做
EOF
```

## 四、高级功能

### 多文件 Skill 结构

对于复杂的 Skills，使用渐进式披露保持主文件简洁：

```
pdf-processing/
├── SKILL.md          # 概述和快速开始
├── FORMS.md          # 表单填充指南
├── REFERENCE.md      # API 参考
├── EXAMPLES.md       # 使用示例
└── scripts/
    ├── analyze_form.py
    ├── fill_form.py
    └── validate.py
```

SKILL.md 内容示例：

```markdown
---
name: pdf-processing
description: 提取文本和表格、填充表单、合并文档。处理 PDF 文件或用户提到 PDF、表单、文档提取时使用。
allowed-tools: Read, Bash(python:*)
---

# PDF 处理

## 快速开始

提取文本：
```python
import pdfplumber
with pdfplumber.open("doc.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```

## 更多资源

- 表单填充：参见 `FORMS.md`
- API 参考：参见 `REFERENCE.md`
- 使用示例：参见 `EXAMPLES.md`

## 环境要求

```bash
pip install pypdf pdfplumber
```
```

### 限制工具访问

使用 `allowed-tools` 限制 Skill 可以使用的工具：

```yaml
---
name: reading-files-safely
description: 安全读取文件而不做修改。需要只读文件访问时使用。
allowed-tools:
  - Read
  - Grep
  - Glob
---
```

### 在分叉上下文中运行

使用 `context: fork` 在独立的子代理中运行 Skill：

```yaml
---
name: code-analysis
description: 分析代码质量并生成详细报告
context: fork
agent: general-purpose
---
```

### 控制 Skill 可见性

| 设置 | 斜杠菜单 | `Skill` 工具 | 自动发现 | 用途 |
|------|----------|-------------|----------|------|
| `user-invocable: true`（默认） | 可见 | 允许 | 是 | 用户直接调用的 Skills |
| `user-invocable: false` | 隐藏 | 允许 | 是 | Claude 使用但用户不应手动调用的 Skills |

示例：仅限模型调用的 Skill

```yaml
---
name: internal-review-standards
description: 审查 PR 时应用内部代码审查标准
user-invocable: false
---
```

## 五、编写有效的描述

`description` 字段是 Skill 发现的关键。它应该回答两个问题：

1. 这个 Skill 做什么？（列出具体功能）
2. Claude 何时应该使用它？（包含触发关键词）

### 描述示例

好的描述：

```yaml
description: 从 PDF 文件提取文本和表格、填充表单、合并文档。处理 PDF 文件或用户提到 PDF、表单、文档提取时使用。
```

不好的描述：

```yaml
description: 帮助处理文档  # 太模糊
```

### 编写技巧

| 原则 | 说明 |
|------|------|
| 具体化 | 列出具体操作（extract、fill、merge） |
| 包含关键词 | 使用用户会提到的术语（PDF、表单、文档提取） |
| 使用第三人称 | "Processes Excel files" 而非 "I can help you..." |
| 限制长度 | 最多 1024 字符 |

## 六、Skills 与子代理

### 给子代理分配 Skills

子代理不会自动继承 Skills，需要显式指定：

```markdown
# .claude/agents/code-reviewer.md
---
name: code-reviewer
description: 审查代码质量和最佳实践
skills: pr-review, security-check
---
```

### 在 Skill 中使用子代理

```yaml
---
name: complex-analysis
description: 执行复杂的多步骤分析
context: fork
agent: Explore
---
```

## 七、命名约定

推荐使用动名词形式（动词 + -ing）命名 Skills：

| 好的命名 | 说明 |
|----------|------|
| `processing-pdfs` | 动名词形式，清晰描述活动 |
| `analyzing-spreadsheets` | 明确的功能描述 |
| `managing-databases` | 一致的命名模式 |

| 避免 | 原因 |
|------|------|
| `helper`, `utils`, `tools` | 太模糊 |
| `documents`, `data`, `files` | 过于通用 |
| `claude-helper` | 包含保留字 |

## 八、实战示例

### 示例 1：代码审查 Skill

```yaml
---
name: reviewing-pull-requests
description: 根据团队标准审查 PR，检查安全性、性能和代码风格。用户要求审查代码、检查 PR 或审查更改时使用。
allowed-tools: Read, Grep, Bash(git:*)
---

# PR 审查流程

## 审查步骤

1. 运行 `git diff` 查看更改
2. 检查以下方面：
   - 安全漏洞
   - 性能问题
   - 代码风格一致性
   - 测试覆盖
3. 提供具体改进建议

## 审查标准

- 所有新代码必须有测试
- 敏感操作需要错误处理
- 复杂逻辑需要注释
```

### 示例 2：多文件数据分析 Skill

```
data-analysis/
├── SKILL.md
├── reference/
│   ├── finance.md    # 财务数据模式
│   ├── sales.md      # 销售数据模式
│   └── product.md    # 产品数据模式
└── scripts/
    └── validate.py   # 数据验证脚本
```

SKILL.md：

```yaml
---
name: analyzing-business-data
description: 分析业务数据、生成报告、创建图表。分析 Excel、电子表格或业务指标时使用。
---

# 业务数据分析

## 可用数据集

财务 ：收入、ARR、计费 → 参见 [reference/finance.md](reference/finance.md)
销售 ：机会、管道、账户 → 参见 [reference/sales.md](reference/sales.md)
产品 ：API 使用、功能采用 → 参见 [reference/product.md](reference/product.md)

## 数据验证

运行验证脚本：
```bash
python scripts/validate.py data.csv
```

## 分析流程

1. 确定数据类型和业务问题
2. 读取相应的参考文档
3. 执行分析并生成报告
```

### 示例 3：带工作流的 Skill

```yaml
---
name: filling-pdf-forms
description: 自动填充 PDF 表单、验证字段、生成输出文档。处理 PDF 表单或文档自动化时使用。
---

# PDF 表单填充工作流

复制此清单并跟踪进度：

```text
任务进度：
- [ ] 步骤 1：分析表单（运行 analyze_form.py）
- [ ] 步骤 2：创建字段映射（编辑 fields.json）
- [ ] 步骤 3：验证映射（运行 validate_fields.py）
- [ ] 步骤 4：填充表单（运行 fill_form.py）
- [ ] 步骤 5：验证输出（运行 verify_output.py）
```

## 步骤 1：分析表单

运行：`python scripts/analyze_form.py input.pdf`

这将提取表单字段及其位置，保存到 `fields.json`。

## 步骤 2：创建字段映射

编辑 `fields.json` 为每个字段添加值。

## 步骤 3：验证映射

运行：`python scripts/validate_fields.py fields.json`

修复任何验证错误后再继续。

## 步骤 4：填充表单

运行：`python scripts/fill_form.py input.pdf fields.json output.pdf`

## 步骤 5：验证输出

运行：`python scripts/verify_output.py output.pdf`

如果验证失败，返回步骤 2。
```

## 九、最佳实践

### 内容编写

| 原则 | 说明 |
|------|------|
| 简洁优先 | 假设 Claude 已经很聪明，只添加它不知道的信息 |
| 适当自由度 | 根据任务稳定性选择高/中/低自由度 |
| 渐进式披露 | 主文件 <500 行，详细信息放入单独文件 |
| 避免深层嵌套 | 所有参考文件应直接从 SKILL.md 链接 |

### 文件组织

```
your-skill/
├── SKILL.md              # 主文件（必需）
├── reference/            # 按领域组织的参考资料
│   ├── domain-a.md
│   └── domain-b.md
├── examples.md           # 使用示例
└── scripts/              # 可执行脚本（不加载到上下文）
    └── helper.py
```

### 脚本使用

区分执行和读取：
- 执行：`运行 analyze.py 提取字段`（推荐）
- 读取：`参考 analyze.py 了解提取算法`（仅当需要理解逻辑时）

## 十、常见问题

### Skill 不触发

原因：描述太模糊，Claude 无法匹配

解决：在描述中包含具体功能和触发关键词

```yaml
# 不好的描述
description: 帮助处理文档

# 好的描述
description: 从 PDF 提取文本和表格、填充表单、合并文档。处理 PDF 文件或用户提到 PDF、表单时使用。
```

### Skill 不加载

检查清单：

1. 文件路径是否正确：
   - 个人：`~/.claude/skills/my-skill/SKILL.md`
   - 项目：`.claude/skills/my-skill/SKILL.md`

2. 文件名是否完全匹配：`SKILL.md`（区分大小写）

3. YAML 语法是否正确：
   ```yaml
   ---
   name: my-skill
   description: My skill description
   ---
   ```

### 多个 Skills 冲突

症状：Claude 使用了错误的 Skill

解决：使描述更具体，使用独特的触发术语

```yaml
# 两个相似的 Skills
# Skill 1
description: 分析 Excel 文件中的销售数据

# Skill 2
description: 分析日志文件和系统指标
```

## 十一、调试技巧

### 查看可用 Skills

向 Claude 提问："What Skills are available?"

### 使用调试模式

```bash
claude --debug
```

查看 Skill 加载错误和详细日志。

### 测试 Skill

向 Claude 提出与 Skill 描述匹配的任务，观察它是否自动使用。

## 十二、项目实战：cc_plugins 的 Skills 实现

### 可用 Skills 列表

| Skill | 触发方式 | 自动触发关键词 | 用途 |
|-------|----------|----------------|------|
| `tdd` | `/tdd` | TDD、测试先行、红绿重构 | 测试驱动开发流程 |
| `bdd` | `/bdd` | BDD、验收测试、Gherkin | 行为驱动开发流程 |
| `squash` | `/squash` | squash、整理 commit | Commit 历史整理 |
| `docs` | `/docs` | 更新文档、同步文档 | 活文档维护 |
| `gh` | `/gh` | gh、GitHub CLI | GitHub CLI 指南 |

### 目录结构

```
.claude/
└── skills/                # 项目 Skills
    ├── bdd/SKILL.md
    ├── docs/SKILL.md
    ├── gh/SKILL.md
    ├── squash/SKILL.md
    └── tdd/SKILL.md
```

### 脚本支持

`scripts/generate_readme_tables.py` 自动扫描并生成 Skills 表格。

---

## 参考链接

### 官方文档

| 名称 | 链接 |
|------|------|
| Claude Code Skills 官方文档 | <https://code.claude.com/docs/zh-CN/skills> |
| Skills 最佳实践 | <https://platform.claude.com/docs/zh-CN/agents-and-tools/agent-skills/best-practices> |
| Slash Commands 文档 | <https://code.claude.com/docs/zh-CN/slash-commands> |
| Claude Code Changelog | <https://code.claude.com/docs/en/changelog> |
| Claude Code GitHub | <https://github.com/anthropics/claude-code> |
| Issue: Skills vs Slash Commands 合并 | <https://github.com/anthropics/claude-code/issues/17632> |

### 官方博客与最佳实践

| 名称 | 链接 |
|------|------|
| Claude Code 最佳实践 | <https://www.anthropic.com/engineering/claude-code-best-practices> |
| Agent Skills 概念深度解析 | <https://leehanchung.github.io/blogs/2025/10/26/claude-skills-deep-dive/> |
| 技术写作与 Agent Skills | <https://medium.com/google-cloud/supercharge-tech-writing-with-claude-code-subagents-and-agent-skills-44eb43e5a9b7> |

### 开源资源集合

| 名称 | 链接 |
|------|------|
| awesome-claude-skills (Composio) | <https://github.com/VoltAgent/awesome-claude-skills> |
| awesome-claude-skills (travisvn) | <https://github.com/travisvn/awesome-claude-skills> |
| awesome-agent-skills (libukai) | <https://github.com/libukai/awesome-agent-skills> |
| claude-code-skills-lab (教学示例) | <https://github.com/panaversity/claude-code-skills-lab> |

### 社区教程与指南

| 名称 | 链接 |
|------|------|
| Claude Skills 完全指南 (YouTube) | <https://www.youtube.com/watch?v=421T2iWTQio> |
| Claude Skills 23 分钟入门 | <https://www.youtube.com/watch?v=vEvytl7wrGM> |
| Claude Code Skills 深度解析 | <https://medium.com/spillwave-solutions/claude-code-skills-deep-dive-part-1-82b572ad9450> |
| 如何使用 Claude Code | <https://www.producttalk.org/how-to-use-claude-code-features> |
| Use Custom Agent Skills | <https://nikiforovall.blog/claude-code-rules/fundamentals/agent-skills> |

### 中文资源

| 名称 | 链接 |
|------|------|
| Claude Skills：让 AI 变身专业工匠 | <https://kaochenlong.com/claude-code-skills> |
| Claude Skills 官方教程详解 | <https://zhuanlan.zhihu.com/p/1987581624360145862> |
| Claude Code Skills 国内实践指南 | <https://www.53ai.com/news/LargeLanguageModel/2026010976504.html> |
| Claude Skills 精选集解析 | <https://www.xmsumi.com/detail/1944> |
| Agent Skills 详细攻略 (视频) | <https://www.youtube.com/watch?v=DNF0FJ9l7wo> |

### 实战案例

| 名称 | 链接 |
|------|------|
| 用 Claude Code Skill 打造责任伙伴 | <https://dev.to/yooi/beyond-coding-your-accountability-buddy-with-claude-code-skill-4omh> |
| Skills 最佳实践 (LinkedIn) | <https://www.linkedin.com/pulse/building-better-ai-agents-best-practices-claude-skills-filipe-melo-sxoge> |
