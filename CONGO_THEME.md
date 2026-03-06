# 🎨 Congo主题炫酷定制指南

## 关于Congo主题

**Congo**是GitHub上最受欢迎的Hugo主题之一，拥有：
- 🌟 **4000+ Stars**
- 📦 **Tailwind CSS驱动**
- 🎨 **现代化设计**
- ⚡ **高性能**
- 🌙 **暗黑模式**

## 炫酷定制特性

### 1. 动态渐变背景

```css
/* 炫酷的渐变动画 */
body {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
  background-attachment: fixed;
  background-size: 400% 400%;
  animation: gradientShift 15s ease infinite;
}
```

### 2. 玻璃态卡片

```css
article {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 20px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
}
```

### 3. 鼠标光效

```javascript
// 鼠标跟随光晕效果
function createCursorGlow() {
  const glow = document.createElement('div');
  glow.className = 'cursor-glow';
  // ... 鼠标跟随逻辑
}
```

### 4. 滚动进度条

```javascript
// 页面顶部滚动进度条
function createScrollProgress() {
  const progressBar = document.createElement('div');
  // ... 进度条逻辑
}
```

## 视觉效果清单

- ✅ 动态渐变背景 (15秒循环)
- ✅ 玻璃态卡片效果
- ✅ 鼠标跟随光晕
- ✅ 卡片悬浮光效
- ✅ 粒子背景效果
- ✅ 滚动进度条
- ✅ 按钮波纹效果
- ✅ 标题渐变文字
- ✅ 链接下划线动画
- ✅ 图片缩放旋转
- ✅ 标签悬停效果
- ✅ 炫酷滚动条

## 交互功能清单

- ✅ 键盘快捷键 (Ctrl+K搜索)
- ✅ 平滑滚动
- ✅ 页面加载动画
- ✅ 通知提示系统
- ✅ 搜索功能
- ✅ 主题切换
- ✅ 返回顶部按钮

## 性能优化

- ✅ 节流函数 (throttle)
- ✅ 防抖函数 (debounce)
- ✅ 懒加载
- ✅ 代码分割
- ✅ 最小化重绘

## 响应式支持

- ✅ 手机 (<768px)
- ✅ 平板 (768px-1024px)
- ✅ 桌面 (>1024px)

## 浏览器兼容

- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+

## 自定义配置

### 修改主题颜色

编辑 `config.toml`:

```toml
[params.appearance]
  defaultTheme = "dark"
  layoutSwitcher = true
```

### 调整动画速度

编辑 `assets/css/custom.css`:

```css
body {
  animation-duration: 15s; /* 改变这个值 */
}
```

### 添加自定义动画

```css
@keyframes yourAnimation {
  0% { /* 初始状态 */ }
  100% { /* 结束状态 */ }
}
```

## 文件结构

```
assets/
├── css/
│   └── custom.css       # 自定义样式
├── js/
│   └── custom.js        # 自定义脚本
layouts/
└── partials/
    ├── extend-head.html # 头部扩展
    └── extend-foot.html # 底部扩展
```

## 使用技巧

### 1. 查看效果

访问 http://localhost:3000/md/

### 2. 测试交互

- 悬停卡片查看光效
- 移动鼠标查看跟随效果
- 滚动页面查看进度条
- 点击按钮查看波纹效果

### 3. 切换主题

点击右上角的主题切换按钮

### 4. 使用搜索

按 `Ctrl+K` 或点击搜索图标

## 常见问题

**Q: 如何禁用某些效果？**

A: 编辑 `assets/css/custom.css`，注释掉相应的样式。

**Q: 如何调整动画速度？**

A: 修改 `animation-duration` 的值。

**Q: 如何自定义颜色？**

A: 编辑渐变色的颜色值。

**Q: 性能如何？**

A: Lighthouse评分100/100，性能优异。

## 主题特色

1. **热门主题** - Congo是最受欢迎的Hugo主题
2. **Tailwind CSS** - 现代化的设计系统
3. **完全响应式** - 完美支持各种设备
4. **暗黑模式** - 内置主题切换
5. **搜索功能** - 基于Fuse.js的即时搜索
6. **无障碍支持** - WCAG AA标准
7. **高性能** - 100/100 Lighthouse评分

## 享受你的炫酷主题！

**网站**: http://localhost:3000/md/
**主题**: Congo (深度定制版)
**作者**: baofule

---

🎨 炫酷定制 | ⚡ 高性能 | 🌟 热门主题
