---
tags:
  - 空间分析
  - PySAL
  - Python
  - 空间统计
  - 空间计量经济学
created: 2026-06-21
---

# PySAL 空间分析 Python 生态

> 上位概念：[[00-空间分析知识体系总索引]] > 知识体系与开源软件生态
> 相关概念：[[GeoDa空间数据分析平台]]、[[空间自相关指标体系]]、[[地理加权回归GWR与MGWR]]

---

## 1. 概述

**PySAL（Python Spatial Analysis Library）** 是空间分析领域最为庞大且功能最全的 Python 生态系统。由 Luc Anselin 与 Sergio J. Rey 联合发起，彻底改变了地理计算依赖封闭软件的局面。

## 2. 模块化架构

PySAL采用完全模块化设计，涵盖从基础几何计算到高级计量经济学的完整链条。

### 2.1 核心子包

| 子包/模块 | 核心功能 | 知识体系映射 |
|-----------|----------|-------------|
| `libpysal` | 空间权重矩阵构建、计算几何算法、经典数据集 | 空间拓扑与关系构建 |
| `esda` | 局部与全局空间自相关统计量 | 探索性空间数据分析 |
| `spreg` | 空间回归模型 | 空间计量经济学建模 |
| `mgwr` | GWR与MGWR参数估计 | 空间异质性分析 |
| `giddy` | 地理空间分布动态演进 | 时空动态 |
| `pointpats` | 点格局分析 | 点模式分析 |
| `inequality` | 空间不平等度量 | 空间公平性 |
| `segregation` | 空间隔离度量 | 社会空间分析 |
| `access` | 可达性计算 | 空间可达性 |
| `spopt` | 空间优化 | 设施选址、区域划分 |

### 2.2 详细功能说明

#### libpysal - 基础库

- **空间权重矩阵**：邻接矩阵、距离阈值矩阵、K近邻矩阵
- **计算几何**：凸包、Voronoi图、Delaunay三角剖分
- **数据集**：内置经典空间数据集用于教学与测试
- **IO模块**：支持Shapefile、GeoJSON等多种格式

#### esda - 探索性空间数据分析

- **全局指标**：Moran's I、Geary's C、Getis-Ord G
- **局部指标**：局部Moran's I（LISA）、局部Geary's C、Gi*
- **Moran散点图**：四象限可视化
- **显著性检验**：置换检验、多重检验校正

```python
from pysal.lib import weights
from pysal.explore import esda

# 构建权重矩阵
w = weights.Queen.from_dataframe(gdf)
w.transform = 'r'

# 全局Moran's I
moran = esda.Moran(gdf['var'], w)
print(f"Moran's I: {moran.I:.4f}, p-value: {moran.p_sim:.4f}")

# 局部Moran's I (LISA)
lisa = esda.Moran_Local(gdf['var'], w)
```

#### spreg - 空间回归

- **空间滞后模型（SLM）**：极大似然估计
- **空间误差模型（SEM）**：极大似然估计
- **空间面板模型**：固定效应、随机效应
- **空间区制模型**：分区回归
- **广义矩估计（GMM）**：现代计量技术

```python
from pysal.model import spreg

# OLS回归
ols = spreg.OLS(gdf[['y']].values, gdf[['x1','x2']].values)

# 空间滞后模型
slm = spreg.ML_Lag(gdf[['y']].values, gdf[['x1','x2']].values, w=w)

# 空间误差模型
sem = spreg.ML_Error(gdf[['y']].values, gdf[['x1','x2']].values, w=w)
```

#### mgwr - 多尺度地理加权回归

- **GWR**：地理加权回归
- **MGWR**：多尺度地理加权回归
- **带宽选择**：AICc、CV准则
- **局部推断**：标准误、假设检验

```python
from mgwr.gwr import GWR
from mgwr.sel_bw import Sel_BW

# 带宽选择
selector = Sel_BW(coords, y, X)
bw = selector.search(criterion='AICc')

# GWR拟合
model = GWR(coords, y, X, bw)
results = model.fit()
```

#### giddy - 时空动态

- **马尔可夫链**：空间马尔可夫、时间马尔可夫
- **分布动态**：核密度估计、σ收敛、β收敛
- **时空相关**：时空自相关

#### pointpats - 点格局分析

- **最近邻分析**：Clark-Evans检验
- **K函数**：Ripley's K、L函数
- **核密度估计**：KDE
- **空间点过程**：泊松过程、簇过程

## 3. 安装与使用

### 3.1 安装方式

```bash
# 安装完整PySAL
pip install pysal

# 安装单个子包
pip install libpysal
pip install esda
pip install spreg
pip install mgwr
```

### 3.2 依赖关系

```
pysal (元包)
├── libpysal (基础)
├── esda (依赖libpysal)
├── spreg (依赖libpysal, esda)
├── mgwr (依赖libpysal)
├── giddy (依赖libpysal)
├── pointpats (依赖libpysal)
└── ...
```

## 4. 与GeoDa的对比

| 特性 | PySAL | GeoDa |
|------|-------|-------|
| **界面** | 编程接口 | 图形化 |
| **语言** | Python | C++ |
| **灵活性** | 高度可定制 | 预设功能 |
| **扩展性** | 易于集成其他Python库 | 功能固定 |
| **学习曲线** | 需要编程基础 | 可视化易上手 |
| **适用场景** | 科研、工程、自动化 | 教学、实证探索 |

## 5. 应用案例

| 应用领域 | 使用模块 | 典型任务 |
|----------|----------|----------|
| 犯罪分析 | esda, spreg | 热点检测、空间回归 |
| 房地产 | mgwr, spreg | 房价建模、局域效应 |
| 流行病学 | esda, pointpats | 空间聚集、点模式 |
| 区域经济 | spreg, giddy | 空间计量、收敛分析 |
| 环境科学 | mgwr, pointpats | 空间异质性、物种分布 |

---

## 关联知识图谱

```
PySAL 空间分析 Python 生态
├── 核心子包
│   ├── libpysal（基础：权重矩阵、几何、数据集）
│   ├── esda（ESDA：Moran's I、LISA、Gi*）
│   ├── spreg（空间回归：SLM、SEM、GMM）
│   ├── mgwr（GWR/MGWR：局域回归）
│   ├── giddy（时空动态：马尔可夫、收敛）
│   ├── pointpats（点格局：K函数、KDE）
│   ├── inequality（空间不平等）
│   ├── segregation（空间隔离）
│   ├── access（可达性）
│   └── spopt（空间优化）
├── 与GeoDa的关系
│   └── → [[GeoDa空间数据分析平台]]
├── 理论基础
│   ├── → [[空间自相关指标体系]]
│   └── → [[地理加权回归GWR与MGWR]]
└── 应用领域
    ├── 犯罪分析
    ├── 房地产
    ├── 流行病学
    └── 区域经济
```
