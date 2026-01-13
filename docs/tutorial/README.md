# Claude Code 教程

本教程带你从零开始掌握 Claude Code 的使用。

## 前置要求

在开始本教程之前，建议你具备以下条件：

1. **了解基本的 Linux 命令行工具**
   - 熟悉终端的基本操作
   - 掌握常用命令（ls, cd, mkdir, rm, cat 等）

2. **会使用 API 调用大模型**
   - 理解 API 密钥的配置方法
   - 了解基本的 HTTP 请求概念
   - 熟悉 OpenAI 兼容接口的调用方式（如 `/v1/chat/completions` 端点）

3. **充足的使用需求**
   - 日均 API 消耗超过 10M tokens
   - 高频使用场景才能充分发挥 Claude Code 的效率优势

## 教程目录

### 第一部分：基础入门

1. **[环境搭建](01-basics/01-getting-started.md)**
   - 安装 Claude Code
   - 配置 GLM 密钥
   - 验证安装

2. **[基础教程](01-basics/02-basic-usage.md)**
   - 工作模式切换
   - 文件引用技巧
   - 常用操作

3. **[MCP 使用教程](01-basics/03-mcp-usage.md)**
   - MCP 配置方式（HTTP/SSE/stdio）
   - 作用域管理（Local/User/Project）
   - 实用服务器推荐
   - 常见问题解决

4. **[Skills 使用教程](01-basics/04-skills-usage.md)**
   - Skills 概念与特点
   - Skills 创建与配置
   - 多文件结构与渐进式披露
   - Skills 最佳实践
   - 常见问题排查

5. **[Agents 使用教程](01-basics/05-subagents-usage.md)**
   - Agents 概念与特点
   - Agent 标准格式（YAML Frontmatter）
   - Agent 存放位置（插件/项目/个人）
   - 创建自定义 Agent
   - Agent 最佳实践
   - 项目实战（scispark-orchestrator）
   - Agent 验证与调试

## 获取帮助

- 官方文档：<https://docs.anthropic.com/en/docs/claude-code>
- GitHub：<https://github.com/anthropics/claude-code>
