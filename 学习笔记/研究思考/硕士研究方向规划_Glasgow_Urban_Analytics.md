---
tags: [研究规划, BigData, 城市计算, Glasgow, 硕士, 博士准备]
---

# 硕士研究方向规划 — Glasgow Urban Analytics

> 个人背景：本科大数据方向，已与姚静教授取得联系（本科导师的老师）
> 目标：授课型硕士期间开展研究，为博士申请积累成果

## 一、背景分析

### 1.1 个人优势
- 大数据技术栈：Hadoop/Spark、Python、数据库
- GIS基础：空间数据处理、空间分析、PostGIS
- 已建立的学术网络：通过本科导师与姚静教授的联系

### 1.2 Glasgow Urban Analytics 资源
- **Urban Big Data Centre (UBDC)**：Glasgow核心城市数据平台，提供多源城市数据
- **姚静教授团队**：空间统计、GeoAI、设施选址、城市绿地
- **School of Geographical & Earth Sciences**：GIS、遥感、空间分析传统强校
- **Glasgow City Council**：实际城市数据和应用场景

### 1.3 硕士阶段研究目标
1. 产出1篇可投稿的学术论文（或至少完成高质量working paper）
2. 掌握独立研究能力（文献综述→方法设计→实验→写作）
3. 建立与姚静教授团队的深度合作关系
4. 为博士申请提供研究计划和推荐信基础

---

## 二、推荐研究方向

### 方向一：GeoAI + 城市绿地/环境感知 ⭐⭐⭐⭐⭐

**推荐理由：** 与姚静教授当前最活跃方向完全契合，团队有现成合作者，数据可得性高。

#### 2.1 研究背景
- 城市绿地对居民身心健康有重要影响（Landscape and Urban Planning, 2025）
- 街景图像+深度学习可量化城市环境质量（Science of Total Environment, 2021）
- 现有研究多关注绿地"数量"，对"质量"和"感知"研究不足

#### 2.2 具体课题建议

**课题A：基于街景图像的城市绿地感知质量评估**
- 研究问题：如何利用街景图像和深度学习量化居民对城市绿地的感知质量？
- 数据源：Google Street View API、OpenStreetMap绿地数据、UBDC城市数据
- 方法：语义分割（DeepLab/U-Net）→ 绿色视图指数 → GWR空间异质性分析
- 创新点：将计算机视觉与空间统计结合，揭示绿地感知的空间分异规律

**课题B：城市绿地空间公平性：多尺度可达性分析**
- 研究问题：Glasgow不同社区的绿地可达性是否存在空间不平等？
- 数据源：UBDC人口数据、OSM绿地数据、路网数据
- 方法：两步移动搜索法（2SFCA）+ MGWR多尺度分析
- 创新点：引入多尺度视角，揭示不同空间尺度下绿地公平性的差异

**课题C：城市绿地与居民情绪的时空关联**
- 研究问题：城市绿地空间特征如何影响居民情绪状态？是否存在时空异质性？
- 数据源：社交媒体情感数据、街景图像、传感器数据
- 方法：NLP情感分析 + GTWR时空建模
- 创新点：融合多模态数据，揭示绿地-情绪关联的时空变异

#### 2.3 可投稿期刊
- Landscape and Urban Planning (Q1, IF ~8)
- Environment and Planning B (Q2)
- Computers, Environment and Urban Systems (Q1)
- Urban Forestry & Urban Greening (Q2)

#### 2.4 团队资源
- **Chongxian Chen**：城市绿地感知方向，4篇合作论文
- **Haiwei Li**：城市绿地与健康方向，3篇合作论文
- **UBDC**：Glasgow城市数据平台

---

### 方向二：空间优化 + 公共服务设施选址 ⭐⭐⭐⭐⭐

**推荐理由：** 姚静教授传统核心方向，方法论成熟，容易快速出成果。

#### 2.5 研究背景
- 城市公共服务设施的合理配置是城市规划核心问题
- 传统选址模型未充分考虑时空需求变化（Int J Digital Earth, 2025）
- 城乡公共服务差距是重要社会公平议题（Socio-Economic Planning Sciences, 2022）

