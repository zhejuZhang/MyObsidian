# reveal.js 使用教程

## 一、安装

### 1.1 方式一：克隆仓库（推荐）
```bash
# 克隆仓库
git clone https://github.com/hakimel/reveal.js.git
cd reveal.js

# 安装依赖
npm install

# 启动开发服务器
npm start
# 访问 http://localhost:8000
```

### 1.2 方式二：CDN 引入（无需安装）
直接创建 HTML 文件，通过 CDN 引入即可。

### 1.3 方式三：npm 安装到项目
```bash
npm install reveal.js
```

---

## 二、快速开始

### 2.1 最小 HTML 模板

创建 `index.html`：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>我的幻灯片</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5/dist/reveal.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5/dist/theme/white.css">
</head>
<body>
  <div class="reveal">
    <div class="slides">
      <section>
        <h1>论文标题</h1>
        <p>作者姓名 | 机构 | 2025</p>
      </section>
      <section>
        <h2>研究背景</h2>
        <ul>
          <li>要点一</li>
          <li>要点二</li>
          <li>要点三</li>
        </ul>
      </section>
    </div>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/reveal.js@5/dist/reveal.js"></script>
  <script>
    Reveal.initialize({
      hash: true,
      slideNumber: true,
      transition: 'slide'
    });
  </script>
</body>
</html>
```

### 2.2 本地预览
```bash
# 使用 reveal.js 自带服务器
npm start

# 或使用 Python 简易服务器
python -m http.server 8000

# 或使用 VS Code Live Server 插件
```

---

## 三、核心语法

### 3.1 基本结构

```html
<div class="reveal">
  <div class="slides">
    <!-- 水平页面（左右切换） -->
    <section>页面 1</section>
    <section>页面 2</section>
    
    <!-- 垂直页面（上下切换） -->
    <section>
      <section>垂直 1-1</section>
      <section>垂直 1-2</section>
    </section>
  </div>
</div>
```

### 3.2 内容元素

#### 标题
```html
<h1>一级标题</h1>
<h2>二级标题</h2>
<h3>三级标题</h3>
```

#### 段落
```html
<p>正文内容</p>
<p>
  多行文本可以
  分行书写
</p>
```

#### 列表
```html
<!-- 无序列表 -->
<ul>
  <li>项目一</li>
  <li>项目二</li>
  <li>项目三</li>
</ul>

<!-- 有序列表 -->
<ol>
  <li>第一步</li>
  <li>第二步</li>
  <li>第三步</li>
</ol>

<!-- 嵌套列表 -->
<ul>
  <li>
    项目一
    <ul>
      <li>子项目</li>
    </ul>
  </li>
</ul>
```

#### 表格
```html
<table>
  <thead>
    <tr>
      <th>方法</th>
      <th>准确率</th>
      <th>F1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Baseline</td>
      <td>0.85</td>
      <td>0.82</td>
    </tr>
    <tr>
      <td><strong>Ours</strong></td>
      <td><strong>0.91</strong></td>
      <td><strong>0.89</strong></td>
    </tr>
  </tbody>
</table>
```

#### 引用
```html
<blockquote>
  "这是一段引用文字。"
  <br>—— 作者
</blockquote>
```

#### 代码
```html
<!-- 行内代码 -->
<p>使用 <code>print()</code> 函数输出</p>

<!-- 代码块 -->
<pre><code class="language-python">
import numpy as np

def mean(data):
    return np.mean(data)
</code></pre>

<!-- 带行号和高亮 -->
<pre><code class="language-python" data-line-numbers="2-3">
def hello():
    # 这行会被高亮
    print("Hello!")
    return True
</code></pre>
```

### 3.3 图片

```html
<!-- 基本图片 -->
<img src="figure.png" alt="描述">

<!-- 控制大小 -->
<img src="figure.png" width="60%">

<!-- 带标题 -->
<figure>
  <img src="result.png" width="70%">
  <figcaption>图1：实验结果对比</figcaption>
</figure>
```

### 3.4 链接

```html
<!-- 外部链接 -->
<a href="https://example.com">链接文字</a>

