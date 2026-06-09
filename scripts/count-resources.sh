#!/bin/bash
# count-resources.sh
# Counts .md files per major section

echo "Iizuka LinkedIn Network — Resource Count"
echo "========================================="

for dir in cities companies jobs communities events startups success-stories resources; do
  count=$(find "./$dir" -name "*.md" 2>/dev/null | wc -l)
  echo "$dir: $count files"
done

echo ""
echo "Total .md files:"
find . -name "*.md" -not -path "./.git/*" | wc -l
