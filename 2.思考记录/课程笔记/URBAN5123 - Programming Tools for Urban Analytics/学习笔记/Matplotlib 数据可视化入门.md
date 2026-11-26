# Matplotlib 简介


### 使用 Matplotlib 进行数据可视化简介

#### 数据可视化的意义
- “一张图胜过千言万语”：可视化不仅能帮助我们从数据中提炼洞见，也能更清晰地向他人传达信息。
- **Matplotlib**：一个广泛用于数据可视化的 Python 库。
- **核心优势**：对图表各项属性有完全的掌控，可以精细地自定义并控制可视化的具体呈现，甚至能编写程序根据数据自动生成可视化。

#### pyplot 接口简介（面向对象接口）
- 通常导入 `matplotlib.pyplot` 并命名为 `plt`。
- `plt.subplots()`：不带参数调用时，会创建一个 **Figure** 对象和一个 **Axes** 对象。
  - **Figure**：容器，页面上看到的所有内容都在其中。
  - **Axes**：承载数据的区域，我们在这块画布上“作画”。
```python
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
plt.show()
```

#### 向坐标轴添加数据
- 绘图命令是 Axes 对象的方法，通常使用 `.plot()`。
- 准备示例数据（如西雅图的天气数据）：
  - `"MONTH"` 列：每个月的三字母名称（X 轴）。
  - `"MLY-TAVG-NORMAL"` 列：每月平均气温（Y 轴）。
- 调用 `ax.plot(x, y)` 将数据添加到 Axes 上，最后调用 `plt.show()` 显示。
```python
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"])
plt.show()
```
- 生成折线图后，数据的趋势比查看原始表格清晰得多。

#### 添加更多数据（图层叠加）
- 可以在同一个 Axes 上叠加多条折线（如加入奥斯汀的平均气温数据）。
```python
ax.plot(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"])
```

#### 综合示例
创建包含两条折线的图表的标准流程：
```python
fig, ax = plt.subplots()
# 添加第一组数据（西雅图）
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"])
# 添加第二组数据（奥斯汀）
ax.plot(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"])
plt.show()
```


---

### 自定义图表

#### 自定义数据外观
- 默认的折线图看起来是连续的，但如果数据是离散的（例如每月测量一次），可以通过添加**标记**来更好地表达这一点，明确数据点的位置。

#### 添加与选择标记
- `plot` 方法接收 `marker` 关键字参数，用于指定标记的形状。
- 例如，传入 `"o"` 表示圆形，传入 `"v"` 表示向下的三角形。
```python
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"], marker="v")
```

#### 设置线型
- 使用 `linestyle` 关键字参数改变连接线的样式，例如传入 `"--"` 表示虚线。
- 如果想彻底去掉连线只保留数据点，可以将 `linestyle` 设置为 `"None"`。
```python
ax.plot(..., marker="v", linestyle="None")
```

#### 选择颜色
- 使用 `color` 关键字参数修改数据（线条和标记）的颜色，例如传入 `"r"` 表示红色。
```python
ax.plot(..., marker="v", linestyle="--", color="r")
```

#### 自定义坐标轴标签
- 清晰的轴标签对可视化非常重要。Axes 对象提供了以 `set_` 开头的方法来修改这些属性。
- **X 轴标签**：使用 `ax.set_xlabel()`。注意标签的大小写应像普通句子一样（首词首字母大写）。
```python
ax.set_xlabel("Time (months)")
```
- **Y 轴标签**：使用 `ax.set_ylabel()`。
```python
ax.set_ylabel("Average temperature (Fahrenheit)")
```

#### 添加标题
- 使用 `ax.set_title()` 方法为图表添加标题，提供更多关于数据的背景信息。
```python
ax.set_title("Weather in Seattle")
```

---


### 小倍数图

#### 为什么需要小倍数图
- 当试图在一张图表中添加过多数据时，画面会变得拥挤，不仅无法揭示模式，反而会掩盖它们。
- **小倍数图（Small multiples）**：使用多张小图，在不同条件下展示相似的数据（例如，按城市分开展示降水数据）。

