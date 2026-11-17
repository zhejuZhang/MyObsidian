# 构建双图层地图：多边形与散点图的结合
## 介绍
###  位置
介绍位置概念,引出斯诺点图(经典霍乱病毒分布地图)

- 如何用地理点绘制散点图
- 如何用 geopanda 绘制集合对象
- 如何从 DataFrame 构建 GeoDataFrame
- 如何进行空间连接
- 如何为图添加街道底图
- 何时以及如何创建分级填色

### 经度与纬度

```python
plt.scatter(schools.Longitude,
			schools.Latitude,
			c = 'darkgreen',
			marker = 'p')
			
# 添加标签 标题 格网。
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Nashville Pulic Schools')
plt.grid()
plt.show()
```

#### 通常需要从数据中提取经纬度

1. 用list的分别提取经纬度
	如(36.12345，-86.123435)
```python
bus_stops['lat'] = [loc[0] for loc in bus_stops.Location]
bus_stops['lng'] = [loc[1] for loc in bus_stops.Location]
bus_stops.head()
```
2. 用正则表达式提取经纬度
	如 “MCC -BAY 11\nNashville, TN\n(36.12345，-86.123435)”
	
```python
lat_lng_pattern = re.compile(r'\((.*),\s*(.*)\))', flags=re.MULTILINE)
def extract_lat_lng(address):
	try:
		lat_lng_match = lat_lng_pattern.seacrch(address)
		lat = float(lat_lng_match.group(1))
		lng = float(lat_lng_match.group(2))
		return (lat, lng)
	except:
		return (np.NaN, np.NaN)
```

```python
lat_lngs = [extract_lat_lng(location) for location in \ 
			bus_stops2.loc[:, 'Location']]
bus_stops2['lat'] = [lat for lat, lng in lat_lngs]
bus_stops2['lng'] = [lat for lat, lng in lat_lngs]
```

## 几何和 Shapefile
shapefile 存储一种称为“几何”的特殊数据
点
线
面

### Shapefile组件

Shapefile文件的后缀和扩展名具有特定的含义，它们帮助用户识别文件的内容和用途。以下是一些主要的Shapefile后缀及其含义：

- **.shp**: 主要文件，存储地理数据的坐标信息。
- **.shx**: 索引文件，存储地理数据的位置索引，记录每个地理数据在shp文件中的位置。
- **.dbf**: 数据表文件，存储地理数据的属性信息。
- **.shp.xml**: 以xml格式保存元数据。
- **.prj**: 存储地理坐标系统和投影信息。
- **.cpg**: 指定.dbf文件的字符编码。
- **.sbn、.sbx**: 空间索引文件。
- **.ixs**: 地理编码索引。
- **.mxs**: 地理编码索引（ODB格式）。
- **.atx**: .dbf文件的属性索引。


### 读取 geopandas

一下代码将 Shapefile 读入 GeoDataFrame，并查看前几行
```python
import geopandas as gpd

geo_df = gpd.read_file('My_Map_Files/my_map.shp')
geo_df.head()
```

### 查看几何
```python
service_district.loc[0,'geometry']
```

### 绘制 GeoDataFrame
```python
school_districts.plot()
plt.show()
```

```python
school_districts.plot(column = 'district', legend = true)
plt.show()
```

## 综合运用
#### 技能清单
- 了解经纬度
- 提取经纬度
- 用经纬度绘制散点图
- 优化散点图外观与解读
- 从Shapefile绘制多边形

### 组合散点图与多边形
```python
school_districts.plot(column = 'district', legend = True, cmap = 'Set2')
plt.scatter(schools.lng, schools.lat, marker = 'p', c= 'darkgreen')
plt.title("Nashville Schools and School Districts')
plt.show()
```

# 创建并连接GeoDataFrame
## 使用 GeoJSON制图
```python
# Set legend style

lgnd_kwds = {'title': 'School Districts',

'loc': 'upper left', 'bbox_to_anchor': (1, 1.03), 'ncol': 1}

  

# Plot the school districts using Set3 colormap without the column argument

school_districts.plot(cmap = 'Set3', legend = True, legend_kwds = lgnd_kwds)

plt.xlabel('Longitude')

plt.ylabel('Latitude')

plt.title('Nashville School Districts')

plt.show();
```

