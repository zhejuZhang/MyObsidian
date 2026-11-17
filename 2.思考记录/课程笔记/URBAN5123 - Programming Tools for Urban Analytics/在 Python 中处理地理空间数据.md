# 地理空间矢量数据入门
## 地理空间数据
### 课程信息
- 课程主题：地理空间数据
- 课程目标：学习如何在 Python 数据科学工作流程中集成地理空间数据
- 讲师：Joris Van den Bossche
- 联合讲师：Dani Arribas-Bel

### 什么是地理空间数据
- 地理空间数据是指每条记录都关联了特定位置的数据。
- 它本质上仍然是数据，因此许多操作与非空间数据的操作非常相似。
- 地理空间数据中的每个观测都有位置，可以放到地图上。
- 这使得我们可以考察数据之间的空间关系。
- 地理空间数据的真正优势：既能利用数据本身，又能利用其位置信息，从而支持更深入的分析。

### 空间数据的来源与形式
- 空间数据形式多样。
- 传统示例：政府人口普查数据，例如美国人口密度图。
- 新兴来源：越来越多新的空间数据来源可用，例如使用智能手机记录的骑行轨迹。

### 记录真实世界的两种数据模型
#### 栅格模型
- 将世界表示为由网格构成的连续表面，类似图片像素。
- 常见例子包括海拔数据和卫星影像。

#### 矢量模型
- 用点、线和多边形表示由离散对象组成的世界。
- 常见例子包括建筑物、道路、国家等。

### 栅格数据与矢量数据
- 同一地区可以用两种数据模型表示。
- 热成像卫星图显示建筑物的热量流失，属于栅格数据示例。
- 同一区域的矢量数据可视化中，建筑物用多边形表示，道路用线表示。
- 本课程将聚焦于矢量数据。

### 矢量要素的几何类型
#### 点
- 表示一个位置。
- 由 X 和 Y 坐标构成。

#### 线
- 由一组相连的点组成。
- 在代码中通常称为 linestring。

#### 多边形
- 由一条闭合的线围成一个区域。
- 一个要素也可以由多个几何体构成，例如 MultiPolygon。

### 矢量数据示例
- 将世界各国表示为多边形。
- 将特大城市的位置作为点要素加上去。
- 将世界上一些最大的河流作为线添加进去。

### 矢量属性数据
- 矢量要素通常还包含附加信息，即要素属性。
- 以国家多边形为例，属性可以包括国家名称、首都、人口数量等信息。
- 当把一类要素的集合放在一起，例如全世界的所有国家，并结合其属性，就得到了一张表。
- 本课程会使用这种类型的数据。

### 进入实践
- 练习假设已具备使用 pandas 处理表格数据的基础知识。
- 练习假设已具备使用 matplotlib 进行可视化的基础知识。
- 课程将先用这两个包做一组入门练习。

### 核心概念总结
- 地理空间数据：每条记录关联特定位置的数据。
- 空间关系：通过位置信息分析数据之间的关系。
- 栅格模型：连续表面，用网格或像素表示。
- 矢量模型：离散对象，用点、线、多边形表示。
- 矢量几何类型：点、线或 linestring、多边形，以及 MultiPolygon 等多几何类型。
- 要素属性：附加在矢量要素上的表格信息。
- 课程重点：矢量数据及其在 Python 数据科学工作流程中的集成。



```python
# Read the restaurants csv file

restaurants = pd.read_csv("paris_restaurants.csv")

  

# Import contextily

import contextily

  

# A figure of all restaurants with background

fig, ax = plt.subplots()

ax.plot(restaurants.x, restaurants.y, 'o',markersize=1)

contextily.add_basemap(ax)

plt.show()
```

---
## GeoPandas 入门

### GeoPandas 简介

#### 课程引入
- 本节开始介绍与空间数据相关的 Python 库。