#### 使用 `plt.subplots` 创建子图
- 在 Matplotlib 中，小倍数图通过子图（subplots）实现。
- 向 `plt.subplots()` 传入行数和列数，即可创建网格布局的子图。
```python
# 创建包含 3 行 2 列子图的 Figure
fig, ax = plt.subplots(3, 2)
```
- **注意**：此时变量 `ax` 不再是一个单一的 Axes 对象，而是一个 **Axes 对象的 numpy 数组**（形状为 `(3, 2)`）。

#### 向子图添加数据
- 需要先对 `ax` 数组进行索引，找到特定的子图，然后再调用 `.plot()` 方法。
```python
# 在左上角（第 1 行，第 1 列）的子图中绘图
ax[0, 0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"], color='b')
```

#### 一维布局的特殊情况
- 如果子图只有一行或只有一列，返回的 `ax` 数组将是**一维**的，只需提供单个索引。
```python
# 创建 2 行 1 列的子图
fig, ax = plt.subplots(2, 1)

# 顶部子图（西雅图）
ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"], color='b')

# 底部子图（奥斯汀）
ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"], color='r')

# 为子图分别设置标签
ax[0].set_ylabel("Precipitation (inches)")
ax[1].set_ylabel("Precipitation (inches)")
ax[1].set_xlabel("Time (months)")
plt.show()
```

#### 共享坐标轴范围
- 上下对比两个城市的数据时，如果两个数据集的数值范围不同，它们的 y 轴范围可能不一致，影响对比。
- 可以在创建子图时，通过设置 `sharey=True` 来让所有子图共享同一个 y 轴范围。
```python
fig, ax = plt.subplots(2, 1, sharey=True)
```
- 共享 y 轴后，跨数据集的比较将更加直接和准确。

#### 最终展示
完成所有自定义后，最后调用 `plt.show()` 显示图表。


# 绘制时间序列

### 绘制时间序列数据

#### 时间序列与 DataFrame 索引
- 时间序列数据（如按时间排列的连续变量）非常适合用来发现数据中的模式。
- 在处理时间序列时，通常需要让 pandas 将日期列解析为 datetime 格式（`parse_dates`），并将其设置为索引（`index_col`），以便利用 pandas 强大的时间索引功能。
- 转换后的索引是一个 **`DatetimeIndex`** 对象。Matplotlib 会自动识别该变量为时间类型，并对 x 轴进行智能化处理（如自动按年份显示刻度）。

#### 绘制时间序列数据
- 在绘图时，直接将 `DatetimeIndex`（即 `df.index`）作为 x 轴，所需的数据列作为 y 轴传入 `plot()` 方法。
```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(climate_change.index, climate_change['co2'])
ax.set_xlabel('Time')
ax.set_ylabel('CO2 (ppm)')
plt.show()
```
- Matplotlib 会自动将 x 轴格式化为年份，并根据数据范围（如几十年）自动设置合适的刻度间隔（如以 10 年为单位）。
- **缺失值处理**：如果数据包含 `NaN`（如 CO2 测量中未测量的月份），Matplotlib 在绘制折线图时会自动在该处断开，显示出缺口。

#### 放大时间序列（切片）
- 通过 pandas 的字符串切片，可以非常方便地对 DataFrame 进行时间维度的子集选择。
- **查看一个十年**：传入起始和结束日期的字符串。Matplotlib 会相应地将 x 轴刻度调整为 1 年。
```python
sixties = climate_change["1960-01-01":"1969-12-31"]
fig, ax = plt.subplots()
ax.plot(sixties.index, sixties['co2'])
# ... 设置标签和显示 ...
```
- **查看一年**：缩小范围到具体的某一年，Matplotlib 会自动将 x 轴标签细化到月份。

---
### 使用不同变量绘制时间序列

#### 将两个时间序列一起绘制
- 当两条时间序列在时间上对齐但记录不同的变量时（如二氧化碳浓度和相对气温），可能需要将它们画在同一张图上。
- **直接绘制的问题**：如果直接画在同一个 Axes 上，由于两个变量的量纲（单位）不在一个数量级，会导致一条线变化明显，另一条线看起来几乎是一条水平直线。

