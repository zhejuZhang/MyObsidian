结合之前的 Formative Assessment 和这份正式的 Summative Assessment 文件，现在可以更准确地确定选址研究项目的设计方向。

这份文件补充了此前没有明确的提交时间、字数限制、提交格式、课程学习成果以及 AI 使用声明等要求。

最重要的是：这门课程考查的核心是完整、规范、可复现的数据科学编程过程，而不是单纯的 GIS 选址结果，也不是一篇传统的学术论文。

因此，你的选址研究需要同时体现城市研究价值、Python 编程能力、数据处理能力、空间分析与建模能力。

## 一、两项 Assessment 的基本要求

|项目|Formative Assessment|Summative Assessment|
|---|---|---|
|作业性质|项目研究计划|完整数据科学项目|
|英文名称|Data Science Project Proposal|Data Science Report|
|截止日期|2026年12月3日|2027年1月13日12:00|
|篇幅限制|最多1页|最多3,000 words|
|提交格式|文件未明确规定|`.ipynb` 和 `.html`|
|编程代码|不要求完成|包含全部 Python 代码|
|研究结果|说明预期成果|提供实际分析结果|
|提交平台|Moodle|Moodle|
|文件大小限制|未明确|100 MB|
|AI使用声明|未明确|需要专门段落|

以上截止时间、提交格式和字数限制均来自 Summative Assessment 文件。

1.PTUA-Summative_assessment-2026-v2(1).pdf

1.PTUA-Summative_assessment-2026-v2(1).pdf

### 关键时间节点

1. 2026年11月26日 — 当前阶段
    
    确定研究主题、数据来源和初步分析方法。
    
2. 2026年12月3日 — Formative Assessment
    
    提交一页 Proposal，获得教师反馈。
    
3. 2026年12月上中旬 — 建议安排
    
    获取数据、清洗数据、构建选址指标和空间分析单元。
    
4. 2026年12月下旬 — 建议安排
    
    完成选址建模、方案比较、敏感性分析与可视化。
    
5. 2027年1月上旬 — 建议安排
    
    撰写报告、检查代码规范和可复现性。
    
6. 2027年1月13日12:00 — Summative Assessment
    
    正式提交 Jupyter Notebook 和 HTML 文件。
    

目前最紧迫的任务不是完成选址模型，而是确定一个数据能够获取、研究范围可控、技术路线清晰的选址问题，并在12月3日前完成 Proposal。

## 二、Summative Assessment 的最终提交形式

文件明确要求提交：

> A single Jupyter Notebook and an HTML file generated from the Jupyter Notebook.

也就是说，最终提交的不是传统 Word 论文，而是一份结合代码、文字、图表和分析结果的计算型研究报告。

1.PTUA-Summative_assessment-2026-v2(1).pdf

Urban_Facility_Location.ipynb

Jupyter Notebook：完整代码、Markdown、分析结果

Urban_Facility_Location.html

由同一 Notebook 导出的可阅读报告

这意味着你需要在 Jupyter Notebook 中交替组织 Markdown Cells 和 Code Cells，而不是先完成全部代码，再独立撰写一份与代码无关的报告。

Jupyter Notebook 结构示意

Markdown Cell

1. Introduction and Research Objectives

本研究旨在识别公共设施服务不足区域，并提出最优新增设施选址方案。

Code Cell [1]

import pandas as pd  
import geopandas as gpd  
import matplotlib.pyplot as plt

Markdown Cell

2. Data Collection and Understanding

介绍人口需求、道路网络和现有设施数据。

Code Cell [2]

population = gpd.read_file("population.gpkg")  
population.head()

Output

Markdown Cell

解释人口空间分布特征及其对后续选址分析的意义。

这样的结构能够直接体现课程所强调的 Transparency（透明性）和 Reproducibility（可复现性）。

## 三、Summative Assessment 明确要求的七项研究内容

文件第1页 Section 2 — Content and Format 明确规定了七项分析内容。这是设计选题和组织最终报告最直接的依据。

1.PTUA-Summative_assessment-2026-v2(1).pdf

### 3.1 Research Questions and Project Objectives

研究问题与研究目标，需要学术文献支持。

老师不要求详细的 Literature Review，但要求引用学术文献支持研究问题、变量选择和研究假设。

