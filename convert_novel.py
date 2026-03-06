#!/usr/bin/env python3
import os
import re
from datetime import datetime
import glob

# 小说目录
novel_dir = "没钱修什么仙"
content_dir = "content/posts"

# 创建内容目录
os.makedirs(content_dir, exist_ok=True)

# 遍历所有章节文件
chapter_files = glob.glob(f"{novel_dir}/**/*.md", recursive=True)
chapter_files = [f for f in chapter_files if "完整设定文档" not in f]

# 按文件名排序
chapter_files.sort()

for file_path in chapter_files:
    # 读取原始内容
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 提取章节信息
    filename = os.path.basename(file_path)
    rel_path = os.path.relpath(file_path, novel_dir)
    category = os.path.dirname(rel_path).replace("第一阶段-", "").strip()

    # 提取章节号和标题
    match = re.search(r'第(\d+)章[：-]\s*(.+?)(?:\.md|$)', filename)
    if match:
        chapter_num = match.group(1)
        chapter_title = match.group(2)
    else:
        chapter_num = "0"
        chapter_title = filename.replace(".md", "")

    # 提取内容中的标题（去除第一行的标题）
    lines = content.split('\n')
    if lines and lines[0].startswith('# 第'):
        content = '\n'.join(lines[1:]).strip()

    # 生成日期（按章节号递增）
    base_date = datetime(2025, 1, 1)
    chapter_date = base_date.replace(day=1 + int(chapter_num) % 28)

    # 创建 front matter
    front_matter = f"""---
title: "第{chapter_num}章 {chapter_title}"
date: {chapter_date.strftime('%Y-%m-%d')}
categories: ["{category}"]
tags: ["小说", "修仙", "第{chapter_num}章"]
draft: false
featured: false
---

# 第{chapter_num}章 {chapter_title}

"""

    # 组合内容
    full_content = front_matter + content

    # 生成 Hugo 文件路径
    hugo_filename = f"chapter{chapter_num.zfill(3)}-{filename.replace('.md', '')}.md"
    hugo_path = os.path.join(content_dir, hugo_filename)

    # 写入文件
    with open(hugo_path, 'w', encoding='utf-8') as f:
        f.write(full_content)

    print(f"转换完成: 第{chapter_num}章 {chapter_title} -> {hugo_filename}")

print(f"\n总共转换了 {len(chapter_files)} 个章节")
