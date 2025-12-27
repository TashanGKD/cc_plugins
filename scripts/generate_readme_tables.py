#!/usr/bin/env python3
"""
自动生成 README 中的插件和命令表格

从配置文件和命令文件中提取元数据，生成 Markdown 表格
"""

import json
import re
from pathlib import Path
from typing import Dict, List


def extract_frontmatter(file_path: Path) -> Dict:
    """从 Markdown 文件中提取 YAML frontmatter"""
    content = file_path.read_text(encoding='utf-8')

    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return {}

    # 解析 YAML（支持简单格式和列表）
    frontmatter = {}
    lines = match.group(1).split('\n')
    current_list = None

    for line in lines:
        # 处理列表项（以 - 开头）
        if line.strip().startswith('- '):
            if current_list is not None:
                current_list.append(line.strip()[2:])
            continue

        # 如果之前在收集列表，现在结束了
        if current_list is not None:
            frontmatter[last_key] = current_list
            current_list = None

        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()

            # 处理内联数组 [a, b, c]
            if value.startswith('[') and value.endswith(']'):
                value = [v.strip() for v in value[1:-1].split(',')]
                frontmatter[key] = value
            # 处理空值（可能是多行列表的开始）
            elif value == '' or value == '[]':
                last_key = key
                current_list = []
            else:
                frontmatter[key] = value

    # 处理文件末尾的列表
    if current_list is not None:
        frontmatter[last_key] = current_list

    return frontmatter


def load_marketplace() -> List[Dict]:
    """加载 marketplace.json 中的插件信息"""
    marketplace_path = Path(__file__).parent.parent / '.claude-plugin' / 'marketplace.json'

    if not marketplace_path.exists():
        return []

    with open(marketplace_path, encoding='utf-8') as f:
        data = json.load(f)

    return data.get('plugins', [])


def discover_commands() -> List[Dict]:
    """扫描所有命令文件"""
    base_path = Path(__file__).parent.parent
    commands = []

    # 扫描项目级命令 (.claude/commands/)
    project_commands_path = base_path / '.claude' / 'commands'
    if project_commands_path.exists():
        for cmd_file in project_commands_path.glob('*.md'):
            frontmatter = extract_frontmatter(cmd_file)
            if frontmatter.get('name'):
                commands.append({
                    'name': f"/{frontmatter['name']}",
                    'description': frontmatter.get('description', ''),
                    'version': frontmatter.get('version', '-'),
                    'tags': frontmatter.get('tags', []),
                    'type': '项目命令',
                    'location': f".claude/commands/{cmd_file.name}"
                })

    # 扫描插件级命令 (plugins/*/commands/)
    plugins_path = base_path / 'plugins'
    if plugins_path.exists():
        for plugin_dir in plugins_path.iterdir():
            commands_path = plugin_dir / 'commands'
            if commands_path.exists():
                for cmd_file in commands_path.glob('*.md'):
                    frontmatter = extract_frontmatter(cmd_file)
                    if frontmatter.get('name'):
                        commands.append({
                            'name': f"/{frontmatter['name']}",
                            'description': frontmatter.get('description', ''),
                            'version': frontmatter.get('version', '-'),
                            'tags': frontmatter.get('tags', []),
                            'type': f'插件 ({plugin_dir.name})',
                            'location': f"plugins/{plugin_dir.name}/commands/{cmd_file.name}"
                        })

    return commands


def generate_plugins_table(plugins: List[Dict]) -> str:
    """生成插件表格 Markdown"""
    if not plugins:
        return "| 暂无插件 |\n|----------|"

    # 从 marketplace 获取详细信息
    marketplace_plugins = load_marketplace()
    plugin_info = {p['name']: p for p in marketplace_plugins}

    lines = [
        "| 插件名称 | 版本 | 类别 | 描述 |",
        "|---------|------|------|------|"
    ]

    for plugin in plugins:
        name = plugin['name']
        info = plugin_info.get(name, {})
        version = plugin.get('version', info.get('version', '-'))
        category = info.get('category', '-')
        description = info.get('description', plugin.get('description', ''))[:50] + '...' if len(info.get('description', '')) > 50 else info.get('description', plugin.get('description', ''))

        lines.append(f"| [{name}](./plugins/{name}/) | {version} | {category} | {description} |")

    return '\n'.join(lines)


def generate_commands_table(commands: List[Dict]) -> str:
    """生成命令表格 Markdown"""
    if not commands:
        return "| 暂无命令 |\n|----------|"

    lines = [
        "| 命令 | 版本 | 类型 | 标签 | 描述 |",
        "|------|------|------|------|------|"
    ]

    for cmd in commands:
        name = cmd['name']
        version = cmd.get('version', '-')
        cmd_type = cmd['type']
        tags = cmd.get('tags', [])
        tags_str = ', '.join(tags[:3]) + ('...' if len(tags) > 3 else '') if tags else '-'
        description = cmd['description'][:40] + '...' if len(cmd['description']) > 40 else cmd['description']

        lines.append(f"| `{name}` | {version} | {cmd_type} | {tags_str} | {description} |")

    return '\n'.join(lines)


def update_readme():
    """更新 README.md 中的表格"""
    readme_path = Path(__file__).parent.parent / 'README.md'

    if not readme_path.exists():
        print("❌ README.md 不存在")
        return False

    content = readme_path.read_text(encoding='utf-8')

    # 获取数据
    plugins = load_marketplace()
    commands = discover_commands()

    # 生成表格
    plugins_table = generate_plugins_table(plugins)
    commands_table = generate_commands_table(commands)

    # 替换插件表格
    content = re.sub(
        r'<!-- AUTO_START:PLUGINS -->.*?<!-- AUTO_END:PLUGINS -->',
        f'<!-- AUTO_START:PLUGINS -->\n{plugins_table}\n<!-- AUTO_END:PLUGINS -->',
        content,
        flags=re.DOTALL
    )

    # 替换命令表格
    content = re.sub(
        r'<!-- AUTO_START:COMMANDS -->.*?<!-- AUTO_END:COMMANDS -->',
        f'<!-- AUTO_START:COMMANDS -->\n{commands_table}\n<!-- AUTO_END:COMMANDS -->',
        content,
        flags=re.DOTALL
    )

    readme_path.write_text(content, encoding='utf-8')

    print(f"✅ README.md 已更新")
    print(f"   - {len(plugins)} 个插件")
    print(f"   - {len(commands)} 个命令")
    return True


if __name__ == '__main__':
    update_readme()
