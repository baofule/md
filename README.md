# 没钱修什么仙 - Paper主题小说网站

这是一个使用Hugo构建的小说网站，采用**Paper主题**的极简主义设计。

## 🌟 关于Paper主题

**Paper**是GitHub上最受欢迎的简约Hugo主题之一，具有：

- ✅ **3000+ GitHub Stars** - 广泛使用和验证
- ✅ **极简设计** - 专注于内容阅读
- ✅ **多色主题** - 6种预设颜色主题
- ✅ **响应式布局** - 完美支持各种设备
- ✅ **高性能** - 快速加载，优化体验
- ✅ **搜索功能** - 内置文章搜索
- ✅ **易于定制** - 简洁的配置文件

## 🎨 主题特色

### 极简设计
- 📝 **干净排版** - 专注阅读体验
- 🎨 **清爽配色** - 护眼的颜色方案
- ✨ **简约风格** - 去除冗余元素
- 📱 **响应式** - 自适应各种屏幕
- ⚡ **快速加载** - 优化的性能

### 颜色主题
Paper主题提供6种颜色主题：
- 🔵 **蓝色** (blue) - 默认，清新专业
- ⚪ **白色** (light) - 简洁明亮
- ⚫ **暗色** (dark) - 护眼舒适
- 🔴 **红色** (red) - 热情活力
- 🟢 **绿色** (green) - 自然清新
- 🟠 **橙色** (orange) - 温暖活力

### 功能特性
- 🔍 **文章搜索** - 快速查找章节
- 📑 **标签分类** - 方便内容组织
- 📊 **阅读时间** - 预计阅读时长
- 📅 **日期显示** - 清晰的时间线
- 🔗 **社交链接** - GitHub、Twitter等

## 📊 当前状态

- ✅ **总页数**: 88页
- ✅ **主题**: Paper (蓝色主题)
- ✅ **服务器**: 运行在3000端口
- ✅ **网站**: http://localhost:3000/md/
- ✅ **章节数**: 24章

## 🚀 快速开始

### 本地预览

```bash
hugo server
```

### 构建网站

```bash
hugo --minify
```

### 添加新章节

1. 在 `没钱修什么仙/` 目录中添加新的Markdown文件
2. 运行转换脚本：
   ```bash
   ./update.sh
   ```

## 🎨 切换颜色主题

编辑 `config.toml` 文件：

```toml
[params]
  color = "blue"  # 可选: light, dark, red, green, orange
```

## 📁 项目结构

```
├── content/             # 网站内容
│   ├── _index.md       # 首页
│   ├── about.md        # 关于页面
│   └── posts/          # 小说章节
├── layouts/            # 自定义布局
├── static/             # 静态文件
├── themes/             # Hugo主题
│   └── paper/          # Paper主题
├── config.toml         # 网站配置
└── convert_novel.py    # 章节转换脚本
```

## 🌐 部署

### GitHub Pages

1. 构建网站：
   ```bash
   hugo --minify
   ```

2. 将 `public/` 目录推送到GitHub

3. 在GitHub设置中启用Pages

### 手动部署

```bash
./deploy.sh
```

## 🔧 配置说明

### 主题配置

```toml
[params]
  description = "没钱修什么仙 - 一部搞笑修仙小说"
  author = "baofule"
  color = "blue"
  showMenu = true
  showReadingTime = true
  showDate = true
  showAuthor = true
  enableSearch = true
```

### 菜单配置

```toml
[[menu.main]]
  identifier = "home"
  name = "首页"
  url = "/"
  weight = 1
```

### 社交链接

```toml
[params]
  github = "baofule/md"
  instagram = ""
  xtwitter = ""
  linkedin = ""
  mastodon = ""
```

## 📚 小说信息

- **标题**: 没钱修什么仙
- **作者**: baofule
- **类型**: 修仙、搞笑、商战
- **章节数**: 24章
- **状态**: 连载中

## 🎯 主题亮点

1. **极简设计** - 专注于内容，无干扰
2. **多色主题** - 6种预设颜色可选
3. **性能优异** - 快速加载，优化体验
4. **易于定制** - 简洁的配置文件
5. **响应式布局** - 完美支持各种设备
6. **搜索功能** - 内置文章搜索

## 🎊 享受你的小说网站！

**网站地址**: http://localhost:3000/md/

**GitHub**: https://github.com/baofule/md

---

Made with ❤️ using Hugo and the Paper Theme