#### 空间专用数据格式
- 传统的 CSV 文件或只有 x、y 坐标列的 DataFrame 很难直观表达线和多边形数据（因为每个对象由多个点构成）。
- 因此，需要使用专门的地理空间数据文件格式，如 GeoJSON、GeoPackage 和 shapefile。
- 这些格式不仅能存储传统的表格数据，也能专业地存放空间数据。
- 要在 Python 中读取这些文件并处理地理空间数据，需使用 GeoPandas 库。

#### 用 GeoPandas 导入空间数据
- GeoPandas 是用于处理表格型地理空间矢量数据的库，它扩展了 pandas 的 DataFrame。
- 使用 `geopandas.read_file()` 函数并传入文件路径，可读取大多数常见的空间矢量格式。
- 示例代码：
```python
import geopandas

countries = geopandas.read_file("countries.geojson")
countries.head()
```
- 使用 `head()` 方法查看前 5 行，会发现有一列是几何信息（如代表各国的多边形），其他列则是描述这些国家的属性。

#### 用 GeoPandas 快速可视化空间数据
- 使用 `plot()` 方法可以对数据集中的几何对象进行基础的可视化。
- 示例代码：
```python
countries.plot()
```

### GeoDataFrame 与 GeoSeries

#### GeoDataFrame 概念
- `read_file` 函数返回的是一个 `GeoDataFrame` 对象。
- 可以将其理解为具备地理空间能力的 pandas DataFrame。
- 它用于表示地理空间要素及其属性，总是包含一列名为 `"geometry"` 的列来存放几何信息（即要素本身），其他列则是描述每个几何对象的属性。

#### "geometry" 属性与 GeoSeries
- `GeoDataFrame` 拥有一个特殊的 `"geometry"` 属性。无论几何列真实的列名是什么，该属性都会返回几何列。
- 对 `countries` 数据集使用该属性，会得到一个由多边形组成的 Series，即 `GeoSeries`。
- 就像 `GeoDataFrame` 是 pandas DataFrame 的地理空间版本，`GeoSeries` 也类似于 pandas 的 Series，但带有额外的空间方法。

#### 具备空间感知的数据框
- 地理空间功能的一个典型例子是 `GeoSeries` 的 `"area"` 属性，它会返回一个包含每个几何对象面积的 Series。

### 小结

#### GeoDataFrame 的特点
- 类似 pandas 的 DataFrame：
  - 普通 pandas DataFrame 的功能皆可用（如用 `head()` 查看前几行）。
- 加入空间功能：
  - `plot()` 方法：绘制几何对象。
  - `geometry` 属性：返回 `GeoSeries` 对象。
  - 空间专用的属性与方法：如 `area` 属性。

---
## 探索与可视化空间数据及其属性

#### 利用 pandas 功能处理空间数据
- `geopandas` 中的 `GeoDataFrame` 是带有空间能力的 pandas DataFrame。
- 因此，pandas DataFrame 的各种常规用法在这里同样适用。
- 用户可以轻松处理几何对象的属性信息，从而进行操作、探索和分析。

#### 筛选数据
- 可以按某个属性对数据框进行筛选，获取子集。
- 以国家数据集为例，它包含了全球所有国家的多边形数据。
- 可以执行比较运算（如 `countries['continent'] == 'Africa'`），生成一个由 True 和 False 组成的布尔 Series（即掩码）。
- 利用这个布尔掩码过滤原始的 `GeoDataFrame`，即可提取出特定大洲的国家：
```python
countries_africa = countries[countries['continent'] == 'Africa']
countries_africa.plot()
```
- 除了基本的筛选，还可以使用 `groupby` 和连接 DataFrames 等 pandas 高级功能。

### 可视化空间数据进阶

#### 基础绘图与统一颜色
- 使用 `plot()` 方法可以快速绘制几何对象。
- 使用 `color` 关键字可以为所有几何对象指定统一的颜色：
```python
countries.plot(color="red")
```