### 投影和参考坐标系
#### 更改参考坐标系
```python
# Print the first row of school districts GeoDataFrame and the crs

print(school_districts.head(1))

print(school_districts.crs)

  

# Convert the crs to epsg:3857

school_districts.geometry = school_districts.geometry.to_crs(epsg = 3857)

# Print the first row of school districts GeoDataFrame and the crs again

print(school_districts.head(1))

print(school_districts.crs)
```

#### 从 DataFrame 构建 GeoDataFrame
```python
import pandas as pd

import geopandas as gpd

import matplotlib.pyplot as plt

  

# Print the first few rows of the art DataFrame

print(art.head())

  

# Create a geometry column in art

art['geometry'] = gpd.points_from_xy(art.lng, art.lat)

  

# Create a GeoDataFrame from art and verify the type

art_geo = gpd.GeoDataFrame(art,

crs = neighborhoods.crs,

geometry = art.geometry)

print(type(art_geo))
```

## 空间连接
#### 相交 intersects
```python
# Spatially join art_geo and neighborhoods

art_intersect_neighborhoods = gpd.sjoin(art_geo, neighborhoods, predicate = 'intersects')

  

# Print the shape property of art_intersect_neighborhoods

print(art_intersect_neighborhoods.shape)
```

#### 位于其内 within
```python
# Create art_within_neighborhoods by spatially joining art_geo and neighborhoods

art_within_neighborhoods = gpd.sjoin(art_geo, neighborhoods, predicate = 'within')

  

# Print the shape property of art_within_neighborhoods

print(art_within_neighborhoods.shape)
```

#### 包含 contains
```python
# Spatially join art_geo and neighborhoods and using the contains predicate

art_containing_neighborhoods = gpd.sjoin(art_geo, neighborhoods, predicate = 'contains')

  

# Print the shape property of art_containing_neighborhoods

print(art_containing_neighborhoods.shape)
```

#### 在多边形内聚合点

现在您已经将 `art` 与 `neighborhoods` 进行了空间连接，接下来可以对数据进行分组、聚合和排序，找出哪个街区拥有最多的公共艺术。您可以统计艺术品的标题数量，以查看每个街区中有多少件艺术品。
```python
# Get name and title from neighborhood_art and group by name

neighborhood_art_grouped = neighborhood_art[['name', 'title']].groupby('name')

  

# Aggregate the grouped data and count the artworks within each polygon

print(neighborhood_art_grouped.agg('count').sort_values(by = 'title', ascending = False))
```

```python
# Create urban_art from neighborhood_art where the neighborhood name is Urban Residents

urban_art = neighborhood_art.loc[neighborhood_art.name == 'Urban Residents']

  

# Get just the Urban Residents neighborhood polygon and save it as urban_polygon

urban_polygon = neighborhoods.loc[neighborhoods.name == "Urban Residents"]

  

# Plot the urban_polygon as ax

ax = urban_polygon.plot(color = 'lightgreen')

  

# Add a plot of the urban_art and show it

urban_art.plot( ax = ax, column = 'type', legend = True);

plt.show()
```

# GeoSeries 与 Folium
## GeoSeries 的属性和方法 一

**Shapely 的属性和方法**

```python
# the geometry column is a GeoSeries
type(school_districts.geometry)
```

```text
geopandas.geoseries.GeoSeries
```

*   `GeoSeries.area` - 返回 GeoSeries 中每个几何体的面积
*   `GeoSeries.centroid` - 返回 GeoSeries 中每个几何体的中心点
*   `GeoSeries.distance(other)` - 返回到 `other` 的最小距离


**学区面积**

GEOSERIES.AREA

```python
# 打印前 4 行及总行数
print(school_districts.head(4))
print('There are ', school_districts.shape[0], ' school districts.' )
```

```python
# calculate area of each school district
district_area = school_districts.area
# print the areas and crs used
print(district_area.sort_values(ascending = False))
print(school_districts.crs)
```