#### 使用双轴（Twin Axes）
- 为了让量纲不同的数据在一张图上清晰展示，可以使用双 y 轴。
- 使用 `ax.twinx()` 方法创建第二个 Axes 对象（孪生轴）。它与第一个 Axes 共享 x 轴，但拥有独立的 y 轴（显示在右侧）。
```python
fig, ax = plt.subplots()

# 绘制第一个变量（左轴）
ax.plot(climate_change.index, climate_change["co2"])
ax.set_xlabel('Time')
ax.set_ylabel('CO2 (ppm)')

# 创建孪生轴并绘制第二个变量（右轴）
ax2 = ax.twinx()
ax2.plot(climate_change.index, climate_change["relative_temp"])
ax2.set_ylabel('Relative temperature (Celsius)')

plt.show()
```

#### 用颜色区分变量
- 使用双轴后，需要利用颜色来辅助区分两条线。
- 可以在 `plot()` 方法和设置坐标轴标签 `set_ylabel()` 时传入 `color` 参数，使线条和文字颜色保持一致。
```python
ax.plot(..., color='blue')
ax.set_ylabel('CO2 (ppm)', color='blue')

ax2.plot(..., color='red')
ax2.set_ylabel('Relative temperature (Celsius)', color='red')
```

#### 为刻度着色
- 除了标签，还可以更改坐标轴的刻度线和刻度标签的颜色，进一步强化颜色编码。
- 使用 `tick_params()` 方法，第一个参数传入 `'y'` 或 `'x'` 指定轴，用 `colors` 参数设置颜色。
```python
ax.tick_params('y', colors='blue')
ax2.tick_params('y', colors='red')
```
- 同时给坐标轴标签和刻度着色，可以清楚地对应每个变量使用的是哪一侧的刻度。

#### 将绘图逻辑封装为函数
- 为了减少代码重复并提高可读性，可以将这套绘图模式封装成一个自定义函数：
```python
def plot_timeseries(axes, x, y, color, xlabel, ylabel):
    axes.plot(x, y, color=color)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel, color=color)
    axes.tick_params('y', colors=color)
```
- 之后在绘图时直接调用该函数，传入相应的参数即可。

---
### 标注时间序列数据

#### 标注的作用
- 改进可视化的一个重要方法是添加标注。标注通常是针对图中某个部分的一小段文字，用于聚焦注意力并解释特定的数据特征。
- 当数据量很大时（如跨越 50 年的气候数据），突出显示某个关键点能让图表传达的信息更清晰。

#### 使用 `annotate()` 方法
- 使用 Axes 对象的 `annotate()` 方法可以添加带有箭头的标注文字。
- 至少需要提供两个核心参数：
  - 标注文本（如 `">1 degree"`）。
  - 要标注的位置坐标（`xy` 参数）。通常是一个元组，例如 `(pd.Timestamp('2015-10-06'), 1)`。
```python
ax2.annotate(">1 degree", xy=(pd.Timestamp("2015-10-06"), 1))
```

#### 定位文本（`xytext`）
- 默认情况下，文本可能会直接盖在数据点或坐标轴上。可以使用可选参数 `xytext` 来指定文字本身的位置（使用相同的元组坐标格式）。
```python
ax2.annotate(">1 degree", 
             xy=(pd.Timestamp('2015-10-06'), 1),
             xytext=(pd.Timestamp('2008-10-06'), -0.2))
```

#### 为标注添加箭头（`arrowprops`）
- 移动文字后，为了让读者明白文字对应的是哪个数据点，需要添加连接文本和数据点的箭头。
- 使用 `arrowprops` 关键字参数，它接收一个字典，用于定义箭头样式。传入空字典 `{}` 即可使用默认样式。
```python
ax2.annotate(">1 degree", 
             xy=(pd.Timestamp('2015-10-06'), 1),
             xytext=(pd.Timestamp('2008-10-06'), -0.2),
             arrowprops={})
```

#### 自定义箭头样式
- 可以在 `arrowprops` 字典中自定义箭头的各项属性，例如箭头样式（`arrowstyle`）和颜色（`color`）。
- 例如，将样式设置为带箭头的细线 `"->"`，并将颜色设置为灰色 `"gray"`，可以让视觉效果更加克制。
```python
arrowprops={"arrowstyle": "->", "color": "gray"}
```
- Matplotlib 提供了丰富的选项来定制标注和箭头属性，可查阅官方文档了解详情。
---





# 定量比较与统计可视化

### 定量比较：条形图

