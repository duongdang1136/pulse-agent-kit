#!/bin/bash
# scripts/new-project.sh — Init project knowledge structure
#
# Usage:
#   bash scripts/new-project.sh fptplay
#   bash scripts/new-project.sh pulsetrend

set -e

PROJECT="${1}"

if [ -z "$PROJECT" ]; then
  echo "Usage: bash scripts/new-project.sh <project-name>"
  exit 1
fi

TARGET="knowledge/projects/$PROJECT"

if [ -d "$TARGET" ]; then
  echo "⚠️  Project already exists: $TARGET"
  exit 0
fi

mkdir -p "$TARGET"/{.rag,pages}

TODAY=$(date +%Y-%m-%d)

cat > "$TARGET/.rag/index.json" << EOF
{
  "version": "1.0",
  "updated_at": "$TODAY",
  "items": []
}
EOF

echo "✅ Created: $TARGET"
echo "   → Add .md files to $TARGET/pages/"
echo "   → Update $TARGET/.rag/index.json when done"
