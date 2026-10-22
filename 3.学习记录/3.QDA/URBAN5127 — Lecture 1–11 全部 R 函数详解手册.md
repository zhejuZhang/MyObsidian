# URBAN5127 — Lecture 1–11 全部 R 函数详解手册

> 基于上传的 `lecture1_notes.html` 至 `lecture11_notes.html`，另将 `lecture8_regressions.html` 作为第 8 讲补充。以**实际 R 代码块**和**课件正文明确提及的 R 函数**为收录范围；不把网页 HTML/JavaScript 函数、R 输出中自动打印的内部函数、课外扩展模型算进来。

- **收录：78 个不同函数/函数调用名**；其中 **73 个在课堂 R 代码块中以括号形式出现**，`fct_rev` 在管道中省略括号，另有 `install.packages`、`View`、`theme_bw`、`theme_void` 在正文讲解。
- **适合：** R 初学者、代码复现、实验检查和期末论文方法索引。
- **重要说明：** 教学用的 `lfs` 是课程数据对象；需先按 Lecture 2 导入并清洗，否则单独复制示例可能因找不到数据或变量而报错。
- **代码说明：** 部分示例为课件原有代码的精简整理，部分为按课堂使用场景的教学化写法，已在有必要处注明；解释尽量保持原课件的模型与数据语境。

## 使用导航

