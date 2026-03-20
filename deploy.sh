#!/bin/bash
# Deploy script: build everything, then deploy to gh-pages

echo "📚 Building MkDocs..."
mkdocs build

echo "📊 Building Slidev slides..."
cd slides
npm run build
cd ..

echo "🚀 Deploying to GitHub Pages..."
mkdocs gh-deploy --no-history

# Rebuild slides after gh-deploy (which cleans the site directory)
echo "📊 Rebuilding Slidev slides for deployment..."
cd slides
npm run build

echo "✅ Deployment complete!"
echo "📈 Site should be live at: https://prgrobots.github.io/mkdocs-cyber/"
