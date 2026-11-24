#  转换 DataFrame


# 聚合 DataFrame
### 汇总统计简介

#### 数据汇总与概要统计
- 在学习了 DataFrame 的排序、筛选子集和添加新列之后，本章进入数据汇总部分。
- 所谓概要统计，就是用一些数字来概括并描述数据集的特征。

### 常用概要统计

#### 汇总数值数据
- 最常见的概要统计之一是均值，它可以揭示数据的大致中心位置。计算一列的均值，先用方括号选中该列，然后调用 `.mean()`。
```python
dogs["height_cm"].mean()
# 输出: 49.714285714285715
```
- 列上还能计算其他多种概要统计：
  - 中位数与众数：`.median()`、`.mode()`
  - 最小与最大值：`.min()`、`.max()`
  - 方差与标准差：`.var()`、`.std()`
  - 求和：`.sum()`

#### 汇总日期
- 日期列同样可以做概要统计。
- 对出生日期列取最小值，可找到最年长的狗的出生日期：
```python
dogs["date_of_birth"].min()
# 输出: '2011-12-11'
```
- 取最大值，可以看到最年轻的狗出生在 2018 年：
```python
dogs["date_of_birth"].max()
# 输出: '2018-02-27'
```

### 自定义聚合与多维度汇总

#### `.agg()` 方法
- `aggregate` 方法（即 `.agg`）允许您计算自定义的概要统计。
- 示例：创建一个名为 `pct30` 的函数，用来计算某列的第 30 个百分位。只需知道这个函数接收一列数据并返回该列的第 30 百分位即可。
```python
def pct30(column):
    return column.quantile(0.3)

dogs["weight_kg"].agg(pct30)
```
- 选中体重列并调用 `.agg`，传入自定义函数名，即可得到所有狗体重的第 30 百分位。

#### 多列汇总
- `agg` 可以同时作用在多列上。通过选中体重和身高两列再调用 `agg`，可同时得到这两列的第 30 百分位。
```python
dogs[["weight_kg", "height_cm"]].agg(pct30)
```

#### 多项汇总
- 可以使用 `agg` 一次性获取多个概要统计。
- 示例：定义 `pct40` 函数计算第 40 个百分位，将函数列表传给 `agg`（传入 `pct30` 和 `pct40`），返回的就是狗的体重在第 30 和第 40 百分位的结果。
```python
def pct40(column):
    return column.quantile(0.4)

dogs["weight_kg"].agg([pct30, pct40])
```

### 累积统计

#### 累积和
- pandas 提供了累计统计的方法。对某一列调用 `.cumsum()`，会为 DataFrame 的每一行返回一个数，而不是单个数字。
- 第一个返回的数等于第一行的值。
- 下一个数是前两行值的和，第三个数是前三行之和，以此类推。
- 最后一个数是所有值的总和。
```python
# 原始数据
dogs["weight_kg"]

# 累积和
dogs["weight_kg"].cumsum()
```

#### 其他累积统计
- pandas 还有其他累计统计的方法，它们都会返回一整列数据：
  - `.cummax()`：累计最大值
  - `.cummin()`：累计最小值
  - `.cumprod()`：累计乘积

### 沃尔玛数据集简介

- 本章将使用 Walmart 门店相关的数据进行练习。
- Walmart 是一家在美国运营的连锁百货商店。
- 数据集包含的信息：
  - 各门店以美元计的每周销售额。
  - 每家门店的 ID 编号和特定的门店类型。
  - 销售额按部门 ID 做了区分。
  - 其他信息：是否为节假日周、该门店所在地当周的平均气温、当周以美元/升计的平均燃油价格，以及当周的全国失业率等。
---

### 计数

#### 避免重复计数
- 汇总分类型数据时，直接统计往往会导致错误，因为同一个实体（如同一只狗）可能在数据集中出现多次。
- 例如，宠物就诊记录中包含多次就诊的狗（如 Max 和 Stella），直接按品种统计会导致重复计数。

#### 按姓名去重
- 使用 `drop_duplicates()` 方法可以去掉数据集中先前已出现的重复行。
- 通过 `subset` 参数指定判定重复的列（如仅按姓名去重）：
```python
vet_visits.drop_duplicates(subset="name")
```
- **局限性**：如果存在两只不同品种但同名的狗（如两只 Max），仅按姓名去重会导致其中一只被错误删除。

#### 按成对字段去重
- 为了保留不同品种的同名狗，可以将多个列名以列表形式传给 `subset` 参数，基于多列组合判断重复：
```python
unique_dogs = vet_visits.drop_duplicates(subset=["name", "breed"])
print(unique_dogs)
```
- 这样，名字和品种完全相同的记录才会被视为重复，两个 Max 都会被保留。

#### 统计频数
- 使用 `value_counts()` 方法统计分类列中每个类别的出现次数。
- 可以通过 `sort=True` 参数对结果进行排序，让计数最多的类别排在前面：
```python
unique_dogs["breed"].value_counts()
unique_dogs["breed"].value_counts(sort=True)
```

#### 计算占比
- 使用 `normalize=True` 参数，可以将计数结果转换为该类别占总体的比例。
```python
unique_dogs["breed"].value_counts(normalize=True)
```
- 例如，结果显示 `Labrador 0.250`，表示有 25% 的狗是拉布拉多。

## 分组汇总统计