#### 基于属性值的颜色调整
- 可根据几何对象的某个属性值为每个多边形着色。
- 将属性的列名传递给 `plot` 方法的 `column` 关键字：
```python
countries.plot(column='gdp_per_cap', figsize=(12, 6))
```
- 代码中还可以通过 `figsize` 指定图像的尺寸（以英寸为单位的宽度和高度）。

#### 多图层绘图
- 经常需要在同一张图里叠加多层几何对象。
- 使用 `plot` 方法的 `ax` 关键字，将现有绘图对象传入。
- `ax` 接收一个 matplotlib 的 `axes` 对象，可通过 matplotlib 的 `subplots` 函数创建：
```python
fig, ax = plt.subplots(figsize=(12, 6))
countries.plot(ax=ax)
cities.plot(ax=ax, color='red', markersize=10)
ax.set_axis_off()
```
- 示例中，在同一个子图上分别绘制了国家和城市位置，并调用 `set_axis_off` 方法去掉了图周围的刻度和标签边框。

#### 结合 matplotlib 微调
- `GeoDataFrame` 生成的图本质上是 matplotlib 图，与普通 pandas dataframe 的绘图一致。
- 因此可以利用 matplotlib 接口继续微调，如设置 x 和 y 的范围、添加标签、修改图像大小等。
---
## 探索与可视化空间数据及其属性

#### 利用 pandas 功能处理空间数据
- `geopandas` 中的 `GeoDataFrame` 是带有空间能力的 pandas DataFrame。
- 因此，pandas DataFrame 的各种常规用法在这里同样适用。
- 用户可以轻松处理几何对象的属性信息，从而进行操作、探索和分析。

#### 筛选数据
- 可以按某个属性对数据框进行筛选，获取子集。
- 以国家数据集为例，它包含了全球所有国家的多边形数据。
- 可以执行比较运算（如 `countries['continent'] == 'Africa'`），生成一个由 True 和 False 组成的布尔 Series（即掩码）。
- 利用这个布尔掩码过滤原始的 `GeoDataFrame`，即可提取出特定大洲的国家：
```python
countries_africa = countries[countries['continent'] == 'Africa']
countries_africa.plot()
```
- 除了基本的筛选，还可以使用 `groupby` 和连接 DataFrames 等 pandas 高级功能。

### 可视化空间数据进阶

#### 基础绘图与统一颜色
- 使用 `plot()` 方法可以快速绘制几何对象。
- 使用 `color` 关键字可以为所有几何对象指定统一的颜色：
```python
countries.plot(color="red")
```

#### 基于属性值的颜色调整
- 可根据几何对象的某个属性值为每个多边形着色。
- 将属性的列名传递给 `plot` 方法的 `column` 关键字：
```python
countries.plot(column='gdp_per_cap', figsize=(12, 6))
```
- 代码中还可以通过 `figsize` 指定图像的尺寸（以英寸为单位的宽度和高度）。

#### 多图层绘图
- 经常需要在同一张图里叠加多层几何对象。
- 使用 `plot` 方法的 `ax` 关键字，将现有绘图对象传入。
- `ax` 接收一个 matplotlib 的 `axes` 对象，可通过 matplotlib 的 `subplots` 函数创建：
```python
fig, ax = plt.subplots(figsize=(12, 6))
countries.plot(ax=ax)
cities.plot(ax=ax, color='red', markersize=10)
ax.set_axis_off()
```
- 示例中，在同一个子图上分别绘制了国家和城市位置，并调用 `set_axis_off` 方法去掉了图周围的刻度和标签边框。

#### 结合 matplotlib 微调
- `GeoDataFrame` 生成的图本质上是 matplotlib 图，与普通 pandas dataframe 的绘图一致。
- 因此可以利用 matplotlib 接口继续微调，如设置 x 和 y 的范围、添加标签、修改图像大小等。


