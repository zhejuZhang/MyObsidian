# Marp - Markdown幻灯片

## Marp是什么

Marp (Markdown Presentation Ecosystem) 是用Markdown写幻灯片的工具链。语法极简，可导出PDF/HTML/PPTX，适合快速制作和版本控制。

## 快速开始

### 安装
```bash
# npm安装CLI
npm install -g @marp-team/marp-cli

# 或使用VS Code插件
# 搜索 "Marp for VS Code"

# 验证
marp --version
```

### 最小示例
```markdown
---
marp: true
theme: default
paginate: true
size: 16:9
---

# 论文标题

作者姓名 \
机构名称 \
日期

---

## 研究背景

- 背景信息一
- 背景信息二
- 背景信息三

---

## 方法

<!-- 分栏 -->
<div class="columns">
<div>

### 步骤

1. 数据收集
2. 特征提取
3. 模型训练

</div>
<div>

![方法示意图](method.png)

</div>
</div>

---

## 结果

| 方法 | 准确率 | F1 |
|------|--------|-----|
| Baseline | 0.82 | 0.79 |
| Ours | **0.91** | **0.88** |

---

## 谢谢！

Q&A
```

### 编译导出
```bash
# 导出PDF
marp slides.md --pdf

# 导出HTML
marp slides.md --html

# 导出PPTX
marp slides.md --pptx

# 监听模式（自动编译）
marp slides.md --watch

# 启动本地服务器预览
marp slides.md --server
```

## 核心语法

### Front Matter配置
```yaml
---
marp: true
theme: default          # 主题: default, gaia, uncover
paginate: true          # 显示页码
size: 16:9              # 宽高比: 16:9, 4:3
backgroundColor: white  # 背景色
color: black            # 文字色
style: |
  section {
    font-size: 28px;
  }
---
```

### 分页
```markdown
# 第一页

---

# 第二页

---

# 第三页
```

### 标题层级
```markdown
<!-- _class: lead -->

# 一级标题（封面用）

## 二级标题（章节标题）

### 三级标题（页面标题）
```

### 列表
```markdown
- 无序列表项一
- 无序列表项二
  - 子项一
  - 子项二

1. 有序列表项一
2. 有序列表项二

- [ ] 待办事项
- [x] 已完成
```

### 表格
```markdown
| 列1 | 列2 | 列3 |
|-----|-----|-----|
| A   | 1   | X   |
| B   | 2   | Y   |
```

### 代码块
````markdown
```python
def hello():
    print("Hello, Marp!")
```

```javascript
console.log("Hello!");
```
````

### 数学公式
```markdown
行内公式：$E = mc^2$

块级公式：

$$
\sum_{i=1}^{n} x_i = x_1 + x_2 + ... + x_n
$$
```

## 高级功能

### 分栏布局
```markdown
<!-- 使用HTML -->
<div style="display: flex; gap: 2em;">
<div style="flex: 1;">

### 左栏

- 要点一
- 要点二

</div>
<div style="flex: 1;">

### 右栏

![图](image.png)

</div>
</div>
```

### 背景图片
```markdown
<!-- ![](bg.png) -->

<!-- 或使用directive -->
<!-- _backgroundImage: url("bg.png") -->
<!-- _backgroundColor: "#233" -->
```

### 动画（逐步显示）
```markdown
<!-- 使用列表动画 -->

- <!-- --> 第一步
- <!-- --> 第二步
- <!-- --> 第三步

<!-- 或使用marp-cli的 --html 选项配合JS -->
```

### 自定义样式
```markdown
---
marp: true
theme: default
style: |
  section {
    font-family: 'Noto Sans SC', sans-serif;
  }
  h1 {
    color: #2563eb;
    text-align: center;
  }
  table {
    font-size: 0.8em;
  }
  .columns {
    display: flex;
    gap: 2em;
  }
---
```

## 主题

### 内置主题
| 主题 | 风格 | 特点 |
|------|------|------|
| `default` | 简洁白底 | 通用 |
| `gaia` | 暖色调 | 优雅 |
| `uncover` | 暗色极简 | 现代 |

### 使用主题
```markdown
---
marp: true
theme: gaia
---

# 使用Gaia主题
```

### 安装社区主题
```bash
# 从npm安装
npm install @marp-team/marp-theme-xxx

# 在front matter中使用
---
marp: true
theme: xxx
---
```

### 推荐自定义主题
```markdown
---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;700&display=swap');
  
  section {
    font-family: 'Noto Sans SC', 'Segoe UI', sans-serif;
    font-size: 28px;
    padding: 40px 60px;
  }
  
  section.lead {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
  }
  
  h1 {
    font-size: 2.5em;
    color: #1e40af;
    margin-bottom: 0.5em;
  }
  
  h2 {
    color: #1e40af;
    border-bottom: 3px solid #1e40af;
    padding-bottom: 0.2em;
  }
  
  table {
    width: 100%;
    font-size: 0.85em;
  }
  
  th {
    background: #1e40af;
    color: white;
  }
  
  blockquote {
    border-left: 5px solid #1e40af;
    background: #eff6ff;
    padding: 0.5em 1em;
  }
  
  code {
    background: #f1f5f9;
    padding: 0.1em 0.3em;
    border-radius: 3px;
  }
  
  pre code {
    background: #1e293b;
    color: #e2e8f0;
    padding: 1em;
    display: block;
    border-radius: 8px;
  }
---

<!-- _class: lead -->

# 论文标题

作者姓名 \
机构名称 \
2025年1月
```

## VS Code工作流

### 插件配置
```json
// settings.json
{
  "markdown.marp.enableHtml": true,
  "markdown.marp.themes": [
    "https://example.com/custom-theme.css"
  ]
}
```

### 快捷键
| 快捷键 | 功能 |
|--------|------|
| `Ctrl+Shift+V` | 预览Markdown |
| `Ctrl+K V` | 侧边预览 |
| `Ctrl+Shift+P` → Marp | Marp命令面板 |

## 导出选项

```bash
# PDF（需要Chrome/Edge）
marp slides.md --pdf --allow-local-files

# HTML（单文件）
marp slides.md --html --output slides.html

# PPTX
marp slides.md --pptx --output slides.pptx

# 带自定义设置
marp slides.md \
  --theme custom.css \
  --html \
  --output slides.html \
  --description "我的幻灯片"
```

## 实用技巧

### 注释与隐藏
```markdown
<!-- 这是HTML注释，不会显示 -->

<!-- _class: lead -->
<!-- 这是Marp directive，控制样式 -->

<!--
多行注释
可以写很多内容
-->
```

### 图片尺寸
```markdown
<!-- Markdown语法 -->
![w:300](image.png)

<!-- 或使用HTML -->
<img src="image.png" width="300">

<!-- 背景图 -->
![bg fit](background.jpg)
![bg contain:60%](logo.png)
```

### 页面样式切换
```markdown
<!-- _class: lead -->
<!-- _paginate: false -->
<!-- _footer: "" -->

# 封面页
无页码、无页脚

---

<!-- _class: default -->
<!-- _paginate: true -->

# 正常页面
有页码
```

## 相关链接

- [Marp官方文档](https://marp.app/)
- [Marp CLI](https://github.com/marp-team/marp-cli)
- [Marp主题集合](https://github.com/marp-team/marp/issues/190)

## 相关链接

- [[10-学术PPT技能体系总览]] - 返回总览
- [[12-Typst幻灯片]] - 更强排版能力
- [[14-reveal-js]] - Web技术方案
