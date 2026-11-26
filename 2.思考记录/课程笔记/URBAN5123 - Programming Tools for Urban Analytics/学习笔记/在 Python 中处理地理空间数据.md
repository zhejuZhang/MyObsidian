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
# 空间关系

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

---

### 使用 GeoPandas 处理空间关系

#### 逐元素空间关系方法
- 前面我们学习了如何检查两个单个几何对象（Shapely 对象）之间的空间关系，例如判断布鲁塞尔是否在法国境内：
```python
brussels.within(france)
# 输出: False

paris.within(france)
# 输出: True
```
- 当需要对数据集中的所有观测同时检查相同的关系时，逐一手动判断效率低下。
- `GeoDataFrame` 提供了类似的方法，并会自动应用到其包含的所有几何对象上。
- 示例：检查 `cities` 数据框中哪些城市位于法国（`france` 多边形）内部：
```python
cities.within(france)
```
- 该操作的结果是一个 pandas 的布尔 Series（掩码），为每个点指示是否位于法国多边形内。这本质上等同于对 `cities` 中的每个几何对象逐一调用 `within()` 方法。

#### 按空间关系筛选
- 由于返回的是布尔序列，可以直接将其作为“掩码”，像过滤普通 DataFrame 一样过滤原始的 `GeoDataFrame`，从而基于空间条件选择行。
- 示例：筛选出位于法国境内的城市：
```python
cities[cities.within(france)]
```
- 在此例中，结果会返回三个城市的数据（Monaco, Andorra, Paris）。需要注意的是，示例使用的是简化的数据集，因此安道尔和摩纳哥这两个小型独立国家的地理点也落在了法国的简化多边形内。

#### 综合示例：亚马逊河流经哪些国家
- 使用河流数据集：
```python
rivers = geopandas.read_file("ne_50m_rivers_lake_centerlines.shp")
```
- 提取亚马逊河的线状几何对象（使用 `squeeze()` 获取标量几何值）：
```python
amazon = rivers[rivers['name'] == 'Amazonas'].geometry.squeeze()
```
- 使用 `intersects` 运算创建一个掩码，检查哪些国家与这条河相交或被其穿过：
```python
mask = countries.intersects(amazon)
```
- 将掩码应用于过滤国家的 `GeoDataFrame`，即可得到结果：
```python
countries[mask]
```
- 查询结果表明，亚马逊河流经秘鲁（Peru）、哥伦比亚（Colombia）和巴西（Brazil）。

#### 核心模式与扩展
- **常用空间关系**：`within`（在内部）、`contains`（包含）、`intersects`（相交）是最常用的空间关系。除此之外，Shapely 和 GeoPandas 还提供了更多方法，可查阅 Shapely 官方文档。
- **核心模式**：几乎每个可用于单个 Shapely 几何对象的方法，在 `GeoDataFrame` 中都有对应的方法。GeoDataFrame 会基于其中存储的每个几何对象逐个自动应用这些方法（向量化操作）。
---

### "空间连接"操作

#### 空间关系 I：数据集合并的需求
- 结合国家（countries）和城市（cities）数据集的可视化可以观察到：大多数城市位于某个国家的范围内，而大多数国家也包含一个或多个城市。
- 这种本质上的空间关系，使得我们可以利用一个数据集的信息来补充另一个数据集。

#### 空间关系 II：从空间筛选到空间连接
- 复习：可以使用 `within` 方法配合布尔筛选，提取特定国家（如巴西）内的城市。
```python
brazil = countries.loc[22, 'geometry']
cities[cities.within(brazil)]
```
- 新需求：如果想知道**每座城市**分别位于哪个国家，用表格的说法就是要在城市的 DataFrame 中新增一列国家名称。
- 因为国家名称在国家数据集中，我们需要把两个数据集的信息合并（连接）。当连接依据是地理位置而不是共享列时，这种操作叫作**空间连接（Spatial Join）**。

#### 空间连接（Spatial Join）概念
- 空间连接 = 基于空间关系将一个图层的属性转移到另一个图层。
- 示例说明：
  - 有一个包含 3 个多边形的数据集（A、B、C）和一个包含 4 个点的数据集（1、2、3、4）。
  - 空间连接会根据每个点落在哪个多边形里，把多边形（GeoDataFrame）中的属性链接到点（GeoDataFrame）上。
  - 例如：多边形 A 的属性会连接到点 1；多边形 B 的属性会连接到点 2 和点 4；点 3 不在任何多边形内，则获取 NaN。
