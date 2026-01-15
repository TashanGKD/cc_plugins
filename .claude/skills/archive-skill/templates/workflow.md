---
name: {{skill_name}}
description: {{one_line_description}}
user-invocable: true
---

# {{skill_title}}

## 技能描述

{{detailed_description}}

## 使用场景

{{when_to_use}}

## 执行流程

```mermaid
flowchart TD
    A[{{step_1}}] --> B[{{step_2}}]
    B --> C[{{step_3}}]
    C --> D[{{step_4}}]
```

## 执行步骤

### 步骤 1：{{step_1_title}}

{{step_1_details}}

**工具**：`{{tool1}}`

### 步骤 2：{{step_2_title}}

{{step_2_details}}

**工具**：`{{tool2}}`

### 步骤 3：{{step_3_title}}

{{step_3_details}}

**工具**：`{{tool3}}`

### 步骤 4：{{step_4_title}}

{{step_4_details}}

**工具**：`{{tool4}}`

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| {{param1}} | string | ✅ | - | {{param1_description}} |
| {{param2}} | integer | ❌ | {{default_value}} | {{param2_description}} |

## 工具依赖

| 工具 | 用途 |
|------|------|
| {{tool1}} | {{tool1_usage}} |
| {{tool2}} | {{tool2_usage}} |
| {{tool3}} | {{tool3_usage}} |

## 输出文件

```
{{output_path}}
├── {{file1}}
└── {{file2}}
```