#### 2.6 具体课题建议

**课题A：考虑时空需求变化的应急设施选址优化**
- 研究问题：如何在消防站/EMS选址中考虑不同时段的需求变化？
- 数据源：Glasgow 999呼叫数据、人口动态数据、路网数据
- 方法：时空需求建模 → 双目标覆盖模型 → 启发式优化算法
- 创新点：将时间维度引入传统覆盖模型，提出动态选址策略

**课题B：城市公园绿地选址的多目标空间优化**
- 研究问题：如何在有限预算下最大化公园绿地的服务覆盖和公平性？
- 数据源：Glasgow人口分布、现有公园、土地利用数据
- 方法：多目标优化（NSGA-II）+ 空间公平性指标
- 创新点：同时优化效率和公平，为城市规划提供决策支持

**课题C：15分钟城市概念的空间可达性评估框架**
- 研究问题：Glasgow在多大程度上满足"15分钟城市"标准？
- 数据源：OSM POI数据、路网数据、UBDC人口数据
- 方法：网络分析 + 可达性指标 + 空间聚类
- 创新点：将国际城市规划理念本地化，提供量化评估框架

#### 2.7 可投稿期刊
- Computers, Environment and Urban Systems (Q1)
- Socio-Economic Planning Sciences (Q2)
- International Journal of Geographical Information Science (Q1)
- European Journal of Operational Research (Q1)

#### 2.8 团队资源
- **Weicong Luo**：EMS选址方向，4篇合作论文
- **Alan T. Murray**：设施选址方法论权威（远程合作）

---

### 方向三：时空数据建模 + 房价/城市经济 ⭐⭐⭐⭐

**推荐理由：** GTWR是姚静教授标志性成果，房价研究数据丰富，方法论成熟。

#### 2.9 研究背景
- 房价受多种因素影响，且影响程度随空间位置变化（Geographical Analysis, 2015）
- GTWR模型可同时捕捉时空非平稳性
- 短租平台（Airbnb）对城市住房市场的影响日益显著

#### 2.10 具体课题建议

**课题A：Glasgow房价的时空异质性驱动因素分析**
- 研究问题：哪些因素驱动Glasgow房价？其影响如何随时间和空间变化？
- 数据源：UK房价交易数据（Land Registry）、人口普查、交通、学校数据
- 方法：GTWR/MGWR → 时空异质性可视化 → 驱动因素分区
- 创新点：揭示Glasgow房价驱动因素的多尺度时空变异

**课题B：Airbnb对Glasgow住房市场的影响：空间计量分析**
- 研究问题：Airbnb密度如何影响周边住房价格和租金？
- 数据源：Airbnb Inside数据、房价数据、社区特征数据
- 方法：空间杜宾模型（SDM）+ GTWR
- 创新点：量化短租平台的空间溢出效应

**课题C：城市更新项目对周边房价的时空溢出效应**
- 研究问题：Glasgow城市更新项目是否提升了周边房价？影响范围和时间滞后？
- 数据源：城市更新项目数据、房价时序数据
- 方法：事件研究法 + GTWR + 空间断点回归
- 创新点：评估城市更新政策效果的时空维度

#### 2.11 可投稿期刊
- Housing Studies (Q2)
- Urban Studies (Q1)
- The Annals of Regional Science (Q3)
- International Journal of Housing Policy (Q2)

#### 2.12 团队资源
- **R (GWmodel包)**：GTWR方法论的成熟工具
- **UK房价数据**：公开可得，质量高

---

### 方向四：GeoAI + 遥感大数据城市监测 ⭐⭐⭐⭐

**推荐理由：** 遥感+AI是最热门交叉方向，数据获取成本低，博士扩展性强。

#### 2.13 研究背景
- 开放遥感数据（Sentinel、Landsat）降低了数据获取门槛
- 深度学习在遥感图像分析中取得突破性进展
- 夜间灯光数据可代理经济活动（Int J Applied Earth Observation, 2024）

#### 2.14 具体课题建议

