# PPT设计与可视化

## 设计原则

### 学术PPT设计黄金法则
```
1. 一致性 — 统一字体、颜色、布局
2. 对齐 — 所有元素严格对齐
3. 对比 — 主次分明，突出重点
4. 留白 — 不要填满每一寸空间
5. 简约 — 每页只传达一个核心信息
```

### 字体选择
| 场景 | 中文字体 | 英文字体 |
|------|---------|---------|
| 标题 | 思源黑体 Bold | Montserrat Bold |
| 正文 | 思源黑体 Regular | Open Sans |
| 代码 | 等距更纱黑体 | Fira Code |
| 数据 | DIN | Roboto Mono |

### 字号规范
```
标题:     32-44pt
副标题:   24-28pt
正文:     20-24pt
注释:     14-16pt
页码:     10-12pt
```

### 配色方案

**学术蓝（推荐）**
```
主色:    #1e40af (深蓝)
次色:    #3b82f6 (亮蓝)
强调:    #f59e0b (金色)
背景:    #ffffff (白色)
文字:    #1e293b (深灰)
```

**科技紫**
```
主色:    #7c3aed (紫色)
次色:    #a78bfa (浅紫)
强调:    #10b981 (绿色)
背景:    #f8fafc (浅灰)
文字:    #1e293b (深灰)
```

**Nature风格**
```
主色:    #c62828 (红色)
次色:    #455a64 (灰蓝)
强调:    #2e7d32 (绿色)
背景:    #ffffff (白色)
文字:    #212121 (黑色)
```

## 数据可视化

### matplotlib生成幻灯片用图表
```python
import matplotlib.pyplot as plt
import numpy as np

# 学术风格配置
plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 16,
    'axes.labelsize': 18,
    'axes.titlesize': 20,
    'xtick.labelsize': 14,
    'ytick.labelsize': 14,
    'legend.fontsize': 14,
    'figure.figsize': (10, 6),
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.transparent': False,
})

# 柱状图
fig, ax = plt.subplots()
methods = ['Baseline', 'Method A', 'Method B', 'Ours']
scores = [0.82, 0.85, 0.87, 0.91]
colors = ['#94a3b8', '#94a3b8', '#94a3b8', '#1e40af']
bars = ax.bar(methods, scores, color=colors, edgecolor='white', linewidth=2)

# 添加数值标签
for bar, score in zip(bars, scores):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01,
            f'{score:.2f}', ha='center', va='bottom', fontweight='bold')

ax.set_ylabel('Accuracy')
ax.set_ylim(0.75, 0.95)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.savefig('bar_chart.png')
plt.close()
```

### Plotly交互式图表
```python
import plotly.graph_objects as go

fig = go.Figure(data=[
    go.Bar(name='Accuracy', x=methods, y=scores,
           marker_color=['#94a3b8']*3 + ['#1e40af'])
])

fig.update_layout(
    font=dict(family="Arial", size=18),
    plot_bgcolor='white',
    yaxis=dict(range=[0.75, 0.95], gridcolor='#e2e8f0'),
    xaxis=dict(showgrid=False),
    margin=dict(l=80, r=40, t=40, b=80),
    width=800,
    height=500,
)

fig.write_image('bar_chart.png', scale=2)
```

### Seaborn统计图
```python
import seaborn as sns
import pandas as pd

# 箱线图
df = pd.DataFrame({
    'Method': np.repeat(['A', 'B', 'C', 'Ours'], 50),
    'Score': np.concatenate([
        np.random.normal(0.82, 0.05, 50),
        np.random.normal(0.85, 0.04, 50),
        np.random.normal(0.87, 0.04, 50),
        np.random.normal(0.91, 0.03, 50),
    ])
})

fig, ax = plt.subplots(figsize=(10, 6))
palette = ['#94a3b8', '#94a3b8', '#94a3b8', '#1e40af']
sns.boxplot(data=df, x='Method', y='Score', palette=palette, ax=ax)
sns.stripplot(data=df, x='Method', y='Score', color='black', 
              alpha=0.3, size=4, ax=ax)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.savefig('boxplot.png', dpi=300, bbox_inches='tight')
```

## 流程图与架构图

### draw.io / diagrams.net
```
使用场景:
├── 系统架构图
├── 流程图
├── 数据流图
├── 网络拓扑图
└── UML图

导出选项:
├── SVG (推荐，矢量)
├── PNG (位图)
└── PDF

在线使用: https://app.diagrams.net
```