- 这是一个**左连接（Left Join）**的例子，会保留左侧数据集（点）的行与顺序。

#### 使用 GeoPandas 进行空间连接
- 空间连接由 `geopandas.sjoin()` 函数提供。
- 示例代码：
```python
joined = geopandas.sjoin(cities,
                         countries[['name', 'geometry']],
                         op="within")
joined.head()
```
- **参数说明**：
  - 第一个参数：想要添加信息的 GeoDataFrame（左表，这里是 `cities`）。
  - 第二个参数：包含要添加信息的 GeoDataFrame（右表，这里是 `countries`，可传入特定列）。
  - `op` 参数：指定用于匹配两个数据集的空间关系（如 `within`）。
- **注意事项**：参数顺序非常重要。必须先传入城市（左表），再传入国家（右表），因为 `within` 这种空间关系只在这个顺序下有意义（即检查城市是否 within 国家）。
- **结果说明**：在连接后的 GeoDataFrame 中，每座城市的原有属性旁会新增对应的国家信息（如国家名称）。结果会**保留左侧输入 GeoDataFrame（城市）的几何对象与行序**。

---
### 分级着色图：空间数据制图

#### 基本概念
- 分级着色图是在地图上展示非空间属性数据的可视化方式。
- 通过一套配色方案来编码属性的取值，每种颜色代表一个或少量取值。
- 在 GeoPandas 中使用 `plot()` 方法，当指定一个数值型列来为多边形着色时，默认会得到一条连续的色带。
- 由于人眼很难在连续色带中分辨细微色差，通常会通过分级将其划分为离散的组，制作成更易读的图。

#### 关键设置与参数
制作分级着色图，需要配合 `plot()` 方法关注三个核心选择：
```python
# 基础示例：指定列，带分类方案、类别数和颜色映射
locations.plot(column='variable', scheme='quantiles', k=7, cmap='viridis')
```
- `column`：指定用于着色的属性列。
- `k`：类别数。
- `scheme`：分类算法。
- `cmap`：颜色映射。

### 类别数（"k"）

#### 权衡与经验法则
- 将大量取值压缩到少量颜色中，必然会有信息损失（这是可以接受的），但会让地图更容易解读。
- 组数太少，地图几乎讲不出有价值的信息。
- 组数太多，又会超过人能有效处理的信息量。
- 经验法则：通常选择在 **3 到 12 个类别** 之间比较合适。

### 分类算法（"scheme"）

如何把连续型变量中的每个值分到 `k` 个组之一，常用的方法有两种。

#### 等距分级（equal_interval）
- 将数据的取值范围切分成等宽的区间，并为每个区间分配不同的颜色。
- 缺点：如果变量在取值范围内分布不均匀，会导致大量观测被分到同一种颜色里。
```python
locations.plot(column='variable', scheme='equal_interval', k=7, cmap='Purples')
```

#### 分位数分级（quantiles）
- 对所有取值排序，把相同比例的观测分到每个颜色箱（例如 7 组，每组包含全部观测的 1/7）。
- 优点：能平衡每种颜色包含的观测数量。
- 缺点：可能会把差异很大的取值放进同一种颜色（如最高一组）。
```python
locations.plot(column='variable', scheme='quantiles', k=7, cmap='Purples')
```

### 颜色映射（"cmap"）

配色方案的选择应与制图目的和数据特性保持一致。

#### 类别型（无顺序）
- 适用场景：分类数据，不暗示梯度或强弱顺序。
- 参数设置：需设置 `categorical=True`。
```python
locations.plot(column='variable', categorical=True, cmap='Purples')
```

#### 顺序型（分级）
- 适用场景：连续数据，且最小值是自然的起点。
- 示例：使用 `RdPu` 等渐变色。
```python
locations.plot(column='variable', k=5, cmap='RdPu')
```

#### 发散型（分级）
- 适用场景：连续数据，且自然起点位于中间。
- 特点：由两组方向相反的顺序型配色组成。
- 示例：使用 `RdYlGn`（红-黄-绿）。
```python
locations.plot(column='variable', k=5, cmap='RdYlGn')
```

---






# 投影与几何变换


