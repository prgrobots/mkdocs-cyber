#!/bin/bash
# Deploy script: build MkDocs + Slidev, then force push site/ to gh-pages

set -e

REPO_URL=$(git remote get-url origin)

echo "📚 Building MkDocs..."
mkdocs build

echo "📊 Building Slidev slides..."
cd slides
for f in week-*.md; do
  week=${f%.md}
  echo "  → Building $f → site/slides/$week/"
  npx slidev build $f --out ../site/slides/$week --base /mkdocs-cyber/slides/$week/
done
cd ..

echo "✅ Build complete — site/slides/ contents:"
ls site/slides/

echo ""
echo "🚀 Deploying site/ to gh-pages branch..."
cd site
git init -q
git checkout -q -b gh-pages
git add -A
git commit -q -m "deploy $(date '+%Y-%m-%d %H:%M')"
git push -q -f "$REPO_URL" gh-pages
cd ..
rm -rf site/.git

echo "✅ Deployed!"
echo "📌 https://prgrobots.github.io/mkdocs-cyber/"
echo "📊 https://prgrobots.github.io/mkdocs-cyber/slides/"
