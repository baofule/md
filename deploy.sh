#!/bin/bash
# 部署脚本 - 将Hugo网站部署到GitHub Pages

echo "开始部署到GitHub Pages..."

# 1. 构建网站
echo "正在构建网站..."
hugo --minify

# 2. 切换到public目录
cd public

# 3. 初始化Git仓库（如果还没有）
if [ ! -d ".git" ]; then
    git init
    git branch -M main
fi

# 4. 添加所有文件
git add .

# 5. 提交更改
git commit -m "Deploy website - $(date +'%Y-%m-%d %H:%M:%S')"

# 6. 推送到GitHub Pages
# 使用你的GitHub用户名和仓库名
# git push -f git@github.com:baofule/md.git main:gh-pages

echo "部署完成！"
echo "如果需要推送到GitHub，请取消注释上面的git push命令"
echo "然后在GitHub仓库设置中启用GitHub Pages，选择gh-pages分支"
