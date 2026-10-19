# Typst幻灯片

## Typst是什么

Typst是LaTeX的现代替代品，编译速度极快（毫秒级），语法简洁，学习曲线低。幻灯片功能通过 `polylux` 或 `touying` 包实现。

## 环境搭建

### 安装Typst
```bash
# Windows (Scoop)
scoop install typst

# macOS
brew install typst

# Cargo (跨平台)
cargo install typst-cli

# 验证
typst --version
```

### VS Code插件
- 安装 `Typst LSP` 插件
- 实时预览、语法高亮、自动补全

## touying包（推荐）

### 最小示例
```typst
#import "@preview/touying:0.5.2": *
#import themes.metropolis: *

#show: metropolis-theme.with(
  aspect-ratio: "16-9",
  footer: self => self.info.institute,
)

#title-slide[
  = 论文标题
  副标题

  #v(2em)

  作者姓名 \
  机构名称 \
  #datetime.today().display()
]

= 引言

== 研究背景

- 背景信息一
- 背景信息二
- 背景信息三

= 方法

== 方法概述

#slide[
  - 步骤一
  - 步骤二
  - 步骤三
][
  #figure(
    image("method.png", width: 80%),
    caption: [方法示意图],
  )
]

= 结论

== 总结

- 结论一
- 结论二

#focus-slide[
  谢谢！
]
```

### 编译
```bash
# 编译为PDF
typst compile slides.typ slides.pdf

# 监听模式（自动编译）
typst watch slides.typ slides.pdf
```

## polylux包

### 基础模板
```typst
#import "@preview/polylux:0.3.1": *

#set page(paper: "presentation-16-9")
#set text(size: 25pt)

#polylux-slide[
  = 论文标题
  
  作者姓名 \
  机构名称 \
  日期
]

#polylux-slide[
  == 研究背景
  
  - 要点一
  - 要点二
  - 要点三
]
```

## 核心语法

### 页面布局
```typst
// 分栏
#slide[
  左栏内容
][
  右栏内容
]

// 指定宽度比例
#slide(align: left)[
  #set par(justify: true)
  较长的文本内容...
][
  #figure(
    image("fig.png", width: 90%),
  )
]
```

### 动画效果
```typst
// 逐步显示
#slide[
  - #pause 第一点
  - #pause 第二点
  - #pause 第三点
]

// touying动画
#touying-fn(repeat: 3, self => {
  let (uncover, only, alternatives) = utils.methods(self)
  
  - #uncover("1-")[始终显示]
  - #uncover("2-")[第2步显示]
  - #uncover("3-")[第3步显示]
})
```

### 数学公式
```typst
// 行内公式
设 $x in RR$，则 $f(x) = x^2 + 1$。

// 块级公式
$ sum_(i=1)^n x_i = x_1 + x_2 + ... + x_n $

// 多行公式
$
  f(x) &= x^2 + 2x + 1 \
       &= (x + 1)^2
$
```

### 图表
```typst
// 图片
#figure(
  image("result.png", width: 70%),
  caption: [实验结果],
)

// 表格
#figure(
  table(
    columns: 3,
    align: center,
    table.header[方法][准确率][F1],
    [Baseline], [0.82], [0.79],
    [Ours], [*0.91*], [*0.88*],
  ),
  caption: [实验结果对比],
)
```

### 代码块
```typst
// 使用内置raw块
```python
def hello():
    print("Hello, Typst!")
```

// 或使用高亮包
#import "@preview/codly:0.2.0": *
#show: codly-init.with()

```python
def hello():
    print("Hello!")
```
```

## 主题定制

### metropolis风格
```typst
#import themes.metropolis: *

#show: metropolis-theme.with(
  aspect-ratio: "16-9",
  config-info(
    title: [论文标题],
    subtitle: [副标题],
    author: [作者],
    institute: [机构],
    date: datetime.today(),
  ),
  config-colors(
    primary: rgb("#eb811b"),
    primary-light: rgb("#f5bf49"),
    secondary: rgb("#23373b"),
    neutral: rgb("#fafafa"),
  ),
)
```

### 自定义主题
```typst
#let my-theme(doc) = {
  set page(
    paper: "presentation-16-9",
    margin: (top: 2em, bottom: 1.5em, x: 2em),
    header: context {
      if counter(page).get().first() > 1 [
        #set text(size: 10pt, fill: gray)
        #h(1fr) 论文标题
      ]
    },
    footer: context {
      #set text(size: 10pt, fill: gray)
      #counter(page).display("1 / 1", both: true)
    },
  )
  
  set text(size: 24pt, font: "New Computer Modern")
  set heading(size: 28pt)
  
  doc
}

#show: my-theme
```

## CeTZ绘图

```typst
#import "@preview/cetz:0.2.2": *

#slide[
  == 流程图
  
  #canvas({
    import draw: *
    
    rect((0, 0), (3, 1), name: "input", fill: blue.lighten(80%))
    content("input", [输入])
    
    rect((5, 0), (8, 1), name: "process", fill: green.lighten(80%))
    content("process", [处理])
    
    rect((10, 0), (13, 1), name: "output", fill: red.lighten(80%))
    content("output", [输出])
    
    line("input", "process", mark: (end: ">"))
    line("process", "output", mark: (end: ">"))
  })
]
```

## 备注

```typst
// 启用备注
#set page(paper: "presentation-16-9")

#polylux-slide[
  == 正文标题
  
  正文内容...
  
  #speaker-note[
    这是演讲者备注。
    观众看不到这些内容。
  ]
]
```

## 导出与分享

### PDF导出
```bash
typst compile slides.typ slides.pdf
```

### 图片导出（每页一张）
```bash
typst compile slides.typ slides-{n}.png --format png
```

### HTML导出（实验性）
```bash
typst compile slides.typ slides.html --format html
```

## Beamer vs Typst

| 特性 | Beamer | Typst |
|------|--------|-------|
| 编译速度 | 秒级 | 毫秒级 |
| 学习曲线 | 高 | 低 |
| 错误信息 | 晦涩 | 友好 |
| 中文支持 | 需配置 | 开箱即用 |
| 生态成熟度 | 成熟 | 发展中 |
| 模板数量 | 极多 | 增长中 |
| 数学排版 | 完美 | 优秀 |

## 相关链接

- [[10-学术PPT技能体系总览]] - 返回总览
- [[11-Beamer学术幻灯片]] - Beamer对比
- [[13-Marp-Markdown幻灯片]] - 更简单的Markdown方案
