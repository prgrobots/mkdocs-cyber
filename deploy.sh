#!/bin/bash
# Deploy script: build everything then push to gh-pages

set -e

echo "📚 Building MkDocs..."
mkdocs build

echo "📊 Building Slidev slides..."
cd slides
npm run build
cd ..

echo "✅ Both MkDocs and Slidev built successfully"
echo ""
echo "📁 Site structure:"
ls -la site/ | grep -E "^d|index.html"
echo ""

echo "🚀 Deploying to gh-pages branch..."
# Add all changes
git add -A
git commit -m "Build site and slides" --allow-empty

# Use git subtree to push site folder to gh-pages
git subtree push --prefix site origin gh-pages

echo "✅ Deployment complete!"
echo "📈 Site available at: https://prgrobots.github.io/mkdocs-cyber/"
echo "📊 Slides available at: https://prgrobots.github.io/mkdocs-cyber/slides/"