<!-- 页面内跳转 -->
<a href="#/3">跳转到第4页</a>
```

---

## 四、配置选项

### 4.1 初始化配置

```javascript
Reveal.initialize({
  // 基础设置
  hash: true,                    // URL hash 导航
  slideNumber: true,             // 显示页码
  width: 1920,                   // 宽度 (px)
  height: 1080,                  // 高度 (px)
  margin: 0.04,                  // 边距比例
  center: true,                  // 垂直居中
  
  // 切换效果
  transition: 'slide',           // none/fade/slide/convex/concave/zoom
  transitionSpeed: 'default',    // default/fast/slow
  backgroundTransition: 'fade',  // 背景切换效果
  
  // 显示元素
  progress: true,                // 进度条
  controls: true,                // 控制按钮
  controlsTutorial: true,        // 控制提示
  controlsLayout: 'bottom-right', // 控制按钮位置
  
  // 自动播放
  autoSlide: 0,                  // 自动播放间隔 (ms), 0=禁用
  loop: false,                   // 循环播放
  
  // 其他
  embedded: false,               // 嵌入模式
  preloadIframes: true,          // 预加载 iframe
  autoPlayMedia: null,           // 自动播放媒体
  pdfMaxPagesPerSlide: 1,        // PDF 每页最大数
  pdfSeparateFragments: false,   // PDF 分离动画
});
```

### 4.2 键盘快捷键

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
| `G` | 跳转到页码 |
| `Ctrl+Shift+F` | 搜索 |

---

## 五、动画效果

### 5.1 Fragment 动画

```html
<!-- 基本逐步显示 -->
<section>
  <p class="fragment">第一步显示</p>
  <p class="fragment">第二步显示</p>
  <p class="fragment">第三步显示</p>
</section>
```

### 5.2 动画类型

```html
<!-- 淡入 -->
<p class="fragment fade-in">淡入</p>

<!-- 淡出 -->
<p class="fragment fade-out">淡出</p>

<!-- 方向性淡入 -->
<p class="fragment fade-up">上浮</p>
<p class="fragment fade-down">下沉</p>
<p class="fragment fade-left">左入</p>
<p class="fragment fade-right">右入</p>

<!-- 缩放 -->
<p class="fragment grow">放大</p>
<p class="fragment shrink">缩小</p>

<!-- 高亮 -->
<p class="fragment highlight-current-blue">高亮当前蓝色</p>
<p class="fragment highlight-red">高亮红色</p>
<p class="fragment highlight-green">高亮绿色</p>

<!-- 删除线 -->
<p class="fragment strike">删除线</p>
```

### 5.3 控制显示顺序

```html
<section>
  <p class="fragment" data-fragment-index="3">第三个显示</p>
  <p class="fragment" data-fragment-index="1">第一个显示</p>
  <p class="fragment" data-fragment-index="2">第二个显示</p>
</section>
```

### 5.4 列表逐步显示

```html
<section>
  <ul>
    <li class="fragment">第一项</li>
    <li class="fragment">第二项</li>
    <li class="fragment">第三项</li>
  </ul>
</section>
```

---

## 六、主题

### 6.1 内置主题

```html
<!-- 在 head 中引入主题 CSS -->
<link rel="stylesheet" href="dist/theme/white.css">

<!-- 可用主题 -->
<!-- white (默认), black, league, beige, night, serif, 
     simple, solarized, moon, dracula -->
```

### 6.2 自定义主题

创建 `css/custom-theme.css`：

```css
:root {
  --r-background-color: #ffffff;
  --r-main-font: 'Microsoft YaHei', sans-serif;
  --r-main-color: #1e293b;
  --r-heading-font: 'Microsoft YaHei', sans-serif;
  --r-heading-color: #1e40af;
  --r-heading1-size: 2.5em;
  --r-heading2-size: 1.8em;
  --r-heading3-size: 1.3em;
  --r-link-color: #2563eb;
  --r-link-color-hover: #1d4ed8;
  --r-selection-background-color: #bfdbfe;
}

/* 自定义样式 */
.reveal h1 {
  border-bottom: 3px solid #1e40af;
  padding-bottom: 0.2em;
}

.reveal h2 {
  color: #1e40af;
}

.reveal table {
  font-size: 0.8em;
  border-collapse: collapse;
  width: 100%;
}

.reveal table th {
  background: #1e40af;
  color: white;
  padding: 0.5em;
}

.reveal table td {
  padding: 0.5em;
  border-bottom: 1px solid #e2e8f0;
}

.reveal blockquote {
  border-left: 5px solid #1e40af;
  background: #eff6ff;
  padding: 0.5em 1em;
  font-style: italic;
}

.reveal pre {
  box-shadow: none;
}

.reveal pre code {
  background: #1e293b;
  color: #e2e8f0;
  padding: 1em;
  border-radius: 8px;
  font-size: 0.75em;
  max-height: 500px;
}
```

使用自定义主题：

```html
<link rel="stylesheet" href="css/custom-theme.css">
```

---

## 七、插件

### 7.1 加载插件

```html
<script src="https://cdn.jsdelivr.net/npm/reveal.js@5/dist/reveal.js"></script>
<script src="https://cdn.jsdelivr.net/npm/reveal.js@5/plugin/markdown/markdown.js"></script>
<script src="https://cdn.jsdelivr.net/npm/reveal.js@5/plugin/highlight/highlight.js"></script>
<script src="https://cdn.jsdelivr.net/npm/reveal.js@5/plugin/notes/notes.js"></script>
<script src="https://cdn.jsdelivr.net/npm/reveal.js@5/plugin/math/math.js"></script>
<script src="https://cdn.jsdelivr.net/npm/reveal.js@5/plugin/zoom/zoom.js"></script>
<script src="https://cdn.jsdelivr.net/npm/reveal.js@5/plugin/search/search.js"></script>

