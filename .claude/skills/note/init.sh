#!/bin/bash
# 笔记系统初始化脚本
# 用途：创建 ~/.note 目录结构并复制模板文件

set -e

NOTE_DIR="$HOME/.note"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "📝 初始化笔记系统..."
echo

# 创建目录结构
echo "📁 创建目录结构..."
mkdir -p "$NOTE_DIR/notes"

# 复制配置文件
if [ ! -f "$NOTE_DIR/config.json" ]; then
    echo "📋 复制配置文件..."
    cp "$SCRIPT_DIR/templates/config.json" "$NOTE_DIR/config.json"
else
    echo "⚠️  配置文件已存在，跳过"
fi

# 创建索引文件
if [ ! -f "$NOTE_DIR/index.json" ]; then
    echo "📇 创建索引文件..."
    cp "$SCRIPT_DIR/templates/index.json" "$NOTE_DIR/index.json"
else
    echo "⚠️  索引文件已存在，跳过"
fi

# 创建 README
if [ ! -f "$NOTE_DIR/README.md" ]; then
    echo "📖 创建 README..."
    cat > "$NOTE_DIR/README.md" << 'EOF'
# 笔记存储目录

本目录由 `/note` skill 自动管理。

## 目录结构

- `config.json` - 配置文件
- `index.json` - 笔记索引
- `notes/` - 笔记存储目录

## 管理

笔记按月存储在 `notes/YYYY-MM/` 目录下。

**请勿手动修改 `index.json`，它由 skill 自动维护。**
EOF
fi

echo
echo "✅ 初始化完成！"
echo "   笔记目录: $NOTE_DIR"
echo
echo "🚀 开始使用："
echo "   /note 记一条测试笔记"
