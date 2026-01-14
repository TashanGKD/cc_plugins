# MCP 使用教程

MCP (Model Context Protocol) 是 Claude Code 连接外部工具和数据的开放标准。通过 MCP 服务器，你可以让 Claude Code 访问数据库、API、文件系统等各种外部资源。

## 一、什么是 MCP

MCP 是一个开源通信协议，让 Claude Code 能够：

| 功能 | 说明 |
|------|------|
| **连接外部工具** | 集成 GitHub、Sentry、Slack 等服务 |
| **访问数据库** | 直接查询 PostgreSQL、MySQL 等数据库 |
| **操作文件系统** | 读写本地文件，批量处理文档 |
| **调用 API** | 与 REST API、GraphQL 等网络服务交互 |
| **自动化工作流** | 跨多个服务自动执行复杂任务 |

## 二、配置 MCP 服务器

MCP 服务器支持三种传输方式，根据你的需求选择：

### 方式 1：HTTP 服务器（推荐云端服务）

适用于：云端 API、SaaS 服务

```bash
# 基本语法
claude mcp add --transport http <name> <url>

# 连接 Notion
claude mcp add --transport http notion https://mcp.notion.com/mcp

# 带认证令牌
claude mcp add --transport http api https://api.example.com/mcp \
  --header "Authorization: Bearer your-token"
```

**对应的 JSON 配置**（存储在 `~/.claude.json` 或 `.mcp.json`）：

```json
{
  "mcpServers": {
    "notion": {
      "type": "http",
      "url": "https://mcp.notion.com/mcp"
    },
    "api": {
      "type": "http",
      "url": "https://api.example.com/mcp",
      "headers": {
        "Authorization": "Bearer your-token"
      }
    }
  }
}
```

### 方式 2：SSE 服务器（实时流式）

适用于：需要实时推送的服务

```bash
# 基本语法
claude mcp add --transport sse <name> <url>

# 连接 Asana
claude mcp add --transport sse asana https://mcp.asana.com/sse

# 带自定义请求头
claude mcp add --transport sse private-api https://api.company.com/sse \
  --header "X-API-Key: your-key"
```

对应的 JSON 配置：

```json
{
  "mcpServers": {
    "asana": {
      "type": "sse",
      "url": "https://mcp.asana.com/sse"
    },
    "private-api": {
      "type": "sse",
      "url": "https://api.company.com/sse",
      "headers": {
        "X-API-Key": "your-key"
      }
    }
  }
}
```

### 方式 3：stdio 服务器（本地进程）

适用于：本地工具、数据库连接、自定义脚本

```bash
# 基本语法
claude mcp add <name> -- <command> [args...]

# 添加 Article MCP（学术文献检索）
claude mcp add article-mcp -- uvx article-mcp server

# 添加 Sequential Thinking（思维链推理）
claude mcp add sequentialthinking -- npx -y @modelcontextprotocol/server-sequential-thinking
```

对应的 JSON 配置：

```json
{
  "mcpServers": {
    "article-mcp": {
      "type": "stdio",
      "command": "uvx",
      "args": ["article-mcp", "server"]
    },
    "sequentialthinking": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    }
  }
}
```

> 注意：
> 1. stdio 服务器的命令部分使用 `--` 分隔，`--` 之后是服务器启动命令
> 2. MCP 服务器配置存储位置：
>    - **User/Local 作用域**：`~/.claude.json`（**没有** `~/.mcp.json`）
>    - **Project 作用域**：项目根目录的 `.mcp.json`
> 3. 项目层面需要额外创建 `.claude/settings.json` 来启用 MCP 服务器（详见后文）
> 4. `settings.json` 仅包含 MCP 相关的控制设置，而非服务器配置本身

### 云端 MCP 部署平台

#### 魔搭 ModelScope（免费）

魔搭 MCP 广场提供 1500+ MCP 服务，支持云托管或本地部署。

使用步骤：

