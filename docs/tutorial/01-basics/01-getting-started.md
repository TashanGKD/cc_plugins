# Claude Code 环境搭建

本指南带你完成 Claude Code 的安装与 GLM 密钥配置。

## 一、安装 Claude Code

> **推荐使用 Linux 系统**以获得最佳体验。如果没有 Linux 设备，请查看「[常见问题 > 没有Linux 设备怎么办？](#没有-linux-设备怎么办)」

### macOS 安装

**方式一：官方脚本（推荐）**
```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**方式二：Homebrew**
```bash
brew install --cask claude-code
```

**方式三：NPM**
```bash
npm install -g @anthropic-ai/claude-code
```
> 注意：NPM 安装需要 Node.js 18+

### Linux 安装

**官方脚本（推荐）**
```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**NPM 安装**
```bash
npm install -g @anthropic-ai/claude-code
```
> 注意：NPM 安装需要 Node.js 18+

### Windows 安装

**官方脚本（PowerShell，推荐）**
```powershell
irm https://claude.ai/install.ps1 | iex
```

**NPM 安装**
```bash
npm install -g @anthropic-ai/claude-code
```
> 注意：NPM 安装需要 Node.js 18+ 和 Git for Windows

### 验证安装

```bash
claude --version
```

成功安装后会显示版本号（如 `2.0.14`）。

### 升级到最新版本

```bash
claude update
```

## 二、配置模型服务

> **原理说明**：Claude Code 通过 Anthropic API 协议连接模型服务。**任何支持 Anthropic API 兼容的服务都可以接入**，包括智谱 GLM、魔搭 ModelScope、阿里云百炼等。

### 配置 GLM Coding Plan（推荐）

> **官方文档**：[GLM Coding Plan 快速开始](https://docs.bigmodel.cn/cn/coding-plan/quick-start)

#### 1. 获取 API Key

访问 [智谱开放平台](https://open.bigmodel.cn/)，注册/登录后进入 **API Keys 管理页面**：

```
https://open.bigmodel.cn/usercenter/proj-mgmt/apikeys
```

点击「创建新的 API Key」并保存。

#### 2. 配置方式（三选一）

**方式一：Coding Tool Helper（推荐，最简单）**

交互式助手，一键完成 Claude Code 安装和 GLM 配置：

```bash
npx @z_ai/coding-helper
```

**前提条件**：需要先安装 Node.js 18+

**功能**：
- 自动安装 Claude Code
- 自动配置 GLM API Key
- 自动管理 MCP 服务器

**方式二：自动化脚本（macOS/Linux）**

```bash
curl -O "https://cdn.bigmodel.cn/install/claude_code_env.sh" && bash ./claude_code_env.sh
```

**方式三：手动配置**

编辑或创建 `~/.claude/settings.json` 文件（Windows 路径：`C:\Users\<用户名>\.claude\settings.json`）：

```json
{
    "env": {
        "ANTHROPIC_AUTH_TOKEN": "your_zhipu_api_key",
        "ANTHROPIC_BASE_URL": "https://open.bigmodel.cn/api/anthropic/",
        "ANTHROPIC_DEFAULT_SONNET_MODEL": "glm-4.7",
        "ANTHROPIC_DEFAULT_OPUS_MODEL": "glm-4.7",
        "API_TIMEOUT_MS": "3000000",
        "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": 1
    }
}
```

> 将 `your_zhipu_api_key` 替换为你的 API Key。配置后需重启终端生效。

## 三、开始使用

### 1. 启动 Claude Code

```bash
claude
```

### 2. 首次启动

启动后：
- 选择信任 Claude Code 访问项目文件夹
- 如遇到「Do you want to use this API key」提示，选择 **Yes**

### 3. 验证模型状态

在 Claude Code 中输入：

```
/status
```

确认 GLM 模型（如 `glm-4.7`）已正常加载。

## 四、常见问题

### 1. 安装时网络连接失败？

**官方脚本**安装需要稳定的网络连接访问 Anthropic 服务器。如果连接失败，推荐使用 **NPM 安装方式**：

```bash
# 使用国内镜像加速（可选）
npm config set registry https://registry.npmmirror.com

# 安装 Claude Code
npm install -g @anthropic-ai/claude-code
```

国内用户推荐使用淘宝镜像源 `registry.npmmirror.com` 进行加速。

### 2. 安装时提示权限错误？

macOS/Linux 使用 `sudo` 安装：
```bash
sudo npm install -g @anthropic-ai/claude-code
```

Windows 以管理员身份运行 PowerShell。

### 3. API Key 配置后不生效？

1. 关闭所有 Claude Code 窗口
2. 重新打开终端，运行 `claude`
3. 确认环境变量已正确设置

### 4. 如何切换模型或使用魔搭？

**切换模型**

编辑配置文件 `~/.claude/settings.json`：
```json
{
  "env": {
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "模型名称",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "模型名称"
  }
}
```

**使用魔搭免费模型**

魔搭社区提供**每天 2000 次**免费调用，适合个人开发使用。

**1. 获取 API Key**

访问 [魔搭开放平台](https://www.modelscope.cn/my/myaccesstoken)，创建 Access Token。

**2. 配置 settings.json**

编辑 `~/.claude/settings.json`：

```json
{
    "env": {
        "ANTHROPIC_AUTH_TOKEN": "你的魔搭API Key",
        "ANTHROPIC_BASE_URL": "https://api-inference.modelscope.cn",
        "ANTHROPIC_DEFAULT_SONNET_MODEL": "Qwen/Qwen3-Coder-480B-A35B-Instruct",
        "ANTHROPIC_DEFAULT_OPUS_MODEL": "Qwen/Qwen3-Coder-480B-A35B-Instruct"
    }
}
```

**可用模型**：
- `deepseek-ai/DeepSeek-V3.2` - DeepSeek V3 模型
- `Qwen/Qwen3-Coder-480B-A35B-Instruct` - 通义千问代码模型

> **注意**：
> - 魔搭需要绑定阿里云账号
> - 在魔搭平台选择模型时，请选择支持 **推理 API-Inference** 的模型

### 5. 没有 Linux 设备怎么办？

可以使用以下云端 Linux 环境：

**方案一：GitHub Codespaces**

1. 访问 [github.com/codespaces](https://github.com/codespaces)
2. 点击 "New codespace" 创建新空间
3. 选择任意仓库（或创建新仓库）
4. 启动后即可在浏览器中使用 Linux 终端
5. 按照本指南安装配置 Claude Code

**学生福利**：通过 [GitHub Student Developer Pack](https://education.github.com/pack) 验证的学生可获得每月 **180 小时**的免费 Codespaces 使用时间，以及 GitHub Pro、GitHub Actions 等其他福利。

**GitHub Codespaces 教程**：[GitHub Codespaces 文档](https://docs.github.com/en/codespaces)

**方案二：魔搭 Notebook**

1. 访问 [魔搭 Notebook](https://www.modelscope.cn/my/mynotebook)
2. 创建新的 Notebook 实例
3. 在终端中按照本指南安装配置 Claude Code

**魔搭 Notebook 优势**：
- **完全免费**，无时间限制
- 提供 **100G 存储**空间
- 国内访问稳定，无需翻墙

## 参考链接

| 名称 | 链接 |
|------|------|
| Claude Code GitHub | https://github.com/anthropics/claude-code |
| GLM Coding Plan 快速开始 | https://docs.bigmodel.cn/cn/coding-plan/quick-start |
| Claude Code 接入文档 | https://docs.bigmodel.cn/cn/guide/develop/claude |
| 智谱 AI 开放平台 | https://open.bigmodel.cn/ |
| API Keys 管理页面 | https://open.bigmodel.cn/usercenter/proj-mgmt/apikeys |
| 魔搭 ModelScope | https://www.modelscope.cn/ |
| 魔搭 Access Token | https://www.modelscope.cn/my/myaccesstoken |
| 魔搭 Notebook | https://www.modelscope.cn/my/mynotebook |
| GitHub Codespaces | https://github.com/features/codespaces |
| GitHub Codespaces 文档 | https://docs.github.com/en/codespaces |
