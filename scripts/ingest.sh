#!/bin/bash
# scripts/ingest.sh — Rebuild .rag/index.json từ pages/*.md
#
# Usage:
#   bash scripts/ingest.sh knowledge/shared/
#   bash scripts/ingest.sh knowledge/projects/fptplay/
#
# Requires: yq (https://github.com/mikefarah/yq) để parse YAML frontmatter
# Install: brew install yq  OR  snap install yq

set -e

KNOWLEDGE_DIR="${1:-.}"
PAGES_DIR="$KNOWLEDGE_DIR/pages"
INDEX_FILE="$KNOWLEDGE_DIR/.rag/index.json"

if [ ! -d "$PAGES_DIR" ]; then
  echo "❌ Pages dir not found: $PAGES_DIR"
  exit 1
fi

echo "🔍 Scanning: $PAGES_DIR"
echo "📝 Output:   $INDEX_FILE"

TODAY=$(date +%Y-%m-%d)
ITEMS="[]"

for f in "$PAGES_DIR"/*.md; do
  [ -f "$f" ] || continue
  SLUG=$(basename "$f" .md)
  TITLE=$(grep -m1 '^title:' "$f" | sed 's/title: *"//' | sed 's/"$//' || echo "$SLUG")
  TAGS=$(grep -m1 '^tags:' "$f" | sed 's/tags: *//' || echo "[]")
  KEYWORDS=$(grep -m1 '^keywords:' "$f" | sed 's/keywords: *//' || echo "[]")
  CATEGORY=$(grep -m1 '^category:' "$f" | sed 's/category: *//' || echo "Other")
  LAST_UPDATED=$(grep -m1 '^last_updated:' "$f" | sed 's/last_updated: *//' || echo "$TODAY")
  TTL=$(grep -m1 '^ttl_days:' "$f" | sed 's/ttl_days: *//' || echo "90")
  SUMMARY=$(grep -m1 '^summary:' "$f" | sed 's/summary: *"//' | sed 's/"$//' || echo "")

  echo "  ✅ $SLUG"
done

echo ""
echo "⚠️  Auto-rebuild chưa implement đầy đủ — edit index.json thủ công theo format trong knowledge/README.md"
echo "   (Script này là placeholder — integrate yq hoặc dùng LLM để rebuild)"
