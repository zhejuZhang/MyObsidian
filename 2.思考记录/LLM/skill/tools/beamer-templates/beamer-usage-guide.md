# LaTeX Beamer 使用教程

## 一、安装 LaTeX

### 1.1 Windows - TeX Live
```bash
# 下载安装器
# https://www.tug.org/texlive/acquire-netinstall.html

# 或使用 Chocolatey
choco install texlive

# 验证
pdflatex --version
xelatex --version
```

### 1.2 macOS - MacTeX
```bash
brew install --cask mactex

# 验证
pdflatex --version
```

### 1.3 Linux - TeX Live
```bash
# Ubuntu/Debian
sudo apt install texlive-full

# 或最小安装
sudo apt install texlive-latex-base texlive-latex-recommended texlive-latex-extra
```

### 1.4 在线方案 - Overleaf
- 访问 https://www.overleaf.com
- 注册账号即可使用
- 无需本地安装

### 1.5 VS Code 配置
1. 安装 `LaTeX Workshop` 插件
2. 配置编译工具：

```json
// settings.json
{
  "latex-workshop.latex.tools": [
    {
      "name": "pdflatex",
      "command": "pdflatex",
      "args": ["-synctex=1", "-interaction=nonstopmode", "%DOC%"]
    },
    {
      "name": "xelatex",
      "command": "xelatex",
      "args": ["-synctex=1", "-interaction=nonstopmode", "%DOC%"]
    }
  ],
  "latex-workshop.latex.recipes": [
    {
      "name": "pdflatex",
      "tools": ["pdflatex"]
    },
    {
      "name": "xelatex",
      "tools": ["xelatex"]
    }
  ]
}
```

---

## 二、快速开始

### 2.1 最小示例

创建 `slides.tex`：

```latex
\documentclass[aspectratio=169]{beamer}
\usetheme{Madrid}

\title{论文标题}
\subtitle{副标题}
\author{作者姓名}
\institute{机构名称}
\date{\today}

\begin{document}

\begin{frame}
  \titlepage
\end{frame}

\begin{frame}{目录}
  \tableofcontents
\end{frame}

\section{引言}
\begin{frame}{研究背景}
  \begin{itemize}
    \item 背景信息一
    \item 背景信息二
    \item 背景信息三
  \end{itemize}
\end{frame}

\section{方法}
\begin{frame}{方法概述}
  正文内容...
\end{frame}

\section{结论}
\begin{frame}{总结}
  \begin{itemize}
    \item 结论一
    \item 结论二
  \end{itemize}
\end{frame}

\end{document}
```

### 2.2 编译

```bash
# 使用 pdflatex
pdflatex slides.tex

# 使用 xelatex（支持中文）
xelatex slides.tex

# 连续编译两次（解决引用）
pdflatex slides.tex && pdflatex slides.tex
```

---

## 三、文档类选项

### 3.1 宽高比

```latex
% 4:3 (传统)
\documentclass[aspectratio=43]{beamer}

% 16:9 (现代，推荐)
\documentclass[aspectratio=169]{beamer}

% 16:10
\documentclass[aspectratio=1610]{beamer}
```

### 3.2 其他选项

```latex
\documentclass[
  aspectratio=169,  % 宽高比
  12pt,             % 字号
  t,                % 顶部对齐
  handout,          % 讲义模式（无动画）
  notes,            % 显示备注
  notes=only        % 只显示备注
]{beamer}
```

---

## 四、主题与配色

### 4.1 内置主题

| 主题 | 风格 | 推荐度 |
|------|------|--------|
| `default` | 默认 | ★★★ |
| `AnnArbor` | 黄蓝色调 | ★★★★ |
| `Antibes` | 绿色调 | ★★★ |
| `Berlin` | 信息丰富 | ★★★★ |
| `Boadilla` | 简洁专业 | ★★★★ |
| `CambridgeUS` | 红色调 | ★★★ |
| `Copenhagen` | 蓝色调 | ★★★ |
| `Darmstadt` | 紫色调 | ★★★ |
| `Frankfurt` | 蓝色调 | ★★★★ |
| `Ilmenau` | 深蓝 | ★★★ |
| `JuanLesPins` | 棕色调 | ★★★ |
| `Luebeck` | 简洁 | ★★★ |
| `Madrid` | 经典 | ★★★★★ |
| `Montpellier` | 浅蓝 | ★★★ |
| `PaloAlto` | 侧边栏 | ★★★ |
| `Singapore` | 紧凑 | ★★★ |
| `Szeged` | 简洁 | ★★★ |