```python
# create a copy of school_districts that uses EPSG:3857
school_districts_3857 = school_districts.to_crs(epsg = 3857)
# define a variable for m^2 to km^2 and get area in kilometers squared
sqm_to_sqkm = 10**6
district_area_km = school_districts_3857.area / sqkm_to_sqm
print(district_area_km.sort_values(ascending = False))
print(school_districts_3857.crs)
```

## GeoSeries 的属性和方法 二


**GeoSeries.centroid**

*   返回 GeoSeries 中每个几何体的中心点

```python
# 第一个多边形的质心
print(districts.geometry.centroid[0])
```
**学区质心**

`GEOSERIES.CENTROID`

```python
# 打印学区的前 5 行
print(school_districts.head())
```

**学区质心**

```python
# 从质心创建 'center' 列
school_districts['center'] = school_districts.geometry.centroid
# 用学区及其中心创建 GeoDataFrame
part = ['district', 'center']
school_district_centers = school_districts[part]
school_district_centers.head(3)
```

**GeoSeries.distance()**

*   `GeoSeries.distance(other)`：返回到 `other` 的最小距离

```python
# red_pt 到质心的距离
cen = districts.geometry.centroid[0]
print(red_pt.distance(other = cen))
```

**两点间距**

GEOSERIES.DISTANCE(OTHER)

```python
district_one = school_districts.loc[school_districts.district == '1']
district_one.head()
```

**两点间距**

```python
schools.head(3)
name                 lat      lng
AZ Kelley Elem      36.021  -86.658
Alex Green Elem     36.252  -86.832
Amqui Elem          36.27   -86.703
```

```python
# create geometry in schools
schools['geometry']=gpd.points_from_xy(schools.lng, schools.lat)

#construct schools GeoDataFrame
school_geo=gpd.GeoDataFrame(schools,crs = district_one.crs,
                            geometry = schools.geometry)
```

**两点间距**

```python
# spatial join schools within dist 1
schools_in_dist1 = gpd.sjoin(schools_geo, district_one, predicate = 'within')
schools_in_dist1.shape
```

```python
# import pprint to format dictionary output
import pprint

distances = {}
for row in schools_in_dist1.iterrows():
    vals = row[1]
    key = vals['name']
    ctr = vals['center']
    distances[key] = vals['geometry'].distance(ctr)
pprint.pprint(distances)
```

## 使用 Folium
在 PYTHON 中可视化地理空间数据
**使用 Folium**
在 PYTHON 中可视化地理空间数据

**Folium**
*   Python 包
*   交互式地图
*   基于 Leaflet.js 构建

**folium.Map()**

```python
import folium
# 构建以埃菲尔铁塔为中心的地图
eiffel_tower = folium.Map(location = [48.8583736, 2.2922926])

# 显示地图
display(eiffel_tower)
```

**从质心获取 Folium 位置**

```python
district_one.head()
```

```python
center_point = district_one.center[0]
type(center_point)
```

**从质心获取 Folium 位置**

```python
# 为 folium 位置数组反转顺序
district_center = [center_point.y, center_point.x]

# 打印 center_point 和 district_center
print(center_point)
print(district_center)
```

**在 folium 地图中添加多边形**

```python
# 创建以第1选区为中心的 folium 地图
district1_map = folium.Map(location = district_center)

# 添加第1选区的边界
folium.GeoJson(district_one.geometry).add_to(district1_map)

# 显示地图
display(district1_map)
```



```python
# Construct a folium map with urban_location

downtown_map = folium.Map(urban_location = urban_location, zoom_start = 15)

  

# Display the map

display(downtown_map)
```

```python
# Create array for called folium_loc from the urban_polygon center point

point = urban_polygon.center[0]

folium_loc = [point.y, point.x]

  

# Construct a map from folium_loc: downtown_map

downtown_map = folium.Map(location = folium_loc, zoom_start = 15)

  

# Draw our neighborhood: Urban Residents

folium.GeoJson(urban_polygon.geometry).add_to(downtown_map)

  

# Display the map

display(downtown_map)
```



