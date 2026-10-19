# Typst Beamer 幻灯片使用教程

## 一、安装 Typst

### 1.1 Windows
```bash
# 使用 Scoop
scoop install typst

# 使用 winget
winget install Typst.Typst

# 或下载二进制：https://github.com/typst/typst/releases
```

### 1.2 macOS
```bash
brew install typst
```

### 1.3 Linux
```bash
# 使用 Cargo
cargo install typst-cli

# 或下载二进制
curl -fsSL https://typst.community/typst-install/install.sh | sh
```

### 1.4 验证安装
```bash
typst --version
```

### 1.5 VS Code 插件
1. 安装 `Tinymist Typst` 插件
2. 支持语法高亮、实时预览、自动补全

---

## 二、快速开始

### 2.1 创建第一个幻灯片

创建文件 `slides.typ`：

```typst
#import "@preview/touying:0.5.2": *
#import themes.metropolis: *

#show: metropolis-theme.with(
  aspect-ratio: "16-9",
)

#title-slide[
  = 我的第一个幻灯片
  
  作者姓名 \
  机构名称 \
  #datetime.today().display()
]

= 引言

== 研究背景

- 要点一
- 要点二
- 要点三

= 方法

== 方法概述

- 步骤一
- 步骤二
- 步骤三

= 结论

== 总结

- 结论一
- 结论二

#focus-slide[
  谢谢！
]
```

### 2.2 编译

```bash
# 编译为 PDF
typst compile slides.typ slides.pdf

# 监听模式（自动编译）
typst watch slides.typ slides.pdf
```

---

## 三、核心语法

### 3.1 文本

```typst
普通文本

*加粗文本*

_斜体文本_

`行内代码`

#underline[下划线文本]

#strike[删除线文本]

#text(fill: red)[红色文本]

#text(size: 20pt)[大号文本]
```

### 3.2 标题

```typst
= 一级标题

== 二级标题

=== 三级标题
```

### 3.3 列表

```typst
// 无序列表
- 项目一
- 项目二
  - 子项目

// 有序列表
+ 第一步
+ 第二步
+ 第三步
```

### 3.4 数学公式

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

// 希腊字母
$alpha, beta, gamma, delta, epsilon, theta, lambda, mu, pi, sigma, omega$

// 数学符号
$forall x in RR, exists y > 0, x + y > 0$
$integral_0^1 f(x) dif x$
$lim_(n -> infinity) a_n$
```

### 3.5 表格

```typst
#figure(
  table(
    columns: 3,
    align: center,
    table.header[方法][准确率][F1],
    [Baseline], [0.82], [0.79],
    [Method A], [0.85], [0.82],
    [Ours], [*0.91*], [*0.88*],
  ),
  caption: [实验结果对比],
)
```

### 3.6 图片

```typst
#figure(
  image("figure.png", width: 70%),
  caption: [实验结果],
)
```

### 3.7 代码块

```typst
```python
def hello():
    print("Hello, Typst!")
```
```

---

## 四、touying 主题系统

### 4.1 metropolis 主题（推荐）

```typst
#import "@preview/touying:0.5.2": *
#import themes.metropolis: *

#show: metropolis-theme.with(
  aspect-ratio: "16-9",
  footer: self => self.info.institute,
  config-info(
    title: [论文标题],
    subtitle: [副标题],
    author: [作者姓名],
    date: datetime.today(),
    institute: [机构名称],
  ),
)
```

### 4.2 其他内置主题

```typst
// default 主题
#import themes.default: *
#show: default-theme.with(...)

// university 主题
#import themes.university: *
#show: university-theme.with(...)

// aqua 主题
#import themes.aqua: *
#show: aqua-theme.with(...)