### 4.2 推荐主题

```latex
% 经典风格
\usetheme{Madrid}
\usecolortheme{whale}

% 现代极简（需安装）
\usetheme{metropolis}

% 简洁风格
\usetheme{Boadilla}
\usecolortheme{seahorse}
```

### 4.3 metropolis 主题（强烈推荐）

```latex
% 需要先安装：tlmgr install metropolis
\documentclass[aspectratio=169]{beamer}
\usetheme{metropolis}
\usepackage{booktabs}

% 可选配置
\setbeamertemplate{frame numbering}[fraction]  % 页码格式
\setbeamercolor{frametitle}{bg=mDarkTeal}

\title{论文标题}
\author{作者}
\date{\today}

\begin{document}
\maketitle

\begin{frame}{标题}
  内容...
\end{frame}

\end{document}
```

### 4.4 配色方案

```latex
% 内置配色
\usecolortheme{default}   % 默认
\usecolortheme{albatross}  % 深蓝
\usecolortheme{beaver}     % 棕色
\usecolortheme{beetle}     % 深灰
\usecolortheme{crane}      % 黄色
\usecolortheme{dolphin}    % 紫色
\usecolortheme{dove}       % 黑白
\usecolortheme{fly}        % 灰色
\usecolortheme{lily}       % 浅蓝
\usecolortheme{orchid}     % 紫红
\usecolortheme{rose}       % 粉色
\usecolortheme{seagull}    % 灰色
\usecolortheme{seahorse}   % 浅蓝
\usecolortheme{sidebartab} % 侧边栏
\usecolortheme{structure}  % 结构色
\usecolortheme{whale}      % 蓝色（推荐）
\usecolortheme{wolverine}  % 蓝金色
```

### 4.5 自定义颜色

```latex
% 定义颜色
\definecolor{myblue}{RGB}{0,82,155}
\definecolor{mygold}{RGB}{255,193,37}

% 设置颜色
\setbeamercolor{structure}{fg=myblue}
\setbeamercolor{frametitle}{bg=myblue, fg=white}
\setbeamercolor{title}{fg=myblue}
\setbeamercolor{block title}{bg=myblue, fg=white}
```

---

## 五、帧环境

### 5.1 基本帧

```latex
\begin{frame}{标题}
  内容...
\end{frame}

% 带副标题
\begin{frame}{主标题}{副标题}
  内容...
\end{frame}

% 无标题
\begin{frame}
  内容...
\end{frame}
```

### 5.2 列表

```latex
\begin{frame}{列表示例}
  % 无序列表
  \begin{itemize}
    \item 第一点
    \item 第二点
    \begin{itemize}
      \item 子项一
      \item 子项二
    \end{itemize}
    \item 第三点
  \end{itemize}
\end{frame}

\begin{frame}{编号列表}
  % 有序列表
  \begin{enumerate}
    \item 步骤一
    \item 步骤二
    \item 步骤三
  \end{enumerate}
\end{frame}
```

### 5.3 分栏

```latex
\begin{frame}{双栏布局}
  \begin{columns}[T]  % T=顶部对齐, C=居中
    \begin{column}{0.48\textwidth}
      左栏内容
      \begin{itemize}
        \item 要点一
        \item 要点二
      \end{itemize}
    \end{column}
    \begin{column}{0.48\textwidth}
      右栏内容
      \includegraphics[width=\textwidth]{figure.png}
    \end{column}
  \end{columns}
\end{frame}
```

### 5.4 定理与证明

```latex
\begin{frame}{定理示例}
  \begin{theorem}[勾股定理]
    直角三角形中，斜边的平方等于两直角边平方之和。
    \[ a^2 + b^2 = c^2 \]
  \end{theorem}
  
  \begin{proof}
    证明过程...
  \end{proof}
\end{frame}
```

### 5.5 引用块

```latex
\begin{frame}{引用示例}
  \begin{quote}
    ``这是一段引用文字。''
    \hfill --- 作者
  \end{quote}
  
  \begin{exampleblock}{示例}
    这是一个示例块。
  \end{exampleblock}
  
  \begin{alertblock}{注意}
    这是一个警告块。
  \end{alertblock}
\end{frame}
```

