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


# 定量比较与统计可视化


# 与他人共享可视化