对于选址研究，应该通过文献解释为什么需要开展设施选址优化、为什么选择某一种选址模型、如何定义服务需求，以及为什么采用特定的服务距离。

这里需要区分三个层次：

|层次|选址研究示例|
|---|---|
|Research Background|城市公共设施存在空间分布不均衡问题|
|Research Question|如何通过新增设施改善公共服务可达性？|
|Research Objectives|识别服务缺口、构建选址模型、评价优化结果|

### 3.2 Data Collection Methods

数据收集方法。

文件明确允许三种数据获取方式：

- API：通过应用程序接口获取数据。
    
- Online Scraping：通过网络爬虫获取数据。
    
- Existing Data Sources：使用现有数据集并解释数据来源。
    

因此，你不一定必须进行网络爬虫，也不一定必须使用 API。

不过，如果能够通过 API 获取 OpenStreetMap 道路网络、POI 或其他新型城市数据，就可以更好地展示本课程的学习成果。

对于选址研究，可以考虑：

|数据|获取方式|Python 工具|
|---|---|---|
|道路网络|OSM / Overpass API|OSMnx|
|城市POI|OSM / Overpass API|OSMnx、Requests|
|人口统计|官方开放数据下载|Pandas|
|行政区边界|官方空间数据|GeoPandas|
|现有设施|开放数据或 API|Requests、GeoPandas|
|候选设施位置|空间数据筛选与构建|GeoPandas、Shapely|

### 3.3 Understanding Your Data

数据理解与探索性数据分析。

这部分需要展示你对原始数据的理解，而不是直接将数据输入模型。

|分析内容|选址研究中的体现|
|---|---|
|Data types|检查人口、经纬度、设施类型等字段|
|Summary statistics|人口数量、设施数量、距离分布|
|Data distribution|人口密度与设施分布特征|
|Data visualisation|人口分布地图、设施分布地图|
|Spatial relationships|人口需求与设施供给的空间关系|

这一部分可以自然地引出研究问题：现有设施是否与人口需求的空间分布相匹配？

### 3.4 Data Cleaning

数据清洗。

文件特别强调，即使使用 Kaggle 等平台中已经可以直接用于分析的数据，也必须包含数据清洗部分。

1.PTUA-Summative_assessment-2026-v2(1).pdf

对于空间选址项目，可以开展以下数据质量检查。

|数据问题|处理方法|
|---|---|
|Missing values|缺失值检查与处理|
|Duplicates|重复设施、重复空间记录检查|
|Outliers|异常人口数值、异常坐标检查|
|Invalid geometry|无效空间几何对象修复|
|CRS inconsistency|统一空间坐标参考系统|
|Spatial mismatch|检查设施与道路网络位置匹配情况|
|Data inconsistency|统一设施分类和属性字段|
|Temporal mismatch|检查不同数据集的时间一致性|

建议保留清洗前后的数据数量和质量检查结果，以说明为什么采取这些处理措施。

### 3.5 Feature Engineering

特征工程。

这是选址项目中非常值得重点设计的部分。它体现的是如何将原始城市数据转化为能够支持空间决策的分析变量。

例如：

|原始数据|特征工程|构建变量|
|---|---|---|
|人口统计|空间聚合|Population density|
|年龄结构|比例计算|Elderly population ratio|
|道路网络|网络最短路径计算|Network distance|
|公交站点|缓冲区统计|Public transport accessibility|
|POI|空间连接与统计|POI density|
|土地利用|空间叠加|Available land ratio|
|现有设施|最近邻或网络距离|Distance to nearest facility|
|人口与现有设施|服务覆盖分析|Unserved population|

对于选址优化模型，需求权重、候选点特征以及需求点到候选点之间的距离成本矩阵，也可以作为变量构建的重要成果。

### 3.6 Data Analysis

数据分析与建模。

文件给出的分析方法包括：

> Time series analysis, machine learning, spatial analysis, advanced regression analysis, etc.

这里的 `etc.` 表明分析方法并不局限于所列出的几种。

因此，空间优化（Spatial Optimisation）、选址—分配模型（Location-Allocation Model）、网络分析（Network Analysis）均可以作为合理的研究方法选择。

但空间优化是否能够充分体现课程中的机器学习相关学习成果，仍值得在 Formative 阶段向老师确认。

### 3.7 Summary of Findings and Suggestions

研究发现总结与建议。