---

## 六、图片与表格

### 6.1 图片

```latex
\begin{frame}{图片示例}
  \begin{figure}
    \centering
    \includegraphics[width=0.8\textwidth]{result.png}
    \caption{实验结果对比}
    \label{fig:results}
  \end{figure}
\end{frame}

% 多图并排
\begin{frame}{多图示例}
  \begin{columns}
    \begin{column}{0.48\textwidth}
      \includegraphics[width=\textwidth]{fig1.png}
      \captionof{figure}{图1}
    \end{column}
    \begin{column}{0.48\textwidth}
      \includegraphics[width=\textwidth]{fig2.png}
      \captionof{figure}{图2}
    \end{column}
  \end{columns}
\end{frame}
```

### 6.2 表格

```latex
\usepackage{booktabs}  % 专业表格

\begin{frame}{表格示例}
  \begin{table}
    \centering
    \begin{tabular}{lcc}
      \toprule
      方法 & 准确率 & F1 \\
      \midrule
      Baseline & 0.82 & 0.79 \\
      Method A & 0.85 & 0.82 \\
      Our Method & \textbf{0.91} & \textbf{0.88} \\
      \bottomrule
    \end{tabular}
    \caption{实验结果对比}
    \label{tab:results}
  \end{table}
\end{frame}
```

---

## 七、动画效果

### 7.1 逐步显示

```latex
\begin{frame}{逐步显示}
  \begin{itemize}
    \item<1-> 第一点（始终显示）
    \item<2-> 第二点（从第2页开始）
    \item<3-> 第三点（从第3页开始）
  \end{itemize}
\end{frame}
```

### 7.2 自动逐步显示

```latex
\begin{frame}{自动逐步显示}
  \begin{itemize}[<+->]
    \item 第一点
    \item 第二点
    \item 第三点
  \end{itemize}
\end{frame}
```

### 7.3 覆盖层

```latex
\begin{frame}{覆盖示例}
  \only<1>{第一页内容}
  \only<2>{第二页内容}
  \only<3>{第三页内容}
\end{frame}

\begin{frame}{交替显示}
  \alt<2>{高亮版本}{普通版本}
\end{frame}
```

### 7.4 高亮

```latex
\begin{frame}{高亮示例}
  \begin{itemize}
    \item 普通文本
    \item \alert<2>{高亮文本}  % 第2页高亮
    \item 普通文本
  \end{itemize}
\end{frame}
```

---

## 八、代码块

### 8.1 使用 listings

```latex
\usepackage{listings}

\lstset{
  basicstyle=\ttfamily\small,
  keywordstyle=\color{blue}\bfseries,
  commentstyle=\color{gray},
  stringstyle=\color{red},
  breaklines=true,
  numbers=left,
  numberstyle=\tiny\color{gray},
  frame=single,
  backgroundcolor=\color{gray!10}
}

\begin{frame}{代码示例}
  \begin{lstlisting}[language=Python]
import numpy as np

def mean(data):
    """计算均值"""
    return np.mean(data)

# 使用
data = [1, 2, 3, 4, 5]
print(mean(data))  # 输出: 3.0
  \end{lstlisting}
\end{frame}
```

### 8.2 使用 minted（需要 Python）

```latex
\usepackage{minted}

\begin{frame}{代码示例}
  \begin{minted}{python}
import numpy as np

def mean(data):
    return np.mean(data)
  \end{minted}
\end{frame}
```

---

## 九、数学公式

### 9.1 基本公式

```latex
% 行内公式
质能方程 $E = mc^2$

% 块级公式
\[
\sum_{i=1}^{n} x_i = x_1 + x_2 + \cdots + x_n
\]

% 编号公式
\begin{equation}
  E = mc^2
  \label{eq:einstein}
\end{equation}
```

### 9.2 多行公式

```latex
\usepackage{amsmath}

\begin{frame}{公式示例}
  \begin{align}
    f(x) &= x^2 + 2x + 1 \\
         &= (x + 1)^2
  \end{align}
\end{frame}
```

---

## 十、TikZ 绘图

### 10.1 流程图

