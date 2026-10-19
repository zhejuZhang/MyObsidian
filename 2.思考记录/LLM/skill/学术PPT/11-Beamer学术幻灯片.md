# Beamer学术幻灯片

## Beamer是什么

Beamer是LaTeX的幻灯片文档类，学术界最标准的演示工具。输出PDF格式，跨平台一致，公式排版完美。

## Beamer基础模板

### 最小示例
```latex
\documentclass[aspectratio=169]{beamer}
\usetheme{Madrid}
\usecolortheme{whale}

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

\end{document}
```

### aspectratio选项
```
4:3  → \documentclass[aspectratio=43]{beamer}   (传统)
16:9 → \documentclass[aspectratio=169]{beamer}  (现代宽屏，推荐)
16:10 → \documentclass[aspectratio=1610]{beamer}
```

## 主题与配色

### 内置主题
| 主题 | 风格 | 推荐度 |
|------|------|--------|
| `Madrid` | 经典、信息丰富 | ★★★★★ |
| `AnnArbor` | 黄蓝色调 | ★★★★ |
| `Boadilla` | 简洁专业 | ★★★★ |
| `CambridgeUS` | 红色调 | ★★★ |
| `Singapore` | 紧凑 | ★★★ |
| `metropolis` | 现代极简（需安装） | ★★★★★ |
| `focus` | 极简专注（需安装） | ★★★★★ |

### metropolis主题（强烈推荐）
```latex
\documentclass[aspectratio=169]{beamer}
\usetheme{metropolis}
\usepackage{booktabs}

% 可选配置
\setbeamertemplate{frame numbering}[none]  % 隐藏页码
\setbeamercolor{frametitle}{bg=mDarkTeal}
\metroset{numbering=fraction}  % 页码格式 1/10

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

### 配色方案
```latex
% 推荐配色组合
\usecolortheme{whale}     % 蓝色系（经典）
\usecolortheme{crane}     % 黄色系
\usecolortheme{seahorse}  % 浅蓝色
\usecolortheme{wolverine} % 蓝金色

% 自定义颜色
\definecolor{myblue}{RGB}{0,82,155}
\setbeamercolor{structure}{fg=myblue}
\setbeamercolor{frametitle}{bg=myblue}
```

## 常用帧环境

### 列表
```latex
\begin{frame}{列表示例}
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

% 编号列表
\begin{frame}{编号列表}
  \begin{enumerate}
    \item 步骤一
    \item 步骤二
    \item 步骤三
  \end{enumerate}
\end{frame}
```

### 分栏
```latex
\begin{frame}{双栏布局}
  \begin{columns}[T]
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

### 定理与证明
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

### 代码块
```latex
\usepackage{listings}
\lstset{
  basicstyle=\ttfamily\small,
  keywordstyle=\color{blue},
  commentstyle=\color{gray},
  breaklines=true
}

\begin{frame}{代码展示}
  \begin{lstlisting}[language=Python]
def hello():
    print("Hello, Beamer!")
  \end{lstlisting}
\end{frame}
```

## 图表与动画

### 图片插入
```latex
\begin{frame}{图片示例}
  \begin{figure}
    \centering
    \includegraphics[width=0.8\textwidth]{result.png}
    \caption{实验结果对比}
  \end{figure}
\end{frame}
```

### 表格
```latex
\begin{frame}{表格示例}
  \begin{table}
    \centering
    \begin{tabular}{lcc}
      \toprule
      方法 & 准确率 & F1 \\
      \midrule
      Baseline & 0.82 & 0.79 \\
      Our Method & \textbf{0.91} & \textbf{0.88} \\
      \bottomrule
    \end{tabular}
    \caption{实验结果}
  \end{table}
\end{frame}
```

### 动画效果
```latex
\begin{frame}{逐步显示}
  \begin{itemize}
    \item<1-> 第一点（始终显示）
    \item<2-> 第二点（从第2页开始）
    \item<3-> 第三点（从第3页开始）
  \end{itemize}
\end{frame}

% 高亮当前项
\begin{frame}{高亮效果}
  \begin{itemize}[<+->]
    \item 第一点
    \item 第二点
    \item 第三点
  \end{itemize}
\end{frame}

% 覆盖层
\begin{frame}{覆盖示例}
  \only<1>{第一页内容}
  \only<2>{第二页内容}
  \only<3>{第三页内容}
\end{frame}
```

### TikZ绘图
```latex
\usepackage{tikz}
\usetikzlibrary{shapes,arrows}

\begin{frame}{流程图}
  \begin{tikzpicture}[node distance=2cm]
    \node (start) [rectangle, draw] {开始};
    \node (process) [rectangle, draw, below of=start] {处理};
    \node (end) [rectangle, draw, below of=process] {结束};
    
    \draw [->] (start) -- (process);
    \draw [->] (process) -- (end);
  \end{tikzpicture}
\end{frame}
```

## 备注与演讲者视图

```latex
% 启用备注
\documentclass[aspectratio=169,notes]{beamer}
% 或只显示备注
\documentclass[aspectratio=169,notes=only]{beamer}

\begin{frame}{有备注的页面}
  正文内容...
  
  \note{这是演讲者备注，观众看不到。}
  \note{可以写更多提示。}
\end{frame}
```

## 编译与工作流

### 命令行编译
```bash
# 基础编译
pdflatex slides.tex

# 含中文
xelatex slides.tex

# 含BibTeX引用
pdflatex slides.tex
bibtex slides
pdflatex slides.tex
pdflatex slides.tex
```

### VS Code + LaTeX Workshop
```json
// settings.json
{
  "latex-workshop.latex.tools": [
    {
      "name": "xelatex",
      "command": "xelatex",
      "args": ["-synctex=1", "-interaction=nonstopmode", "%DOC%"]
    }
  ],
  "latex-workshop.latex.recipes": [
    {
      "name": "xelatex",
      "tools": ["xelatex"]
    }
  ]
}
```

### Overleaf
- 在线编辑，无需本地安装
- 实时预览
- 自动编译
- 版本历史
- 团队协作

## 常见问题

### 中文支持
```latex
\documentclass[aspectratio=169]{beamer}
\usepackage[UTF8]{ctex}  % 中文支持
\usetheme{Madrid}

\begin{document}
\begin{frame}{中文标题}
  中文内容...
\end{frame}
\end{document}
```

### 压缩PDF
```bash
# Ghostscript压缩
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook \
   -dNOPAUSE -dBATCH -sOutputFile=slides_compressed.pdf slides.pdf
```

## 参考资源

- [Beamer用户手册](https://ctan.org/pkg/beamer)
- [metropolis主题](https://github.com/matze/mtheme)
- [LaTeX Beamer模板集合](https://www.latextemplates.com/cat/conference-posters)

## 相关链接

- [[10-学术PPT技能体系总览]] - 返回总览
- [[12-Typst幻灯片]] - Typst替代方案
- [[16-AI辅助PPT制作]] - AI生成Beamer代码