#### 为什么使用条形图
- 条形图适合用于数据各部分之间的定量比较。
- 以 2016 年奥运会部分国家的奖牌数量为例：直接在数据表中查看数字，难以直观比较国家之间的差异；而可视化后，柱子高度的差异能让对比一目了然。

#### 绘制基础条形图
- 读取数据并将国家名称设为索引。
- 使用 Axes 对象的 `.bar()` 方法绘制条形图：x 轴为 DataFrame 的索引（国家名称），y 轴为 "Gold" 列的数据（金牌数量）。
```python
medals = pd.read_csv('medals_by_country_2016.csv', index_col=0)
fig, ax = plt.subplots()
ax.bar(medals.index, medals["Gold"])
plt.show()
```

#### 旋转刻度标签
- 国家名称较长，直接显示会导致 x 轴标签相互重叠。
- 使用 `ax.set_xticklabels()` 方法将标签旋转 90 度，使其纵向排列，避免重叠。
- 同时设置 y 轴标签说明图表含义。
```python
ax.set_xticklabels(medals.index, rotation=90)
ax.set_ylabel("Number of medals")
```

#### 堆叠条形图
- 若要在同一张图中展示多种数据（如金、银、铜牌），可以使用堆叠条形图，将新数据叠加在原有数据的上方。
- 通过 `.bar()` 方法的 `bottom` 参数，指定新柱子的起始高度。
  - **银牌**：底部设为金牌的数量。
  - **铜牌**：底部设为金牌与银牌数量的总和。
```python
# 金牌（底部默认是 0）
ax.bar(medals.index, medals["Gold"])

# 银牌（堆叠在金牌上方）
ax.bar(medals.index, medals["Silver"], bottom=medals["Gold"])

# 铜牌（堆叠在金牌+银牌上方）
ax.bar(medals.index, medals["Bronze"], 
       bottom=medals["Gold"] + medals["Silver"])
```

#### 添加图例
- 图例能帮助读者理解每种颜色代表的数据类别。需要两步：
  1. 在每次调用 `.bar()` 时，通过 `label` 参数传入标签名称。
  2. 在展示前调用 `ax.legend()` 生成图例。
```python
ax.bar(medals.index, medals["Gold"], label="Gold")
ax.bar(medals.index, medals["Silver"], bottom=medals["Gold"], label="Silver")
ax.bar(medals.index, medals["Bronze"], 
       bottom=medals["Gold"] + medals["Silver"], label="Bronze")

ax.legend()
plt.show()
```
---
### 定量比较：直方图

#### 直方图的作用
- 条形图通常用于比较不同分类下的单一数值（如平均值），而**直方图**能够展示数值变量内部的**完整取值分布**。

#### 基础直方图绘制
- 使用 Axes 对象的 `.hist()` 方法，传入需要分析的数据列。
- x 轴表示变量的取值范围（自动划分为若干个区间），y 轴表示落在该区间内的观测数量（频数）。
```python
fig, ax = plt.subplots()
ax.hist(mens_rowing["Height"])
ax.hist(mens_gymnastics["Height"])
ax.set_xlabel("Height (cm)")
ax.set_ylabel("# of observations")
plt.show()
```

#### 添加图例标签
- 当同一张图里展示多个变量的分布时，必须添加图例以区分不同颜色代表的数据。
- 在调用 `hist()` 时通过 `label` 参数指定名称，然后在最后调用 `ax.legend()` 显示图例。
```python
ax.hist(mens_rowing["Height"], label="Rowing")
ax.hist(mens_gymnastics["Height"], label="Gymnastics")
ax.legend()
```

#### 自定义分箱（Bins）
- Matplotlib 默认将数据分成 10 个箱（柱子）。可以通过 `bins` 参数自定义：
  - **设置箱数**：传入一个整数，指定分箱的数量。
    ```python
    ax.hist(..., bins=5)
    ```
  - **设置箱边界**：传入一个数值列表（序列），明确指定每个箱子的边界值。
    ```python
    ax.hist(..., bins=[150, 160, 170, 180, 190, 200, 210])
    ```