```latex
\usepackage{tikz}
\usetikzlibrary{shapes,arrows,positioning}

\begin{frame}{流程图}
  \begin{tikzpicture}[
    node distance=2cm,
    block/.style={
      rectangle, 
      draw, 
      fill=blue!20, 
      text width=5em, 
      text centered, 
      rounded corners,
      minimum height=3em
    },
    line/.style={draw, -latex}
  ]
    \node [block] (input) {输入};
    \node [block, right of=input] (process) {处理};
    \node [block, right of=process] (output) {输出};
    
    \path [line] (input) -- (process);
    \path [line] (process) -- (output);
  \end{tikzpicture}
\end{frame}
```

### 10.2 神经网络

```latex
\usepackage{tikz}
\usetikzlibrary{positioning}

\begin{frame}{神经网络}
  \begin{tikzpicture}[
    neuron/.style={circle, draw, minimum size=1cm},
    layer/.style={neuron, fill=blue!20},
  ]
    % 输入层
    \foreach \i in {1,2,3}
      \node[layer] (I\i) at (0,-\i*1.5) {$x_\i$};
    
    % 隐藏层
    \foreach \i in {1,2}
      \node[layer] (H\i) at (3,-\i*1.5-0.75) {$h_\i$};
    
    % 输出层
    \node[layer] (O) at (6,-2.25) {$y$};
    
    % 连接
    \foreach \i in {1,2,3}
      \foreach \j in {1,2}
        \draw[->] (I\i) -- (H\j);
    
    \foreach \i in {1,2}
      \draw[->] (H\i) -- (O);
  \end{tikzpicture}
\end{frame}
```

---

## 十一、中文支持

### 11.1 使用 ctex

```latex
\documentclass[aspectratio=169]{beamer}
\usepackage[UTF8]{ctex}
\usetheme{Madrid}

\begin{document}
\begin{frame}{中文标题}
  中文内容...
\end{frame}
\end{document}
```

### 11.2 使用 xeCJK

```latex
\documentclass[aspectratio=169]{beamer}
\usepackage{xeCJK}
\setCJKmainfont{Microsoft YaHei}  % 设置中文字体
\usetheme{Madrid}

\begin{document}
\begin{frame}{中文标题}
  中文内容...
\end{frame}
\end{document}
```

---

## 十二、备注与讲义

### 12.1 演讲者备注

```latex
% 在文档类中启用
\documentclass[aspectratio=169,notes]{beamer}

% 或只显示备注
\documentclass[aspectratio=169,notes=only]{beamer}

\begin{frame}{有备注的页面}
  正文内容...
  
  \note{这是演讲者备注。}
  \note{观众看不到这些内容。}
  \note{可以写提示、要点等。}
\end{frame}
```

### 12.2 讲义模式

```latex
% 讲义模式：每帧只输出一页
\documentclass[aspectratio=169,handout]{beamer}
```

---

## 十三、完整学术模板