## 在 folium 中创建标记和弹出框
在 PYTHON 中可视化地理空间数据

```python
for row in schools_in_dist1.iterrows():
    row_values = row[1]
    print(row_values)
```

**构建标记位置**

```python
# 为学区 1 构建 folium 地图
district1_map = folium.Map(location = district_center, zoom_start = 11)

# 为每所学校创建一个标记
for row in schools_in_dist1.iterrows():
    row_values = row[1]
    location = [row_values['lat'], row_values['lng']]
    marker = folium.Marker(location = location)
    marker.add_to(district1_map)

display(district1_map)
```

**从 DataFrame 创建弹出框**

```python
# 为学区 1 构建 folium 地图
district1_map = folium.Map(location = district_center, zoom_start = 11)

# 为每所学校创建一个标记
for row in schools_in_dist1.iterrows():
    row_values = row[1]
    location = [row_values['lat'], row_values['lng']]
    popup = popup = '<strong>' + row_values['name'] + '</strong>'
    marker = folium.Marker(location = location, popup = popup)
    marker.add_to(district1_map)

display(district1_map)
```



**排查数据问题**

将使用 `urban_art` DataFrame 中的 `title` 和 `desc` 列为市中心公共艺术创建弹出信息（popup）。在这里，您需要先检查这两列，识别并清理存在问题的取值。

- 打印并检查 `urban_art` DataFrame 中 `title` 列的取值。
- 打印并检查 `urban_art` DataFrame 中 `desc` 列的取值。
- 使用 `fillna()` 将 `desc` 列中的 `NaN` 替换为空字符串，并使用 `.str.replace` 将撇号（**'**）替换为反引号（**`**）。
- 再次打印描述以验证结果。



```python
# Print the urban_art titles

print(urban_art.title)

  

#Print the urban_art descriptions

print(urban_art.desc)

  

# Replace Nan and ' values in description

urban_art.desc.fillna('', inplace = True)

urban_art.desc = urban_art.desc.str.replace("'", "`")

  

#Print the urban_art descriptions again

print(urban_art.desc)
```



# 创建分级设色图：纳什维尔建筑许可密度
## 什么是分级设色图？

**密度**

```python
schools_in_districts.head(2)
```

**获取计数**

```python
school_counts = schools_in_districts.groupby(['district']).size()
print(school_counts)
```

**添加计数**

```python
school_counts_df = school_counts.to_frame()
school_counts_df = school_counts_df.reset_index()
school_counts_df.columns = ['district', 'school_count']

districts_with_counts = pd.merge(school_districts, school_counts_df,
                                 on = 'district')
districts_with_counts.head(2)
```

**用面积归一化计数**

```python
districts_with_counts['area'] = districts_with_counts.area

districts_with_counts['school_density'] = districts_with_counts.apply(
    lambda row: row.school_count/row.area, axis = 1)

districts_with_counts.head(2)
```


## 使用 geopandas 绘制分级着色图

**使用 GeoDataFrame.plot() 的分级着色图**

```python
districts_with_counts.plot(column = 'school_density', legend = True)
plt.title('每平方十进制的学校数')
plt.xlabel('经度')
plt.ylabel('纬度');
```

**使用 GeoDataFrame.plot() 的分级着色图**

```python
districts_with_counts.plot(column = 'school_density', cmap = 'BuGn', edgecolor = 'black', legend = True)
plt.title('每平方十进制的学校数')
plt.xlabel('经度')
plt.ylabel('纬度');
```

**以平方千米计算面积**

```python
# starting CRS
print(school_districts.crs)
```

```python
# convert to EPSG 3857
school_districts = school_districts.to_crs(epsg = 3857)
print(school_districts.crs)
```

**以平方千米计算面积**

```python
# define a variable for m^2 to km^2
sqm_to_sqkm = 10**6

school_districts['area'] = school_districts.area / sqm_to_sqkm
school_districts.head(2)
```

```python
# change crs back to 4326
school_districts = school_districts.to_crs(epsg = 4326)
print(school_districts.crs)
```

```python
print(school_districts.head(2))
```

```python
# aggregate to get counts
school_counts = schools_in_districts.groupby(['district']).size()