#### 解决遮挡问题：设置透明度/样式
- 在叠加直方图时，后画的实心柱子可能会遮挡住前面的柱子（例如体操的柱子挡住了赛艇 <180cm 的部分）。
- 可以通过 `histtype` 参数更改绘图类型，将其设置为 `"step"`，直方图将以轮廓线（细线）显示，而不是实心柱子，从而看清所有的分布情况。
```python
ax.hist(mens_rowing["Height"], label="Rowing", 
        bins=[150, 160, 170, 180, 190, 200, 210], histtype="step")
ax.hist(mens_gymnastics["Height"], label="Gymnastics", 
        bins=[150, 160, 170, 180, 190, 200, 210], histtype="step")
```

### 统计绘图（重点）

#### 什么是统计绘图
- 上一节学习了用直方图比较数据的完整分布。**统计绘图**是一组用可视化来进行更规范比较的方法。
- 本节介绍两种常用技术：**误差线**和**箱线图**。

#### 误差线
- 误差线是一种添加在图表上的额外标记，用于概括数据分布的离散程度（如标准差）。它将分布信息浓缩为一个数值。
- **在柱状图中添加**：使用 `ax.bar()` 的 `yerr` 参数。
  - `y` 通常设置为中心值（如均值）。
  - `yerr` 设置为误差量（如标准差）。
```python
ax.bar("Rowing", mens_rowing["Height"].mean(), 
       yerr=mens_rowing["Height"].std())
```
- **在折线图中添加**：使用 `ax.errorbar()` 方法。
  - 类似 `plot` 方法，传入 x 和 y 的值，然后通过 `yerr` 传入包含误差值的列。
```python
ax.errorbar(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"], 
            yerr=seattle_weather["MLY-TAVG-STDDEV"])
```

#### 箱线图
- 箱线图由 John Tukey 提出，能直观展示分布的多个关键统计量。
- **绘制方法**：使用 `ax.boxplot()` 方法，传入包含多个数据序列的列表。
```python
fig, ax = plt.subplots()
ax.boxplot([mens_rowing["Height"], mens_gymnastics["Height"]])
ax.set_xticklabels(["Rowing", "Gymnastics"])
ax.set_ylabel("Height (cm)")
plt.show()
```
- **解读箱线图**：
  - **红线（中位线）**：表示中位数。
  - **箱体**：表示四分位距（IQR），即从第 25 百分位到第 75 百分位的范围。
  - **须（Whiskers）**：从箱体边缘向外延伸 1.5 倍 IQR 的范围。
  - **离群值（Outliers）**：超出须范围的点，表示数值异常大或异常小。例如图表中显示少数特别矮的赛艇运动员和特别高的体操运动员。

---

### 定量比较：散点图

#### 散点图的用途
- 条形图用于展示同一个变量在不同类别下的取值。如果我们要比较**两个不同变量**在各个观测（数据点）上的对应关系，这种**双变量比较**最适合使用散点图。

#### 基础散点图
- 使用 Axes 对象的 `scatter()` 方法。
- 第一个参数对应 x 轴数值，第二个参数对应 y 轴数值。每个数据点由一对 (x, y) 值确定。
```python
fig, ax = plt.subplots()
ax.scatter(climate_change["co2"], climate_change["relative_temp"])
ax.set_xlabel("CO2 (ppm)")
ax.set_ylabel("Relative temperature (Celsius)")
plt.show()
```

#### 通过颜色/标签区分不同分组
- 可以在同一张图上叠加多个散点图，通过设置不同的 `color` 和 `label` 来比较不同条件下的数据。
- 示例：对比 1980 年代和 1990 年代的数据分布。
```python
# 提取不同年代的数据子集
eighties = climate_change["1980-01-01":"1989-12-31"]
nineties = climate_change["1990-01-01":"1999-12-31"]

fig, ax = plt.subplots()

# 绘制 1980 年代数据（红色）
ax.scatter(eighties["co2"], eighties["relative_temp"], 
           color="red", label="eighties")

# 绘制 1990 年代数据（蓝色）
ax.scatter(nineties["co2"], nineties["relative_temp"], 
           color="blue", label="nineties")

ax.legend()
```

#### 用颜色编码第三个变量
- 当数据中包含连续的时间变量时，可以使用 `scatter()` 方法的 `c` 参数（注意是单字母，区别于 `color`），将数值映射到点颜色上。
- 这里直接将 DataFrame 的时间索引 (`climate_change.index`) 传给 `c`，可以实现根据时间先后改变点的颜色。
```python
fig, ax = plt.subplots()
# 使用 c 参数，用时间索引作为颜色编码
ax.scatter(climate_change["co2"], climate_change["relative_temp"],
           c=climate_change.index)
ax.set_xlabel("CO2 (ppm)")
ax.set_ylabel("Relative temperature (Celsius)")
plt.show()
```
- 此时，图上的颜色（如从深蓝到亮黄）不仅区分了不同的点，还直观展示了时间的推移，为数据比较提供了更丰富的信息。

