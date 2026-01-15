# Scispark 输出模板

本目录包含 Scispark 工作流的输出模板文件。

## 文件说明

### 研究想法报告模板

| 文件 | 用途 | 适用阶段 |
|------|------|---------|
| `final_idea_template.md` | 最终研究想法报告模板 | 阶段6 |

### Quarto 幻灯片模板

| 文件 | 用途 | 复制位置 |
|------|------|---------|
| `_quarto.yml.template` | Quarto 项目配置 | `slides/_quarto.yml` |
| `custom.scss.template` | 自定义样式 | `slides/custom.scss` |
| `academic.csl.template` | 引用格式样式 | `slides/academic.csl` |

## 使用方法

### 研究想法报告

阶段6输出时，基于 `final_idea_template.md` 生成 `{keyword}_final_idea.md`。

### 幻灯片模板

阶段7执行时，Claude 会自动从模板创建配置文件：

```bash
# 复制模板到项目目录
cp slides/_quarto.yml.template slides/_quarto.yml
cp slides/custom.scss.template slides/custom.scss
cp slides/academic.csl.template slides/academic.csl
```

## 模板结构

```
templates/
├── final_idea_template.md       # 研究想法报告模板
└── slides/                      # Quarto 幻灯片模板
    ├── _quarto.yml.template     # Quarto 配置
    ├── custom.scss.template     # 自定义样式
    ├── academic.csl.template    # 引用格式
    └── README.md               # 本文件
```

## 自定义配置

### 修改颜色主题

编辑 `custom.scss.template` 中的颜色变量：

```scss
:root {
  --primary-color: #003366;    /* 主色调 */
  --secondary-color: #b8860b;  /* 辅助色 */
  --accent-color: #800020;     /* 强调色 */
}
```

### 修改幻灯片尺寸

编辑 `_quarto.yml.template` 中的尺寸配置：

```yaml
width: 1280   # 宽度
height: 720   # 高度（16:9）
```

## 参考资源

- [Quarto Presentations](https://quarto.org/docs/presentations/)
- [reveal.js Documentation](https://revealjs.com/)
- [CSL Styles](https://github.com/citation-style-language/styles)
