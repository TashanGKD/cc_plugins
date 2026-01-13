# 贡献指南

感谢你对 cc_plugins 项目的关注！我们欢迎任何形式的贡献。

## 贡献方式

### 报告问题

在 [GitHub Issues](https://github.com/TashanGKD/cc_plugins/issues) 中报告 Bug 或提出功能请求。

### 提交代码

1. **Fork 仓库**并创建功能分支
2. **编写代码**并确保通过测试
3. **提交 Pull Request** 并详细描述变更内容

### 改进文档

修正错别字、补充示例、完善说明都是宝贵的贡献。

## 开发流程

### 环境准备

```bash
# 克隆仓库
git clone https://github.com/TashanGKD/cc_plugins.git
cd cc_plugins

# 安装 pre-commit hooks
pip install pre-commit
pre-commit install
```

### 分支命名

遵循以下命名规范：

- `feat/` - 新功能
- `fix/` - Bug 修复
- `docs/` - 文档更新
- `refactor/` - 代码重构
- `test/` - 测试相关
- `chore/` - 构建/工具相关

### 提交规范

使用项目的 `.gitmessage` 模板：

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

**类型 (type):**
- `feat` - 新功能
- `fix` - Bug 修复
- `docs` - 文档变更
- `style` - 代码格式
- `refactor` - 重构
- `test` - 测试
- `chore` - 构建/工具

**作用域 (scope):**
- `agent` - 智能体
- `skill` - 技能
- `command` - 命令
- `template` - 模板
- `config` - 配置
- `workflow` - 工作流命令

### Pull Request

PR 标题应遵循相同的提交规范。描述中需包含：

- 变更目的
- 实现方式
- 测试情况
- 相关 Issue

## Pre-commit 验证

项目使用 pre-commit 确保代码质量：

```bash
# 手动运行验证
pre-commit run --all-files

# 跳过 hooks（不推荐）
git commit --no-verify
```

## 行为准则

- 尊重不同观点和经验
- 优雅地接受建设性批评
- 关注对社区最有利的事情
- 对其他社区成员表示同理心
