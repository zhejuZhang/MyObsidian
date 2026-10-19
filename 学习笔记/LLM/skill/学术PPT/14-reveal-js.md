# reveal.js

## reveal.js是什么

reveal.js是最流行的HTML幻灯片框架，基于Web技术，支持丰富的动画和交互效果。适合技术分享和在线演示。

## 快速开始

### 方式一：直接下载
```bash
# 克隆仓库
git clone https://github.com/hakimel/reveal.js.git
cd reveal.js

# 安装依赖
npm install

# 启动服务器
npm start
# 访问 http://localhost:8000
```

### 方式二：CDN引入
```html
<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5/dist/reveal.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5/dist/theme/white.css">
</head>
<body>
  <div class="reveal">
    <div class="slides">
      <section>
        <h1>论文标题</h1>
        <p>作者姓名</p>
      </section>
      <section>
        <h2>研究背景</h2>
        <ul>
          <li>要点一</li>
          <li>要点二</li>
        </ul>
      </section>
    </div>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/reveal.js@5/dist/reveal.js"></script>
  <script>Reveal.initialize();</script>
</body>
</html>
```

## 核心语法

### 基础结构
```html
<div class="reveal">
  <div class="slides">
    <!-- 水平页面 -->
    <section>页面1</section>
    <section>页面2</section>
    
    <!-- 垂直页面（嵌套） -->
    <section>
      <section>垂直1-1</section>
      <section>垂直1-2</section>
    </section>
  </div>
</div>
```

### 内容元素
```html
<!-- 标题 -->
<h1>一级标题</h1>
<h2>二级标题</h2>

<!-- 段落 -->
<p>正文内容</p>

<!-- 列表 -->
<ul>
  <li>无序列表</li>
  <li>项目二</li>
</ul>

<ol>
  <li>有序列表</li>
  <li>项目二</li>
</ol>

<!-- 引用 -->
<blockquote>
  "引用内容"
</blockquote>

<!-- 代码 -->
<pre><code class="language-python">
def hello():
    print("Hello!")
</code></pre>

<!-- 表格 -->
<table>
  <thead><tr><th>列1</th><th>列2</th></tr></thead>
  <tbody><tr><td>A</td><td>B</td></tr></tbody>
</table>
```

### 图片与媒体
```html
<!-- 图片 -->
<img src="figure.png" alt="描述" width="60%">

<!-- 背景图片 -->
<section data-background-image="bg.jpg">
  <h2>带背景的页面</h2>
</section>

<!-- 视频 -->
<video data-autoplay src="demo.mp4"></video>

<!-- iframe嵌入 -->
<iframe src="https://example.com" width="80%" height="400"></iframe>
```

## 动画效果

### Fragment动画
```html
<!-- 逐步显示 -->
<section>
  <p class="fragment">第一步显示</p>
  <p class="fragment">第二步显示</p>
  <p class="fragment">第三步显示</p>
</section>

<!-- 动画类型 -->
<p class="fragment fade-in">淡入</p>
<p class="fragment fade-out">淡出</p>
<p class="fragment fade-up">上浮</p>
<p class="fragment fade-down">下沉</p>
<p class="fragment fade-left">左入</p>
<p class="fragment fade-right">右入</p>
<p class="fragment grow">放大</p>
<p class="fragment shrink">缩小</p>
<p class="fragment highlight-current-blue">高亮当前</p>
<p class="fragment strike">删除线</p>

<!-- 组合动画 -->
<p class="fragment fade-up" data-fragment-index="1">先显示</p>
<p class="fragment fade-up" data-fragment-index="2">后显示</p>
```

### 列表动画
```html
<ul>
  <li class="fragment">第一项</li>
  <li class="fragment">第二项</li>
  <li class="fragment">第三项</li>
</ul>
```

## 配置选项

### 基础配置
```javascript
Reveal.initialize({
  hash: true,                    // URL hash导航
  slideNumber: true,             // 显示页码
  width: 1920,                   // 宽度
  height: 1080,                  // 高度
  margin: 0.04,                  // 边距
  transition: 'slide',           // 切换效果: none/fade/slide/convex/concave/zoom
  transitionSpeed: 'default',    // 切换速度
  backgroundTransition: 'fade',  // 背景切换效果
  center: true,                  // 垂直居中
  progress: true,                // 进度条
  controls: true,                // 控制按钮
  embedded: false,               // 嵌入模式
  autoPlayMedia: null,           // 自动播放媒体
  preloadIframes: true,          // 预加载iframe
});
```

### 键盘快捷键
| 快捷键 | 功能 |
|--------|------|
| `→` / `Space` | 下一页 |
| `←` | 上一页 |
| `↑` | 上一垂直页 |
| `↓` | 下一垂直页 |
| `Esc` | 总览模式 |
| `S` | 演讲者视图 |
| `F` | 全屏 |
| `O` | 总览 |
| `B` | 暂停（黑屏） |

