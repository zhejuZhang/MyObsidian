#  转换 DataFrame


# 聚合 DataFrame
### 汇总统计简介

#### 课程背景
- 本门课由讲师 Maggie 讲解。
- 回顾第一章：学习了 DataFrame 的排序、筛选子集以及添加新列。
- 本章主题：数据汇总（Summary Statistics）。用一些数字来概括并描述数据集。

### 数值与日期的概要统计

#### 汇总数值数据
- 最常见的概要统计之一是**均值（mean）**，用于了解数据的中心位置。
- 选取列并调用 `.mean()` 方法计算均值。
- 其他常见的统计量包括：中位数、众数、最小值、最大值、方差、标准差、求和以及分位数。
```python
# 计算某列的均值
df['column_name'].mean()

# 计算中位数
df['column_name'].median()

# 计算最大值/最小值
df['column_name'].max()
df['column_name'].min()

# 计算方差和标准差
df['column_name'].var()
df['column_name'].std()
```

#### 汇总日期
- 日期列也可以进行概要统计。
- 使用 `min()` 可以找到最早的日期（例如最年长的狗的出生日期）。
- 使用 `max()` 可以找到最晚的日期（例如最年轻的狗的出生日期）。
```python
df['birth_date'].min()
df['birth_date'].max()
```

### 自定义聚合与累积统计

#### .agg() 方法
- `aggregate()`（简写为 `agg()`）允许计算自定义的概要统计。
- 示例：创建一个名为 `pct30` 的自定义函数，用于计算某列的第 30 个百分位。
```python
# 定义自定义函数
def pct30(column):
    return column.quantile(0.3)

# 对体重列调用自定义函数
df['weight'].agg(pct30)
```

#### 多列汇总
- `agg` 可以同时作用于多个列，只需在传入函数前选择多列即可。
```python
# 同时获取体重和身高两列的第 30 百分位
df[['weight', 'height']].agg(pct30)
```

#### 多项汇总
- 将函数列表传给 `agg`，可以一次性获取多个概要统计。
```python
# 定义另一个自定义函数
def pct40(column):
    return column.quantile(0.4)

# 同时计算第 30 和第 40 百分位
df['weight'].agg([pct30, pct40])
```

#### 累积和
- pandas 提供了累计统计方法，如 `.cumsum()`。
- `cumsum` 会为 DataFrame 的每一行返回一个累加值。
- 第一个数是第一行的值，第二个数是前两行之和，以此类推，最后一个数是所有行的总和。
```python
df['weight'].cumsum()
```

#### 累积统计
- pandas 还提供了其他累计统计方法，它们都会返回一整列数据而不是单个数字。
```python
# 累计最大值
df['column_name'].cummax()

# 累计最小值
df['column_name'].cummin()

# 累计乘积
df['column_name'].cumprod()
```

### 沃尔玛数据集介绍

#### 数据集背景
- 本章将使用沃尔玛（Walmart）门店相关的数据。
- 沃尔玛是一家在美国运营的连锁百货商店。

#### 数据字段说明
数据集包含各门店的以下信息：
- 每家门店的 ID 编号和特定的门店类型。
- 以美元计的每周销售额（按部门 ID 区分）。
- 是否为节假日周。
- 该门店所在地当周的平均气温。
- 当周以美元每升计的平均燃油价格。
- 当周的全国失业率。