// dewdrop 主题
#import themes.dewdrop: *
#show: dewdrop-theme.with(...)
```

### 4.3 自定义配色

```typst
#show: metropolis-theme.with(
  aspect-ratio: "16-9",
  config-colors(
    primary: rgb("#1e40af"),       // 主色
    primary-light: rgb("#3b82f6"), // 浅主色
    secondary: rgb("#1e293b"),     // 次色
    neutral: rgb("#ffffff"),       // 中性色
    neutral-light: rgb("#f8fafc"), // 浅中性色
    neutral-dark: rgb("#1e293b"),  // 深中性色
  ),
)
```

---

## 五、页面布局

### 5.1 分栏

```typst
#slide[
  == 左栏标题

  - 要点一
  - 要点二
  - 要点三
][
  == 右栏标题

  #figure(
    image("figure.png", width: 90%),
    caption: [示意图],
  )
]
```

### 5.2 垂直对齐

```typst
// 顶部对齐
#slide(align: top)[
  顶部内容
][
  右侧内容
]

// 居中对齐
#slide(align: center)[
  居中内容
]
```

### 5.3 全宽页面

```typst
#slide[
  = 全宽标题
  
  #figure(
    image("wide-figure.png", width: 100%),
    caption: [全宽图片],
  )
]
```

---

## 六、动画效果

### 6.1 逐步显示

```typst
#slide[
  - #pause 第一点
  - #pause 第二点
  - #pause 第三点
]
```

### 6.2 高级动画

```typst
#import "@preview/touying:0.5.2": *

#slide(repeat: 3, self => {
  let (uncover, only, alternatives) = utils.methods(self)
  
  - #uncover("1-")[始终显示]
  - #uncover("2-")[第 2 步显示]
  - #uncover("3-")[第 3 步显示]
})
```

---

## 七、演讲者备注

```typst
#show: metropolis-theme.with(
  aspect-ratio: "16-9",
  config-common(show-notes-on-second-screen: right),
)

= 引言

== 研究背景

- 要点一
- 要点二

#speaker-note[
  这是演讲者备注。
  详细解释背景问题。
  强调研究的重要性。
]
```

---

## 八、TikZ/CeTZ 绘图

### 8.1 CeTZ 基础

```typst
#import "@preview/cetz:0.2.2": *

#slide[
  == 流程图
  
  #canvas({
    import draw: *
    
    // 定义样式
    let box(pos, name, content, color: blue) = {
      rect(
        pos, 
        (pos.at(0) + 2.5, pos.at(1) + 0.8),
        name: name,
        fill: color.lighten(80%),
        stroke: color,
        radius: 4pt,
      )
      content(name, text(size: 14pt, content))
    }
    
    // 绘制节点
    box((0, 0), "input", "输入")
    box((4, 0), "process", "处理", color: green)
    box((8, 0), "output", "输出", color: red)
    
    // 绘制箭头
    line("input", "process", mark: (end: ">"))
    line("process", "output", mark: (end: ">"))
  })
]
```

### 8.2 坐标图

```typst
#import "@preview/cetz:0.2.2": *
#import "@preview/cetz-plot:0.1.0": *

#slide[
  == 数据可视化
  
  #canvas({
    plot.plot(
      size: (10, 6),
      x-tick-step: 1,
      y-tick-step: 0.2,
      {
        plot.add(
          domain: (0, 5),
          x => calc.pow(x, 2) / 10,
          label: $x^2 / 10$,
        )
        plot.add(
          domain: (0, 5),
          x => calc.sin(x) + 1,
          label: $sin(x) + 1$,
        )
      }
    )
  })
]
```

---

## 九、完整学术模板

```typst
#import "@preview/touying:0.5.2": *
#import themes.metropolis: *
#import "@preview/cetz:0.2.2": *

#show: metropolis-theme.with(
  aspect-ratio: "16-9",
  footer: self => self.info.institute,
  config-info(
    title: [基于 Transformer 的文本分类研究],
    subtitle: [学术报告],
    author: [作者姓名],
    date: datetime.today(),
    institute: [某某大学计算机学院],
  ),
  config-colors(
    primary: rgb("#1e40af"),
    primary-light: rgb("#3b82f6"),
    secondary: rgb("#1e293b"),
  ),
)

#title-slide()

= 引言

== 研究背景

- 传统文本分类方法准确率有限
- 特征工程耗时耗力
- 难以处理语义复杂性

#speaker-note[
  详细说明现有方法的局限性，引出研究动机。
]

== 研究目标

#quote[
  提出一种基于 Transformer 的文本分类方法，
  提升分类准确率并降低人工特征工程成本。
]

