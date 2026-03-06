#!/bin/bash
# 自动化更新脚本 - 添加新章节并构建网站

echo "🚀 开始更新小说网站..."

# 1. 转换新章节
echo "📖 转换章节文件..."
python3 convert_novel.py

# 2. 构建网站
echo "🔨 构建网站..."
hugo --minify

# 3. 显示统计信息
echo ""
echo "✅ 更新完成！"
echo "📊 网站统计："
echo "   - 总章节数: $(ls -1 content/posts/*.md | wc -l)"
echo "   - 生成页面: $(ls -1 public/posts/*.html | wc -l)"
echo ""
echo "🌐 预览网站: hugo server"
echo "🚀 部署网站: ./deploy.sh"