### 坐标参考系统 (CRS) 简介

#### 概念定义
- 几何数据通常带有特定的坐标，但坐标本身并不能直接说明位置。
- **坐标参考系统（CRS）**：将坐标与地球上的实际位置关联起来的参考系统。

#### 地理坐标
- 最常见的坐标类型，利用纬度和经度的角度值，相对于赤道和本初子午线来定位。
- **示例**：`48°51'N, 2°17'E`（度分秒表示）。
- 广泛应用于 GPS 和网络地图等。
- **Python 中的使用注意**：
  - 顺序为 `(lon, lat)`，即（经度，纬度），而非（纬度，经度）。
  - 经度范围：`[-180, 180]`。
  - 纬度范围：`[-90, 90]`。

#### 地图投影
- 地球是球体，但在实际工作中通常将其表示在二维平面（地图、屏幕）上。
- 将球面变成平面地图的过程叫**投影**。

#### 投影坐标
- 将地球表面投影到二维平面后，用笛卡尔的 `x, y` 坐标来表示位置。
- 通常使用米等长度单位，便于分析。
- **注意**：三维地球在二维地图上的表示必然存在失真。存在不同的投影方法以尽量减小误差，各有优缺点：
  - **阿尔伯斯等面积投影**：尽量保持几何对象的面积。
  - **墨卡托投影**：尽量保持角度，但面积失真会很大。
  - **Web Mercator 投影**：展示面积失真情况（有些国家显得比实际大得多）。

#### 指定 CRS 的方式
- CRS 由一组参数定义，可通过不同方式描述：
  - **proj4 字符串**：例如 `+proj=longlat +datum=WGS84 +no_defs`。
  - **字典表示**：例如 `{'proj': 'longlat', 'datum': 'WGS84', 'no_defs': True}`。
  - **EPSG 代码**：在 EPSG 体系中每个 CRS 有唯一编号。最常用的是 `EPSG:4326`，即 **WGS84 地理坐标系**。
- 如果坐标是以经纬度表示，很可能就是 WGS84。

#### GeoPandas 中的 CRS
- CRS 信息存储在 `GeoDataFrame` 或 `GeoSeries` 的 `.crs` 属性中。
```python
import geopandas
gdf = geopandas.read_file("countries.shp")
print(gdf.crs)
# 输出示例: {'init': 'epsg:4326'}
```

### 小结

#### 核心对比
- **地理坐标**：用经、纬度（角度）表示。
- **投影坐标**：用 x, y（如米）表示。

#### 关键操作
- GeoPandas 使用 `.crs` 属性存储坐标参考系统信息。

#### 常用标准
- 最常用的地理坐标系是 **WGS84** 或 **EPSG:4326**。

---
### 在 GeoPandas 中处理坐标系

#### GeoPandas 中的 CRS 信息
- GeoPandas 将 CRS 信息存储在 `GeoDataFrame` 和 `GeoSeries` 的 `.crs` 属性中。
- 用于把坐标定位到地球表面的全部信息，会以 proj4 字符串或字典的形式保存。
- 如果文件自带 CRS 信息，读取时会自动加载。
```python
import geopandas
gdf = geopandas.read_file("countries.shp")
print(gdf.crs)
```

#### 手动设置 CRS
- 如果文件没有相关信息，但已知数据所使用的 CRS，可以手动补充。
```python
# 方式 1：使用 EPSG 代码字典
gdf.crs = {'init': 'epsg:4326'}

# 方式 2：使用 proj4 字典表示
gdf.crs = {'proj': 'longlat', 'datum': 'WGS84', 'no_defs': True}
```

#### 转换到另一种 CRS
- 一旦设置好 CRS，可以使用 `to_crs()` 方法将一个 `GeoDataFrame` 转换到另一套坐标系统。
- 目标 CRS 同样可以用 proj4 字符串、字典或直接指定 EPSG 编号来表示。
```python
# 读取一个使用 Web Mercator 投影的文件
gdf = geopandas.read_file("countries_web_mercator.shp")

# 转换为 WGS84 坐标系统
gdf2 = gdf.to_crs({'proj': 'longlat', 'datum': 'WGS84', 'no_defs': True})
# 或者直接使用 EPSG 编号
# gdf2 = gdf.to_crs(epsg=4326)
```

### 为何要转换 CRS？