*主要创新点*：
1. 动态注意力机制
2. 多尺度特征融合
3. 对比学习损失

= 研究方法

== 模型架构

#slide[
  === 模型结构
  
  + 预训练编码器 (BERT)
  + 注意力池化层
  + 分类头 (MLP)
  
  === 训练策略
  
  - 学习率：2e-5
  - Batch size：32
  - Epochs：10
][
  #figure(
    image("model.png", width: 90%),
    caption: [模型架构图],
  )
]

== 损失函数

$
  cal(L) = cal(L)_"CE" + lambda cal(L)_"CL"
$

其中：

$
  cal(L)_"CL" = -log frac(exp(sim(z_i, z_j) \/ tau), sum_(k=1)^(2N) bb(1)_(k != i) exp(sim(z_i, z_k) \/ tau))
$

= 实验

== 数据集

#figure(
  table(
    columns: 4,
    align: center,
    table.header[数据集][训练集][测试集][类别数],
    [AG News], [120K], [7.6K], [4],
    [IMDB], [25K], [25K], [2],
    [SST-2], [67K], [1.8K], [2],
  ),
  caption: [实验数据集统计],
)

== 实验结果

#figure(
  table(
    columns: 4,
    align: center,
    table.header[方法][AG News][IMDB][SST-2],
    [TextCNN], [91.2%], [89.5%], [90.1%],
    [LSTM], [92.1%], [90.3%], [91.2%],
    [BERT], [94.5%], [93.2%], [93.5%],
    [*Ours*], [*96.1%*], [*95.3%*], [*95.8%*],
  ),
  caption: [各方法在不同数据集上的准确率],
)

#speaker-note[
  重点解释为什么我们的方法更好，突出创新点的贡献。
]

= 结论

== 主要贡献

+ 提出了动态注意力池化机制
+ 设计了多尺度特征融合模块
+ 在三个基准数据集上取得 SOTA

== 未来工作

- 扩展到多语言场景
- 探索更高效的预训练方法
- 降低模型计算复杂度

#focus-slide[
  谢谢！ \
  Q&A
]
```

---

## 十、编译与导出

### 10.1 基本编译

```bash
# 编译为 PDF
typst compile slides.typ slides.pdf

# 指定根目录
typst compile --root . slides.typ slides.pdf

# 监听模式
typst watch slides.typ slides.pdf
```

### 10.2 导出为图片

```bash
# 导出为 PNG（每页一张）
typst compile slides.typ slides-{n}.png --format png

# 指定 DPI
typst compile slides.typ slides-{n}.png --format png --ppi 300
```

### 10.3 参数传递

```bash
# 传递参数
typst compile slides.typ --input theme=dark slides.pdf
```

```typst
// 在文档中使用
#let theme = sys.inputs.at("theme", default: "light")
```

---

## 十一、常见问题

### Q1: 包下载失败？
检查网络连接，或设置代理：
```bash
set HTTPS_PROXY=http://proxy:port
typst compile slides.typ
```

### Q2: 中文显示问题？
Typst 默认支持中文，确保系统安装了中文字体。

### Q3: 如何使用本地包？
将包放在 `~/.local/share/typst/packages/` 目录下。

### Q4: 如何调试编译错误？
Typst 错误信息很友好，直接阅读错误提示即可定位问题。

---

## 十二、Beamer vs Typst 对比

| 特性 | Beamer | Typst |
|------|--------|-------|
| 编译速度 | 秒级 | 毫秒级 |
| 学习曲线 | 高 | 低 |
| 错误信息 | 晦涩 | 友好 |
| 中文支持 | 需配置 | 开箱即用 |
| 生态成熟度 | 成熟 | 发展中 |
| 模板数量 | 极多 | 增长中 |
| 数学排版 | 完美 | 优秀 |

---

## 十三、相关资源

- [Typst 官方文档](https://typst.app/docs/)
- [Typst Universe 包](https://typst.app/universe/)
- [touying 主题库](https://github.com/OrangeX4/typst-touying)
- [CeTZ 绘图库](https://github.com/johannes-wolf/cetz)