## 主题

### 内置主题
| 主题 | 风格 |
|------|------|
| `white` | 白底（默认） |
| `black` | 黑底 |
| `league` | 深蓝 |
| `beige` | 米色 |
| `night` | 暗色 |
| `serif` | 衬线字体 |
| `simple` | 极简 |
| `solarized` | Solarized配色 |
| `moon` | 月球暗色 |
| `dracula` | Dracula配色 |

```html
<link rel="stylesheet" href="dist/theme/white.css">
```

### 自定义主题
```css
/* custom-theme.css */
:root {
  --r-background-color: #ffffff;
  --r-main-font: 'Noto Sans SC', sans-serif;
  --r-main-color: #1e293b;
  --r-heading-font: 'Noto Sans SC', sans-serif;
  --r-heading-color: #1e40af;
  --r-heading1-size: 2.5em;
  --r-heading2-size: 1.8em;
  --r-link-color: #2563eb;
  --r-link-color-hover: #1d4ed8;
  --r-selection-background-color: #bfdbfe;
}

.reveal h1 { border-bottom: 3px solid #1e40af; padding-bottom: 0.2em; }
.reveal h2 { color: #1e40af; }
.reveal table th { background: #1e40af; color: white; }
.reveal blockquote { border-left: 5px solid #1e40af; background: #eff6ff; }
```

## 代码高亮

```html
<script src="https://cdn.jsdelivr.net/npm/reveal.js@5/plugin/highlight/highlight.js"></script>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5/plugin/highlight/monokai.css">

<pre><code class="language-python" data-trim data-noescape>
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
</code></pre>
```

## 数学公式

```html
<script src="https://cdn.jsdelivr.net/npm/reveal.js@5/plugin/math/math.js"></script>
<script>
  Reveal.initialize({
    plugins: [RevealMath.KaTeX]
  });
</script>

<section>
  <h2>公式示例</h2>
  <p>
    质能方程: \( E = mc^2 \)
  </p>
  <p>
    $$\sum_{i=1}^{n} x_i = x_1 + x_2 + ... + x_n$$
  </p>
</section>
```

## 演讲者视图

```html
<!-- 按S键打开演讲者视图 -->
<!-- 显示：当前幻灯片、下一张幻灯片、备注、计时器 -->

<section>
  <h2>页面标题</h2>
  <p>正文内容</p>
  <aside class="notes">
    这是演讲者备注。
    观众看不到这些内容。
  </aside>
</section>
```

## Markdown模式

```html
<section data-markdown>
  <textarea data-template>
    ## 页面标题
    
    - 要点一
    - 要点二
    
    $$E = mc^2$$
  </textarea>
</section>

<!-- 外部Markdown文件 -->
<section data-markdown="slides.md"
         data-separator="^\n---\n$"
         data-separator-vertical="^\n--\n$">
</section>
```

## 插件系统

```javascript
Reveal.initialize({
  plugins: [
    RevealMarkdown,    // Markdown支持
    RevealHighlight,   // 代码高亮
    RevealNotes,       // 演讲者备注
    RevealMath,        // 数学公式
    RevealZoom,        // 缩放
    RevealSearch,      // 搜索
    RevealMermaid,     // Mermaid图表
  ]
});
```

## 部署与分享

### 静态托管
```bash
# 构建静态文件
npm run build

# 部署到GitHub Pages
# 或使用Vercel/Netlify
```

### 导出PDF
```bash
# 安装puppeteer
npm install puppeteer

# 导出
node print.js --output slides.pdf
```

## 与其他方案对比

| 特性 | reveal.js | Beamer | Marp |
|------|-----------|--------|------|
| 格式 | HTML | PDF | PDF/HTML |
| 动画 | 优秀 | 基础 | 基础 |
| 交互 | 强 | 无 | 无 |
| 学习曲线 | 中 | 高 | 低 |
| 数学公式 | KaTeX/MathJax | 原生 | KaTeX |
| 代码高亮 | 原生 | 需配置 | 原生 |
| 离线使用 | 需服务器 | 纯PDF | 纯PDF |
| 版本控制 | ✅ | ✅ | ✅ |

## 相关链接

- [reveal.js官网](https://revealjs.com/)
- [reveal.js文档](https://revealjs.com/markdown/)
- [reveal.js主题](https://revealjs.com/themes/)

## 相关链接

- [[10-学术PPT技能体系总览]] - 返回总览
- [[13-Marp-Markdown幻灯片]] - 更简单的Markdown方案
- [[16-AI辅助PPT制作]] - AI生成内容