### Excalidraw手绘风格
```markdown
# 在Obsidian中使用Excalidraw插件
# 优点：手绘风格，学术海报常用

# 导出为SVG/PNG后插入幻灯片
```

### Mermaid流程图
```markdown
<!-- 在Marp中使用 -->
```mermaid
graph LR
    A[输入] --> B[预处理]
    B --> C[特征提取]
    C --> D[模型]
    D --> E[输出]
```
```

### TikZ (LaTeX/Beamer)
```latex
\usetikzlibrary{shapes,arrows,positioning}

\begin{tikzpicture}[
    node distance=2cm,
    block/.style={rectangle, draw, fill=blue!20, 
                  text width=5em, text centered, rounded corners},
    line/.style={draw, -latex}
]
    \node [block] (input) {输入};
    \node [block, right of=input] (process) {处理};
    \node [block, right of=process] (output) {输出};
    
    \path [line] (input) -- (process);
    \path [line] (process) -- (output);
\end{tikzpicture}
```

### Typst CeTZ
```typst
#import "@preview/cetz:0.2.2": *

#canvas({
  import draw: *
  
  // 流程图
  let box(pos, name, content, color: blue) = {
    rect(pos, (pos.at(0) + 2.5, pos.at(1) + 0.8), 
         name: name, fill: color.lighten(80%), stroke: color, radius: 4pt)
    content(name, text(size: 14pt, content))
  }
  
  box((0, 0), "input", "输入")
  box((4, 0), "process", "处理", color: green)
  box((8, 0), "output", "输出", color: red)
  
  line("input", "process", mark: (end: ">"))
  line("process", "output", mark: (end: ">"))
})
```

## 图表设计原则

### 图表选择指南
```
展示什么？
├── 比较 → 柱状图、条形图
├── 趋势 → 折线图、面积图
├── 分布 → 直方图、箱线图、小提琴图
├── 相关 → 散点图、热力图
├── 组成 → 饼图、堆叠柱状图（慎用）
└── 地理 → 地图
```

### 饼图替代方案
```
避免使用饼图的原因:
├── 人眼不擅长比较角度
├── 超过5个类别难以区分
└── 难以比较不同饼图

替代方案:
├── 水平条形图 (推荐)
├── 堆叠条形图
└── 树状图
```

### 颜色使用
```python
# 色盲友好调色板
colorblind_friendly = {
    'blue': '#0072B2',
    'orange': '#E69F00',
    'green': '#009E73',
    'red': '#D55E00',
    'purple': '#CC79A7',
    'cyan': '#56B4E9',
    'yellow': '#F0E442',
}

# 序列色板（单变量）
sequential = ['#f7fbff', '#deebf7', '#c6dbef', '#9ecae1', 
              '#6baed6', '#4292c6', '#2171b5', '#08519c', '#08306b']

# 发散色板（正负）
diverging = ['#b2182b', '#d6604d', '#f4a582', '#fddbc7',
             '#f7f7f7',
             '#d1e5f0', '#92c5de', '#4393c3', '#2166ac']
```

## 表格设计

### 三线表（学术标准）
```
设计要点:
├── 只有三条横线（顶线、栏目线、底线）
├── 无竖线
├── 表头加粗或灰色背景
└── 数字右对齐，文字左对齐
```

### 表格替代方案
```
避免表格的情况:
├── 只有1-2列数据 → 用文字表述
├── 数据适合可视化 → 用图表
└── 比较多组数据 → 用分组柱状图
```

## 排版技巧

### 对齐网格
```
使用4px或8px网格系统:
├── 元素间距: 8px的倍数
├── 边距: 24px或32px
├── 文本行高: 字号的1.2-1.5倍
└── 元素对齐: 使用参考线
```

### 视觉层次
```
层次结构:
├── 一级: 标题 (最大、最粗、对比色)
├── 二级: 小标题 (中等、次色)
├── 三级: 正文 (常规)
└── 四级: 注释 (最小、灰色)

实现手段:
├── 字号大小
├── 字重粗细
├── 颜色对比
└── 空间位置
```

### 留白
```
留白的作用:
├── 分组相关内容
├── 突出重点信息
├── 提高可读性
└── 创造呼吸感

实践建议:
├── 页面边距: 至少10%
├── 元素间距: 大于元素内部间距
├── 段落间距: 大于行间距
└── 不要害怕空白
```

## 相关链接

- [[10-学术PPT技能体系总览]] - 返回总览
- [[02-数据分析与可视化#可视化最佳实践|数据可视化]] - 详细图表规范
- [[16-AI辅助PPT制作]] - AI辅助设计