#### 分组汇总的动机
- 之前学习的是为整个数据集的所有行计算单一的汇总统计量。
- 但用汇总统计量来对比不同分组往往能获得更多洞见。例如，不同毛色的狗平均体重有差异吗？母犬比公犬更高吗？
- 可以通过筛选（如按毛色提取子集）分别计算均值，但这样步骤繁琐，且重复代码容易因复制粘贴而出错。
```python
# 繁琐的方式：每次筛选后单独计算
dogs[dogs["color"] == "Black"]["weight_kg"].mean()
dogs[dogs["color"] == "Brown"]["weight_kg"].mean()
dogs[dogs["color"] == "White"]["weight_kg"].mean()
```

#### 使用 `groupby` 方法
- 使用 `groupby` 方法可以简洁地对数据进行分组汇总。
- 按指定变量（如“颜色”）分组，选取目标列（如“体重”），计算聚合统计量（如均值）：
```python
dogs.groupby("color")["weight_kg"].mean()
```
- 相比手动筛选，一行代码即可得到每种毛色对应的平均体重，简洁高效。

### 进阶分组汇总

#### 多种分组汇总
- 与未分组的汇总统计类似，可以使用 `.agg()` 方法在一次分组中同时计算多个统计量。
- 按颜色分组后，将函数列表传递给 `agg`，可得到不同毛色狗体重的最小值、最大值和总和：
```python
dogs.groupby("color")["weight_kg"].agg([min, max, sum])
```

#### 按多个变量分组
- 传入一个列名列表给 `groupby`，即可按多列进行分组。
- 例如，按颜色和品种分组，计算平均体重，得到每种颜色下各个品种的平均体重：
```python
dogs.groupby(["color", "breed"])["weight_kg"].mean()
```

#### 多组与多指标汇总
- 在按多列分组的基础上，还可以同时对多列数据做聚合。
- 示例：按颜色和品种分组，同时计算体重和身高的平均值：
```python
dogs.groupby(["color", "breed"])[["weight_kg", "height_cm"]].mean()
```


```python
# For each store type, aggregate weekly_sales: get min, max, mean, and median

sales_stats = sales.groupby('type')['weekly_sales'].agg(['min', 'max', 'mean', 'median'])

  

# Print sales_stats

print(sales_stats)

  

# For each store type, aggregate unemployment and fuel_price_usd_per_l: get min, max, mean, and median

unemp_fuel_stats = sales.groupby('type')[['unemployment','fuel_price_usd_per_l']].agg(['min', 'max', 'mean', 'median'])

  

# Print unemp_fuel_stats

print(unemp_fuel_stats)
```



## 数据透视表

#### 基本概念
- 数据透视表是另一种计算分组汇总统计的方法，与电子表格中的透视表功能类似。
- 在 pandas 中，使用 `pivot_table()` 方法可以轻松实现。

#### 从分组到透视表
- 使用 `pivot_table` 可以达到与 `groupby` 相同的效果。
  - `values` 参数：指定您想要汇总的列。
  - `index` 参数：指定您想要分组的列。
- 默认情况下，`pivot_table` 会对每个分组取**平均值**。
```python
# 使用 groupby
dogs.groupby("color")["weight_kg"].mean()

# 使用 pivot_table
dogs.pivot_table(values="weight_kg", index="color")
```

#### 应用不同统计量
- 如果需要计算不同的汇总统计，可以使用 `aggfunc` 参数并传入相应的函数（如计算中位数）。
```python
dogs.pivot_table(values="weight_kg", index="color", aggfunc="median")
```

#### 计算多种统计量
- 如果想一次性获得多种汇总统计，可以给 `aggfunc` 参数传入一个函数列表（如同时计算平均值和中位数）。
```python
dogs.pivot_table(values="weight_kg", index="color", aggfunc=["mean", "median"])
```

#### 按两个变量透视
- 要按两个变量（如颜色和品种）分组，可以在 `columns` 参数中指定第二个变量。
```python
dogs.pivot_table(values="weight_kg", index="color", columns="breed")
```
- **注意**：结果中会出现 `NaN`（缺失值），这是因为某些组合在数据集中不存在（例如没有黑色吉娃娃或灰色拉布拉多）。展示方式与 `groupby` 略有不同（形成矩阵式表格），但数值含义相同。

#### 在透视表中填充缺失值
- 如果不希望显示缺失值，可以使用 `fill_value` 参数指定填充内容（如填充为 0）。
```python
dogs.pivot_table(values="weight_kg", index="color", columns="breed", fill_value=0)
```

#### 透视表求和（添加边际汇总）
- 将 `margins` 参数设置为 `True` 后，数据透视表的最后一行和最后一列会给出各自列或行的总体均值汇总。
- **注意**：计算均值时，不会把用 0 填充的缺失值算进去。
- **示例解读**：
  - 拉布拉多列的最后一行：拉布拉多犬的平均体重（26 kg）。
  - 棕色行的最后一列：棕色狗的平均体重（24 kg）。
  - 右下角数值：整个数据集中所有狗的平均体重。
```python
dogs.pivot_table(values="weight_kg", index="color", columns="breed", 
                 fill_value=0, margins=True)
```
- **优势**：开启 `margins=True` 可以同时查看到多个层级的汇总统计（整个数据集、按单一变量分组、按双变量分组）。