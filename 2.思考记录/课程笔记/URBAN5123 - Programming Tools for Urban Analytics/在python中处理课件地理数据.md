# 介绍
##  位置
介绍位置概念,引出斯诺点图(经典霍乱病毒分布地图)

## 课程将学到
- 如何用地理点绘制散点图
- 如何用 geopanda 绘制集合对象
- 如何从 DataFrame 构建 GeoDataFrame
- 如何进行空间连接
- 如何为图添加街道底图
- 何时以及如何创建分级填色

## 经度与纬度

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

# 几何和 Shapefile
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

