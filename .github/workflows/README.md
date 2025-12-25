# GitHub Actions 工作流文档

本文档说明了项目中使用的 GitHub Actions 工作流配置。

## 📋 工作流概览

### 1. 增强插件验证工作流 (`plugin-validation.yml`)

这是项目的主要验证工作流，确保所有插件的配置、结构和内容质量符合标准。

#### 触发条件
- **Push**: 推送到 `main` 或 `develop` 分支时（当插件文件发生变化）
- **Pull Request**: 创建针对 `main` 分支的 PR 时（当插件文件发生变化）
- **手动触发**: 通过 `workflow_dispatch` 事件手动运行

#### 文件变化监控路径
```yaml
paths:
  - '.claude-plugin/**'
  - 'plugins/**'
  - '.github/workflows/plugin-validation.yml'
```

## 🔍 验证层次结构

### 第一层：基础结构验证
每个插件并行执行以下验证：

1. **文件结构检查**
   - ✅ 检查必需文件：`plugin.json`, `README.md`
   - ✅ 检查必需目录：`agents/`, `skills/`
   - ✅ 检查可选目录：`commands/`, `templates/`
   - ✅ 确保目录非空

2. **配置文件验证**
   - ✅ JSON 格式有效性检查
   - ✅ 必需字段验证：`name`, `version`, `description`, `category`
   - ✅ 语义化版本格式检查

3. **文件引用检查**
   - ✅ 验证 `marketplace.json` 中的所有文件引用
   - ✅ 检查 agents 和 skills 文件是否存在
   - ✅ 插件配置一致性检查

4. **内容质量验证**
   - ✅ README.md 内容质量检查
   - ✅ Agent 文件结构和工具引用检查
   - ✅ Skill 文件内容完整性检查
   - ✅ 命令文件使用说明检查

### 第二层：集成验证
当所有插件通过基础验证后，执行：

1. **配置加载测试**
   - ✅ 检查 `marketplace.json` 解析
   - ✅ 验证插件基本信息

2. **MCP 依赖检查**
   - ✅ 检查 MCP 服务器配置
   - ✅ 生成安装指南
   - ✅ 验证依赖关系

## 📊 验证报告

工作流会生成详细的验证报告：

### 单个插件报告
```markdown
## 📊 Plugin Validation Report

**Plugin:** evolutionary-biology-expert
**Status:** success

### Validation Results
- 📋 Marketplace: true
- 🏗️  Structure: true
- ⚙️  Configuration: true
- 🔗 References: true
- 📝 Content: true
```

### 最终汇总报告
```markdown
## 🏁 Complete Validation Summary

**Workflow Status:** success

### Job Results
- 📊 Individual Validation: success
- 🔗 Integration Validation: success

🎉 **All validations passed! Plugin collection is ready for deployment.**
```

## 🛠️ 验证脚本

项目使用三个核心验证脚本：

### 1. 文件引用检查脚本
**位置**: `.github/scripts/check_references.py`

**功能**:
- 验证 `marketplace.json` 中的文件引用
- 检查插件配置一致性
- 生成详细的引用检查报告

### 2. 内容质量验证脚本
**位置**: `.github/scripts/validate_content.py`

**功能**:
- 检查 README.md 内容质量
- 验证 Agent 文件结构和工具引用
- 检查 Skill 文件内容完整性
- 评估文档结构和格式

### 3. MCP 依赖检查脚本
**位置**: `.github/scripts/check_mcp_dependencies.py`

**功能**:
- 验证 MCP 服务器配置
- 检查依赖关系完整性
- 生成 MCP 安装指南
- 分析服务器配置结构

## 🧪 本地测试

### 运行完整测试套件
```bash
./.github/scripts/test_workflow.sh
```

### 运行单个验证脚本
```bash
# 文件引用检查
python3 .github/scripts/check_references.py

# 内容质量验证
python3 .github/scripts/validate_content.py

# MCP 依赖检查
python3 .github/scripts/check_mcp_dependencies.py

# 验证单个插件
python3 .github/scripts/validate_content.py plugins/evolutionary-biology-expert
```

