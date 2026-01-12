# 开发指南

本章节面向希望贡献代码、开发新插件或深入了解项目架构的开发者。

## 目录

- [贡献指南](contributing.md) - 如何参与项目贡献

> 更多开发文档正在补充中...

## 快速贡献

```bash
# 1. Fork 并克隆仓库
git clone https://github.com/YOUR-USERNAME/cc_plugins.git

# 2. 安装开发依赖
pip install pre-commit
pre-commit install

# 3. 创建功能分支
git checkout -b feat/your-feature

# 4. 提交变更（遵循 .gitmessage 格式）
git commit -a

# 5. 推送并创建 Pull Request
git push origin feat/your-feature
```

## 代码规范

- 提交信息遵循 [Conventional Commits](https://www.conventionalcommits.org/)
- 代码变更需通过 pre-commit 验证
- 插件配置需符合 marketplace.json 规范

## 许可证

本项目采用 MIT 许可证。