**课题A：基于Sentinel时序数据的城市扩张监测与预测**
- 研究问题：Glasgow城市扩张的时空模式是什么？未来趋势如何？
- 数据源：Sentinel-2时序影像、土地利用数据
- 方法：时序分类（LSTM/Transformer）+ CA-Markov预测
- 创新点：深度学习时序分类在城市扩张监测中的应用

**课题B：城市热岛效应的时空演变与驱动因素**
- 研究问题：Glasgow热岛效应的时空格局如何？哪些因素驱动其变化？
- 数据源：Landsat地表温度、土地覆盖、建筑密度、绿地覆盖
- 方法：遥感反演 + GTWR驱动因素分析
- 创新点：揭示城市热岛驱动因素的时空异质性

**课题C：夜间灯光+深度学习的城市经济活动估计**
- 研究问题：能否用夜间灯光数据估计Glasgow社区级别的经济活动水平？
- 数据源：VIIRS夜间灯光、经济统计数据
- 方法：CNN回归模型 + 空间验证
- 创新点：为缺乏经济统计的区域提供估计方法

#### 2.15 可投稿期刊
- Remote Sensing of Environment (Q1)
- ISPRS Journal of Photogrammetry and Remote Sensing (Q1)
- International Journal of Applied Earth Observation and Geoinformation (Q1)
- Remote Sensing (Q2)

#### 2.16 团队资源
- **Google Earth Engine**：免费遥感数据处理平台
- **Glasgow遥感数据**：Sentinel/Landsat覆盖良好

---

### 方向五：城市韧性与可持续性 ⭐⭐⭐

**推荐理由：** 全球研究热点，资助机会多，但与姚静教授当前方向匹配度稍低。

#### 2.17 研究背景
- COVID-19暴露了城市系统的脆弱性（Journal of Urban Management, 2024）
- 碳排放的空间异质性分析对精准减排有指导意义（Energy, 2022）
- 极端气候事件频率增加，城市韧性评估需求迫切

#### 2.18 具体课题建议

**课题A：极端热浪事件下的城市脆弱性评估**
- 研究问题：Glasgow哪些社区在极端热浪事件中最脆弱？
- 数据源：气象数据、人口数据、建筑数据、社会经济数据
- 方法：脆弱性指数构建 + 空间聚类 + 情景分析
- 创新点：将气候风险与社会脆弱性结合的空间评估框架

**课题B：Glasgow碳排放的空间异质性与驱动因素**
- 研究问题：Glasgow不同区域的碳排放水平有何差异？驱动因素是什么？
- 数据源：能源消耗数据、交通数据、土地利用数据
- 方法：空间统计 + GTWR驱动因素分解
- 创新点：为精准减排提供空间决策依据

---

## 三、方向选择决策矩阵

| 维度 | 方向一：GeoAI+绿地 | 方向二：空间优化+选址 | 方向三：时空建模+房价 | 方向四：GeoAI+遥感 | 方向五：城市韧性 |
|------|:---:|:---:|:---:|:---:|:---:|
| 与姚静教授匹配 | ★★★★★ | ★★★★★ | ★★★★★ | ★★★★ | ★★★ |
| 发文潜力 | ★★★★ | ★★★★ | ★★★★ | ★★★★★ | ★★★★ |
| 博士衔接性 | ★★★★ | ★★★★★ | ★★★★ | ★★★★★ | ★★★★ |
| 数据可得性 | ★★★★★ | ★★★★ | ★★★★★ | ★★★★★ | ★★★ |
| 方法创新空间 | ★★★★ | ★★★★ | ★★★ | ★★★★★ | ★★★ |
| 个人背景匹配 | ★★★★ | ★★★★ | ★★★ | ★★★★★ | ★★★ |
| **综合推荐** | **首选** | **首选** | **推荐** | **推荐** | **可选** |

---

## 四、硕士期间时间规划