<script>
  Reveal.initialize({
    plugins: [
      RevealMarkdown,
      RevealHighlight,
      RevealNotes,
      RevealMath.KaTeX,
      RevealZoom,
      RevealSearch
    ]
  });
</script>
```

### 7.2 代码高亮

```html
<!-- 引入 highlight.js 插件和主题 -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5/plugin/highlight/monokai.css">

<!-- 使用 -->
<pre><code class="language-python" data-trim data-noescape>
def fibonacci(n):
    """计算斐波那契数列"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 测试
print(fibonacci(10))  # 输出: 55
</code></pre>
```

**选项**：
- `data-trim`：去除首尾空白
- `data-noescape`：不转义 HTML
- `data-line-numbers`：显示行号
- `data-line-numbers="2-3,5"`：高亮指定行

### 7.3 数学公式

```html
<!-- 引入 KaTeX -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>

<script>
  Reveal.initialize({
    plugins: [RevealMath.KaTeX]
  });
</script>

<!-- 使用 -->
<section>
  <h2>数学公式</h2>
  
  <!-- 行内公式 -->
  <p>质能方程: \( E = mc^2 \)</p>
  
  <!-- 块级公式 -->
  <p>
    \[ \sum_{i=1}^{n} x_i = x_1 + x_2 + \cdots + x_n \]
  </p>
  
  <!-- 多行公式 -->
  <p>
    \[
    \begin{aligned}
    \nabla \times \vec{E} &= -\frac{\partial \vec{B}}{\partial t} \\
    \nabla \times \vec{B} &= \mu_0 \vec{J} + \mu_0 \epsilon_0 \frac{\partial \vec{E}}{\partial t}
    \end{aligned}
    \]
  </p>
</section>
```

### 7.4 Markdown 模式

```html
<script>
  Reveal.initialize({
    plugins: [RevealMarkdown]
  });
</script>

<!-- 内联 Markdown -->
<section data-markdown>
  <textarea data-template>
    ## 标题
    
    - 要点一
    - 要点二
    
    $$E = mc^2$$
  </textarea>
</section>

<!-- 外部 Markdown 文件 -->
<section data-markdown="slides.md"
         data-separator="^\n---\n$"
         data-separator-vertical="^\n--\n$">
</section>
```

---

## 八、演讲者视图

### 8.1 使用方法

1. 按 `S` 键打开演讲者视图
2. 显示内容：
   - 当前幻灯片
   - 下一张幻灯片预览
   - 演讲者备注
   - 计时器

### 8.2 添加备注

```html
<section>
  <h2>页面标题</h2>
  <p>正文内容</p>
  
  <aside class="notes">
    这是演讲者备注。
    观众看不到这些内容。
    可以写提示、要点、时间提醒等。
  </aside>
</section>
```

---

## 九、背景设置

### 9.1 颜色背景

```html
<section data-background-color="#1e40af">
  <h2 style="color: white;">深色背景页面</h2>
</section>
```

### 9.2 图片背景

```html
<!-- 基本背景图 -->
<section data-background-image="bg.jpg">
  <h2>带背景的页面</h2>
</section>

<!-- 背景图设置 -->
<section data-background-image="bg.jpg"
          data-background-size="cover"
          data-background-position="center"
          data-background-opacity="0.3">
  <h2>半透明背景</h2>
</section>
```

### 9.3 渐变背景

```html
<section data-background-gradient="linear-gradient(to bottom, #1e40af, #3b82f6)">
  <h2 style="color: white;">渐变背景</h2>
</section>
```

### 9.4 视频背景

```html
<section data-background-video="bg.mp4"
          data-background-video-loop
          data-background-video-muted>
  <h2>视频背景</h2>
</section>
```

---

## 十、导出 PDF

### 10.1 使用打印功能

1. 在幻灯片页面按 `Ctrl+P`（或 `Cmd+P`）
2. 选择"保存为 PDF"
3. 设置：
   - 布局：横向
   - 边距：无
   - 背景图形：勾选

### 10.2 使用 puppeteer

```bash
# 安装 puppeteer
npm install puppeteer

# 创建导出脚本 export-pdf.js
```

```javascript
// export-pdf.js
const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  
  await page.goto('http://localhost:8000', {
    waitUntil: 'networkidle0'
  });
  
  await page.pdf({
    path: 'slides.pdf',
    width: '1920px',
    height: '1080px',
    printBackground: true
  });
  
  await browser.close();
  console.log('PDF exported successfully!');
})();
```

```bash
# 启动服务器
npm start

# 另一个终端运行导出
node export-pdf.js
```

---

## 十一、完整学术示例

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>学术报告</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5/dist/reveal.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5/dist/theme/white.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5/plugin/highlight/monokai.css">
  <style>
    :root {
      --r-heading-color: #1e40af;
    }
    .reveal h1 { border-bottom: 3px solid #1e40af; padding-bottom: 0.2em; }
    .reveal h2 { color: #1e40af; }
    .reveal table th { background: #1e40af; color: white; }
    .reveal blockquote { border-left: 5px solid #1e40af; background: #eff6ff; }
  </style>
</head>
<body>
  <div class="reveal">
    <div class="slides">
      
      <!-- 封面 -->
      <section>
        <h1>论文标题</h1>
        <h3>副标题</h3>
        <p>作者姓名<br>机构名称<br>2025年1月</p>
      </section>
      
      <!-- 目录 -->
      <section>
        <h2>目录</h2>
        <ol>
          <li>研究背景</li>
          <li>研究方法</li>
          <li>实验结果</li>
          <li>结论</li>
        </ol>
      </section>
      
      <!-- 背景 -->
      <section>
        <section>
          <h2>研究背景</h2>
          <blockquote>
            现有方法存在以下局限性...
          </blockquote>
          <aside class="notes">
            详细解释背景问题，强调研究的重要性。
          </aside>
        </section>
        <section>
          <h2>相关工作</h2>
          <ul>
            <li class="fragment">方法 A：准确率 85%</li>
            <li class="fragment">方法 B：准确率 88%</li>
            <li class="fragment">方法 C：准确率 90%</li>
          </ul>
        </section>
      </section>
      
      <!-- 方法 -->
      <section>
        <h2>研究方法</h2>
        <div style="display: flex; gap: 2em;">
          <div style="flex: 1;">
            <h3>步骤</h3>
            <ol>
              <li>数据预处理</li>
              <li>特征提取</li>
              <li>模型训练</li>
            </ol>
          </div>
          <div style="flex: 1;">
            <img src="method.png" width="100%">
          </div>
        </div>
      </section>
      
      <!-- 结果 -->
      <section>
        <h2>实验结果</h2>
        <table>
          <thead>
            <tr><th>方法</th><th>准确率</th><th>F1</th></tr>
          </thead>
          <tbody>
            <tr><td>Baseline</td><td>0.85</td><td>0.82</td></tr>
            <tr><td>Method A</td><td>0.88</td><td>0.85</td></tr>
            <tr><td><strong>Ours</strong></td><td><strong>0.95</strong></td><td><strong>0.93</strong></td></tr>
          </tbody>
        </table>
        <aside class="notes">
          重点解释为什么我们的方法更好。
        </aside>
      </section>
      
      <!-- 结论 -->
      <section>
        <h2>结论</h2>
        <ul>
          <li>提出新方法，准确率达 95%</li>
          <li>在三个数据集上取得最优</li>
          <li>计算效率提升 3 倍</li>
        </ul>
      </section>
      
      <!-- 致谢 -->
      <section>
        <h1>谢谢！</h1>
        <p>Q&A</p>
        <p><small>联系方式：email@example.com</small></p>
      </section>
      
    </div>
  </div>
  
  <script src="https://cdn.jsdelivr.net/npm/reveal.js@5/dist/reveal.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/reveal.js@5/plugin/notes/notes.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/reveal.js@5/plugin/highlight/highlight.js"></script>
  <script>
    Reveal.initialize({
      hash: true,
      slideNumber: true,
      transition: 'slide',
      plugins: [RevealNotes, RevealHighlight]
    });
  </script>
</body>
</html>
```

---

## 十二、常见问题

### Q1: 如何离线使用？
将所有依赖下载到本地，修改 `src` 路径。

### Q2: 如何添加页码？
```javascript
Reveal.initialize({ slideNumber: true });
```

### Q3: 如何全屏？
按 `F` 键。

### Q4: 如何搜索内容？
按 `Ctrl+Shift+F`。

### Q5: 如何导出带动画的 PDF？
使用 puppeteer 导出，设置 `pdfSeparateFragments: true`。

---

## 十三、相关资源

- [reveal.js 官方文档](https://revealjs.com/)
- [reveal.js GitHub](https://github.com/hakimel/reveal.js)
- [reveal.js 示例](https://revealjs.com/examples/)
- [reveal.js 主题](https://revealjs.com/themes/)
