#!/bin/bash
# check-links.sh
# Finds potentially broken internal links in all .md files

echo "Iizuka LinkedIn Network — Internal Link Checker"
echo "================================================"

BROKEN=0
TOTAL=0

while IFS= read -r -d '' file; do
  while IFS= read -r line; do
    # Extract markdown links [text](path)
    if echo "$line" | grep -qE '\[.*\]\((?!http)[^)]+\.md[^)]*\)'; then
      link=$(echo "$line" | grep -oE '\((?!http)[^)]+\.md[^)]*\)' | tr -d '()')
      dir=$(dirname "$file")
      target="$dir/$link"
      TOTAL=$((TOTAL + 1))
      if [ ! -f "$target" ]; then
        echo "❌ BROKEN: $file → $link"
        BROKEN=$((BROKEN + 1))
      fi
    fi
  done < "$file"
done < <(find . -name "*.md" -not -path "./.git/*" -print0)

echo ""
echo "Total links checked: $TOTAL"
echo "Broken links found: $BROKEN"
