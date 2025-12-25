# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

他山团队 (Tashan) Claude Code 研究插件集合，基于 Scispark 方法的结构化研究想法生成工作流。

## 开发命令

### Pre-commit 验证
```bash
# 安装 pre-commit hooks
pip install pre-commit && pre-commit install

# 手动运行验证
pre-commit run --all-files
```

Pre-commit 会在 `marketplace.json` 变更时自动验证插件配置格式。

### 插件配置验证
```bash
# 验证 marketplace 配置格式
claude plugin validate .claude-plugin/marketplace.json
```

## 核心架构

### Scispark 工作流插件 (`plugins/scispark/`)

Scispark 是一个7阶段结构化研究想法生成系统：

```
阶段1: 事实提取 → 阶段2: 假设生成 → 阶段3: 初始想法
→ 阶段4: 技术优化+Review → 阶段5: MoA优化+Review
→ 阶段6: 人机协作+Review → (可选) 阶段7: 幻灯片生成
```

#### 目录结构
- **agents/** - 编排智能体，定义完整工作流和状态管理
- **commands/** - 用户命令接口 (`/scispark`)
- **skills/** - 7个独立技能模块，每个对应一个阶段
- **templates/** - 输出模板（研究想法、幻灯片）
- **tools/.mcp.json** - MCP 服务器依赖配置

#### 关键设计模式

**状态管理**: 通过 `scispark-state.json` 跟踪每个阶段的执行状态、输出文件和文献统计。

**文献追踪**: `literature.csv` 累积记录所有文献及其使用情况，stage 和 usage 字段支持分号分隔的多值追加。

**Review循环**: 阶段4-6集成评审机制，每次评审包含：当前版本评估 → 专家系统视角 → 改进计划（生成问题ID: S{阶段}-P{序号}）。

**专家系统**: 在阶段1前、4前、5前、6前调用不同类型专家，输出保存在 `experts/` 目录。

**分级阈值**: 根据全文文献数量自适应执行模式：
- ≥50篇：理想执行（深度分析）
- ≥30篇：标准执行
- ≥15篇：降级执行（+局限说明）
- <15篇：错误终止

## MCP 依赖

```bash
# 必需
claude mcp add article-mcp uvx article-mcp server
claude mcp add sequentialthinking npx -y @modelcontextprotocol/server-sequential-thinking@latest

# 可选
claude mcp add mediawiki-mcp-server npx @professional-wiki/mediawiki-mcp-server@latest
claude mcp add playwright npx @playwright/mcp@latest --browser chrome --headless
```

## 添加新插件

1. 在 `plugins/` 创建新目录
2. 创建标准的子目录结构：`commands/`, `agents/`, `skills/`, `templates/`
3. 在 `.claude-plugin/marketplace.json` 的 `plugins` 数组中添加条目
4. 更新主 README.md 的插件列表
5. 提交信息遵循 `.gitmessage` 格式规范

## 修改现有插件

- Agent 修改：更新对应的 `.md` 文件，同步更新技能调用流程
- 技能修改：更新 `skills/` 下的对应文件
- 配置修改：更新 `marketplace.json` 后 pre-commit 会自动验证
- 版本更新：同步更新 `marketplace.json` 中的版本号和插件 README

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

类型: feat / fix / docs / style / refactor / test / chore
作用域: agent / skill / command / template / config / docs