## 📋 验证标准

### 插件结构要求
```
plugins/
├── plugin-name/
│   ├── plugin.json          # 必需：插件配置文件
│   ├── README.md            # 必需：插件说明文档
│   ├── agents/              # 必需：Agent 文件目录
│   │   └── *.md
│   ├── skills/              # 必需：Skill 文件目录
│   │   └── *.md
│   ├── commands/            # 可选：命令文件目录
│   │   └── *.md
│   ├── templates/           # 可选：模板文件目录
│   │   └── *.md
│   └── tools/               # 可选：MCP 配置目录
│       └── .mcp.json
```

### plugin.json 必需字段
```json
{
  "name": "plugin-name",
  "version": "0.1.0",
  "description": "Plugin description",
  "category": "category-name",
  "author": "author-name",
  "license": "MIT",
  "homepage": "https://github.com/user/repo",
  "repository": "https://github.com/user/repo",
  "keywords": ["keyword1", "keyword2"]
}
```

### 版本格式要求
- 必须遵循语义化版本规范：`MAJOR.MINOR.PATCH`
- 可选预发布版本：`MAJOR.MINOR.PATCH-prerelease`

### marketplace.json 引用要求
- 所有 agents 和 skills 路径必须指向存在的文件
- 路径必须是相对于项目根目录的完整路径
- 插件源目录必须存在

## 🔧 故障排除

### 常见问题

1. **文件引用错误**
   ```
   ❌ Agent file missing: ./plugins/plugin-name/agents/agent.md
   ```
   **解决方案**: 确保引用的文件存在，路径正确

2. **JSON 格式错误**
   ```
   ❌ plugin.json is invalid JSON
   ```
   **解决方案**: 使用 JSON 验证工具检查格式

3. **缺少必需字段**
   ```
   ❌ Missing required field: category
   ```
   **解决方案**: 在 plugin.json 中添加必需字段

4. **版本格式错误**
   ```
   ⚠️ Version may not follow semantic versioning: 1.0
   ```
   **解决方案**: 使用 `MAJOR.MINOR.PATCH` 格式

### 调试技巧

1. **本地运行验证**
   ```bash
   # 运行测试脚本
   ./.github/scripts/test_workflow.sh
   
   # 检查 JSON 格式
   jq empty .claude-plugin/marketplace.json
   jq empty plugins/plugin-name/plugin.json
   ```

2. **查看详细错误信息**
   ```bash
   # 运行单个脚本查看详细输出
   python3 .github/scripts/check_references.py
   ```

3. **检查文件权限**
   ```bash
   chmod +x .github/scripts/*.sh
   ```

## 📈 性能优化

- **并行验证**: 使用矩阵策略并行验证多个插件
- **fail-fast: false**: 允许其他插件继续验证即使某个插件失败
- **条件执行**: 只有当基础验证通过时才执行集成验证
- **缓存依赖**: 使用 GitHub Actions 缓存减少重复安装时间

## 🔄 工作流演进

### v1.0 (基础验证)
- 简单的 marketplace.json 验证

### v2.0 (增强验证) - 当前版本
- 完整的插件结构验证
- 内容质量检查
- MCP 依赖管理
- 详细的验证报告
- 本地测试支持

### 未来改进
- [ ] 自动化内容改进建议
- [ ] 插件性能测试
- [ ] 安全扫描集成
- [ ] 自动化文档生成

## 📞 支持

如果遇到工作流相关问题：

1. 查看 [GitHub Actions 运行日志](https://github.com/gqy20/cc_plugins/actions)
2. 运行本地测试脚本进行诊断
3. 检查本文档的故障排除部分
4. 提交 Issue 寻求帮助

---

**最后更新**: 2025-10-30  
**版本**: v2.0  
**维护者**: qingyu_ge