```python
# Load the restaurants dataset

restaurants = geopandas.read_file("paris_restaurants.geosjon")

  

# Take a subset of the African restaurants

african_restaurants = restaurants[restaurants['type'] == 'African restaurant']

  

# Make a multi-layered plot

fig, ax = plt.subplots(figsize=(10, 10))

restaurants.plot(ax=ax,color="grey")

african_restaurants.plot(ax=ax,color='red')

# Remove the box, ticks and labels

ax.set_axis_off()

plt.show()
```

---

### Shapely 几何与空间关系

#### 标量几何值
- 在 `GeoDataFrame` 中，`geometry` 列保存的是矢量要素（如点、线、多边形）。
- 使用 `loc` 属性可以根据行标签和列名提取单个几何值。
- 示例代码：提取行标签为 170（布鲁塞尔）的几何值并查看类型：
```python
brussels = cities.loc[170, 'geometry']
print(brussels)
# 输出: POINT (4.33137074969045 50.83526293533032)

type(brussels)
# 输出: shapely.geometry.point.Point
```
- 提取出的单个值是一个 `shapely` 的 `Point` 对象。

#### Shapely 包
- Shapely 是用于几何对象操作与分析的 Python 包。
- 它提供了 `Point`、`LineString` 和 `Polygon` 等几何对象，GeoPandas 在底层正是基于 Shapely 工作。
- `GeoDataFrame` 中的 `geometry` 列（`GeoSeries`）实际上是由 Shapely 对象组成的。

#### 几何对象
- 可以像访问 pandas DataFrame 里的任意单个值一样，访问 `GeoDataFrame` 中的几何对象。
- 示例代码，提取多个几何对象以备后续使用：
```python
brussels = cities.loc[170, 'geometry']
paris = cities.loc[235, 'geometry']
belgium = countries.loc[countries['name'] == 'Belgium', 'geometry'].squeeze()
france = countries.loc[countries['name'] == 'France', 'geometry'].squeeze()
uk = countries.loc[countries['name'] == 'United Kingdom', 'geometry'].squeeze()
```
- 几何对象也可以手动创建，例如创建一个坐标为 `1` 和 `2` 的 `Point`：
```python
from shapely.geometry import Point
p = Point(1, 2)
print(p)
# 输出: POINT (1 2)
```

#### 空间方法
- Shapely 的几何对象内置了空间功能。
- **面积属性**：`Polygon` 具有 `area` 属性：
```python
belgium.area
# 输出: 3.8299974609075753
```
- **距离方法**：`distance` 方法用于计算两个几何之间的距离（如直线距离）：
```python
brussels.distance(paris)
# 输出: 2.8049127723186214
```
- 此外，Shapely 还提供了许多其他开箱即用的空间方法。

#### 空间关系
- Shapely 可以用来描述不同几何之间的空间关系。
- 将多个几何对象放入一个 `GeoSeries` 中可以同时可视化它们：
```python
geopandas.GeoSeries([belgium, france, uk, paris, brussels, line]).plot()
```
- **常见空间关系概念**：
  - 布鲁塞尔位于比利时多边形的“内部”。
  - 比利时“包含”布鲁塞尔这个点。
  - 比利时边界与法国边界“相接”，即它们是邻国。
  - 连接巴黎和布鲁塞尔的线“相交”了法国和比利时，但未相交英国。
- **代码实现**：
  - 使用 `contains` 方法检查包含关系：
```python
belgium.contains(brussels)
# 输出: True

france.contains(brussels)
# 输出: False
```
  - 其他空间关系可通过 `within`（在内部）、`touches`（相接）、`intersects`（相交）等方法表达：
```python
brussels.within(belgium)   # 输出: True
belgium.touches(france)    # 输出: True
line.intersects(france)    # 输出: True
line.intersects(uk)        # 输出: False
```


# 空间关系







# 投影与几何变换







# 综合实战——手工采矿点案例研究