1. [11 讲函数索引](#一11-讲函数索引)
2. [按功能分类的函数详解](#二按功能分类的函数详解)
3. [不是普通函数但一定要会的 R 语法](#三不是普通函数但一定要会的-r-语法)
4. [完整课程工作流例子](#四完整课程工作流示意)
5. [作业重点函数速查](#五最终研究论文的重点函数)

## 一、11 讲函数索引

| 讲次 | 实际函数（课堂代码 + 正文提及） | 所做操作 |
|---|---|---|
| Lecture 1 | — | 定量研究设计、测量尺度与假设；没有可执行 R 函数代码 |
| Lecture 2 | `View()`、`c()`、`dim()`、`factor()`、`filter()`、`glimpse()`、`install.packages()`、`library()`、`mutate()`、`read_tsv()`、`select()` | R 基础、读入调查数据、筛选、类型重编码、数据检查 |
| Lecture 3 | `arrange()`、`c()`、`count()`、`group_by()`、`head()`、`max()`、`mean()`、`median()`、`min()`、`mutate()`、`prop.table()`、`pull()`、`quantile()`、`reframe()`、`round()`、`sd()`、`sum()`、`summarise()`、`summary()`、`table()`、`tail()`、`var()` | 汇总统计、分位数、分组和交叉表 |
| Lecture 4 | `aes()`、`arrange()`、`c()`、`coord_cartesian()`、`element_blank()`、`filter()`、`geom_density()`、`geom_histogram()`、`geom_rug()`、`ggplot()`、`head()`、`labs()`、`scale_x_log10()`、`select()`、`theme()`、`theme_bw()`、`theme_dark()`、`theme_minimal()`、`theme_void()` | 单变量图、密度图、对数轴、主题与标注 |
| Lecture 5 | `aes()`、`coord_flip()`、`element_blank()`、`element_text()`、`facet_grid()`、`facet_wrap()`、`fct_infreq()`、`fct_reorder()`、`fct_rev()`、`filter()`、`geom_bar()`、`geom_boxplot()`、`geom_density()`、`geom_jitter()`、`geom_point()`、`geom_tile()`、`geom_violin()`、`ggplot()`、`group_by()`、`labs()`、`library()`、`mean()`、`mutate()`、`scale_fill_colorblind()`、`scale_x_log10()`、`scale_y_log10()`、`summarise()`、`theme()`、`theme_minimal()` | 箱线图、分面、热力图、类别排序、比例柱状图 |
| Lecture 6 | `group_by()`、`knitr::kable()`、`lm()`、`mean()`、`pnorm()`、`round()`、`summarise()`、`summary()`、`t.test()` | 概率、t 检验、均值差异的线性回归表达、表格输出 |
| Lecture 7 | `aov()`、`cor()`、`cor.test()`、`lm()`、`summary()` | ANOVA、相关及简单线性回归 |
| Lecture 8 | `c()`、`data.frame()`、`filter()`、`lm()`、`plot()` | 逐步构建多变量 OLS、异常点诊断；含补充课件 |
| Lecture 9 | `bptest()`、`lm()`、`log()`、`mutate()`、`plot()`、`resettest()` | 不同函数形式、残差图、RESET 与 BP 检验 |
| Lecture 10 | `bptest()`、`case_when()`、`coeftest()`、`factor()`、`lm()`、`log()`、`mutate()`、`relevel()`、`resettest()`、`vcovHC()`、`vif()` | VIF、变量重构、稳健标准误 |
| Lecture 11 | `lm.cluster()`、`log()`、`mutate()`、`select()`、`summary()` | 家庭聚类稳健标准误、最终回归模型讨论 |

**索引阅读提醒：** 每讲出现的函数会重复列出，但下文函数详解中每个名字只解释一次。第 8 讲的独立 `lecture8_regressions.html` 归并到 Lecture 8。

## 二、按功能分类的函数详解

### 01｜R 环境、数据结构与查看

#### `install.packages()`

- **来源课次：** Lecture 2（正文提到）
- **所属包：** `utils（R 基础发行版）`
- **作用：** 把 CRAN 上的 R 扩展包安装到本机库中；通常一台机器安装一次即可。
- **常用形式：** `install.packages("包名")`
- **参数与输入：** 首个参数是包名字符串；`repos` 可指定镜像。

```r
install.packages("tidyverse")
```

**理解重点 / 易错点：** **与 `library()` 不同**：安装并不等于在当前 R 会话加载。课件正文提到，未在 R 代码块执行。

#### `library()`

- **来源课次：** L2、L5
- **所属包：** `base`
- **作用：** 将已安装的包附加到当前 R 会话，使其中的函数可以直接调用。
- **常用形式：** `library(package)`
- **参数与输入：** `package` 可写成不带引号的包名。

```r
library(tidyverse)
```

**理解重点 / 易错点：** 若提示没有该包，应先 `install.packages()`；不要在每次运行脚本时重复安装。

#### `View()`

- **来源课次：** Lecture 2（正文提到）
- **所属包：** `utils / RStudio 数据查看器`
- **作用：** 以近似电子表格的方式打开数据查看窗口，便于人工检查变量。
- **常用形式：** `View(x)`
- **参数与输入：** `x` 是数据框或其他可查看对象；注意首字母 **V 必须大写**。

```r
View(lfs)
```

**理解重点 / 易错点：** 课件正文提到，没有在代码块执行；此函数主要用于交互查看，不负责数据清洗。

#### `c()`

- **来源课次：** L2、L3、L4、L8
- **所属包：** `base`
- **作用：** 将多个值连接为一个向量；同一向量内元素需要兼容的数据类型。
- **常用形式：** `c(value1, value2, ...)`
- **参数与输入：** 各参数是待合并的元素；混合字符和数字时通常发生类型转换。

```r
numbers <- c(1, 2, 3, 4, 5)
```

**理解重点 / 易错点：** 课件也用它设置 `factor()` 的 `levels` 与 `labels`、`quantile()` 的 `probs`。

#### `data.frame()`

- **来源课次：** L8
- **所属包：** `base`
- **作用：** 按列创建数据框，供后续建模、绘图或统计使用。
- **常用形式：** `data.frame(column_a = ..., column_b = ...)`
- **参数与输入：** 各列长度必须一致或可合法回收。

```r
fake_data <- data.frame(
  age = c(20, 23, 25, 26, 28, 30, 32, 33, 65),
  wage = c(10, 11, 15, 9, 8, 20, 22, 25, 200)
)
```

**理解重点 / 易错点：** Lecture 8 用它制造含极端观测的数据，演示高杠杆点对模型的影响。

#### `dim()`

- **来源课次：** L2
- **所属包：** `base`
- **作用：** 返回数据对象的行数和列数。
- **常用形式：** `dim(x)`
- **参数与输入：** `x` 是有维度属性的对象；数据框返回长度为 2 的向量：行、列。

```r
dim(lfs)
```

**理解重点 / 易错点：** Lecture 2 反复在 `filter()` 前后使用它，追踪样本筛选是否导致观测数量减少。

#### `glimpse()`

- **来源课次：** L2
- **所属包：** `dplyr / tibble`
- **作用：** 快速显示行列规模、每列类型及前几个值，比打印整张数据表更适合变量检查。
- **常用形式：** `glimpse(data)`
- **参数与输入：** `data` 是数据框。

```r
glimpse(lfs)
```

**理解重点 / 易错点：** 尤其要在 `factor()` 重编码后检查 `SEX` 等字段是否成为 factor。

#### `head()`

- **来源课次：** L3、L4
- **所属包：** `utils`
- **作用：** 返回对象前几条记录，便于查看结构与排序结果。
- **常用形式：** `head(x, n = 6)`
- **参数与输入：** `n` 指显示行数，默认 6。

```r
lfs %>% arrange(-HOURPAY) %>% select(HOURPAY) %>% head(n = 10)
```

**理解重点 / 易错点：** 这是 Lecture 4 查看最高工资记录时的用法。

#### `tail()`

- **来源课次：** L3
- **所属包：** `utils`
- **作用：** 返回对象最后几条记录。
- **常用形式：** `tail(x, n = 6)`
- **参数与输入：** `n` 是希望返回的末尾行数。

```r
lfs %>% arrange(HOURPAY) %>% tail()
```

**理解重点 / 易错点：** 在升序排列工资后，末尾是工资最高的部分观测。

#### `summary()`

- **来源课次：** L3、L6、L7、L11
- **所属包：** `base / stats（按对象类型分派）`
- **作用：** 输出对象的概要：数值向量的分位数、均值等；`lm` 模型的系数、标准误、t 值、P 值和拟合优度等。
- **常用形式：** `summary(object)`
- **参数与输入：** `object` 可为数值向量、数据框或回归模型；输出依其类型变化。

```r
summary(lfs$HOURPAY)
# 或
lm(HOURPAY ~ AGE, data = lfs) %>% summary()
```

**理解重点 / 易错点：** 这是一个通用函数：**对向量的 summary 不等于对回归模型的 summary**。第 8 讲补充材料部分写成 `%>% summary`，也能传递函数。

### 02｜读取、筛选、重编码与数据变形

#### `read_tsv()`

- **来源课次：** L2
- **所属包：** `readr（tidyverse）`
- **作用：** 从磁盘读取 Tab 分隔的 `.tab` / `.tsv` 文本数据。
- **常用形式：** `read_tsv(file, ...)`
- **参数与输入：** `file` 是相对或绝对路径；可用 `col_types` 控制类型。

```r
lfs <- read_tsv("../UKDA-9388-tab/tab/lfsp_jm25_eul_pwt24.tab")
```

**理解重点 / 易错点：** 路径以当前工作目录为准；课件使用 UK Data Service 的 Labour Force Survey 教学数据。

#### `select()`

- **来源课次：** L2、L4、L11
- **所属包：** `dplyr`
- **作用：** 按列名选择、保留或排列数据字段。
- **常用形式：** `select(data, column1, column2, ...)`
- **参数与输入：** 可以传列名、选择辅助表达式或用 `-` 排除列。

```r
lfs <- select(lfs, SEX, HOURPAY, AGE, GOR9D, EMPLEN, FTPT)
```

**理解重点 / 易错点：** Lecture 2 的完整教学代码还选取学历、行业、工作性质等字段；Lecture 11 为聚类标准误额外保留 `HSERIALP`。

#### `filter()`

- **来源课次：** L2、L4、L5、L8
- **所属包：** `dplyr`
- **作用：** 筛选满足条件的行；逗号分隔的多个条件表示同时满足（逻辑 AND）。
- **常用形式：** `filter(data, condition1, condition2, ...)`
- **参数与输入：** 条件应返回 TRUE/FALSE；比较符含 `>=`、`<=`、`!=` 等。

```r
lfs <- filter(lfs, AGE >= 16, AGE <= 64)
```

**理解重点 / 易错点：** 课程示范筛选有效工资、工作时长及负数缺失编码。**筛选不是缺失值填补**；条件为 NA 的行也可能被排除。

#### `mutate()`

- **来源课次：** L2、L3、L5、L9、L10、L11
- **所属包：** `dplyr`
- **作用：** 创建新列或修改原列，是数据重编码与特征构建的主函数。
- **常用形式：** `mutate(data, new_column = expression, ...)`
- **参数与输入：** 列名在左、表达式在右，可一次构建多列。

```r
lfs <- mutate(lfs, SEX = factor(SEX, levels = 1:2, labels = c("Male", "Female")))
```

**理解重点 / 易错点：** 改变源变量类型前先核对原始代码字典，避免把特殊缺失码解释成合法类别。

#### `factor()`

- **来源课次：** L2、L10
- **所属包：** `base`
- **作用：** 把编码值转换为离散分类变量，并指定合法水平及显示标签。
- **常用形式：** `factor(x, levels = ..., labels = ...)`
- **参数与输入：** `levels` 对应原始值顺序；`labels` 对应输出名称。

```r
factor(SEX, levels = 1:2, labels = c("Male", "Female"))
```

**理解重点 / 易错点：** 顺序错位会把类别标签配错；不在 `levels` 内的值通常成为 NA。

#### `case_when()`

- **来源课次：** L10
- **所属包：** `dplyr`
- **作用：** 按多条件逐行分配结果，适合将细分类别合并为较粗的类别。
- **常用形式：** `case_when(condition1 ~ value1, condition2 ~ value2, TRUE ~ default)`
- **参数与输入：** 顺序匹配，通常最先满足的规则生效；`TRUE ~ ...` 处理剩余情况。

```r
case_when(
  MARSTA == "Married, living with spouse" ~ "Married",
  MARSTA == "Divorced" ~ "Divorced",
  TRUE ~ "Other"
)
```

**理解重点 / 易错点：** Lecture 10 之后继续使用 `factor()`、`relevel()` 来定义新分类变量的回归参考组。

#### `relevel()`

- **来源课次：** L10
- **所属包：** `stats`
- **作用：** 为无序因子变量重新指定参考类别；用于改变回归中的对比基准。
- **常用形式：** `relevel(x, ref = "参考类别")`
- **参数与输入：** `ref` 必须已是该 factor 的水平。

```r
relevel(INDE07M, ref = "Public admin, education and health")
```

**理解重点 / 易错点：** **不会改变观测值本身**；只会影响回归系数相对哪个基准组解释。

#### `arrange()`

- **来源课次：** L3、L4
- **所属包：** `dplyr`
- **作用：** 按一列或多列对数据行排序。
- **常用形式：** `arrange(data, column)`
- **参数与输入：** 正向默认升序；课件用负号在数值列上表示逆序。

```r
lfs %>% arrange(HOURPAY) %>% tail()
```

**理解重点 / 易错点：** 缺失值排序规则需要留意；用于查看极端观测时应结合 `head()`/`tail()`。

#### `pull()`

- **来源课次：** L3
- **所属包：** `dplyr`
- **作用：** 从数据框抽出单列向量，便于传给 Base R 统计函数。
- **常用形式：** `pull(data, var)`
- **参数与输入：** `var` 为待提取列名。

```r
lfs %>% pull(BUSHR) %>% summary()
```

**理解重点 / 易错点：** 与 `select()` 返回数据框不同，`pull()` 通常返回向量。

### 03｜描述性统计、分组汇总与频数表

#### `mean()`

- **来源课次：** L3、L5、L6
- **所属包：** `base`
- **作用：** 计算算术平均数，适用于连续型变量的中心水平。
- **常用形式：** `mean(x, na.rm = FALSE)`
- **参数与输入：** `x` 应为数值；`na.rm = TRUE` 可忽略 NA。

```r
mean(c(1, 9, 8, 2, 7, 3, 2))
```

**理解重点 / 易错点：** 均值容易受极端值影响；课程将其与中位数比较以理解工资右偏。

#### `median()`

- **来源课次：** L3
- **所属包：** `stats`
- **作用：** 计算中位数，即 50% 分位数。
- **常用形式：** `median(x, na.rm = FALSE)`
- **参数与输入：** `x` 是数值向量；`na.rm` 控制是否忽略缺失值。

```r
lfs %>% summarise(median_pay = median(HOURPAY))
```

**理解重点 / 易错点：** 在偏态数据中通常比均值更稳健。

#### `min()`

- **来源课次：** L3
- **所属包：** `base`
- **作用：** 计算最小值。
- **常用形式：** `min(x, na.rm = FALSE)`
- **参数与输入：** `x` 是数值或可比较向量。

```r
lfs %>% summarise(minimum_pay = min(HOURPAY))
```

**理解重点 / 易错点：** 最低值可能代表异常编码，应结合数据字典解释。

#### `max()`

- **来源课次：** L3
- **所属包：** `base`
- **作用：** 计算最大值。
- **常用形式：** `max(x, na.rm = FALSE)`
- **参数与输入：** `x` 是数值或可比较向量。

```r
lfs %>% summarise(maximum_pay = max(HOURPAY))
```

**理解重点 / 易错点：** 极端最大值可能严重影响均值与线性回归。

#### `var()`

- **来源课次：** L3
- **所属包：** `stats`
- **作用：** 计算**样本方差**，反映围绕均值的离散程度。
- **常用形式：** `var(x, na.rm = FALSE)`
- **参数与输入：** `x` 为数值；样本方差使用 `n - 1` 分母。

```r
lfs %>% summarise(wage_var = var(HOURPAY))
```

**理解重点 / 易错点：** 方差的单位是原变量单位的平方；与 `sd()` 联合理解。

#### `sd()`

- **来源课次：** L3
- **所属包：** `stats`
- **作用：** 计算样本标准差，是样本方差的平方根。
- **常用形式：** `sd(x, na.rm = FALSE)`
- **参数与输入：** `x` 为数值。

```r
lfs %>% summarise(wage_sd = sd(HOURPAY))
```

**理解重点 / 易错点：** 标准差与原变量单位相同，解读更直观。

#### `quantile()`

- **来源课次：** L3
- **所属包：** `stats`
- **作用：** 计算给定概率位置上的分位数，可获得 Q1、Q2、Q3 或其他百分位点。
- **常用形式：** `quantile(x, probs = c(0, 0.25, 0.5, 0.75, 1))`
- **参数与输入：** `probs` 中每个数字应在 0–1 之间；`na.rm` 控制缺失值。

```r
quantile(HOURPAY, probs = c(0.25, 0.5, 0.75))
```

**理解重点 / 易错点：** Lecture 3 详细说明 `probs` 可以自由设为不同百分位，**不是只能填 0.25、0.5、0.75**。

#### `summarise()`

- **来源课次：** L3、L5、L6
- **所属包：** `dplyr`
- **作用：** 将多行数据汇总为统计结果，每组通常返回一行。
- **常用形式：** `summarise(data, result = expression, ...)`
- **参数与输入：** `result` 自定义输出字段名；接在 `group_by()` 后逐组计算。

```r
lfs %>% group_by(SEX) %>% summarise(mean_wage = mean(HOURPAY))
```

**理解重点 / 易错点：** 在 dplyr 中按组汇总后可能保留某些分组，后续计算要留意。

#### `reframe()`

- **来源课次：** L3
- **所属包：** `dplyr`
- **作用：** 允许每组返回任意多行的新汇总表，适用于把多个分位数堆叠输出。
- **常用形式：** `reframe(data, new = expression, ...)`
- **参数与输入：** 每个表达式可输出长度大于 1 的向量。

```r
reframe(lfs,
  quartiles = quantile(HOURPAY, probs = c(0.25, 0.5, 0.75)),
  q = c("First quartile", "Second Quartile", "Third Quartile")
)
```

**理解重点 / 易错点：** 与 `summarise()` 相比，`reframe()` 更自然地生成多行分位数结果。

#### `round()`

- **来源课次：** L3、L6
- **所属包：** `base`
- **作用：** 按指定小数位对数值四舍五入，改善统计表的可读性。
- **常用形式：** `round(x, digits = 0)`
- **参数与输入：** `digits` 表示保留的小数位数。

```r
lfs %>% group_by(SEX) %>% summarise(mean_wage = round(mean(HOURPAY), 2))
```

**理解重点 / 易错点：** 建议在显示阶段四舍五入，不要过早降低后续计算精度。

#### `sum()`

- **来源课次：** L3
- **所属包：** `base`
- **作用：** 求和；课堂主要用于计算频数总计，从而获得组别比例。
- **常用形式：** `sum(..., na.rm = FALSE)`
- **参数与输入：** 可传一个或多个数值向量。

```r
lfs %>% count(SEX) %>% mutate(percent = n / sum(n) * 100)
```

**理解重点 / 易错点：** 这里 `sum(n)` 是各类别频数之和，不是对调查对象工资求和。

#### `count()`

- **来源课次：** L3
- **所属包：** `dplyr`
- **作用：** 计算某一个或多个分类组合的观测数。
- **常用形式：** `count(data, column1, column2, ...)`
- **参数与输入：** 支持按列分组计数；结果默认叫 `n`。

```r
lfs %>% count(EMPLEN)
```

**理解重点 / 易错点：** 若需要百分比，再接 `mutate(percent = n / sum(n) * 100)`。

#### `group_by()`

- **来源课次：** L3、L5、L6
- **所属包：** `dplyr`
- **作用：** 给数据框设置分组信息，让后续汇总函数按组计算。
- **常用形式：** `group_by(data, column1, column2, ...)`
- **参数与输入：** 可按一个或多个分类变量分组。

```r
lfs %>% group_by(SEX) %>% summarise(mean_wage = mean(HOURPAY))
```

**理解重点 / 易错点：** `group_by()` 本身不会自动计算统计量，通常要接 `summarise()`。

#### `table()`

- **来源课次：** L3
- **所属包：** `base`
- **作用：** 生成一个或多个分类变量的频数表。
- **常用形式：** `table(x, y, ...)`
- **参数与输入：** 传入分类向量；二维表的顺序决定行和列。

```r
table(lfs$HIQUL22D, lfs$SEX)
```

**理解重点 / 易错点：** 课件用其制作教育水平 × 性别、行业 × 性别的交叉表。

#### `prop.table()`

- **来源课次：** L3
- **所属包：** `base`
- **作用：** 将频数表转换为比例表，可以以全表、行或列作为分母。
- **常用形式：** `prop.table(x, margin = NULL)`
- **参数与输入：** `margin = 1` 表示行内比例；`margin = 2` 表示列内比例；不填为整表比例。

```r
table(lfs$HIQUL22D, lfs$SEX) %>% prop.table(1) %>% round(2)
```

**理解重点 / 易错点：** 解读时务必说明分母：行比例与列比例对应完全不同的问题。

### 04｜ggplot2 绘图基础、坐标与主题

#### `ggplot()`

- **来源课次：** L4、L5
- **所属包：** `ggplot2`
- **作用：** 创建一个 ggplot 图对象，后续用 `+` 叠加图层和样式。
- **常用形式：** `ggplot(data, mapping = aes(...))`
- **参数与输入：** `data` 是绘图数据；`mapping` 指图形属性映射。

```r
lfs %>% ggplot(aes(HOURPAY)) + geom_histogram()
```

**理解重点 / 易错点：** `ggplot()` 本身仅设定绘图基础，实际图形通常需要几何对象层（如 `geom_histogram()`）。

#### `aes()`

- **来源课次：** L4、L5
- **所属包：** `ggplot2`
- **作用：** 定义数据字段与视觉通道（x、y、fill、colour 等）之间的映射。
- **常用形式：** `aes(x, y, fill = ..., colour = ...)`
- **参数与输入：** 列名通常无需引号；`fill = SEX` 表示依据数据列分组上色。

```r
ggplot(lfs, aes(HOURPAY, fill = SEX)) + geom_density(alpha = 0.2)
```

**理解重点 / 易错点：** 要区分 `aes(fill = SEX)`（数据映射）和 `geom_density(fill = "blue")`（固定颜色）。

#### `labs()`

- **来源课次：** L4、L5
- **所属包：** `ggplot2`
- **作用：** 设置图表标题、副标题、横纵轴标签、图例标题及来源注释。
- **常用形式：** `labs(title = ..., subtitle = ..., x = ..., y = ..., fill = ..., caption = ...)`
- **参数与输入：** 参数决定图表各个文本位置。

```r
ggplot(lfs, aes(HOURPAY)) + geom_histogram() +
  labs(title = "Distribution of hourly wage", x = "Hourly wage (£)", y = "Count")
```

**理解重点 / 易错点：** 课程强调图表要让读者在不看代码时也能理解变量、单位和来源。

#### `theme()`

- **来源课次：** L4、L5
- **所属包：** `ggplot2`
- **作用：** 对图的细节元素进行定制，例如图例位置、标题、坐标轴文字。
- **常用形式：** `theme(legend.position = ..., axis.text.x = element_text(...))`
- **参数与输入：** 主题元素常接收 `element_text()`、`element_blank()` 等对象。

```r
theme(legend.title = element_blank())
```

**理解重点 / 易错点：** `theme()` 是精细调整；`theme_minimal()` 等是整体预设主题。

#### `theme_dark()`

- **来源课次：** L4
- **所属包：** `ggplot2`
- **作用：** 使用内置深色绘图主题。
- **常用形式：** `theme_dark()`
- **参数与输入：** 没有必填参数。

```r
ggplot(lfs, aes(HOURPAY)) + geom_histogram() + theme_dark()
```

**理解重点 / 易错点：** Lecture 4 用于比较不同图形主题的视觉效果。

#### `theme_minimal()`

- **来源课次：** L4、L5
- **所属包：** `ggplot2`
- **作用：** 使用留白较多、减少装饰元素的预设主题。
- **常用形式：** `theme_minimal()`
- **参数与输入：** 没有必填参数。

```r
ggplot(lfs, aes(HOURPAY)) + geom_histogram() + theme_minimal()
```

**理解重点 / 易错点：** 课程多个正式示例使用它。

#### `theme_bw()`

- **来源课次：** Lecture 4（正文提到）
- **所属包：** `ggplot2`
- **作用：** 使用黑白背景、具有较清晰网格的预设主题。
- **常用形式：** `theme_bw()`
- **参数与输入：** 没有必填参数。

```r
ggplot(lfs, aes(HOURPAY)) + geom_histogram() + theme_bw()
```

**理解重点 / 易错点：** Lecture 4 正文提到，但未放入可执行代码块；本行是按课件语境补写的示例。

#### `theme_void()`

- **来源课次：** Lecture 4（正文提到）
- **所属包：** `ggplot2`
- **作用：** 使用极简无轴线、无网格、无背景信息的主题。
- **常用形式：** `theme_void()`
- **参数与输入：** 没有必填参数。

```r
ggplot(lfs, aes(HOURPAY)) + geom_histogram() + theme_void()
```

**理解重点 / 易错点：** Lecture 4 正文提到但未实际执行；对于必须标注数值和轴的课程统计图未必合适。

#### `element_blank()`

- **来源课次：** L4、L5
- **所属包：** `ggplot2`
- **作用：** 生成空白主题元素，常用于隐藏图例标题等装饰项。
- **常用形式：** `element_blank()`
- **参数与输入：** 没有必填参数。

```r
theme(legend.title = element_blank())
```

**理解重点 / 易错点：** 是主题元素构造函数，不是独立的绘图图层。

#### `element_text()`

- **来源课次：** L5
- **所属包：** `ggplot2`
- **作用：** 设定主题中文字的角度、大小、颜色等属性。
- **常用形式：** `element_text(angle = ..., size = ..., colour = ...)`
- **参数与输入：** 课堂使用 `angle = 90` 调整横轴文本旋转。

```r
theme(axis.text.x = element_text(angle = 90))
```

**理解重点 / 易错点：** 旋转标签适合横轴分类较多的热力图，需注意实际可读性。

#### `scale_x_log10()`

- **来源课次：** L4、L5
- **所属包：** `ggplot2`
- **作用：** 将图形 x 轴变换为以 10 为底的对数尺度。
- **常用形式：** `scale_x_log10()`
- **参数与输入：** 可附加刻度和标签参数；课件主要使用无参数形式。

```r
ggplot(lfs, aes(HOURPAY)) + geom_density() + scale_x_log10()
```

**理解重点 / 易错点：** 只改变绘图尺度/统计计算的尺度表达，不等同于回归中先生成 `log(HOURPAY)`；非正数无法直接取对数。

#### `scale_y_log10()`

- **来源课次：** L5
- **所属包：** `ggplot2`
- **作用：** 将图形 y 轴转为以 10 为底的对数尺度。
- **常用形式：** `scale_y_log10()`
- **参数与输入：** 可设置刻度、标签等；课件主要在工资箱线图使用。

```r
ggplot(lfs, aes(SEX, HOURPAY)) + geom_boxplot() + scale_y_log10()
```

**理解重点 / 易错点：** 直观展示跨度较大的工资数据，非正数不能在对数尺度上正常显示。

#### `coord_cartesian()`

- **来源课次：** L4
- **所属包：** `ggplot2`
- **作用：** 调整图表显示视窗，不直接删除基础数据。
- **常用形式：** `coord_cartesian(xlim = c(lower, upper), ylim = c(lower, upper))`
- **参数与输入：** `xlim` 与 `ylim` 控制可视范围。

```r
ggplot(lfs, aes(HOURPAY)) + geom_histogram() + coord_cartesian(xlim = c(0, 70))
```

**理解重点 / 易错点：** 与 `filter(HOURPAY < 70)` 实际移除行不同；zoom 和数据过滤应在方法中区分。

#### `coord_flip()`

- **来源课次：** L5
- **所属包：** `ggplot2`
- **作用：** 交换绘图的横纵坐标显示方向，将垂直箱线图/柱状图转为横向。
- **常用形式：** `coord_flip()`
- **参数与输入：** 没有必填参数。

```r
ggplot(lfs, aes(INDE07M, HOURPAY)) + geom_boxplot() + coord_flip()
```

**理解重点 / 易错点：** 方便展示名称较长的地区、行业等类别标签。

#### `scale_fill_colorblind()`

- **来源课次：** L5
- **所属包：** `ggthemes`
- **作用：** 使用针对部分色觉缺陷更友好的离散填充调色板。
- **常用形式：** `scale_fill_colorblind()`
- **参数与输入：** 可以设置图例等可选参数；课堂使用默认参数。

```r
library(ggthemes)
ggplot(lfs, aes(INDE07M, fill = HIQUL22D)) +
  geom_bar(position = "fill") + scale_fill_colorblind()
```

**理解重点 / 易错点：** 需要先安装/加载 `ggthemes`；颜色改善不代表所有阅读障碍都被解决。

### 05｜ggplot2 图层与多变量展示

#### `geom_histogram()`

- **来源课次：** L4
- **所属包：** `ggplot2`
- **作用：** 绘制连续型变量频数直方图。
- **常用形式：** `geom_histogram(binwidth = ..., bins = ...)`
- **参数与输入：** `binwidth` 指箱宽；`bins` 指分箱数量；二者通常择一。

```r
ggplot(lfs, aes(HOURPAY)) + geom_histogram(binwidth = 10)
```

**理解重点 / 易错点：** 分箱宽度对形状影响很大，课件比较了不同宽度的结果。

#### `geom_density()`

- **来源课次：** L4、L5
- **所属包：** `ggplot2`
- **作用：** 基于核密度估计绘制连续变量的平滑概率密度曲线。
- **常用形式：** `geom_density(alpha = ..., fill = ...)`
- **参数与输入：** `alpha` 是透明度；`fill` 可以是固定颜色，也可以放在 `aes()` 中表示分组。

```r
ggplot(lfs, aes(HOURPAY, fill = SEX)) + geom_density(alpha = 0.2)
```

**理解重点 / 易错点：** 密度曲线纵轴不是人数；组别曲线在默认设置下通常各自积分为 1，不能直接判断组间样本规模。

#### `geom_rug()`

- **来源课次：** L4
- **所属包：** `ggplot2`
- **作用：** 在坐标轴边缘绘制小刻痕，标记观测值位置。
- **常用形式：** `geom_rug()`
- **参数与输入：** 可设置方向、透明度等；课件调用默认参数。

```r
ggplot(lfs, aes(HOURPAY)) + geom_density() + geom_rug()
```

**理解重点 / 易错点：** 数据点过多时刻痕可能重叠严重。

#### `geom_boxplot()`

- **来源课次：** L5
- **所属包：** `ggplot2`
- **作用：** 绘制箱线图，直观展示中位数、四分位区间、须和异常值。
- **常用形式：** `geom_boxplot(width = ..., aes(fill = ...))`
- **参数与输入：** `width` 调箱宽；`fill` 用于填充颜色及组间比较。

```r
ggplot(lfs, aes(SEX, HOURPAY)) + geom_boxplot()
```

**理解重点 / 易错点：** 课件用于比较性别、地区、行业和学历之间的工资分布。

#### `geom_violin()`

- **来源课次：** L5
- **所属包：** `ggplot2`
- **作用：** 绘制小提琴图，以核密度形状比较不同类别的数值分布。
- **常用形式：** `geom_violin()`
- **参数与输入：** 可调整带宽等；课件主要使用默认参数。

```r
ggplot(lfs, aes(HIQUL22D, HOURPAY)) + geom_violin()
```

**理解重点 / 易错点：** 第 5 讲将其与窄箱线图 `geom_boxplot(width = 0.2)` 叠加展示。

#### `geom_jitter()`

- **来源课次：** L5
- **所属包：** `ggplot2`
- **作用：** 绘制加随机抖动的散点，减少类别或重复数值造成的重叠。
- **常用形式：** `geom_jitter(alpha = ...)`
- **参数与输入：** `alpha` 控制点透明度；还能设置抖动范围。

```r
ggplot(lfs, aes(AGE, HOURPAY)) + geom_jitter(alpha = 0.2)
```

**理解重点 / 易错点：** 抖动是可视化技巧，不代表观测值在数据层面真的改变。

#### `geom_point()`

- **来源课次：** L5
- **所属包：** `ggplot2`
- **作用：** 绘制普通散点图，展示两连续变量的二维关系。
- **常用形式：** `geom_point()`
- **参数与输入：** 可用 `aes()` 映射颜色、大小等属性。

```r
ggplot(lfs, aes(AGE, HOURPAY)) + geom_point()
```

**理解重点 / 易错点：** 课件进一步与 `geom_jitter()` 比较，以减少相同年龄造成的点重叠。

#### `geom_tile()`

- **来源课次：** L5
- **所属包：** `ggplot2`
- **作用：** 用矩形色块呈现两个离散维度上计算好的第三个数值，构成热力图。
- **常用形式：** `geom_tile()`
- **参数与输入：** 通过 `aes(x, y, fill = value)` 指定坐标和色块指标。

```r
lfs %>% group_by(HIQUL22D, INDE07M) %>%
  summarise(mean_wage = mean(HOURPAY)) %>%
  ggplot(aes(HIQUL22D, INDE07M, fill = mean_wage)) + geom_tile()
```

**理解重点 / 易错点：** 应先按行列组合汇总目标指标，而不是直接把原始工资逐行绘图。

#### `geom_bar()`

- **来源课次：** L5
- **所属包：** `ggplot2`
- **作用：** 绘制分类频数柱状图；若映射 `fill`，可堆叠类别数量或比例。
- **常用形式：** `geom_bar(position = "stack" / "fill")`
- **参数与输入：** 默认 `position = "stack"`；`position = "fill"` 每组标准化为比例。

```r
ggplot(lfs, aes(INDE07M, fill = HIQUL22D)) + geom_bar(position = "fill")
```

**理解重点 / 易错点：** `position="fill"` 的组内总高度均为 1，不能直接显示组间原始数量差异。

#### `facet_wrap()`

- **来源课次：** L5
- **所属包：** `ggplot2`
- **作用：** 按一个分类变量创建多个小面板，便于分组比较图形形状。
- **常用形式：** `facet_wrap(~ GROUP)`
- **参数与输入：** `~ GROUP` 是分面公式，指定分组变量。

```r
ggplot(lfs, aes(HOURPAY, fill = SEX)) + geom_density(alpha = 0.3) + facet_wrap(~GOR9D)
```

**理解重点 / 易错点：** 课件用于分地区比较男女工资密度分布。

#### `facet_grid()`

- **来源课次：** L5
- **所属包：** `ggplot2`
- **作用：** 按行和列两个变量排列分面，适合二维分类对照。
- **常用形式：** `facet_grid(ROW ~ COLUMN)`
- **参数与输入：** 公式左边控制行、右边控制列。

```r
ggplot(lfs, aes(HOURPAY, fill = SEX)) + geom_density(alpha = 0.3) + facet_grid(FTPT ~ JOBTYP)
```

**理解重点 / 易错点：** Lecture 5 比较全职/兼职 × 永久/非永久工作的工资分布。

#### `fct_reorder()`

- **来源课次：** L5
- **所属包：** `forcats`
- **作用：** 根据另一数值变量的汇总结果调整因子类别顺序。
- **常用形式：** `fct_reorder(f, x, .fun = median, .desc = FALSE)`
- **参数与输入：** `f` 是类别因子，`x` 是数值，`.fun` 是汇总函数，`.desc` 控制降序。

```r
mutate(GOR9D = fct_reorder(GOR9D, HOURPAY, median, .desc = TRUE))
```

**理解重点 / 易错点：** 课堂以地区工资中位数重新排序，再绘制更易比较的箱线图。

#### `fct_infreq()`

- **来源课次：** L5
- **所属包：** `forcats`
- **作用：** 按类别出现频率重新排序因子。
- **常用形式：** `fct_infreq(f)`
- **参数与输入：** `f` 为分类因子。

```r
mutate(INDE07M = fct_infreq(INDE07M))
```

**理解重点 / 易错点：** Lecture 5 与 `fct_rev` 联合使用，控制横向柱状图类别顺序。

#### `fct_rev()`

- **来源课次：** L5
- **所属包：** `forcats`
- **作用：** 反转因子水平的原有顺序。
- **常用形式：** `fct_rev(f)`
- **参数与输入：** `f` 为因子变量。

```r
mutate(INDE07M = fct_infreq(INDE07M) %>% fct_rev)
```

**理解重点 / 易错点：** 课堂在管道中直接写 `fct_rev` 而不加括号，这是合法的函数传递方式。

### 06｜概率、假设检验、方差分析与相关

#### `pnorm()`

- **来源课次：** L6
- **所属包：** `stats`
- **作用：** 计算正态分布在指定点左侧的累积概率。
- **常用形式：** `pnorm(q, mean = 0, sd = 1)`
- **参数与输入：** `q` 是阈值；默认计算标准正态分布 N(0,1) 的 CDF。

```r
1 - pnorm(11.26)
```

**理解重点 / 易错点：** 这里 `1 - pnorm(...)` 给出**右尾概率**；如果 z 非常大，计算机可能显示为 0（数值精度所致）。

#### `t.test()`

- **来源课次：** L6
- **所属包：** `stats`
- **作用：** 进行 t 检验，例如比较两组均值是否存在显著差异。
- **常用形式：** `t.test(y ~ group, data = data)`
- **参数与输入：** `y` 为数值因变量，`group` 为恰好两组的分类变量；默认进行 Welch 双样本 t 检验。

```r
t.test(HOURPAY ~ SEX, data = lfs)
```

**理解重点 / 易错点：** 判断均值差异时要结合置信区间、统计假设及可能的抽样设计局限。

#### `aov()`

- **来源课次：** L7
- **所属包：** `stats`
- **作用：** 拟合方差分析（ANOVA）模型，用于检验多个类别的均值是否一致。
- **常用形式：** `aov(y ~ group, data = data)`
- **参数与输入：** 左边为连续型结果，右边为分类组别。

```r
aov(HOURPAY ~ HIQUL22D, data = lfs) %>% summary()
```

**理解重点 / 易错点：** 整体 F 检验显著不等于所有组两两之间都显著不同。

#### `cor()`

- **来源课次：** L7
- **所属包：** `stats`
- **作用：** 计算两个数值变量之间的相关系数，默认 Pearson 线性相关。
- **常用形式：** `cor(x, y, method = "pearson")`
- **参数与输入：** `x`、`y` 是数值；可指定 `method`。

```r
cor(lfs$HOURPAY, lfs$AGE)
```

**理解重点 / 易错点：** 相关系数范围在 -1 到 1；相关关系不能直接解释为因果效应。

#### `cor.test()`

- **来源课次：** L7
- **所属包：** `stats`
- **作用：** 计算相关系数并检验其是否显著，输出置信区间和 P 值。
- **常用形式：** `cor.test(x, y) / cor.test(~ x + y, data = data)`
- **参数与输入：** 可传两个向量，或使用公式接口。

```r
cor.test(lfs$HOURPAY, lfs$AGE)
# 课堂还给出公式写法
cor.test(~ HOURPAY + AGE, data = lfs)
```

**理解重点 / 易错点：** 与 `cor()` 的主要区别是它会进行正式的统计推断。

### 07｜OLS 回归、函数形式与模型诊断

#### `lm()`

- **来源课次：** L6、L7、L8、L8 补充回归课件、L9、L10
- **所属包：** `stats`
- **作用：** 拟合线性回归模型：可含连续自变量、虚拟变量、多个控制变量。
- **常用形式：** `lm(formula, data = data)`
- **参数与输入：** 公式 `Y ~ X1 + X2`；左侧是因变量，右侧是解释变量；常与 `summary()` 联用。

```r
lm(HOURPAY ~ SEX + AGE + HIQUL22D, data = lfs) %>% summary()
```

**理解重点 / 易错点：** 课程核心函数。系数显著不是因果证明；解释时说明参照组、变量单位与其他控制变量。

#### `log()`

- **来源课次：** L9、L10、L11
- **所属包：** `base`
- **作用：** 计算自然对数（默认底数 e），用于线性化部分非线性关系、缓解严重右偏。
- **常用形式：** `log(x, base = exp(1))`
- **参数与输入：** `x` 是正数向量；在课堂中应用 `log(HOURPAY)`、`log(mpg)`、`log(wt)`。

```r
lfs %>% mutate(log_wage = log(HOURPAY))
```

**理解重点 / 易错点：** 必须检查 `x > 0`；对数因变量模型的斜率通常按百分比变化近似解释，不应当作原单位变化。

#### `plot()`

- **来源课次：** L8、L9
- **所属包：** `graphics（对 `lm` 对象使用 stats 绘图方法）`
- **作用：** 对回归模型输出诊断图；对一般数据也可直接绘图。
- **常用形式：** `plot(model, which = 1 / 2 / 5)`
- **参数与输入：** 课堂重点：`which=1` Residuals vs Fitted，`which=2` Normal Q-Q，`which=5` Residuals vs Leverage。

```r
lm(HOURPAY ~ AGE, data = lfs) %>% plot(which = 1)
```

**理解重点 / 易错点：** 需要先明确绘图对象：`plot(lm_object)` 是回归诊断图，不等同于 ggplot 图层。

#### `resettest()`

- **来源课次：** L9、L10
- **所属包：** `lmtest`
- **作用：** Ramsey RESET 检验，用于检测某些函数形式或遗漏非线性设定问题。
- **常用形式：** `resettest(model)`
- **参数与输入：** 传入 `lm` 模型对象，返回检验统计量和 P 值。

```r
mtcars %>% lm(mpg ~ wt, data = .) %>% resettest()
```

**理解重点 / 易错点：** 显著通常意味着设定可能有问题；不显著也不能证明模型一定正确。课件比较线性、半对数与双对数模型。

#### `bptest()`

- **来源课次：** L9、L10
- **所属包：** `lmtest`
- **作用：** Breusch–Pagan 检验，用于检测回归残差是否存在异方差。
- **常用形式：** `bptest(model)`
- **参数与输入：** 传入 `lm` 模型对象，返回 BP 统计量和 P 值。

```r
lfs %>% lm(HOURPAY ~ SEX + AGE, data = .) %>% bptest()
```

**理解重点 / 易错点：** 零假设通常是同方差；拒绝它提示有异方差证据，但不自动修复模型。

#### `vif()`

- **来源课次：** L10
- **所属包：** `car`
- **作用：** 计算方差膨胀因子，辅助评估解释变量之间的多重共线性。
- **常用形式：** `vif(model)`
- **参数与输入：** 传入回归模型；多自由度因子可能报告 GVIF 和调整后的 GVIF。

```r
lfs %>% lm(HOURPAY ~ SEX + AGE + HIQUL22D, data = .) %>% vif()
```

**理解重点 / 易错点：** 高 VIF 不必然要求删除变量；要结合理论、解释目标和类别变量自由度判断。

#### `coeftest()`

- **来源课次：** L10
- **所属包：** `lmtest`
- **作用：** 以给定协方差矩阵重新检验回归系数，输出估计、标准误、统计量和 P 值。
- **常用形式：** `coeftest(model, vcov. = covariance_matrix)`
- **参数与输入：** 可以提供稳健协方差矩阵；课件用管道及 `vcov` 参数传入。

```r
model <- lm(HOURPAY ~ SEX + AGE, data = lfs)
coeftest(model, vcov. = vcovHC(model))
```

**理解重点 / 易错点：** 系数点估计通常不变，主要改变标准误与推断；此处是教学化展开写法，与课件中的管道写法等价。

#### `vcovHC()`

- **来源课次：** L10
- **所属包：** `sandwich`
- **作用：** 计算异方差稳健协方差矩阵（heteroskedasticity-consistent covariance matrix）。
- **常用形式：** `vcovHC(model, type = ...)`
- **参数与输入：** `model` 为回归对象；`type` 用于选择 HC 类型。

```r
lfs %>% lm(HOURPAY ~ SEX + AGE, data = .) %>%
  coeftest(., vcov = vcovHC(.))
```

**理解重点 / 易错点：** Lecture 10 将其嵌套在 `coeftest()` 中；**它自身不是重新估计回归系数**。

#### `lm.cluster()`

- **来源课次：** L11
- **所属包：** `miceadds`
- **作用：** 拟合线性模型，并按指定聚类组计算聚类稳健标准误。
- **常用形式：** `lm.cluster(data, formula, cluster = "聚类ID")`
- **参数与输入：** `data` 是分析数据框，`formula` 是回归公式，`cluster` 为组别标识字段名。

```r
lfs %>%
  mutate(log_wage = log(HOURPAY)) %>%
  lm.cluster(data = ., log_wage ~ SEX + AGE, cluster = "HSERIALP") %>%
  summary()
```

**理解重点 / 易错点：** Lecture 11 聚类单位是家庭 `HSERIALP`；运行前要保留该字段，并检查每个聚类的记录情况。

### 08｜结果排版与论文输出

#### `knitr::kable()`

- **来源课次：** L6
- **所属包：** `knitr`
- **作用：** 把数据框或统计汇总转换为可在 R Markdown / Quarto 中显示的表格。
- **常用形式：** `knitr::kable(x)`
- **参数与输入：** `x` 是表格对象；可设置列名、标题、格式。

```r
lfs %>% group_by(SEX) %>%
  summarise(mean_wage = round(mean(HOURPAY), 2)) %>%
  knitr::kable()
```

**理解重点 / 易错点：** Lecture 6 用于展示男女平均工资表。对图表之外的结果，也应配文字解释。

## 三、不是普通函数但一定要会的 R 语法

这些符号实际在课程代码中频繁出现。它们不是本手册所统计的独立命名函数条目，但对于读懂前述函数调用不可缺少。

### 赋值 `<-`

```r
lfs <- read_tsv("file.tab")
```

把右边的结果保存到左边的对象。`=` 在某些情境也可赋值，但 `<-` 是课程常用风格。

### magrittr 管道 `%>%`

```r
lfs %>% group_by(SEX) %>% summarise(mean_wage = mean(HOURPAY))
```

将左侧对象作为右侧函数参数输入，便于从左到右书写数据流程。课件多处使用。

### Base R 管道 `|>`

```r
lfs |> count(SEX)
```

Lecture 3 在文字中提到 Base R 管道；思路相似但细节并非与 `%>%` 完全一致。

### 公式符号 `~`

```r
lm(HOURPAY ~ SEX + AGE, data = lfs)
```

左边是结果，右边是解释变量；在 `t.test()`、`aov()`、`lm()` 和 `facet_wrap()` 等函数中语义依上下文而定。

### 加号 `+`

```r
ggplot(lfs, aes(HOURPAY)) + geom_histogram() + theme_minimal()
```

在 ggplot 中用于增加图层；在回归公式右侧用于列出多个解释变量，并不是把变量数值直接相加。

### 点占位符 `.`

```r
lfs %>% lm(HOURPAY ~ AGE, data = .)
```

代表传入管道的左侧对象；`vcovHC(.)` 和 `data = .` 均是课堂使用例子。

### 字段提取 `$`

```r
summary(lfs$HOURPAY)
```

从数据框中取出列向量，与 tidyverse 非标准求值略有区别。

### 包命名空间 `::`

```r
knitr::kable(lfs)
```

指定从某包使用特定函数，无需先 `library(knitr)`；课件使用 `knitr::kable()`。

### 连续整数 `:`

```r
factor(SEX, levels = 1:2)
```

生成整数序列 `1, 2`，常用于类别代码范围。

### 逻辑比较

```r
filter(lfs, HOURPAY >= 6.4, FTPT != 3)
```

课堂用到 `<`、`>`、`<=`、`>=`、`==`、`!=`；`==` 表示比较而非赋值。

### 管道中的无括号函数名

```r
lfs %>% count(SEX) %>% summary
```

函数可直接作为管道右侧对象传入，不一定要写成 `summary()`；课件有 `%>% summary` 和 `%>% fct_rev`。

## 四、完整课程工作流示意

以下为将课上已教授的函数组织成一个研究顺序的**教学化综合示例**，并非对单一课件代码块的原样复制；执行前请确保原始数据路径和类别代码符合你手头的文件。

```r
library(tidyverse)

# 1. 数据导入（使用课程自己的文件路径）
lfs <- read_tsv("../UKDA-9388-tab/tab/lfsp_jm25_eul_pwt24.tab")

# 2. 保留研究所需变量并筛选范围
lfs <- lfs %>%
  select(SEX, HOURPAY, AGE, HIQUL22D) %>%
  filter(HOURPAY >= 6.4, HOURPAY <= 100, AGE >= 16, AGE <= 64) %>%
  mutate(SEX = factor(SEX, levels = 1:2, labels = c("Male", "Female")))

# 注意：完整课堂数据清理还有其他编码与缺失值筛选步骤
glimpse(lfs)

# 3. 描述性统计
lfs %>% group_by(SEX) %>% summarise(
  n = sum(!is.na(HOURPAY)),
  mean_wage = mean(HOURPAY, na.rm = TRUE),
  median_wage = median(HOURPAY, na.rm = TRUE)
)

# 4. 单变量分布和组间图
lfs %>% ggplot(aes(HOURPAY)) + geom_histogram(binwidth = 5) + theme_minimal()
lfs %>% ggplot(aes(SEX, HOURPAY)) + geom_boxplot() + scale_y_log10()

# 5. 多变量 OLS 与诊断
model <- lm(HOURPAY ~ SEX + AGE + HIQUL22D, data = lfs)
summary(model)
plot(model, which = 1)   # Residuals vs Fitted
plot(model, which = 2)   # Normal Q-Q
lmtest::resettest(model)
lmtest::bptest(model)
car::vif(model)
lmtest::coeftest(model, vcov. = sandwich::vcovHC(model))
```

**新增说明：** 此综合示例中的 `is.na()` 和 `!` 仅用于演示如何在 `summarise()` 中计算有效观测数，**不计入上述 78 个源课件收录函数**；若要求严格只使用课上实际调用的函数，可删去 `n = ...` 行。课件的数据可能存在非标准负数缺失编码，因此不要只依赖 `na.rm = TRUE`。

## 五、最终研究论文的重点函数

| 作业阶段 | 推荐重点 | 原因 |
|---|---|---|
| 数据导入与清洗 | `read_tsv`, `select`, `filter`, `mutate`, `factor`, `glimpse` | 明确样本筛选与变量构建是否合理 |
| 描述性统计 | `summarise`, `group_by`, `mean`, `median`, `sd`, `quantile`, `count`, `table`, `prop.table` | 说明数据分布和样本组成 |
| 数据可视化 | `ggplot`, `aes`, `geom_histogram`, `geom_density`, `geom_boxplot`, `geom_point`, `labs` | 展示因变量和关键自变量的关系 |
| 推断统计 | `t.test`, `aov`, `cor.test` | 需要时用于前期假设检验；不必机械地全部使用 |
| 核心回归 | `lm`, `summary`, `log`, `relevel` | 明确控制变量、函数形式和系数解释 |
| 模型诊断 | `plot`, `resettest`, `bptest`, `vif` | 检查函数形式、异方差、共线性与影响点 |
| 稳健推断 | `coeftest`, `vcovHC`, `lm.cluster` | 在研究设计需要时报告稳健或聚类标准误 |
| 论文展示 | `knitr::kable` | 在 R Markdown 或 Quarto 中输出整洁表格 |

## 六、适用范围与来源文件

课件标题和文件：
- Lecture 1: `lecture1_notes.html`
- Lecture 2: `lecture2_notes.html`
- Lecture 3: `lecture3_notes.html`
- Lecture 4: `lecture4_notes.html`
- Lecture 5: `lecture5_notes.html`
- Lecture 6: `lecture6_notes.html`
- Lecture 7: `lecture7_notes.html`
- Lecture 8: `lecture8_notes.html`
- Lecture 8 补充：`lecture8_regressions.html`
- Lecture 9: `lecture9_notes.html`
- Lecture 10: `lecture10_notes.html`
- Lecture 11: `lecture11_notes.html`

**范围边界：** 没有纳入 `Summative-assessment_example.html`、Assessment Brief 或 Formative Brief 的函数；这些并非本次指定的 11 讲课件。也没有把教师在 Lecture 11 的 Beyond OLS 部分概念性介绍的 Poisson、Logit、Panel Models 等方法当成 R 函数。

**重要学习建议：** 课程的正式核心是构建、诊断并解释线性回归，不是尽可能添加课外机器学习算法。Lecture 11 还明确表示对介绍的 Beyond OLS 其他回归方法不额外加分，且不希望学生将这些方法加入本次作业。

---

**核对信息：** 本手册按 Python 提取的课件 R 代码函数名清单生成，逐条比对所有带括号的函数调用，额外纳入无括号的 `fct_rev` 和 4 个明确提到的函数。