---



# 与他人共享可视化

### 准备与他人分享的图表

#### 更改整体图表样式
- 之前学习的是自定义图表中的单个元素（如线条颜色、标记形状）。本节介绍如何通过设置样式来一次性改变图表的整体外观。
- **应用样式**：使用 `plt.style.use("样式名称")`。此操作会同时改变颜色、字体、背景、网格线等多个元素，并且在当前会话中对后续所有图表生效。
```python
import matplotlib.pyplot as plt

# 应用类似于 R 语言 ggplot2 的样式
plt.style.use("ggplot")

fig, ax = plt.subplots()
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"])
plt.show()
```

#### 回到默认值
- 如果要恢复到 Matplotlib 的初始外观，可以将样式设置为 `"default"`。
```python
plt.style.use("default")
```

#### 可用的内置样式
- Matplotlib 内置了多种样式（如 `"bmh"` 等），可以访问官方文档查看样式参考指南。此外，一些样式是以基于 Matplotlib 的统计可视化库 Seaborn 命名的，如 `"seaborn-colorblind"`。

#### 选择绘图样式的指南
在选择图表样式时，应重点考虑**受众的观看体验**和使用场景：
- **避免深色背景**：深色背景通常可读性较差，除非有充分理由，否则应尽量避免使用。
- **考虑色觉缺陷（色盲友好）**：如果图表中颜色的区分至关重要，建议使用对色盲友好的样式，如 `"seaborn-colorblind"` 或 `"tableau-colorblind10"`。这能确保约 5% 存在色觉缺陷的读者也能清晰分辨数据。
- **考虑打印需求（省墨）**：如果图表需要被打印在纸质报告上，应避免使用大面积彩色背景（如 `"ggplot"` 的灰色背景），以减少墨水消耗。
- **适应黑白打印**：如果图表可能会被黑白打印机打印，应使用 `"grayscale"` 样式，以确保在失去色彩后，数据之间依然保持清晰的视觉差异。
---

### 与他人分享你的可视化

#### 将图形保存到文件
- 在完成可视化后，如果需要分享，可以将代码末尾的 `plt.show()` 替换为 Figure 对象的 `savefig()` 方法。
- 传入一个带有扩展名的文件名，图形就会被保存在文件系统中。
```python
fig.savefig("gold_medals.png")
```

#### 不同的文件格式
可以根据具体用途选择合适的文件格式：
- **PNG**：无损压缩，图像质量高，但文件相对较大。
- **JPG**：有损压缩，文件体积小，适合用于网页。可以通过 `quality` 参数（1-100）控制压缩率，建议不要超过 95。
```python
fig.savefig("gold_medals.jpg", quality=50)
```
- **SVG**：矢量图形格式。放大不失真，且可以使用 Adobe Illustrator 或 Gimp 等专业软件进行后续编辑。
```python
fig.savefig("gold_medals.svg")
```

#### 分辨率（DPI）
- 使用 `dpi` 关键字参数控制图像的分辨率（每英寸点数）。
- 数值越高，图像越清晰，但文件体积也会随之增大。例如，对于高质量打印，通常设置为 300。
```python
fig.savefig("gold_medals.png", dpi=300)
```

#### 尺寸与纵横比
- 使用 Figure 对象的 `set_size_inches()` 方法控制图形尺寸。
- 传入一个包含宽度和高度的列表或元组（单位为英寸）。这不仅改变了大小，也决定了图形的纵横比（如又宽又矮或又长又窄）。
```python
# 设置宽度为 5 英寸，高度为 3 英寸
fig.set_size_inches([5, 3])
```


---

### 从数据自动生成图表

