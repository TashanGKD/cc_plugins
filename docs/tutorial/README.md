# Claude Code 教程

本教程带你从零开始掌握 Claude Code 的使用。

## 前置要求

在开始本教程之前，建议你具备以下条件：

### 1. 了解基本的 Linux 命令行工具

- 熟悉终端的基本操作
- 掌握常用命令（`ls`、`cd`、`mkdir`、`rm`、`cat` 等）

### 2. API 使用经验与使用需求

- 了解 API 密钥配置与 HTTP 请求基础
- 熟悉 OpenAI 兼容接口（如 `/v1/chat/completions` 端点）或 Anthropic 原生接口（Messages API）
- 日均消耗超过 10M tokens，高频使用场景才能充分发挥 Claude Code 的效率优势

### 3. Git 与 GitHub 基础

- 了解基本概念（commit、branch、merge）
- 会执行常用 Git 操作（`git status`、`git add`、`git commit`）
- 了解 GitHub 工作流（PR、Issue、分支管理）

### 4. 基本编程能力（非必需，仅针对代码开发场景）

- 熟悉至少一种编程语言
- 理解变量、函数、文件系统等基本概念

> **注**：即使暂时不具备上述技术基础，若你有信心在 **一周内实现日均消耗 API 超过 20M tokens** （约 1,000 次请求，或 100 次复杂对话任务），也强烈建议学习 Claude Code。高频使用场景会让你快速掌握所需技能。

## 教程目录

### 第一部分：基础入门

#### 1. [环境搭建](01-basics/01-getting-started.md)

- 安装 Claude Code
- 配置 GLM 密钥
- 验证安装

#### 2. [基础教程](01-basics/02-basic-usage.md)

- 工作模式切换
- 文件引用技巧
- 常用操作

#### 3. [MCP 使用教程](01-basics/03-mcp-usage.md)

- MCP 配置方式（HTTP/SSE/stdio）
- 作用域管理（Local/User/Project）
- 实用服务器推荐与常见问题

#### 4. [Skills 使用教程](01-basics/04-skills-usage.md)

- Skills 概念与特点
- Skills 创建与配置
- 最佳实践与常见问题

#### 5. [Agents 使用教程](01-basics/05-subagents-usage.md)

- Agents 概念与格式（YAML Frontmatter）
- 存放位置与创建方法
- 最佳实践与项目实战

## 获取帮助

- 官方文档：<https://docs.anthropic.com/en/docs/claude-code>
- GitHub：<https://github.com/anthropics/claude-code>