1. 访问 [魔搭 MCP 广场](https://modelscope.cn/mcp)
2. 选择需要的 MCP 服务（如高德地图、支付宝等）
3. 点击进入详情页，配置所需参数（如 API Key）
4. 在"通过 SSE URL 连接服务"模块点击"连接"
5. 获取生成的 SSE 端点 URL
6. 连接到 Claude Code：

```bash
claude mcp add --transport sse my-mcp https://modelscope.cn/api/mcp/sse/xxx
```

自定义 MCP 托管：

对于自己开发的 MCP 服务，可选择"可托管部署"方式，上传代码后获得云端托管地址。

#### 阿里云百炼（收费）

企业级 MCP 部署服务，提供稳定性和技术支持。

使用步骤：

1. 访问 [阿里云百炼 MCP 文档](https://help.aliyun.com/zh/model-studio/mcp)
2. 开通服务并创建工作空间
3. 封装 MCP 服务并发布到 npm
4. 在百炼平台创建自定义 MCP
5. 部署并获取服务端点
6. 连接到 Claude Code：

```bash
claude mcp add --transport sse my-mcp https://your-bailian-endpoint
```

| 需求 | 推荐平台 |
|------|----------|
| 个人开发/测试 | 魔搭（免费） |
| 小团队协作 | 魔搭（免费额度充足） |
| 企业生产环境 | 阿里云百炼（稳定性保障） |

## 三、MCP 服务器作用域

MCP 服务器可以在三个不同作用域级别配置：

| 作用域 | MCP 配置位置 | 启用控制 | 可用范围 | 适用场景 |
|--------|--------------|----------|----------|----------|
| **User** | `~/.claude.json` | 自动启用 | 所有项目 | 常用全局工具 |
| **Local** | `~/.claude.json` | 自动启用 | 当前项目 | 个人项目特定工具 |
| **Project** | `.mcp.json` | 需要创建 `.claude/settings.json` | 团队共享 | 团队协作工具 |

> **重要**：
> - 用户层面**没有** `~/.mcp.json`，所有 User/Local 配置都在 `~/.claude.json` 中
> - 项目层面的 `.mcp.json` **默认不启用**，需要创建 `.claude/settings.json`（详见后文"settings.json 中的 MCP 配置"章节）

### Local 作用域

```bash
# 默认添加到当前项目
claude mcp add --transport http stripe https://mcp.stripe.com

# 显式指定 local
claude mcp add --transport http stripe --scope local https://mcp.stripe.com
```

### User 作用域

```bash
# 添加到用户全局配置，所有项目可用
claude mcp add --transport http hubspot --scope user https://mcp.hubspot.com/anthropic
```

### Project 作用域

```bash
# 添加到项目配置，自动创建 .mcp.json
claude mcp add --transport http paypal --scope project https://mcp.paypal.com/mcp
```

Project 作用域会在项目根目录创建两个文件：

```
your-project/
├── .mcp.json           ← MCP 服务器配置
└── .claude/
    └── settings.json   ← 需要手动创建，启用项目 MCP
```

**`.mcp.json`**（自动创建）：
```json
{
  "mcpServers": {
    "shared-server": {
      "type": "http",
      "url": "https://mcp.example.com/mcp"
    }
  }
}
```

**`.claude/settings.json`**（需要手动创建）：
```json
{
  "enableAllProjectMcpServers": true
}
```

!!! info "环境变量扩展"
    `.mcp.json` 支持环境变量展开，团队可共享配置而各自使用不同的密钥：

    ```json
    {
      "mcpServers": {
        "api-server": {
          "type": "http",
          "url": "${API_BASE_URL:-https://api.example.com}/mcp",
          "headers": {
            "Authorization": "Bearer ${API_KEY}"
          }
        }
      }
    }
    ```

    语法：`${VAR}` 或 `${VAR:-default}`（默认值）

### 作用域优先级

当同名服务器存在于多个作用域时，按以下优先级解析：

**Local > Project > User**

## 四、管理 MCP 服务器

### 基本管理命令

```bash
# 列出所有已配置的服务器
claude mcp list

# 查看特定服务器详情
claude mcp get github

# 删除服务器
claude mcp remove github

# 在 Claude Code 中检查 MCP 状态
/mcp
```

### 动态工具更新

!!! info "版本要求：Claude Code 2.1+"
    MCP `list_changed` 通知支持在 **Claude Code 2.1** 系列（2.1.0 及更高版本）中引入。

Claude Code 支持 MCP `list_changed` 通知，服务器可以动态更新其可用工具、提示和资源，无需断开重连。

工作原理：

当 MCP 服务器发送 `list_changed` 通知时，Claude Code 会自动刷新该服务器的可用功能。

适用场景：

- MCP 服务器添加了新工具
- 服务器更新了现有工具的行为
- 资源列表发生变化

检查版本：

```bash
claude --version
# 输出示例：claude-code version 2.1.4
```

### 从 JSON 配置添加

如果你有 MCP 服务器的 JSON 配置，可以直接添加：

```bash
claude mcp add < config.json
```

### 从 Claude Desktop 导入

如果你已在 Claude Desktop 配置了 MCP 服务器，可以导入：

```bash
claude mcp import-from-desktop
```

## 五、实用 MCP 服务器推荐

以下是基于实际使用场景推荐的 MCP 服务器：

### 智谱官方 MCP（GLM Coding Plan 专属）

智谱为 GLM Coding Plan 用户提供 4 个官方 MCP 服务器，涵盖视觉理解、联网搜索、网页读取和开源仓库查询。

| 服务器 | 功能 | 类型 | 安装命令 |
|--------|------|------|----------|
| **zai-mcp-server** | 视觉理解，基于 GLM-4.6V，支持图像/视频分析、UI 转代码、OCR、错误诊断等 | stdio | `claude mcp add -s user zai-mcp-server --env Z_AI_API_KEY=your_api_key -- npx -y "@z_ai/mcp-server"` |
| **web-search-prime** | 联网搜索，获取实时网络信息和资源 | HTTP | `claude mcp add -s user -t http web-search-prime https://open.bigmodel.cn/api/mcp/web_search_prime/mcp --header "Authorization: Bearer your_api_key"` |
| **web-reader** | 网页读取，抓取网页内容和结构化数据 | HTTP | `claude mcp add -s user -t http web-reader https://open.bigmodel.cn/api/mcp/web_reader/mcp --header "Authorization: Bearer your_api_key"` |
| **zread** | 开源仓库，搜索文档、获取仓库结构、读取代码 | HTTP | `claude mcp add -s user -t http zread https://api.z.ai/api/mcp/zread/mcp --header "Authorization: Bearer your_api_key"` |

> 前提条件：需要订阅 [GLM Coding Plan](https://docs.bigmodel.cn/cn/coding-plan/overview) 并获取智谱 API Key。
>
> 使用额度：
> - Lite 套餐：联网搜索/网页读取/Zread 合计 100 次/月
> - Pro 套餐：联网搜索/网页读取/Zread 合计 1,000 次/月
> - Max 套餐：联网搜索/网页读取/Zread 合计 4,000 次/月
> - 视觉理解 MCP 共享套餐的 5 小时最大 prompt 资源池

详细文档：
- [视觉理解 MCP](https://docs.bigmodel.cn/cn/coding-plan/mcp/vision-mcp-server)
- [联网搜索 MCP](https://docs.bigmodel.cn/cn/coding-plan/mcp/search-mcp-server)
- [网页读取 MCP](https://docs.bigmodel.cn/cn/coding-plan/mcp/reader-mcp-server)
- [开源仓库 MCP](https://docs.bigmodel.cn/cn/coding-plan/mcp/zread-mcp-server)

---

### 他山 MCP（Tashan）

他山团队（Tashan）开发的一系列学术研究专用 MCP 服务器，涵盖文献检索、基因组学、蛋白质科学、RAG 问答等领域。

| 服务器 | 功能 | GitHub | 安装命令 |
|--------|------|--------|----------|
| **article-mcp** | 学术文献检索，支持多源数据库搜索（ArXiv、PubMed、bioRxiv 等） | <https://github.com/gqy20/article-mcp> | `claude mcp add article-mcp uvx article-mcp server` |
| **genome-mcp** | 基因组数据查询，NCBI Gene 数据库访问，支持基因信息、同源基因查询 | <https://github.com/gqy20/genome-mcp> | `claude mcp add genome-mcp uvx genome-mcp==0.1.5` |
| **protein-mcp** | 蛋白质结构数据访问，RCSB PDB 数据库查询，支持结构搜索、序列分析、文件下载 | <https://github.com/gqy20/protein-mcp> | `claude mcp add protein-mcp uvx protein-mcp` |
| **crawl-mcp** | 网页内容爬取和批量处理，基于 crawl4ai 和 FastMCP，支持 AI 分析 | <https://github.com/gqy20/crawl-mcp> | `claude mcp add crawl-mcp uvx crawl-mcp` |
| **TashanRAG** | 多论文 RAG 问答系统，从本地论文库检索相关论文并生成带引用的综合答案 | <https://github.com/TashanGKD/TashanRAG> | `claude mcp add TashanRAG uvx ts-rag` |

> 说明：以上 MCP 服务器由他山团队开发维护，专为科研工作流设计。
>
> TashanRAG 配置要求：
> - 需要配置 LLM API（如阿里云百炼 / Dashscope）
> - 在 `~/.claude.json` 或 `.mcp.json` 中添加环境变量：
> ```json
> {
>   "mcpServers": {
>     "TashanRAG": {
>       "command": "uvx",
>       "args": ["ts-rag"],
>       "env": {
>         "OPENAI_API_KEY": "your-api-key",
>         "OPENAI_BASE_URL": "https://dashscope.aliyuncs.com/compatible-mode/v1",
>         "MODEL_NAME": "openai/qwen-flash"
>       }
>     }
>   }
> }
> ```

---

### 开源社区 MCP

### 开发工具类

| 服务器 | 功能 | GitHub | 安装命令 |
|--------|------|--------|----------|
| **GitHub** | 管理 issues、PR、代码审查 | 官方服务 | `claude mcp add --transport http github https://api.githubcopilot.com/mcp/` |
| **playwright** | 浏览器自动化，支持页面交互、快照、表单填充、控制台日志、网络请求监控等 | <https://github.com/microsoft/playwright-mcp> | `claude mcp add playwright npx @playwright/mcp@latest` |

### 辅助工具类

| 服务器 | 功能 | GitHub | 安装命令 |
|--------|------|--------|----------|
| **sequential-thinking** | 结构化思维链推理，将复杂问题分解为可管理步骤，支持思考修订、分支推理和假设验证 | <https://github.com/modelcontextprotocol/servers> | `claude mcp add sequentialthinking npx -y @modelcontextprotocol/server-sequential-thinking` |

## 六、实战示例

### 示例 1：使用 GitHub MCP 管理项目

```bash
# 1. 添加 GitHub MCP 服务器
claude mcp add --transport http github https://api.githubcopilot.com/mcp/

# 2. 在 Claude Code 中认证
> /mcp
# 选择 "Authenticate" for GitHub

# 3. 使用 GitHub 功能
# 创建 issue
> "为登录页面的样式问题创建一个 issue，标签设为 bug"

# 分析项目
> "分析这个仓库的主要贡献者分布"

# 审查 PR
> "审查 PR #123，检查代码质量并提出改进建议"

# 查看 release
> "列出最近 5 个 release 版本"
```

### 示例 2：使用 Article MCP 查找学术文献

```bash
# 1. 添加 Article MCP 服务器
claude mcp add article-mcp uvx article-mcp server

# 2. 搜索文献
# 按关键词搜索
> "搜索关于 'large language model code generation' 的最新文献"

# 按 DOI 获取详情
> "获取 DOI 10.1038/s41586-021-03819-2 的文献详情"

# 分析文献关系
> "分析这篇文献的引用关系，找出高被引的相关研究"

# 获取参考文献
> "列出这篇文献的主要参考文献"

# 期刊质量评估
> "评估 Nature 期刊的影响因子和质量指标"
```

### 示例 3：组合使用多个 MCP

```bash
# 场景：为研究项目创建 GitHub issue 并引用相关文献

# 1. 确保 GitHub 和 Article MCP 已配置
> "为项目创建一个 issue：
     标题：实现基于 Transformer 的代码生成模型
     内容：根据以下文献实现功能...

     同时使用 article-mcp 搜索：
     'Attention Is All You Need'
     'Codex: Evaluating Large Language Models Trained on Code'"
```

## 七、常见问题

### 问题 1：服务器名称验证失败

错误信息：

```
API Error 400: "tools.11.custom.name: String should match pattern '^[a-zA-Z0-9_-]{1,64}$'"
```

解决方案：

- 名称只能包含字母、数字、下划线 `_` 和连字符 `-`
- 名称长度不超过 64 个字符
- 不能使用特殊字符或空格

### 问题 2：找不到 MCP 服务器

错误信息：

```
MCP server 'my-server' not found
```

解决方案：

1. 检查作用域设置是否正确
2. 运行 `claude mcp list` 确认服务器已添加
3. 确保在正确的目录下（对于 local 作用域）
4. 重启 Claude Code

### 问题 3：Windows 路径问题

错误信息：

```
Error: Cannot find module 'C:UsersusernameDocuments'
```

解决方案：

Windows 路径需要使用正斜杠或双反斜杠：

```bash
# 错误
claude mcp add fs -- npx -y @modelcontextprotocol/server-filesystem C:\Users\username\Documents

# 正确（使用正斜杠）
claude mcp add fs -- npx -y @modelcontextprotocol/server-filesystem C:/Users/username/Documents

# 正确（使用双反斜杠）
claude mcp add fs -- npx -y @modelcontextprotocol/server-filesystem C:\\Users\\username\\Documents
```

### 问题 4：权限问题

错误信息：

```
Permission denied
```

解决方案：

1. macOS/Linux：修改文件权限或使用用户目录
2. Windows：以管理员身份运行
3. 推荐：将 MCP 服务器安装在用户目录而非系统目录

### 问题 5：中文路径问题

避免在路径中使用中文字符：

```bash
# 避免
claude mcp add fs -- npx -y @modelcontextprotocol/server-filesystem ~/文档

# 推荐
claude mcp add fs -- npx -y @modelcontextprotocol/server-filesystem ~/Documents
```

### 问题 6：国内下载速度慢

使用淘宝 npm 镜像加速：

```bash
# 临时使用
claude mcp add fs -- npx -y --registry=https://registry.npmmirror.com @modelcontextprotocol/server-filesystem ~/Documents

# 或永久设置
npm config set registry https://registry.npmmirror.com
```

## 八、高级功能

### 使用 MCP 资源

MCP 服务器可以暴露资源，使用 `@` 符号引用，类似引用文件：

```bash
# 引用 MCP 资源
@resource://server-name/resource-path
```

### MCP Prompts 作为斜杠命令

!!! info "MCP 规范特性"
    Prompts 是 MCP 协议的规范特性。服务器可以暴露提示模板，客户端将其作为斜杠命令提供。

MCP 服务器可以暴露 prompts（提示模板），在 Claude Code 中作为斜杠命令使用。

工作原理：

1. MCP 服务器在初始化时声明 `prompts` 能力
2. 客户端通过 `prompts/list` 获取可用的 prompts 列表
3. 用户通过斜杠命令调用 prompt
4. 服务器通过 `prompts/get` 返回结构化的消息内容


官方文档：
- [MCP Prompts 规范](https://modelcontextprotocol.io/docs/concepts/prompts/)
- [MCP Server Specification - Prompts](https://modelcontextprotocol.io/specification/2025-11-25/server/prompts)

### settings.json 中的 MCP 配置

除了 MCP 服务器本身（配置在 `~/.claude.json` 或 `.mcp.json`），settings.json 提供了多个 MCP 相关的控制设置。

#### 项目 MCP 服务器控制

!!! warning "重要：项目层面需要单独配置"
    项目 `.mcp.json` 中的 MCP 服务器**默认不会自动启用**，出于安全考虑。

    你需要在项目中创建 **`.claude/settings.json`** 文件来启用项目层面 MCP：

    ```bash
    # 项目目录结构
    your-project/
    ├── .claude/
    │   └── settings.json    ← 创建此文件启用项目 MCP
    └── .mcp.json            ← MCP 服务器配置
    ```

    **`.claude/settings.json`** 内容：

    ```json
    {
      "enableAllProjectMcpServers": true
    }
    ```

    或者使用白名单方式（更安全）：

    ```json
    {
      "enableAllProjectMcpServers": false,
      "enabledMcpjsonServers": ["memory", "github"]
    }
    ```

| 设置 | 类型 | 说明 |
|------|------|------|
| `enableAllProjectMcpServers` | boolean | 自动批准所有项目 `.mcp.json` 中的 MCP 服务器 |
| `enabledMcpjsonServers` | array | 特定批准的 MCP 服务器列表 |
| `disabledMcpjsonServers` | array | 特定拒绝的 MCP 服务器列表 |

> **注意**：这些设置应该放在 **项目的 `.claude/settings.json`** 中，而不是全局的 `~/.claude/settings.json`。

#### Managed 环境控制（仅 managed-settings.json）

| 设置 | 类型 | 说明 |
|------|------|------|
| `allowedMcpServers` | array | 允许的 MCP 服务器白名单 |
| `deniedMcpServers` | array | 拒绝的 MCP 服务器黑名单（优先级高于白名单） |

配置示例：

```json
{
  "allowedMcpServers": [
    { "serverName": "github" },
    { "serverName": "memory" }
  ],
  "deniedMcpServers": [
    { "serverName": "filesystem" }
  ]
}
```

#### MCP 输出限制

| 设置 | 默认值 | 说明 |
|------|--------|------|
| 警告阈值 | 10,000 tokens | 超过此值显示警告 |
| 最大限制 | 25,000 tokens | 可通过环境变量或 settings.json 调整 |

**方式 1：环境变量**

```bash
# 临时设置
export MAX_MCP_OUTPUT_TOKENS=50000
claude

# 或永久设置（添加到 ~/.zshrc 或 ~/.bashrc）
echo 'export MAX_MCP_OUTPUT_TOKENS=50000' >> ~/.zshrc
```

**方式 2：settings.json**

```json
{
  "env": {
    "MAX_MCP_OUTPUT_TOKENS": "50000"
  }
}
```

#### 其他 MCP 超时配置

```json
{
  "env": {
    "MCP_TIMEOUT": "30000",
    "MCP_TOOL_TIMEOUT": "60000"
  }
}
```

### 使用 Claude Code 作为 MCP 服务器

你可以将 Claude Code 本身作为 MCP 服务器供其他应用连接：

```bash
# 启动 Claude 作为 stdio MCP 服务器
claude mcp serve
```

在 Claude Desktop 的 `claude_desktop_config.json` 中配置：

```json
{
  "mcpServers": {
    "claude-code": {
      "type": "stdio",
      "command": "claude",
      "args": ["mcp", "serve"],
      "env": {}
    }
  }
}
```

## 九、插件提供的 MCP 服务器

插件可以捆绑 MCP 服务器，在插件启用时自动提供工具和集成。

### 插件 MCP 配置方式

**方式 1：在 `.mcp.json` 中配置**（插件根目录）

```json
{
  "database-tools": {
    "command": "${CLAUDE_PLUGIN_ROOT}/servers/db-server/",
    "args": ["--config", "${CLAUDE_PLUGIN_ROOT}/config.json"],
    "env": {
      "DB_URL": "${DB_URL}"
    }
  }
}
```

**方式 2：在 `plugin.json` 中内联配置**

```json
{
  "name": "my-plugin",
  "mcpServers": {
    "plugin-api": {
      "command": "${CLAUDE_PLUGIN_ROOT}/servers/api-server/",
      "args": ["--port", "8080"]
    }
  }
}
```

### 插件 MCP 特性

| 特性 | 说明 |
|------|------|
| **自动生命周期** | 服务器随插件启用而启动 |
| **环境变量** | 使用 `${CLAUDE_PLUGIN_ROOT}` 引用插件路径 |
| **多种传输类型** | 支持 stdio、SSE 和 HTTP 传输 |
| **查看状态** | 在 Claude Code 中使用 `/mcp` 查看 |

> 注意：修改插件 MCP 服务器配置后需要重启 Claude Code 才能生效。

### 插件 MCP 的优势

- 捆绑分发：工具和服务器打包在一起
- 自动设置：无需手动 MCP 配置
- 团队一致性：所有团队成员安装插件后获得相同工具


## 十、最佳实践

| 原则 | 说明 |
|------|------|
| **按需添加** | 不要一次性添加太多服务器，会影响性能 |
| **定期清理** | 使用 `claude mcp remove <name>` 删除不用的服务器 |
| **安全第一** | 只添加可信的 MCP 服务器，特别是需要网络访问的 |
| **备份配置** | 定期备份 `~/.claude.json` 文件 |
| **团队协作** | 使用 project 作用域共享常用配置 |
| **使用环境变量** | 敏感信息（API 密钥）通过环境变量传递，不要硬编码 |

## 参考链接

| 名称 | 链接 |
|------|------|
| Claude Code MCP 官方文档 | <https://code.claude.com/docs/en/mcp> |
| MCP 官方文档 | <https://modelcontextprotocol.io> |
| MCP 规范 | <https://modelcontextprotocol.io/specification/draft> |
| MCP GitHub | <https://github.com/modelcontextprotocol/modelcontextprotocol> |
| Claude Code GitHub | <https://github.com/anthropics/claude-code> |