### 4.1 入学前（现在 - 9月）
- [ ] 精读姚静教授近3年论文（重点关注方向一/二的文献）
- [ ] 学习R语言GWmodel包 / Python空间分析库（GeoPandas、PySAL）
- [ ] 复习空间统计基础（GWR、空间自相关、空间回归）
- [ ] 了解UBDC数据资源和申请流程
- [ ] 与姚静教授邮件沟通研究意向

### 4.2 第一学期（9月 - 12月）
- 完成授课课程（GIS、空间分析、数据科学基础）
- 确定研究方向和具体课题
- 完成文献综述初稿
- 开始数据收集和预处理
- 与姚静教授/团队成员建立定期meeting

### 4.3 第二学期（1月 - 4月）
- 完成方法设计和实验
- 初步结果分析和可视化
- 撰写论文初稿
- 参加校内研讨会展示进展

### 4.4 暑期（5月 - 9月）
- 完善论文和实验
- 投稿学术论文（目标：Q2及以上期刊）
- 准备博士申请材料（研究计划、推荐信）
- 与姚静教授讨论博士方向

---

## 五、关键参考文献

### GeoAI + 城市绿地
1. Chen, C., Li, H., Luo, W., Xie, J., **Yao, J.**, Wu, L. (2021). Predicting the effect of street environment on residents' mood states in large urban areas using machine learning and street view images. *Science of The Total Environment*, 786, 151605. [110 cited]
2. Chen, C., Feng, X., **Yao, J.**, Xiong, X. (2025). Perceived leisure service benefits of peri-urban community green spaces. *Landscape and Urban Planning*, 105338. [20 cited]
3. Song, D., Zhong, D., Chen, Z., et al. (2025). A satellite perspective of greenspace and human exposure over urban and peri-urban areas in Chinese cities. *Landscape and Urban Planning*, 105354. [11 cited]

### 空间优化 + 设施选址
4. **Yao, J.**, Zhang, X., Murray, A.T. (2018). Location optimization of urban fire stations: Access and service coverage. *Computers, Environment and Urban Systems*, 73, 152-162. [133 cited]
5. Luo, W., **Yao, J.**, Mitchell, R., Zhang, X., Li, W. (2022). Locating emergency medical services to reduce urban-rural inequalities. *Socio-Economic Planning Sciences*, 84, 101416. [36 cited]
6. Chen, Y., **Yao, J.**, Wang, S., et al. (2025). Location optimization of urban fire stations: a bi-objective coverage model. *International Journal of Digital Earth*. [5 cited]

### GTWR + 房价建模
7. Fotheringham, A.S., Crespo, R., **Yao, J.** (2015). Geographical and Temporal Weighted Regression (GTWR). *Geographical Analysis*, 47(4), 431-452. [589 cited]
8. Fotheringham, A.S., Crespo, R., **Yao, J.** (2015). Exploring, modelling and predicting spatiotemporal variations in house prices. *The Annals of Regional Science*, 54(2), 417-436. [66 cited]
9. **Yao, J.**, Fotheringham, A.S. (2015). Local Spatiotemporal Modeling of House Prices: A Mixed Model Approach. *The Professional Geographer*, 68(2), 238-251. [50 cited]

### GeoAI 综述
10. Song, Y., Kalácska, M., Gašparović, M., **Yao, J.**, Najibi, N. (2023). Advances in geocomputation and geospatial artificial intelligence (GeoAI) for mapping. *International Journal of Applied Earth Observation and Geoinformation*, 118, 103300. [78 cited]

---

## 六、与姚静教授沟通建议

### 6.1 首次邮件沟通要点
- 自我介绍：本科背景、导师关系、Glasgow录取
- 表达研究兴趣：明确倾向方向（建议方向一或二）
- 询问团队seminar参与方式
- 请求推荐pre-read文献

### 6.2 建议提问
1. 团队目前在哪些方向有活跃的研究项目？
- 硕士论文是否有机会与团队现有项目结合？
- UBDC数据申请流程和时间线？
- 是否有博士名额和资助机会？

### 6.3 展示价值的方式
- 主动承担数据分析工作（你有大数据技术背景）
- 参与团队论文的数据处理和可视化
- 在seminar中积极展示和讨论
- 提出Glasgow本地数据的新应用场景