#### 统一数据源的 CRS
- 处理多个数据集时，它们可能各自使用不同的坐标系统。
- 合并数据前必须确保采用相同的 CRS。可以将它们统一转换到一个通用 CRS，或把其中一个转换为另一个的 CRS。
```python
df2 = df2.to_crs(df1.crs)
```

#### 制图避免失真
- 直接用经纬度绘图会导致形状与距离失真（因为在地球各处，一度纬度与一度经度代表的实际距离不同）。
- 可视化数据时，选用合适的投影 CRS 可以得到更准确的图形。

#### 确保距离与面积计算准确
- 当分析需要进行基于距离或面积的计算时，数据必须采用合适的投影坐标系统。
- `geopandas` 和 `shapely` 的几何计算假定数据位于二维笛卡尔平面，只有正确投影时，计算结果才会准确（单位如米、英尺才有意义）。

### 如何选择使用哪种 CRS？

#### 选择提示
- 很难为整个地球找到一个各方面完美的投影，失真总是存在的。
- 使用与数据区域匹配的投影。
- 多数国家有自己标准的 CRS，小区域更容易控制失真。

#### 实用网站
- [Spatial Reference](https://spatialreference.org/)
- [EPSG.io](https://epsg.io/)

### 小结

#### 核心要点
- 转换 CRS：使用 `to_crs()` 方法。
- 确保不同数据集的 CRS 一致。
- 计算距离、面积等时使用投影坐标系。
---
### 空间操作：创建新几何体

#### 基本概念
- 上一章学习了如何识别并使用几何对象之间的空间关系。
- 本节介绍如何基于这些关系**创建新的几何对象**。
- 假设有两个部分重叠的几何对象 A 和 B，可以通过不同的空间关系生成新的几何体。

#### 基础空间操作方法
对于单独的两个 Shapely 几何对象（a 和 b），常用的创建新几何体的操作有三种：

##### 相交（Intersection）
- 获取 A 与 B 的重叠部分。
- Python 代码示例：
```python
# 返回 A 与 B 重叠部分的新多边形
result = a.intersection(b)
```

##### 并集（Union）
- 将两者的重叠区域和非重叠区域合并成一个几何对象。
- Python 代码示例：
```python
# 返回包含 A 和 B 所有区域的新多边形
result = a.union(b)
```

##### 差集（Difference）
- 生成只属于 A、且不与 B 重叠的那一部分。
- Python 代码示例：
```python
# 返回 A 减去 B 之后剩余的几何体
result = a.difference(b)
```

#### GeoPandas 中的空间操作
- 上述针对单个几何对象的操作，同样可以扩展到 `GeoDataFrame`。
- 可以将数据框中的**每一个几何体**与另一个单独的几何体（如一个矩形区域）分别计算交集、并集或差集。
- 示例场景：一个包含非洲国家多边形的 `GeoDataFrame`（`africa`），以及一个表示赤道附近区域的矩形多边形（`box`）。
```python
# 对 africa 中的每个国家多边形计算与 box 的交集
africa.intersection(box)
```

#### 注意事项
- **返回类型**：操作返回的是一个与原始数据框长度相同的 `GeoSeries`。每个国家一行，包含计算后的新几何体。
- **空几何**：如果数据框中的某个几何体（如某个国家）与目标几何体（如矩形）没有重叠，对应的结果将是一个**空几何（Empty Geometry）**。
- 从示例输出中可以看到，没有交集的元素返回的是 `()`。

---

### 叠加空间数据集

#### 基于单多边形的相交操作及其局限
- 在之前的练习中，已经学会了如何用一个多边形（如一个圆）与一组国家求交集。
- 使用 `intersection` 方法完成：
```python
countries.intersection(circle)
```
- **局限性**：
  - 只能直接与单个多边形进行相交操作。若要与多个多边形相交，需要手动重复，失去简单性。
  - 不保留相交多边形的属性信息。

#### 叠加两个数据集
- 针对稍复杂的场景，GeoPandas 提供了 `overlay`（覆盖/叠加）操作。
- **场景示例**：
  - 左侧数据集：3个国家的多边形。
  - 右侧数据集：同一区域的一些地质分区多边形。
- 直接叠加绘制两层，可以看到多边形发生了相交。
- 通过对这两层做 overlay 操作，可以生成第三层，包含两层相交的结果（即每个国家与每个地质分区的所有交集）。最终只保留在两层中都出现的区域。
- **操作名称**：交集覆盖。
- **代码实现**：
```python
geopandas.overlay(countries, geologic_regions, how='intersection')
```

### 叠加与相交的对比

#### 相交方法（Intersection）
- **代码**：`countries.intersection(geologic_region_A)`
- **输入**：仅传入单个多边形（如地质分区 A）。
- **输出**：返回3个国家分别与该多边形的交集（第一行结果可能为空多边形 `()`）。
- **属性**：**不保留**输入多边形的属性信息，仅返回几何对象（`GeoSeries`）。

#### 叠加方法（Overlay）
- **代码**：`geopandas.overlay(countries, geologic_regions, how='intersection')`
- **输入**：传入包含所有分区的完整 `GeoDataFrame` 与相关数据集求交。
- **输出**：包含所有国家与所有地质分区之间**非空**的交集组合。如果某个国家跨越多个地质分区，它会被拆分并产生多行记录。
- **属性**：**会保留**国家和地质分区这两侧的属性信息（如 `name` 和 `geologic_region`），这在后续分析中非常有用。
---




```md
# 探索土地利用数据集

在接下来的练习中，我们先引入一个新数据集：关于巴黎土地利用的数据集（基于欧洲开放的 [Urban Atlas](https://land.copernicus.eu/local/urban-atlas) 的简化版本）。土地利用表示某片区域用于何种活动，例如居住或休闲。该数据集由多边形组成，并包含表示巴黎不同区域土地利用类别的标签。

本练习将读取数据、进行可视化探索，并计算巴黎地区不同土地利用类别的总面积。

GeoPandas 和 matplotlib 已经导入。

## 说明

100 XP

- 读取 `'paris_land_use.shp'` 文件，并将结果赋给变量 `land_use`。
- 绘制 `land_use` 的图形，使用 `'class'` 列为多边形着色，并添加图例。注意：由于多边形很多，生成图可能需要几秒钟。
- 新增一列 `'area'`，表示每个多边形的面积。
- 使用 `groupby()` 方法按 `'class'` 计算总面积（单位 km²），并打印结果。
```

```python
# Import the land use dataset

land_use = geopandas.read_file('paris_land_use.shp')

print(land_use.head())

  

# Make a plot of the land use with 'class' as the color

land_use.plot(column='class', legend=True, figsize=(15, 10))

plt.show()

  

# Add the area as a new column

land_use['area'] = land_use.area

  

# Calculate the total area for each land use class

total_area = land_use.groupby('class')['area'].sum() / 1000**2

print(total_area)
```

---

```python
# 移除坐标轴边框和标签。
ax.set_axis_off()
import matplotlib.pyplot as plt
# 创建一个子图
ax = plt.subplot()
# 关闭x轴和y轴的刻度
ax.set_xticks([])
ax.set_yticks([])
```













# 综合实战——手工采矿点案例研究

### 数据集简介与地理空间文件格式

#### 数据集背景介绍
- 本章是课程的最后一章，主题是用 Python 处理地理空间数据。
- 更换一套全新的数据集：刚果东部的手工采矿点。
- 数据来源：IPIS（国际和平信息服务机构）。这是一个开放数据集。
- 数据内容：刚果东部矿产开采活跃，IPIS 收集了矿点位置、开采矿种以及社会与安全状况等数据。
- 项目目标：更好地理解这些矿点在本地区冲突中的作用。
- 练习重点：将把范围限定在与矿点位置和国家公园相关的空间分析。

#### 地理空间文件格式（读取）
- 使用 `geopandas.read_file()` 函数可以读取多种格式的文件：
```python
geopandas.read_file("path/to/file.geojson")
```
- **常见支持的格式**：
  - **ESRI Shapefile**：目前最常用的矢量数据格式。需要注意的是，它由多个文件组成（如 `.shp`, `.dbf`, `.shx`, `.prj` 等），在复制或移动时务必把所有相关文件一起处理。
  - **GeoJSON**：基于 JSON 的轻量格式，常用于网页应用。
  - **GeoPackage (`.gpkg`)**：相对较新的开放标准格式，功能更强，常作为 shapefile 的现代化替代方案。
- 除文件外，GeoPandas 也支持从空间数据库读取数据（如 PostGIS）。

#### 地理空间文件格式（写入）
- GeoPandas 底层依赖 GDAL 库，因此既可以用 `read_file` 读取，也可以用 `to_file()` 方法将 GeoDataFrame 写入为这些格式。
- 写入时，第一个参数是输出文件名或完整路径，同时必须通过 `driver` 参数指定文件格式。
- 示例代码：
```python
# 写入 Shapefile 文件
geodataframe.to_file("mydata.shp", driver='ESRI Shapefile')

# 写入 GeoJSON 文件
geodataframe.to_file("mydata.geojson", driver='GeoJSON')

# 写入 GeoPackage 文件
geodataframe.to_file("mydata.gpkg", driver='GPKG')
```


---
### 其他空间操作

#### 空间操作概览
- **空间关系（返回布尔结果）**：
  - 用于检查几何对象之间的关系，例如 `intersects`（相交）、`within`（在内部）、`contains`（包含）等。
  - 既可作用于单个 Shapely 几何对象，也可在 `GeoDataFrame` 或 `GeoSeries` 上按元素逐个应用。
- **几何操作（创建新几何）**：
  - 通过求两个几何对象的 `intersection`（交集）、`union`（并集）或 `difference`（差集）来生成新几何。
- **高级空间组合函数**：
  - `geopandas.sjoin`（空间连接）：根据给定的空间关系连接不同数据集的属性信息。
  - `geopandas.overlay`（叠加）：通过计算两个数据集中所有几何的交集、并集或差集来组合两个 `GeoDataFrame`。

#### 一元并集（unary union）
- **用途**：将一整列几何体（即一个 `GeoSeries`）统一合并为单个几何体。
- **示例**：对非洲所有国家的多边形求并集，得到覆盖整个非洲大陆轮廓的单一几何体。
- **代码实现**：使用 `.unary_union` 属性。
```python
# 返回覆盖所有参与运算的几何体的单一几何
merged_geometry = gdf.geometry.unary_union
```

#### 缓冲区操作
- **概念**：在给定几何对象周围生成一定距离范围内的多边形区域。
- **不同几何类型的缓冲区效果**：
  - **点**：生成一个圆形多边形，包含点本身及指定距离内的区域。
  - **线**：生成一个围绕线的带状多边形。
  - **多边形**：生成一个包含原多边形且向外扩展指定距离的更大新多边形。
- **注意事项**：缓冲区结果是**包含原对象**和扩展区域的新多边形。
- **向量化操作**：在 `GeoSeries` 上调用 `buffer()` 方法，会对该列中的每个几何对象逐个生成缓冲区。
- **代码实现**：
```python
point.buffer(distance)
line.buffer(distance)
polygon.buffer(distance)
```
- **应用场景**：常用于基于邻近性（proximity）的空间分析。

---
### 应用自定义空间操作

#### 背景与需求
- Shapely 和 GeoPandas 提供了许多现成的空间功能，但有时我们需要更专业的查询或操作。可以将这些现成函数当作积木，组合成**自定义的空间操作**。
- **分析目标示例**：计算每座城市周边 50 公里范围内的河流总长度。

#### 基础操作（以单个城市开罗为例）
通过组合之前学过的空间方法和属性即可完成：
1. 在点周围创建缓冲区（50公里即 50,000 米）。
2. 将缓冲区与河流图层求相交。
3. 获取相交线段的长度并求和（转换为千米）。
```python
area = cairo.buffer(50000)
rivers_within_area = rivers.intersection(area)
print(rivers_within_area.length.sum() / 1000)
# 输出: 186.3972196423455
```

#### `apply()` 方法
- 如果要将上述分析应用到 `GeoDataFrame` 中的每个点，可以使用 pandas 的 `apply` 方法。
- **作用**：对 Series 或 GeoSeries 的每个值调用函数，并返回一个新的 Series。
- **语法**：`Series.apply(function, **kwargs)`
  - `function`：要应用的函数。对于 `GeoSeries`，该函数会将每个几何对象（`geom`）作为第一个参数传入。
  - `**kwargs`：传递给函数的其他关键字参数。

#### 封装自定义函数
将单城市的分析逻辑封装成一个独立的函数，接受几何对象和河流数据框作为参数：
```python
def river_length(geom, rivers):
    area = geom.buffer(50000)
    rivers_within_area = rivers.intersection(area)
    return rivers_within_area.length.sum() / 1000
```
- 对单个几何体调用（结果与之前一致）：
```python
river_length(cairo, rivers=rivers)
```

#### 批量应用与结果赋值
- 对 `cities` 数据集的几何列使用 `apply` 方法，并传入河流 dataframe 作为额外参数：
```python
cities.geometry.apply(river_length, rivers=rivers)
```
- 这会返回一个包含每座城市对应计算结果的 `Series`。
- 将结果作为新列添加到原始数据框中，并查看结果：
```python
cities['river_length'] = cities.geometry.apply(river_length, rivers=rivers)
cities.head()
```


```python
# Define a function that returns the closest national park

def closest_national_park(geom, national_parks):

dist = national_parks.distance(geom)

idx = dist.idxmin()

closest_park = national_parks.loc[idx,'Name']

return closest_park

  

# Call the function on single_mine

print(closest_national_park(single_mine, national_parks))

  

# Apply the function to all mining sites

mining_sites['closest_park'] = mining_sites.geometry.apply(closest_national_park, national_parks=national_parks)

print(mining_sites.head())
```

---

### 栅格数据处理

#### 栅格数据简介
- 地理空间数据主要包括矢量数据和栅格数据。在实际工作中，常常需要将两者结合使用。
- **栅格数据**把世界表示成网格，网格中的每个像素都有一个连续或离散的数值。
- 连续数据示例：降雨概率图。
- 离散数据示例：土地覆被类型图。

#### 多波段栅格数据
- 栅格数据可以只有单个波段（每个像素只有一个数值）。
- 也可以有多个波段，卫星影像通常包含多个波段。

#### rasterio 包
- 用途：处理栅格数据的 Python 包。
- 它是 GDAL 库的“Pythonic”绑定。
- 功能：
  - 读取与写入多种栅格文件格式。
  - 处理工具：掩膜、重投影、重采样等。
- 文档链接：[https://rasterio.readthedocs.io/en/latest/](https://rasterio.readthedocs.io/en/latest/)

#### 打开栅格文件与元数据
- 使用 `rasterio.open()` 打开文件。与矢量数据不同，此操作只读取元数据，不会将数据读入内存。
- 可以查看文件信息，如波段数、宽和高。
```python
import rasterio

src = rasterio.open("DEM_world.tif")

# 查看波段数
print(src.count)  # 输出: 1

# 查看宽和高（像素）
print(src.width, src.height)  # 输出: (4320, 2160)
```

#### 读取栅格数据
- 使用已打开栅格对象的 `read()` 方法，会将栅格数据读入内存，并存储为标准的 `numpy` 数组。
- 一旦转换为 `numpy` 数组，即可使用熟悉的 Python 科学计算工具进行处理。
```python
array = src.read()
```

#### 绘制栅格数据集
- 借助 `rasterio.plot` 可以方便地绘制栅格数据。
```python
import rasterio.plot

rasterio.plot.show(src, cmap='terrain')
```

### 结合矢量数据提取栅格信息

#### rasterstats 包
- 用于基于给定的矢量数据（如点、多边形）从栅格中提取信息并计算汇总统计量。
- 项目地址：[https://github.com/perrygeo/python-rasterstats](https://github.com/perrygeo/python-rasterstats)

#### 点要素提取 (point_query)
- 提取点位置的像素值。
- 可指定插值方法（如 `'nearest'` 或 `'bilinear'`）。
```python
rasterstats.point_query(geometries, "path/to/raster", 
                        interpolation='nearest' | 'bilinear')
```

#### 多边形要素提取 (zonal_stats)
- 提取多边形范围内的像素值，并可指定需要计算的统计量（如最小值、平均值、最大值）。
```python
rasterstats.zonal_stats(geometries, "path/to/raster", 
                        stats=['min', 'mean', 'max'])
```

#### 综合应用示例
- 目标：计算每个国家的平均海拔。
- 步骤：将国家的几何对象与高程栅格文件路径传入 `zonal_stats`，指定计算均值，并将结果添加为 DataFrame 的新列。
```python
result = rasterstats.zonal_stats(countries.geometry, "DEM_gworld.tif", 
                                 stats=['mean'])

countries['mean_elevation'] = pd.DataFrame(result)

# 找出平均海拔最高的国家
countries.sort_values('mean_elevation', ascending=False).head()
```