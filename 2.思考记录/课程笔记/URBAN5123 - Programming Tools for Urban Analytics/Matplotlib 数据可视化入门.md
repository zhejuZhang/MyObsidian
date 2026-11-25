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




# 定量比较与统计可视化


# 与他人共享可视化