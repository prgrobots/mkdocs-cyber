#!/bin/bash
# Build script: MkDocs first, then Slidev

echo "📚 Building MkDocs..."
mkdocs build

echo "📊 Building Slidev slides..."
cd slides
npm run build

echo "✅ Build complete!"
echo "📌 Site ready at: site/"
echo "📈 Slides at: site/slides/"