最终结果不能只是输出最优设施位置，而应该解释：

- 为什么模型选择这些位置？
    
- 新增设施能够改善多少服务覆盖？
    
- 哪些地区仍然存在服务不足？
    
- 不同选址目标是否会产生不同结果？
    
- 选址方案对距离阈值、人口权重等参数是否敏感？
    
- 研究结果能够为城市规划提供什么建议？
    

这将选址模型的计算结果转化为 Urban Analytics 的研究发现。

## 四、Marking：老师究竟希望考查哪些能力？

文件第2页没有给出具体的评分比例，而是列出了六项 Intended Learning Outcomes（预期学习成果）。

1.PTUA-Summative_assessment-2026-v2(1).pdf

|官方学习成果|中文理解|选址项目中的体现|
|---|---|---|
|Write code according to best practice and produce tidy data|规范编程与整洁数据|函数封装、数据清洗、变量命名|
|Collaborate effectively with other analysts using appropriate tools|使用适当工具开展协作|Git、GitHub、版本管理|
|Produce transparent and reproducible documentation|透明且可复现的研究文档|Notebook、数据来源、参数记录|
|Set up, connect to and query a simple relational database by Python|使用Python操作关系型数据库|SQLite、SQL查询|
|Retrieve and analyse data from an API|API数据获取与分析|OSM API、Requests|
|Perform basic machine learning and AI related tasks|基础机器学习与AI任务|聚类、回归、需求预测|

这部分对我们之前讨论的选址研究非常重要。

如果只是使用 GeoPandas 进行缓冲区分析，再利用 AHP 进行加权叠加，虽然能够完成选址研究，但展示的课程学习成果相对有限。

如果能将 API 数据获取、数据清洗、空间特征工程、需求建模、空间优化及可复现编程结合起来，就能更全面地体现课程内容。

不过，文件没有明确规定必须逐项完成全部六项学习成果，也没有规定每一项的评分权重，因此不应为了覆盖所有技术而强行增加无关分析。

## 五、哪些要求是强制的，哪些是鼓励的？

|内容|要求性质|
|---|---|
|提交 Jupyter Notebook|强制|
|提交 Notebook 生成的 HTML|强制|
|包含完整 Python 代码|强制|
|Markdown形式的研究报告|强制|
|3,000 words 篇幅限制|强制|
|学术文献支持研究问题与目标|明确要求|
|数据理解与数据清洗|明确要求|
|特征工程|明确要求|
|数据分析与结果解释|明确要求|
|AI Usage Statement|明确要求|
|使用新形式的城市数据|强烈推荐|
|使用课程以外的 Python packages|积极鼓励|
|使用 Kaggle 数据|允许|
|完整的文献综述|不需要|
|必须使用深度学习|未规定|
|必须使用机器学习|未单独规定为项目硬性要求|
|必须使用关系型数据库|未单独规定为项目硬性要求|
|必须通过API获取数据|未规定，可使用现有数据|
|必须进行空间分析|未规定|

尤其值得注意的是，文件明确指出：

> Using extra Python packages to achieve your project goals is highly favourable.

使用课程以外的 Python 程序包受到积极鼓励。

1.PTUA-Summative_assessment-2026-v2(1).pdf

这意味着使用 OSMnx、NetworkX、PySAL、spopt、PuLP 等与选址研究相关的工具具有充分的课程依据。

## 六、重新审视之前提出的选址研究方向

根据 Summative 的实际要求，我建议调整此前的选题优先级。

|研究方向|数据科学体现|编程深度|实施难度|
|---|---|---|---|
|AHP多指标选址适宜性分析|中等|较低|较低|
|基于机器学习的商业设施选址|高|高|较高|
|公共设施空间优化选址|高|高|中等|
|共享单车需求预测与站点选址|很高|高|较高|
|电动汽车充电需求与选址优化|很高|高|较高|
|空间尺度与选址决策敏感性|高|高|中等|
|多目标设施选址优化|高|高|较高|

以上是根据作业要求作出的主观判断，并不是官方评分标准。

我认为有三条值得深入考虑的技术路线。

### 路线 A：城市设施空间优化

Spatial Optimisation

城市人口、道路网络、设施数据

空间数据清洗与特征工程

现有设施可达性及服务缺口分析

MCLP / P-median 空间优化模型

