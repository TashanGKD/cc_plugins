# 他山团队 (Tashan) Claude Code 研究工作流

> 用 AI 助手重塑学术研究流程，从文献综述到论文发表

## 🎯 我们做什么

帮助学术研究者**掌握 Claude Code**，建立**高效的 AI 辅助研究工作流**。

- 📚 **教程体系** - 从零开始学会 Claude Code
- 🔄 **工作流模板** - 开箱即用的研究流程
- 🛠️ **实用工具** - 文献分析、数学可视化等插件
- 🌱 **成长社区** - 分享经验、共同进步

## 🚀 快速开始

### 第一次使用 Claude Code？

```bash
# 1. 安装（1 分钟）
curl -fsSL https://claude.ai/install.sh | bash

# 2. 配置 GLM 模型（2 分钟）
# 访问 https://open.bigmodel.cn/ 获取 API Key
npx @z_ai/coding-helper

# 3. 开始使用
claude
```

### 想直接体验研究工作流？

```bash
# 7 阶段结构化研究想法生成
/scispark "杂交物种形成"

# 数学可视化
/manim "绘制函数 f(x) = sin(x)/x 的图像"
```

## 📚 学习路径

```
基础 → 工作流 → 进阶
  ↓       ↓        ↓
安装配置  研究流程  开发插件
基础操作  文献管理  贡献社区
```

### 第一步：掌握基础

阅读 **[Claude Code 环境搭建](./docs/tutorial/01-basics/01-getting-started.md)**

### 第二步：使用工作流

| 研究场景 | 工作流工具 | 说明 |
|----------|-----------|------|
| **文献综述** | [Scispark](./docs/plugins/scispark.md) | 7 阶段生成研究想法 |
| **数学可视化** | [Manim Creator](./docs/plugins/manim-creator.md) | 一键生成学术动画 |
| **代码开发** | `/tdd` | 测试驱动开发 |
| **文档维护** | `/docs` | 自动同步文档 |

### 第三步：深度定制

- **[开发指南](./docs/development/)** - 开发自己的工作流插件
- **[贡献指南](./docs/development/contributing.md)** - 加入项目共建

## 🌟 为什么选择我们

| 方面 | 说明 |
|------|------|
| **零门槛** | 详细教程，无需编程基础 |
| **开箱即用** | 预配置的研究工作流 |
| **开源免费** | MIT 许可，完全开放 |
| **中文支持** | 面向中文研究社区 |

## 📦 可用工作流

### 研究工作流

| 命令 | 功能 | 适用场景 |
|------|------|----------|
| `/scispark` | 7 阶段研究想法生成 | 文献综述、研究设计 |
| `/manim` | 数学动画生成 | 教学视频、学术展示 |

### 开发工作流

| 命令 | 功能 | 适用场景 |
|------|------|----------|
| `/tdd` | 测试驱动开发 | 功能开发 |
| `/bdd` | 行为驱动开发 | 验收测试 |
| `/docs` | 活文档维护 | 文档同步 |
| `/gh` | GitHub CLI 指南 | Git/GitHub 操作 |
| `/squash` | Commit 历史整理 | 版本管理 |

> 💡 工作流命令支持会话状态管理和智能分析，详见 [完整文档](./docs/)

## 🔗 相关资源

- **[完整教程](./docs/)** - Claude Code 入门到进阶
- **[插件文档](./docs/plugins/)** - 各工作流详细说明
- **[常见问题](./docs/tutorial/01-basics/01-getting-started.md#四常见问题)** - 安装配置问题解答
- **[在线文档](https://tashangkd.github.io/cc_plugins/)** - GitHub Pages 部署版本

## 🤝 参与贡献

我们欢迎各种形式的贡献：

- 💡 提出研究工作流的改进建议
- 📖 完善教程文档
- 🛠️ 开发新的工作流插件
- 🐛 报告问题、修复 Bug

详见 [贡献指南](./docs/development/contributing.md)

## 📄 许可证

MIT License - 详见 [LICENSE](./LICENSE)

## 👤 团队

**他山团队 (Tashan)** - 科研工具开发团队

> "他山之石，可以攻玉" - 用 AI 工具提升科研效率

- 📧 Email: qingyuge@foxmail.com
- 🔗 GitHub: [@TashanGKD](https://github.com/TashanGKD)

---

⭐ 如果这个项目对你有帮助，请给我们一个 Star！