#### 为何自动化
- 使用编程语言（如 Python）和可视化库（如 Matplotlib）的一大优势是：只要代码写得当，就能根据传入的数据灵活适配，自动调整行为。
- **自动化的优点**：
  - **高效快捷**：比每次都通过图形界面手动操作要快得多。
  - **灵活**：程序能根据读入的数据动态改变行为。
  - **稳健**：代码能适应不同规模或类别的数据。
  - **可复现**：能够随数据自动调整的程序，在多次运行中也能保持一致的输出表现。

#### 获取数据中的唯一值
- 在处理未知数据集时，我们可能不知道某个分类列（如 "Sport"）里具体包含多少种不同的值。
- 可以对 pandas Series 调用 `.unique()` 方法，获取该列包含的所有不重复的值。
```python
# 获取数据中所有不同的运动项目
sports = summer_2016_medals["Sport"].unique()
```

#### 在循环中自动绘图
- 利用 `for` 循环遍历这些唯一值，并在每次迭代中动态生成图表元素。
- **步骤**：
  1. 遍历唯一值列表。
  2. 利用布尔索引筛选出当前类别的数据子集。
  3. 计算子集数据的均值（如身高）和标准差，添加到柱状图中。
```python
fig, ax = plt.subplots()

# 遍历每一个运动项目
for sport in sports:
    # 筛选出当前项目的数据
    sport_df = summer_2016_medals[summer_2016_medals["Sport"] == sport]
    
    # 绘制柱状图及误差线
    ax.bar(sport, sport_df["Height"].mean(), 
           yerr=sport_df["Height"].std())

# 统一设置坐标轴标签，并旋转 x 轴标签防止重叠
ax.set_ylabel("Height (cm)")
ax.set_xticklabels(sports, rotation=90)
plt.show()
```
- **核心优势**：在这整个过程中，我们不需要事先知道数据集中到底有多少个运动项目。代码会根据输入数据自动调整图表中柱子的数量和 x 轴的标签。
---

这是一份非常棒的课程总结！视频为你梳理了 Matplotlib 入门之后，可以继续探索的高级用法和周边生态库。

作为你的 AI 助手，我为你整理并归纳了这段视频的核心要点，方便你以后在实际工作中查阅：

### 🚀 Matplotlib 进阶与扩展指南

#### 1. 快速上手法：Matplotlib 示例画廊 (Gallery)
*   **核心技巧**：不要从零开始写复杂图表。直接访问 Matplotlib 官网的 Gallery，找到类似的图后，**直接复制源码并修改数据**。这是最高效的作图方式。

#### 2. 突破二维：三维绘图 (3D Plotting)
*   **应用场景**：当你的数据有 X、Y、Z 三个维度时（例如一条穿越三维空间的参数曲线），可以在平面上加入透视效果，增加数据的表达力。

#### 3. 图像可视化：伪彩色 (Pseudocolor)
*   **应用场景**：用于展示图像矩阵数据（如图像处理、热力图）。它可以将二维数组中的每个数值映射为一种颜色，非常适合观察数值的分布规律。

#### 4. 动态呈现：动画 (Animations)
*   **实现方式**：将时间作为额外维度，生成多帧独立的可视化画面。虽然可以用外部工具合成视频，但 Matplotlib 也提供了专门的动画接口（如 `FuncAnimation`），可以在代码中直接生成动画。

#### 5. 地理空间扩展：Cartopy
*   **应用场景**：专门用于地理空间数据（绘制地图）。它能扩展 Matplotlib 的能力，让你在地图上绘制气象、人口等空间分布数据。（**这与你之前学的 GeoPandas 是很好的搭档**）。

#### 6. 统计可视化神器：Seaborn
*   **应用场景**：基于 Pandas DataFrame 构建的高级统计绘图库。
*   **核心优势**：**代码极简，颜值极高**。
*   **强大功能**：可以轻松实现多维数据的映射，比如用一个散点图同时展示：X轴（马力）、Y轴（燃油效率）、颜色（产地）、气泡大小（汽车重量）。
*   **推荐**：Seaborn 同样拥有丰富的官方 Gallery，值得一看。

---

**💡 下一步学习建议：**
如果你接下来的工作涉及大量**数据分析报告**，强烈建议优先学习 **Seaborn**；如果涉及**地图或气象数据**，则建议结合你之前学过的地理空间数据处理，看看 **Cartopy** 或者 **GeoPandas 内置的绘图功能**。如果只是想快速出好看的图，随时去官网 Gallery 参考示例代码！