选址方案与优化效果评价

优势是技术路线清晰，模型具有明确的数学依据，实施范围容易控制。

不足是如果只采用人口作为需求代理变量，对于新型城市大数据与机器学习的体现可能相对有限。

### 路线 B：数据驱动的需求预测与选址优化

Demand Prediction and Location Optimisation

城市活动大数据

建成环境数据

道路网络数据

多源数据融合与特征工程

Machine Learning

Linear Regression / Random Forest

空间需求预测与需求权重构建

Spatial Optimisation

MCLP / P-median

最优设施选址及结果评价

这一方向在形式上能够较全面地体现课程的学习成果。

它不是简单地将人口密度作为需求，而是利用城市活动、人口、交通、建成环境等数据估计需求，再将需求预测结果输入选址模型。

关键问题在于能否获取真实的需求观测数据，并且验证模型对潜在候选位置的预测能力。

### 路线 C：空间选址决策的敏感性研究

Sensitivity and Robustness of Spatial Location Decisions

相同的原始城市数据

250m Grid

500m Grid

1000m Grid

不同尺度下的需求变量构建

相同的候选位置与空间优化模型

Solution A

Solution B

Solution C

选址结果差异与决策稳健性评价

这一方向具有更强的方法论研究潜力，能够将你此前关注的 MAUP 与空间决策研究结合起来。

需要注意的是，比较不同尺度产生的选址方案时，应尽量使用共同的高分辨率需求数据进行最终评价，否则评价指标本身也可能受到空间尺度变化的影响。

### 三条路线的比较

|比较维度|路线 A|路线 B|路线 C|
|---|---|---|---|
|API数据获取|可以体现|可以体现|可以体现|
|数据清洗|强|强|强|
|特征工程|较强|强|强|
|机器学习|不一定涉及|强|不一定涉及|
|空间分析|强|强|强|
|空间优化|强|强|强|
|方法论研究|中等|中等至高|高|
|研究工作量|中等|较大|中等至较大|
|数据获取风险|较低|较高|中等|

如果以课程学习成果的覆盖程度为主要考虑，路线 B 值得优先探索；如果以研究深度和未来科研方向为主要考虑，路线 C 更值得关注。

## 七、推荐的 Python 技术体系

|研究阶段|Python package|功能|
|---|---|---|
|Data Collection|`requests`|API请求|
|Data Collection|`osmnx`|OSM道路网络与设施数据|
|Data Management|`sqlite3`|关系型数据库存储与查询|
|Data Cleaning|`pandas`|数据清洗与整理|
|Spatial Processing|`geopandas`|空间数据处理|
|Geometry Processing|`shapely`|空间几何计算|
|Numerical Computing|`numpy`|数值计算|
|Network Analysis|`networkx`|道路网络距离计算|
|Feature Engineering|`scikit-learn`|特征标准化、转换与构建|
|Machine Learning|`scikit-learn`|回归、聚类及预测|
|Spatial Statistics|`libpysal`、`esda`|空间统计|
|Location Optimisation|`spopt`、`pulp`|空间选址优化|
|Visualisation|`matplotlib`、`seaborn`|地图和统计图表|
|Interactive Mapping|`folium`|交互式地图|
|Reproducibility|Jupyter Notebook|可复现研究过程|
|Version Control|Git、GitHub|代码版本管理|

不需要使用全部这些工具。应该先确定研究问题，再决定需要哪些程序包。

## 八、最终3,000 words报告的结构设计

根据文件要求，我建议使用下面的 Notebook 章节结构。这是针对选址研究设计的写作方案，而非官方指定的章节或字数分配。

建议正文总字数

# 3,000 words

1. Introduction and Research Objectives

350

2. Study Area and Data Collection

300

3. Data Understanding and EDA

300

4. Data Cleaning

250

5. Feature Engineering

400

6. Modelling and Spatial Optimisation

500

7. Results and Discussion

500

8. Conclusion and Limitations

300

9. AI Usage Statement

100

代码和参考文献不计入字数限制。

### 超出字数的扣分规则

文件中还明确规定了超字数的处罚。

1.PTUA-Summative_assessment-2026-v2(1).pdf

|超出比例|对应总字数区间（按整数百分比区间理解）|处罚|
|---|---|---|
|10–14%|3,300–3,449|扣1分|
|15–19%|3,450–3,599|扣2分|
|20–24%|3,600–3,749|扣3分|
|25%及以上|3,750及以上|Fail，记零分并要求重新提交|

