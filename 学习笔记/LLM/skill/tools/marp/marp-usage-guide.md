# Marp 使用教程

## 一、安装

### 1.1 安装 Node.js
```bash
# 访问 https://nodejs.org 下载LTS版本
# 验证安装
node --version
npm --version
```

### 1.2 安装 Marp CLI
```bash
# 全局安装
npm install -g @marp-team/marp-cli

# 验证
marp --version
```

### 1.3 VS Code 插件
1. 打开 VS Code
2. 搜索扩展 `marp-team.vscode-marp`
3. 安装并启用

---

## 二、快速开始

### 2.1 创建第一个幻灯片

创建文件 `slides.md`：

```markdown
---
marp: true
theme: default
paginate: true
size: 16:9
---

# 我的第一个幻灯片

姓名 | 机构 | 日期

---

## 目录

1. 研究背景
2. 方法
3. 结果
4. 结论

---

## 研究背景

- 背景要点一
- 背景要点二
- 背景要点三

---

## 谢谢！

Q&A
```

### 2.2 预览与导出
```bash
# 本地预览（自动刷新）
marp slides.md --watch

# 启动本地服务器
marp slides.md --server

# 导出 PDF
marp slides.md --pdf

# 导出 HTML（单文件）
marp slides.md --html

# 导出 PPTX
marp slides.md --pptx
```

---

## 三、核心语法

### 3.1 Front Matter 配置

```yaml
---
marp: true              # 启用Marp
theme: default          # 主题: default, gaia, uncover
paginate: true          # 显示页码
size: 16:9              # 宽高比: 16:9 或 4:3
backgroundColor: white  # 背景色
color: #333             # 文字色
math: katex             # 数学公式引擎
header: "会议名称"       # 页眉
footer: "作者姓名"       # 页脚
---
```

### 3.2 分页

使用三个短横线 `---` 分隔每页幻灯片：

```markdown
# 第一页

---

# 第二页

---

# 第三页
```

### 3.3 标题层级

```markdown
# 一级标题（封面用，最大）
## 二级标题（章节标题）
### 三级标题（页面标题，最小）
```

### 3.4 文本格式

```markdown
**加粗文本**
*斜体文本*
~~删除线~~
`行内代码`

> 引用块
> 可以多行

[链接文字](https://example.com)
```

### 3.5 列表

```markdown
# 无序列表
- 项目一
- 项目二
  - 子项目
  - 子项目

# 有序列表
1. 第一步
2. 第二步
3. 第三步

# 任务列表
- [ ] 待办事项
- [x] 已完成
```

### 3.6 表格

```markdown
| 方法 | 准确率 | F1分数 |
|------|--------|--------|
| A    | 0.85   | 0.82   |
| B    | 0.88   | 0.85   |
| C    | 0.91   | 0.89   |

# 右对齐
| 方法 | 准确率 |
|------|-------:|
| A    |   0.85 |
| B    |   0.91 |
```

### 3.7 代码块

````markdown
```python
import numpy as np

def mean(data):
    return sum(data) / len(data)
```

```javascript
const sum = arr => arr.reduce((a, b) => a + b, 0);
```
````

### 3.8 数学公式

```markdown
# 行内公式
质能方程 $E = mc^2$

# 块级公式
$$
\sum_{i=1}^{n} x_i = x_1 + x_2 + \cdots + x_n
$$

# 多行公式
$$
\begin{aligned}
f(x) &= x^2 + 2x + 1 \\
     &= (x + 1)^2
\end{aligned}
$$
```

---

## 四、布局技巧

### 4.1 分栏布局

```markdown
<div style="display: flex; gap: 2em; align-items: flex-start;">
<div style="flex: 1;">

### 左栏标题

- 要点一
- 要点二
- 要点三

</div>
<div style="flex: 1;">

### 右栏标题

![图](figure.png)

</div>
</div>
```

### 4.2 图片控制

```markdown
# 基本插入
![替代文字](image.png)

# 控制大小
![w:400](image.png)
![h:300](image.png)
![w:50%](image.png)

# 背景图片
![bg](background.jpg)
![bg fit](background.jpg)       # 适应页面
![bg contain](background.jpg)   # 包含完整图片
![bg cover](background.jpg)     # 覆盖整个页面
![bg contain:60%](logo.png)     # 60%透明度
```

### 4.3 页面样式切换

```markdown
<!-- _class: lead -->
<!-- _paginate: false -->
<!-- _footer: "" -->

# 封面页
无页码、无页脚、居中布局

---

<!-- _class: default -->
<!-- _paginate: true -->

# 正常页面
恢复页码显示
```

---

## 五、自定义主题

### 5.1 内联样式

```markdown
---
marp: true
theme: default
style: |
  section {
    font-family: 'Microsoft YaHei', sans-serif;
    font-size: 28px;
  }
  h1 {
    color: #1e40af;
    text-align: center;
    font-size: 2.5em;
  }
  h2 {
    color: #1e40af;
    border-bottom: 3px solid #1e40af;
    padding-bottom: 0.2em;
  }
  table th {
    background: #1e40af;
    color: white;
  }
  blockquote {
    border-left: 5px solid #1e40af;
    background: #eff6ff;
    padding: 0.5em 1em;
  }
---
```

### 5.2 学术风格 CSS 文件

创建 `academic.css`：

```css
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
  border-collapse: collapse;
}

th {
  background: #1e40af;
  color: white;
  padding: 0.5em;
}

td {
  padding: 0.5em;
  border-bottom: 1px solid #e2e8f0;
}

blockquote {
  border-left: 5px solid #1e40af;
  background: #eff6ff;
  padding: 0.5em 1em;
  margin: 1em 0;
}

code {
  background: #f1f5f9;
  padding: 0.1em 0.3em;
  border-radius: 3px;
  font-size: 0.9em;
}

pre code {
  background: #1e293b;
  color: #e2e8f0;
  padding: 1em;
  display: block;
  border-radius: 8px;
  font-size: 0.8em;
}

img {
  max-width: 100%;
  display: block;
  margin: 0 auto;
}
```