# convert school_counts to a df
school_counts_df = school_counts.to_frame()
school_counts_df = school_counts_df.reset_index(level=0)
school_counts_df.columns = ['district', 'school_count']

# merge
districts_with_counts = pd.merge(school_districts, 
                                 school_counts_df, on = 'district')

districts_with_counts.head(1)
```

**计算学校密度**

```python
# create school_density
districts_with_counts['school_density'] = districts_with_counts.apply(
    lambda row: row.school_count/row.area, axis = 1)

# plot it
districts_with_counts.plot(column = 'school_density', cmap = 'BuGn', 
                           edgecolor = 'black', legend = True)
plt.title('每平方千米的学校数')
plt.xlabel('经度')
plt.ylabel('纬度')
plt.show();
```




### 空间连接与计数

您将继续为绘制 `geopandas` 分级设色图（choropleth）准备数据集，方法是创建一个将建筑许可与议会选区进行空间连接得到的 GeoDataFrame。之后，您就可以获取每个议会选区签发的建筑许可数量。
- 使用 `permits`、`council_districts.crs` 和 `permits` 中的 `geometry` 创建 `permits_geo`。
- 将 `permits_geo` 与 `council_districts` 进行空间连接，获取每个议会选区 `within` 的建筑许可。将结果命名为 `permits_by_district`。
- 通过链式调用 `groupby()` 和 `size()` 方法，统计每个选区的许可数量，命名为 `permit_counts`。
- 由 `permit_counts` 创建 `counts_df`。重置索引，并将列命名为 `district` 和 `bldg_permits`。

```python
# Create permits_geo

permits_geo = gpd.GeoDataFrame(permits, crs = council_districts.crs, geometry = permits.geometry)

  

# Spatially join permits_geo and council_districts

permits_by_district = gpd.sjoin(permits_geo, council_districts, predicate = 'within')

print(permits_by_district.head(2))

  

# Count permits in each district

permit_counts = permits_by_district.groupby('district').size()

  

# Convert permit_counts to a df with 2 columns: district and bldg_permits

counts_df = permit_counts.to_frame()

counts_df = counts_df.reset_index()

counts_df.columns = ['district', 'bldg_permits']

print(counts_df.head(2))
```


## **使用 folium 制作分级着色图**

**folium.Map 分级着色图**

```python
# Construct a map object for Nashville
nashville = [36.1636,-86.7823]
m = folium.Map(location=nashville, zoom_start=10)

# Create a choropleth using the folium Choropleth class
folium.Choropleth(...)
```

**folium 分级着色图的参数**

*   `geo_data` - 多边形源数据（geojson 文件或 GeoDataFrame）
*   `name` - 多边形的几何列名（或 geojson 属性）
*   `data` - 归一化数据的 DataFrame 或 Series 来源
*   `columns` - 列表：一列对应多边形，另一列为要绘制的值

**folium 分级着色图的其他参数**

*   `key_on` - 绑定数据的 GeoJSON 变量（始终以 `feature` 开头）
*   `fill_color` - 多边形填充色（默认蓝色）
*   `fill_opacity` - 0（透明）到 1（不透明）
*   `line_color` - 多边形边界线颜色（默认黑色）
*   `line_opacity` - 0（透明）到 1（不透明）
*   `legend_name` - 图例标题

```python
# Center point and map for Nashville
nashville = [36.1636,-86.7823]
m = folium.Map(location=nashville, zoom_start=10)
```

```python
# Define a choropleth layer for the map
folium.Choropleth(
    geo_data=districts_with_counts,
    name='geometry',
    data=districts_with_counts,
    columns=['district', 'school_density'],
    key_on='feature.properties.district',
    fill_color='YlGn',
    fill_opacity=0.75,
    line_opacity=0.5,
    legend_name='Schools per km squared by School District'
).add_to(m)

folium.LayerControl().add_to_map()
```

```python
display(m)
```





```python

```