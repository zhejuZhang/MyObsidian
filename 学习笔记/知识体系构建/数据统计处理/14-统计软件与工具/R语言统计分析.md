# R语言统计分析

> R是统计学家开发的语言，是统计分析的黄金标准。

---

## R的优势

| 优势 | 描述 |
|------|------|
| 统计功能完善 | 最全面的统计包 |
| 可视化强大 | ggplot2 |
| 免费开源 | 无成本 |
| 学术界标准 | 大量统计方法首先在R中实现 |
| CRAN | 20000+包 |

---

## 基础操作

### 数据类型

```r
# 向量
x <- c(1, 2, 3, 4, 5)

# 数据框
df <- data.frame(
  name = c("A", "B", "C"),
  value = c(10, 20, 30)
)

# 列表
lst <- list(a = 1, b = "hello", c = TRUE)

# 矩阵
m <- matrix(1:6, nrow = 2, ncol = 3)
```

### 数据读写

```r
# CSV
df <- read.csv("data.csv")
write.csv(df, "output.csv", row.names = FALSE)

# Excel
library(readxl)
df <- read_excel("data.xlsx")

# 数据库
library(DBI)
con <- dbConnect(RSQLite::SQLite(), "db.sqlite")
df <- dbGetQuery(con, "SELECT * FROM table")
```

---

## 描述性统计

```r
# 基本统计量
summary(df)
mean(x)
median(x)
sd(x)
var(x)

# 频次表
table(df$category)
prop.table(table(df$category))

# 相关系数
cor(df$x, df$y)
cor(df)  # 相关矩阵
```

---

## 假设检验

```r
# t检验
t.test(x, mu = 0)  # 单样本
t.test(x, y)  # 独立样本
t.test(x, y, paired = TRUE)  # 配对样本

# 方差分析
aov_result <- aov(value ~ group, data = df)
summary(aov_result)
TukeyHSD(aov_result)

# 卡方检验
chisq.test(table(df$var1, df$var2))

# 非参数检验
wilcox.test(x, y)  # Mann-Whitney
kruskal.test(value ~ group, data = df)  # Kruskal-Wallis
```

---

## 回归分析

```r
# 线性回归
model <- lm(y ~ x1 + x2, data = df)
summary(model)
confint(model)
predict(model, newdata)

# 逻辑回归
model <- glm(y ~ x1 + x2, data = df, family = binomial)
summary(model)

# 多项式回归
model <- lm(y ~ poly(x, 2), data = df)
```

---

## 可视化

### ggplot2

```r
library(ggplot2)

# 散点图
ggplot(df, aes(x = x, y = y)) +
  geom_point() +
  geom_smooth(method = "lm") +
  theme_minimal()

# 直方图
ggplot(df, aes(x = value)) +
  geom_histogram(binwidth = 1)

# 箱线图
ggplot(df, aes(x = group, y = value)) +
  geom_boxplot()
```

### 基础绘图

```r
plot(x, y)
hist(x)
boxplot(x)
barplot(table(df$category))
```

---

## 常用包

| 包 | 用途 |
|------|------|
| dplyr | 数据处理 |
| ggplot2 | 可视化 |
| tidyr | 数据整理 |
| readr | 数据读取 |
| stringr | 字符串处理 |
| lubridate | 日期处理 |
| caret | 机器学习 |
| lme4 | 混合效应模型 |
| survival | 生存分析 |
| lavaan | 结构方程模型 |

---

## 数据处理（dplyr）

```r
library(dplyr)

df %>%
  filter(age > 18) %>%
  select(name, age, income) %>%
  mutate(income_k = income / 1000) %>%
  group_by(gender) %>%
  summarise(
    mean_income = mean(income),
    n = n()
  ) %>%
  arrange(desc(mean_income))
```

---

## R vs Python

| 维度 | R | Python |
|------|---|--------|
| 统计分析 | ✓ 更强 | ✓ |
| 机器学习 | ✓ | ✓ 更强 |
| 深度学习 | 弱 | ✓ 更强 |
| 可视化 | ✓ 更强 | ✓ |
| 数据处理 | ✓ | ✓ |
| 生产部署 | 弱 | ✓ 更强 |
| 学习曲线 | 中 | 低 |

---

## 相关概念

- [[Python统计分析]] — Python的统计分析
- [[其他统计软件]] — 其他工具

---

## 常见误区

1. **不向量化**：R的向量化操作比循环快
2. **不用管道**：管道操作更清晰
3. **忽视包管理**：应使用renv管理依赖
4. **不看文档**：R的文档非常详细
