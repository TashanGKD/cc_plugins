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

## 循环流程

```mermaid
flowchart LR
    A[{{phase_1}}] --> B[{{phase_2}}]
    B --> C[{{phase_3}}]
    C --> D{验证}
    D -->|未通过| B
    D -->|通过| E[完成]
```

## 循环阶段

### 阶段 1：{{phase_1_title}}

{{phase_1_description}}

**执行**：
```bash
{{phase_1_command}}
```

**输出**：{{phase_1_output}}

### 阶段 2：{{phase_2_title}}

{{phase_2_description}}

**执行**：
```bash
{{phase_2_command}}
```

**输出**：{{phase_2_output}}

### 阶段 3：{{phase_3_title}}

{{phase_3_description}}

**执行**：
```bash
{{phase_3_command}}
```

**输出**：{{phase_3_output}}

### 验证检查

| 检查项 | 预期结果 | 命令 |
|--------|----------|------|
| {{check1}} | {{check1_expected}} | {{check1_command}} |
| {{check2}} | {{check2_expected}} | {{check2_command}} |

## 参数说明

| 参数 | 类型 | 说明 |
|------|------|------|
| {{param1}} | string | {{param1_description}} |
| {{param2}} | integer | {{param2_description}} |
| {{max_iterations}} | integer | 最大循环次数 |

## 工具依赖

| 工具 | 用途 |
|------|------|
| {{tool1}} | {{tool1_usage}} |
| {{tool2}} | {{tool2_usage}} |

## 状态追踪

状态文件：`{{state_file}}`

```json
{
  "iteration": {{current_iteration}},
  "phase": "{{current_phase}}",
  "last_result": "{{last_result}}",
  "start_time": "{{start_time}}"
}
```
