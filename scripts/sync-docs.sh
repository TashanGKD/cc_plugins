#!/bin/bash
# 同步插件 README 到 docs 目录（用于 GitHub Pages）

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
DOCS_DIR="$PROJECT_ROOT/docs"

echo "🔄 同步文档到 docs 目录..."

# 复制主 README
if [ -f "$PROJECT_ROOT/README.md" ]; then
  cp "$PROJECT_ROOT/README.md" "$DOCS_DIR/README.md"
  echo "  ✓ README.md"
fi

# 复制插件 README
found_plugins=0
for plugin_dir in "$PROJECT_ROOT"/plugins/*/; do
  if [ -d "$plugin_dir" ]; then
    plugin_name=$(basename "$plugin_dir")
    plugin_readme="$plugin_dir/README.md"

    if [ -f "$plugin_readme" ]; then
      cp "$plugin_readme" "$DOCS_DIR/${plugin_name}.md"
      echo "  ✓ ${plugin_name}.md"
      found_plugins=$((found_plugins + 1))
    fi
  fi
done

# 自动添加到 git（如果不在 git 仓库中跳过）
if git rev-parse --git-dir > /dev/null 2>&1; then
  git add docs/ 2>/dev/null || true
fi

echo "✅ docs 已同步 (主文档 + ${found_plugins} 个插件文档)"
exit 0