使用方式：

```markdown
---
marp: true
theme: default
paginate: true
style: @import url('academic.css')
---
```

或命令行：

```bash
marp slides.md --theme academic.css --pdf
```

---

## 六、VS Code 工作流

### 6.1 插件设置

```json
// .vscode/settings.json
{
  "markdown.marp.enableHtml": true,
  "markdown.marp.themes": [
    "./themes/academic.css"
  ],
  "markdown.marp.exportType": "pdf"
}
```

### 6.2 快捷键

| 快捷键 | 功能 |
|--------|------|
| `Ctrl+Shift+V` | Markdown 预览 |
| `Ctrl+K V` | 侧边预览 |
| `Ctrl+Shift+P` → `Marp` | Marp 命令面板 |

### 6.3 实时预览

1. 打开 `.md` 文件
2. 右上角点击 Marp 图标预览
3. 或使用 `Ctrl+K V` 侧边预览

---

## 七、导出选项

### 7.1 PDF 导出

```bash
# 基础导出
marp slides.md --pdf

# 指定输出文件名
marp slides.md --pdf -o report.pdf

# 允许本地文件
marp slides.md --pdf --allow-local-files

# 设置页面大小
marp slides.md --pdf --pdf-notes
```

**注意**：PDF 导出需要安装 Chrome 或 Edge 浏览器。

### 7.2 HTML 导出

```bash
# 单文件HTML（可离线使用）
marp slides.md --html -o slides.html

# 带自定义设置
marp slides.md --html \
  --title "我的幻灯片" \
  --description "学术报告" \
  --author "作者" \
  -o slides.html
```

### 7.3 PPTX 导出

```bash
# 导出为PowerPoint
marp slides.md --pptx -o slides.pptx
```

### 7.4 图片导出

```bash
# 导出为PNG（每页一张）
marp slides.md --images png

# 导出为JPEG
marp slides.md --images jpeg
```

---

## 八、完整示例模板

### 8.1 学术报告模板

```markdown
---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section {
    font-family: 'Microsoft YaHei', sans-serif;
    font-size: 26px;
  }
  h1 { color: #1e40af; text-align: center; }
  h2 { color: #1e40af; border-bottom: 3px solid #1e40af; }
  table th { background: #1e40af; color: white; }
  blockquote { border-left: 5px solid #1e40af; background: #eff6ff; }
---

<!-- _class: lead -->
<!-- _paginate: false -->

# 基于深度学习的文本分类研究

**作者姓名** \
机构名称 \
2025年1月

---

## 目录

1. 研究背景与动机
2. 研究方法
3. 实验设计
4. 实验结果
5. 结论与展望

---

## 研究背景

### 现有问题
- 传统方法准确率有限
- 特征工程耗时耗力
- 难以处理语义复杂性

### 研究目标
> 提出一种基于 Transformer 的文本分类方法，
> 提升分类准确率并降低人工特征工程成本。

---

## 研究方法

<div style="display: flex; gap: 2em;">
<div style="flex: 1;">

### 模型架构
1. 预训练编码器 (BERT)
2. 注意力池化层
3. 分类头 (MLP)

</div>
<div style="flex: 1;">

### 创新点
- 动态注意力机制
- 多尺度特征融合
- 对比学习损失

</div>
</div>

---

## 实验设计

### 数据集

| 数据集 | 训练集 | 测试集 | 类别数 |
|--------|--------|--------|--------|
| AG News | 120K | 7.6K | 4 |
| IMDB | 25K | 25K | 2 |
| SST-2 | 67K | 1.8K | 2 |

### 评估指标
- 准确率 (Accuracy)
- 精确率 (Precision)
- 召回率 (Recall)
- F1 分数

---

## 实验结果

| 方法 | AG News | IMDB | SST-2 |
|------|---------|------|-------|
| TextCNN | 91.2% | 89.5% | 90.1% |
| LSTM | 92.1% | 90.3% | 91.2% |
| BERT | 94.5% | 93.2% | 93.5% |
| **Ours** | **96.1%** | **95.3%** | **95.8%** |

> 我们的方法在所有数据集上均取得最优结果。

---

## 结论

### 主要贡献
1. 提出了动态注意力池化机制
2. 设计了多尺度特征融合模块
3. 在三个基准数据集上取得 SOTA

### 未来工作
- 扩展到多语言场景
- 探索更高效的预训练方法
- 降低模型计算复杂度

---

<!-- _class: lead -->

# 谢谢！

**Q&A**

联系方式：email@example.com
```

---

## 九、常见问题

### Q1: 中文显示乱码？
确保系统安装了相应字体，或在样式中指定中文字体。

### Q2: 图片不显示？
使用 `--allow-local-files` 参数，或使用绝对路径/URL。

### Q3: PDF 导出失败？
确保安装了 Chrome 或 Edge 浏览器。

### Q4: 如何添加演讲者备注？
```markdown
<!-- 这是HTML注释，不会显示在幻灯片中 -->
<!-- 可以作为简单的备注使用 -->
```

### Q5: 如何插入视频？
导出为 HTML 后，使用 `<video>` 标签：
```html
<video src="demo.mp4" controls width="80%"></video>
```

---

## 十、相关资源

- [Marp 官方文档](https://marp.app/)
- [Marp CLI GitHub](https://github.com/marp-team/marp-cli)
- [Marp 示例](https://marp.app/examples)
- [Marp 主题集合](https://github.com/topics/marp-theme)