```latex
\documentclass[aspectratio=169]{beamer}

% 主题
\usetheme{Madrid}
\usecolortheme{whale}

% 包
\usepackage[UTF8]{ctex}
\usepackage{amsmath,amssymb}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{listings}
\usepackage{tikz}
\usetikzlibrary{shapes,arrows,positioning}

% 代码样式
\lstset{
  basicstyle=\ttfamily\small,
  keywordstyle=\color{blue}\bfseries,
  commentstyle=\color{gray},
  breaklines=true,
  frame=single,
  backgroundcolor=\color{gray!10}
}

% 标题信息
\title{基于 Transformer 的文本分类研究}
\subtitle{学术报告}
\author{作者姓名}
\institute{某某大学 \\ 计算机学院}
\date{\today}

\begin{document}

% 封面
\begin{frame}
  \titlepage
\end{frame}

% 目录
\begin{frame}{目录}
  \tableofcontents
\end{frame}

% 引言
\section{引言}

\begin{frame}{研究背景}
  \begin{itemize}
    \item 传统文本分类方法准确率有限
    \item 特征工程耗时耗力
    \item 难以处理语义复杂性
  \end{itemize}
\end{frame}

\begin{frame}{研究目标}
  \begin{quote}
    提出一种基于 Transformer 的文本分类方法，提升分类准确率并降低人工特征工程成本。
  \end{quote}
  
  \vspace{1em}
  \textbf{主要创新点：}
  \begin{enumerate}
    \item 动态注意力机制
    \item 多尺度特征融合
    \item 对比学习损失
  \end{enumerate}
\end{frame}

% 方法
\section{研究方法}

\begin{frame}{模型架构}
  \begin{columns}[T]
    \begin{column}{0.5\textwidth}
      \textbf{模型结构：}
      \begin{enumerate}
        \item 预训练编码器 (BERT)
        \item 注意力池化层
        \item 分类头 (MLP)
      \end{enumerate}
      
      \vspace{1em}
      \textbf{训练策略：}
      \begin{itemize}
        \item 学习率：2e-5
        \item Batch size：32
        \item Epochs：10
      \end{itemize}
    \end{column}
    \begin{column}{0.48\textwidth}
      \centering
      \includegraphics[width=\textwidth]{model.png}
      \captionof{figure}{模型架构图}
    \end{column}
  \end{columns}
\end{frame}

\begin{frame}{损失函数}
  \begin{equation*}
    \mathcal{L} = \mathcal{L}_{CE} + \lambda \mathcal{L}_{CL}
  \end{equation*}
  
  其中对比学习损失：
  \begin{equation*}
    \mathcal{L}_{CL} = -\log \frac{\exp(\text{sim}(z_i, z_j) / \tau)}{\sum_{k=1}^{2N} \mathbb{1}_{k \neq i} \exp(\text{sim}(z_i, z_k) / \tau)}
  \end{equation*}
\end{frame}

% 实验
\section{实验}

\begin{frame}{数据集}
  \begin{table}
    \centering
    \begin{tabular}{lccc}
      \toprule
      数据集 & 训练集 & 测试集 & 类别数 \\
      \midrule
      AG News & 120K & 7.6K & 4 \\
      IMDB & 25K & 25K & 2 \\
      SST-2 & 67K & 1.8K & 2 \\
      \bottomrule
    \end{tabular}
    \caption{实验数据集统计}
  \end{table}
\end{frame}

\begin{frame}{实验结果}
  \begin{table}
    \centering
    \begin{tabular}{lccc}
      \toprule
      方法 & AG News & IMDB & SST-2 \\
      \midrule
      TextCNN & 91.2\% & 89.5\% & 90.1\% \\
      LSTM & 92.1\% & 90.3\% & 91.2\% \\
      BERT & 94.5\% & 93.2\% & 93.5\% \\
      \textbf{Ours} & \textbf{96.1\%} & \textbf{95.3\%} & \textbf{95.8\%} \\
      \bottomrule
    \end{tabular}
    \caption{各方法在不同数据集上的准确率}
  \end{table}
\end{frame}

% 结论
\section{结论}

\begin{frame}{主要贡献}
  \begin{enumerate}
    \item 提出了动态注意力池化机制
    \item 设计了多尺度特征融合模块
    \item 在三个基准数据集上取得 SOTA
  \end{enumerate}
\end{frame}

\begin{frame}{未来工作}
  \begin{itemize}
    \item 扩展到多语言场景
    \item 探索更高效的预训练方法
    \item 降低模型计算复杂度
  \end{itemize}
\end{frame}

% 致谢
\begin{frame}
  \centering
  \Huge 谢谢！
  
  \vspace{2em}
  \Large Q\&A
  
  \vspace{2em}
  \normalsize 联系方式：email@example.com
\end{frame}

\end{document}
```

---

## 十四、编译命令

```bash
# 基础编译
pdflatex slides.tex

# 支持中文
xelatex slides.tex

# 含 BibTeX 引用
pdflatex slides.tex
bibtex slides
pdflatex slides.tex
pdflatex slides.tex

# 压缩 PDF
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook \
   -dNOPAUSE -dBATCH -sOutputFile=slides_compressed.pdf slides.pdf
```

---

## 十五、常见问题

### Q1: 中文显示问题？
使用 `xelatex` 编译，并加载 `ctex` 包。

### Q2: 图片路径问题？
确保图片在正确路径，或使用绝对路径。

### Q3: 字体问题？
使用 `xelatex` 编译，可以使用系统字体。

### Q4: 如何压缩 PDF？
使用 Ghostscript 压缩，见编译命令。

### Q5: 如何生成 4:3 幻灯片？
修改 `aspectratio=43`。

---

## 十六、相关资源

- [Beamer 用户手册](https://ctan.org/pkg/beamer)
- [metropolis 主题](https://github.com/matze/mtheme)
- [LaTeX Beamer 模板](https://www.latextemplates.com/cat/conference-posters)
- [Overleaf Beamer 教程](https://www.overleaf.com/latex/templates/tagged/presentations)