文件对于恰好超出10%的边界表述存在一定歧义。因此建议不要将3,300 words作为写作目标，尽量将正文控制在2,800–3,000 words。

## 九、AI Usage Statement

这是之前 Formative 文件中没有提及、而 Summative 明确提出的一项新要求。

老师要求有一个专门的段落，讨论如何使用 AI 辅助数据分析。

1.PTUA-Summative_assessment-2026-v2(1).pdf

你可以在实际完成项目后说明 AI 是否用于代码解释、调试、方法探索、文档编写，以及你如何验证 AI 提供的内容。

建议在项目进行过程中保留 AI 使用记录，包括使用目的、生成内容、自行修改及验证过程。

不能仅凭这个段落的要求推断所有形式的 AI 使用均被允许，具体使用边界仍需遵守学校的学术诚信政策。

## 十、目前 Formative Assessment 应该如何设计？

综合两份文件，我建议将一页 Proposal 组织为以下六个部分。

|部分|建议字数|内容|
|---|---|---|
|Project Title|15|明确选址对象和研究方向|
|Background and Research Question|80|城市问题、研究动机、文献依据|
|Research Objectives|50|明确2–3个研究目标|
|Data Sources|65|数据来源与研究范围|
|Methodology and Programming Tools|130|数据清洗、特征工程、建模、优化、评价|
|Expected Outcomes and Feedback|60|预期成果及希望教师反馈的问题|
|合计|400|不超过一页|

其中，Methodology and Programming Tools 应该是占比最大的一部分，因为这门课程本身就是 Programming Tools for Urban Analytics。

## 十一、下一步：确定具体选址研究对象

在阅读完两份文件之后，我认为现在不应该立即开始撰写 Proposal，而应该优先解决具体选址对象和数据可用性问题。

结合你的研究兴趣，可以从以下选题矩阵开始筛选。

|选址对象|需求数据|预测分析|空间优化|空间尺度研究|
|---|---|---|---|---|
|共享单车站点|历史骑行记录|适合|适合|适合|
|电动汽车充电站|车辆及充电需求|适合|适合|适合|
|公共图书馆|人口、人口结构|可选|适合|适合|
|社区医疗中心|人口、医疗需求|可选|适合|适合|
|咖啡店|客流、消费、POI|适合但标签难获取|可以|可以|
|城市绿地|人口、绿地可达性|可选|适合|适合|
|公交站点|出行需求、人口|适合|适合|适合|
|物流配送中心|订单与运输需求|适合但数据难获取|适合|可以|

### 我建议优先研究的三个方向

1. 基于城市出行大数据的共享单车站点选址优化

Data-Driven Optimisation of Bike-Sharing Station Locations Using Urban Mobility Data

优势：城市大数据、特征工程、机器学习、空间优化。

2. 考虑空间公平性的电动汽车充电站选址优化

Optimising Electric Vehicle Charging Station Locations Considering Spatial Equity

优势：可持续城市交通、服务覆盖、需求建模。

3. 城市公共服务设施选址优化中的空间尺度敏感性研究

Investigating Spatial Scale Sensitivity in Urban Public Facility Location Optimisation

优势：MAUP、空间表征、空间优化、决策稳健性。

## 十二、总体建议

结合你之前关注的空间表征、变量构建和统计推断问题，我建议将选址研究定位为：

Data-driven Spatial Location Optimisation（数据驱动的空间选址优化）

在传统选址优化的基础上，增加一个具有研究价值的分析问题，而不是单纯地求解最优位置。

例如：

- 不同需求估计方法是否会改变选址结果？
    
- 不同空间尺度是否会影响最优设施位置？
    
- 不同优化目标如何影响服务效率与空间公平性？
    
- 道路网络距离与欧氏距离会产生多大的选址决策差异？
    

其中选择一个问题进行深入研究即可，不需要全部完成。

目前仍未确定具体设施类型、研究城市及实际可用数据，文件也未提供详细的分项评分权重。因此，下一阶段最值得开展的工作是选址相关文献调研与开放数据集筛选，在确认数据能够支撑研究问题后，再确定最终技术路线，并完成12月3日需要提交的一页 Formative Assessment。