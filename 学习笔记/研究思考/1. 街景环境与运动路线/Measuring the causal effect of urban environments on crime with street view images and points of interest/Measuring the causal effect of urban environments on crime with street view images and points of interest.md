---
tags: [论文笔记, 因果效应, 街景影像, 兴趣点, 犯罪, FCI算法, 城市环境, 范例研究, 姚静教授]
aliases: [He2026因果效应论文, 城市环境与犯罪因果研究, 街景犯罪因果研究]
---

# 论文信息

标题：Measuring the causal effect of urban environments on crime with street view images and points of interest

作者：zhanjun He, Wantong Meng , **Jing Yao** , Yuejian Gong, Liang Wu, Liufeng Tao

期刊：

年份：

DOI：

引用量：

key:

> 关联文档：[[3.因果算法选择]], [[5.1.城市环境与微观运动路线：基于多源空间数据与混合因果模型的路径选择机制研究]], [[因果发现（Causal Discovery）领域]]

## 研究问题

- **解决什么问题：**
	城市建成环境对犯罪的影响是环境犯罪学的核心议题。现有研究主要关注城市建成环境与犯罪之间的相关性，而非因果关系，导致结论常常相互矛盾（如有的研究发现繁忙街道更安全，有的则认为交通流量增加犯罪风险）。此外，街景感知特征、城市设施与犯罪之间的因果机制尚未被探索。
	本文要回答两个核心问题：
	1. 城市建成环境特征与犯罪之间存在怎样的因果关系？
	2. 如何定量评估这些环境特征对犯罪的因果效应？
	
- **解决问题思路：**
	采用三步研究框架：
	1. 数据提取与环境量化：基于街景图像（SVI）和兴趣点（POI）两类城市大数据，量化城市建成环境
		- SVI → FCN-8s语义分割 → 提取4个街道感知指标（围合感、开放性、交通流量、步行性）
		- POI → 按犯罪模式理论分为三类：犯罪吸引子、犯罪生成器、犯罪威慑器
	2. 因果发现：采用FCI算法（Fast Causal Inference），在结构因果模型（SCM）框架下识别环境特征与犯罪之间的因果图
		- 可处理潜在未观测混杂因素
		- 两步：骨架图构建（条件独立性检验）→ 边定向
	3. 因果效应测量：在因果图基础上，利用回归识别规则计算路径系数，进而通过路径系数乘积求和得到平均因果效应（ACE）
	
	**案例：** 纽约曼哈顿区，4249个街道段，2018-2020年数据
	
- **核心创新：**
	1. **方法论创新**：首次将**结构因果模型（SCM）** 应用于街景感知特征、城市设施与犯罪之间的因果关系研究，突破了传统相关性方法的局限，能够揭示多变量影响路径（包括直接效应和间接效应）
	2. **发现"间接效应"机制**：证明**街道感知特征不直接影响犯罪**，而是通过城市设施间接影响犯罪——这一发现挑战了以往直接用街景感知特征预测犯罪的研究范式
	3. **揭示设施类型的调节效应**：同一街道感知特征对犯罪的影响随**城市设施类型不同而不同**（如开放性在犯罪吸引子附近抑制犯罪，但在犯罪生成器附近增加犯罪）
	4. **定量因果效应：** 不仅发现因果关系方向，还量化了具体的ACE值（如每增加1个犯罪生成器，犯罪增加1.62起）
- **结论：**
	1. 街道感知特征（开放性、围合感、交通流量、步行性）**不直接影响犯罪**，而是通过城市设施**间接影响**犯罪
	2. 开放性（openness）的影响具有**双重性**：
		-     对犯罪吸引子（如酒吧、酒店）：开放性**降低**犯罪（增强监控，提高犯罪者被发现风险）
		- 对犯罪生成器（如学校、超市）：开放性**增加**犯罪（吸引更多人流，增加潜在受害者和犯罪机会）
	3. 犯罪生成器对犯罪的平均因果效应（ACE=1.62）**大于**犯罪吸引子（ACE=1.53），因为犯罪吸引子会吸引更多的警力部署和预防措施
	4. 对城市规划的启示：应重点关注城市设施的空间布局（尤其是犯罪生成器），通过调整设施位置实现犯罪预防
        
- **重要语句：**
	- “Street perception characteristics do not directly affect crime but rather impose an indirect influence through urban facilities.”
	- “The impact of street perception characteristics on crime varies depending on the type of urban facilities involved.”
	- “A major limitation of correlation-based methods is their inability to uncover the causal relationships between urban built environment and crime occurrence, thereby usually leading to conflicting conclusions.”
	- “Compared to RCM, SCMs offer several advantages in causal inference, particularly in terms of flexibility, interpretability, and capability to model complex systems.”
	- “Urban facilities primarily reflect residents’ routine activities, creating convergence opportunities between potential offenders and victims — a fundamental condition for crime opportunities.”
	- “Street perception characteristics are more strongly linked to environmental guardianship, indicating varying risks of detection.”
	
- 缺陷不足：
	作者在Discussion（Section 5）中明确指出**三个主要局限**：
	1. **忽略其他影响因素**：仅考虑物理建成环境（SVI和POI），未纳入自然环境条件、社会经济因素和人类行为因素等——犯罪实际受多因素复杂交互影响
	2. **犯罪类型粗放**：将入室盗窃和抢劫统归为财产犯罪进行分析，但不同类型的犯罪可能有不同的影响机制——未来应对每种犯罪类型进行单独分析
	3. **忽略空间异质性**：ACE衡量的是整个研究区域的平均因果效应，**忽略了建成环境与犯罪之间因果关系的空间异质性**——未来应探索因果效应的地理变异
    
- 启发展望：
	1. POI和路网数据缺乏精确时间戳，假设与犯罪数据（2018-2020）时间对齐
	2. 假设变量间为线性关系，可能无法捕捉非线性因果效应
	3. 因果发现算法依赖条件独立性检验，结果可能受样本量和变量选择影响
    
- 与我的研究关系：
	1. 可以考虑更改因果算法，例如GFCI
	2. 研究对象换成其他例如人们出行或者运动
	3. 

## 1. Introduction
### 第一段-引出犯罪与建筑环境

CPTED->犯罪机会/特殊地点->三个基础的维度：犯人、受害者、地点/环境
	例如：
		routine activity theory：犯罪-有动机的罪犯遇到脆弱的目标（没有监护人存在）
		Crime pattern theory：典型位置在个体行动与犯罪机会和地点的影响。以及某些地点被判定为犯罪吸引要素，生成原因和detractors
	place 是物理和意识space
		rational choice theory: 有犯罪动机的人会weight crime opportunities, rewards and risks.

概念：
犯罪学中place的概念 built environment（建筑公共设施(e.g., parks, schools and roads).
目的：
understanding the mechanisms of crime occurrence, developing effective crime prevention measures, and even guiding urban planning policies

### 第二段-量化城市建设环境方法
量化城市建设环境——关键——modeling its influence on crime occurrence
传统的方法：questionnaires / field surveys / environmental audits环境审计
缺陷：subjective and labor-intensive
last two decades
创新方法：使用emerging urban big data（points of interest (POIs) and street view images (SVIs)）
example：bus stops and supermarkets 作为离散点和POI
介绍POI和SVI的好处
利用artificial intelligence (AI) technology（图像语义分割）从SVIs中得到multi-scale environmental features（physical built environment elements and scene perception）
**总结：** urban big data 用于联系 between crime and built environment
POIs - physical elements
SVIs - visual perceptions（用于shape cognitive awareness spaces）


### 第三段-模型构建技术
城市环境-犯罪关系模型构建技术Techniques for modeling 依赖于 相关性方法
举例：①相关性分析-SVIs②spatial co-location pattern空间同位格局-POIs
However
缺陷/不足 unable 揭示真实的因果关系reveal real causal relationships
城市建成环境特征对犯罪行为的因果效应仍未得到充分研究。the causal effects of urban built environment features on crime remain underexplored.

### 第四段-研究目的
研究目的-通过SVIs和POIs调查城市建筑环境和犯罪事件之间的因果关系
(1) What kind of causal relationship exists between built environment features and crime? 
(2) How can we quantitatively assess定量评估 the causal effects of these urban built environment features on crime?


### 第五段-论文结构
- Section 1 引言
- Section 2  回顾已有研究（回顾了城市建成环境与犯罪关系建模的已有研究。）
- Section 3 研究区域、数据集、分析方法概述（outlines the study area, datasets, and analytical methods）
- Section 4 给出结果+讨论主要发现/政策影响/研究显示/潜在未来方向。
- 最后 总结 Finally, the paper concludes with a summary of the main insights obtained.


## 2. 相关著作-Related works

categorized into two groups: correlation-based and causality-based methods.
correlation-based - 变量统计关联
causality-based - 因果关系 cause-and-effect relationship（whether change of a variable will correspondingly cause the variation of another variable）
### 2.1 Correlation-based methods（基于相关性的方法）
分为两大子类
1. 聚合方法（Aggregated-based）将环境因素和犯罪事件聚合到预定义的分析单元上，然后用回归模型建立关系。需要解决两个问题：
	1. 犯罪事件空间聚集且计数数据零值多 → 使用泊松回归、负二项回归等模型。
	   
	2. 犯罪与环境特征的关系具有空间非平稳性 → 使用空间回归模型（如空间滤波泊松回归、地理加权泊松回归、多尺度地理加权回归等）
2. 离散点方法（Discrete-point-based）：旨在识别与犯罪事件相关的特定设施或设施组合，如使用联合案例配置分析（CACC）和空间共现模式（SCP）挖掘
   
- **核心局限：无法揭示因果关系**，通常导致矛盾结论。例如：有些研究发现交通繁忙的街道更安全，而另一些研究则认为高交通流量会增加犯罪风险

### 2.2 Causality-based methods（基于因果性的方法）
- **趋势**：近年来研究重心从相关性转向因果性，关注街道感知特征和城市设施
- **两大因果推断框架**：
	1. **潜在结果框架（POF）/ Rubin因果模型（RCM）**：
		- 为每个变量设置两个潜在状态（如某设/施存在/不存在），因果效应定义为两个潜在结果之差
		- 常用方法：随机对照实验、差分法（DID）、断点回归、工具变量法
	2. **结构因果模型（SCMs）/ Pearl框架**：
		- 结合结构方程模型（SEM）和有向无环图（DAG）描述因果关系
		- **相比RCM的优势**：更灵活、可解释性更强、能建模复杂系统；通过DAG显式表示因果机制，便于分析多条路径和混杂因素
	- **研究缺口**：尽管SCM已被用于探究绿色空间、街道活动等环境因素对犯罪的因果影响，但**街道感知特征、城市设施与犯罪之间的因果机制尚未被探索**——这正是本文的研究目标
### 2.3 Summary of existing studies
- 当前研究集中与相关性研究，忽略因果性研究
- 存在一部分研究因果关系的，但是主要基于RCM，关注犯罪与单一环境特征之间的潜在因果关系
本研究利用SVIs和POIs，利用SCMs考察了多种类型城市建成环境特征与犯罪之间的因果关系

## 3. 研究方法-Methods
### 3.1 研究区域与数据

- **研究区域**：纽约市曼哈顿区，分为上城（uptown）、中城（midtown）和下城（downtown）三个区域，分析单元为**街道段**（共4249段）
- **四类数据**：
  - **犯罪数据**（2018-2020）：财产犯罪：街道入室盗窃和抢劫-图3
  - **街景图像（SVIs）**：沿路网每100米采样，每点4个方向（0°/90°/180°/270°）计算围合度、开放度、交通流量、可步行性
	- - **街道感知指标**（基于CPTED理论选取了六个指标理论中的几个）：围合感（enclosure）、开放性（openness）、交通流量（traffic flow）、步行性（walkability），通过**FCN-8s语义分割**从SVI中提取
		- 围合感（enclosure）：行人感受到的空间封闭感 → 反映领地性
		- 开放性（openness）：街道环境的隐蔽程度 → 反映监控性
		- 交通流量（traffic flow）：车辆和行人移动量 → 反映活动支持
		- 步行性（walkability）：步行基础设施（道路和人行道）质量 → 反映活动支持
  - **兴趣点（POIs）**：
		空间聚合：与犯罪数据相同，统计每个街道段50米缓冲区内的POI数量
		POI空间分布（Fig. 4）：城市设施主要分布在中城和下城曼哈顿
  - 基于犯罪模式理论分为三类——
    - **犯罪吸引子**（crime attractors）：ATM、银行、酒吧、酒店、夜店等
    - **犯罪生成器**（crime generators）：学校、购物中心、
    - 超市、公园、公交站等
    - **犯罪威慑器**（crime detractors）：警察局等
    
  - **路网数据**

		CPTED理论 → 街道感知指标选择 → SVI语义分割 → 4个感知变量
		犯罪模式理论 → POI分类 → 3类城市设施变量
		犯罪数据 → 50米缓冲区聚合 → 1个犯罪因变量
                    ↓
           8个变量 → FCI因果发现算法 → 因果图 → ACE测量

### 3.2 因果关系发现（Causal Discovery）

#### 一、算法选择：FCI（Fast Causal Inference）

- **全称**：快速因果推断算法（Spirtes et al., 2001）
- **性质**：结构因果模型（SCMs）中的经典**因果发现算法**
- **核心优势**：在推断观测变量之间因果结构的同时，**能够处理潜在未观测混杂因素**（unobserved confounders）——这一点使其优于需要假设所有混杂因素都已被观测的方法

---

#### 二、基本假设

研究假设：**真实的因果关系可以被表示为一个因果图（causal graph）**

---

#### 三、FCI算法的两步流程

##### 第一步：骨架图构建（Skeleton Graph Construction）

1. **初始化**：将图初始化为**完全无向图**（completely undirected graph）
   - **节点**（nodes）= 环境指标变量 + 犯罪事件变量
   - **边**（edges）= 所有可能的连接
2. **条件独立性检验**：对所有节点对执行条件独立性检验，判断两个变量是否独立
3. **移除边**：基于检验结果，**删除独立变量对之间的边**
4. **输出**：无向骨架图（undirected skeleton graph）

##### 第二步：边定向（Edge Orientation）

1. **应用定向规则**：对每条边施加若干定向规则，确定因果关系的方向
2. **重复执行**：直到所有边都被定向

---

#### 四、因果图中边的类型与含义

| 边的类型 | 视觉表示 | 含义 |
|----------|----------|------|
| **有向边**（directed） | X → Y（箭头） | X对Y有因果影响 |
| **双向边**（bidirectional） | X ↔ Y | 双向因果关系，或存在影响两者的隐藏变量 |
| **无向/模糊边**（undirected/ambiguous） | X ○ Y（圆圈） | 因果方向无法确定 |
| **前向箭头** | X → Y | 正因果关系 |
| **后向箭头** | Z ← Y | 负因果关系 |

##### 直接效应 vs 间接效应

| 效应类型 | 定义 | 路径形式 |
|----------|------|----------|
| **直接效应**（direct effect） | 自变量X对因变量Y的影响**不经过**任何中间变量 | X → Y |
| **间接效应**（indirect effect） | 自变量X对因变量Y的影响**通过**中间变量M传递 | X → M → Y |

---

#### 五、核心意义

这部分的核心价值在于：

1. **方法论层面**：用FCI替代传统的相关性分析，从"关联"升级为"因果发现"
2. **处理隐藏混杂**：城市环境中可能存在大量未被测量的因素（如社会经济条件、人类活动模式等），FCI能识别这些隐藏混杂的存在（通过双向边表示）
3. **区分直接/间接效应**：这对于理解城市建成环境如何影响犯罪至关重要——例如后文发现街道感知特征**不直接影响犯罪**，而是通过城市设施**间接影响**，正是FCI算法能够识别的因果路径结构

---

#### 六、算法流程总结

```
完全无向图（所有变量对之间都有边）
        ↓
条件独立性检验（测试所有变量对）
        ↓
删除独立变量对的边 → 无向骨架图
        ↓
应用定向规则 → 确定每条边的因果方向
        ↓
输出因果图（有向边 + 双向边 + 模糊边）
        ↓
区分直接效应 vs 间接效应
```

**简言之**：这一节描述的是如何从数据中"发现"因果结构——不是人为假设因果方向，而是让数据通过FCI算法自动生成因果图，进而为下一步（3.3节）的ACE量化计算提供基础。

- 采用**FCI算法**（Fast Causal Inference）识别环境特征与犯罪之间的因果关系
- FCI是结构因果模型（SCM）中的经典因果发现算法，能**处理潜在未观测混杂因素**
- 两个主要步骤：
  1. **骨架图构建**：对所有变量对进行条件独立性检验，移除独立变量之间的边，得到无向骨架图
  2. **边定向**：应用定向规则确定每条边的因果方向
- 因果图中的边可分为：有向边（因果影响）、双向边（相互影响/隐藏混杂）、无向/模糊边（因果方向不明）

### 3.3 因果效应测量（Causal Effect Measurement）

#### 一、核心概念：平均因果效应（ACE）

##### 定义
- **ACE（Average Causal Effect）**：衡量对自变量进行特定**干预**前后，因变量**期望值的差异**（Pearl et al., 2016）
- 这里的"干预"即SCM中的 **do算子**（do-operator）——人为改变某个变量的值，观察结果变量如何变化

##### ACE的分类

| 类型 | 定义 | 路径形式 |
|------|------|----------|
| **直接因果效应** | 两个节点之间**直接通过边**连接 | X → Y |
| **间接因果效应** | 通过**中间变量**传递影响 | X → M → Y |

---

#### 二、线性系统假设

研究将变量系统视为**线性系统**，需满足两个条件：
1. 内生变量之间存在**线性关系**
2. 所有外生变量**相互独立**且服从**高斯分布**

##### 变量分类

| 变量类型 | 含义 | 示例（Fig. 6） |
|----------|------|----------------|
| **内生变量**（endogenous） | 模型中的显式变量 | W, X, Z, Y |
| **外生变量**（exogenous） | 模型隐含但影响内生变量的变量 | U_W, U_X, U_Z, U_Y |

---

#### 三、路径系数（Path Coefficient）

- 每条**有向边**对应一个**路径系数**，量化两个变量之间的因果关系
- 含义：保持其他变量不变时，原因变量变化1个单位对结果变量的**直接因果效应**
- **ACE的计算规则**：ACE等于因果图中从X到Y的所有**有向路径上路径系数的乘积之和**

---

#### 四、ACE计算公式推导

论文以Fig. 6的简单SCM为例，给出了ACE的具体计算过程：

##### 公式（1）

$$ACE(X \rightarrow Y) = E[Y|do(X=x+1)] - E[Y|do(X=x)] = \beta + \delta\gamma$$

##### 计算步骤

| 步骤      | 操作                    | 说明                      |
| ------- | --------------------- | ----------------------- |
| **步骤1** | 移除所有指向X的有向边，改变X的值     | 这就是"**do算子**"——对变量X进行干预 |
| **步骤2** | 基于因果图和结构方程，建立Y与X之间的方程 | 利用路径关系推导ACE             |

##### 含义解读

- **β**：X → Y 的**直接效应**（X到Y的单条边系数）
- **δγ**：X → Z → Y 的**间接效应**（两条边系数的乘积）
- **ACE = β + δγ**：直接效应 + 间接效应

---

#### 五、路径系数的计算方法：回归识别规则（Regression Rule for Identification）

##### 回归识别规则的定义

给定因果图G和有向边 "X → Y"（路径系数为β）：
- 令G_β为从G中**删除**边 "X → Y" 后得到的新图
- 如果存在一组变量Z满足以下**两个条件**，则β可以通过回归模型计算：

| 条件 | 含义 |
|------|------|
| **条件1** | Z**不包含**Y的任何后代（descendant） |
| **条件2** | Z **d-分离**（d-separate）X和Y，即Z阻断了X和Y之间的所有路径 |

##### 实际计算

当满足上述条件时，路径系数β等于**偏回归系数** γ_X，即通过以下回归方程获得：

$$Y = \gamma_X X + \gamma_Z Z + \varepsilon$$

在Fig. 6的示例中，删除 X → Y 边后，Z满足回归识别规则的两个条件，因此β = γ_X。

---

#### 六、整个方法论的闭环

原文最后一段总结了三个步骤的整体逻辑：

```
步骤1（3.1节）：从SVI和POI中提取城市建成环境特征 → 作为关键变量
        ↓
步骤2（3.2节）：利用SCM发现多变量之间的因果关系 → 生成因果图
        ↓
步骤3（3.3节）：基于回归识别规则定量测量因果效应 → 计算ACE
```

---

#### 七、核心意义

1. **从定性到定量**：3.2节的FCI算法只能告诉我们"谁影响谁"（因果方向），3.3节则回答了"**影响多大**"（因果效应大小）
2. **理论严谨性**：通过do算子确保计算的是真正的**因果效应**而非相关性
3. **可操作性**：回归识别规则使得路径系数可以通过标准**OLS回归**计算，便于实证操作
4. **区分直接与间接**：通过路径系数乘积，能够分离出直接效应和间接效应，这直接支撑了后文"街道感知特征通过城市设施**间接**影响犯罪"这一核心发现

**简言之**：3.3节描述的是"如何量化因果效应"——在FCI算法发现的因果图基础上，利用回归识别规则计算路径系数，进而通过路径系数乘积求和得到ACE，实现对城市建成环境影响犯罪的**定量因果推断**。

## 4. 研究结果-Results


### 一、4.1. Causal relationships between urban built environment and crime incidents

#### 4.1.1. Causal relationships between street perception characteristics and crime incidents（Fig. 7）

**核心发现**：仅考虑街道感知特征与犯罪的因果关系时——

| 发现 | 具体内容 |
|------|----------|
| **无直接因果** | 四个街道感知指标与犯罪事件之间**没有有向边**，即街道感知特征**不直接影响犯罪** |
| **感知指标间的交互** | ① 开放性（openness）→ 交通流量（traffic flow）：**负向**影响；② 开放性 → 围合感（enclosure）：**负向**影响；③ 步行性（walkability）→ 交通流量：**负向**影响；④ 步行性 → 围合感：**正向**影响 |
| **双向边** | 围合感与交通流量之间存在**双向边**，暗示存在未观测的隐藏变量同时影响二者 |

**意义**：揭示了四个感知指标之间存在复杂的交互关系，但它们对犯罪无直接影响，需要通过中介变量（城市设施）传递。

---

#### 4.1.2. Causal relationships between street perception characteristics, urban facilities, and crime incidents（Fig. 8）

这是Results部分的**核心发现**，将城市设施纳入因果图后，按三类设施分别讨论：

##### (a) 犯罪吸引子（Crime Attractors）— Fig. 8(a)

| 因果路径 | 方向 | 含义 |
|----------|------|------|
| 犯罪吸引子 → 犯罪 | **正向** | 犯罪吸引子数量增加会增加犯罪 |
| 开放性 → 犯罪吸引子 | **负向** | 开放性高的地方犯罪吸引子更少 |
| 交通流量 → 犯罪吸引子 | **负向** | 交通流量高的地方犯罪吸引子更少 |

- **间接效应**：开放性和交通流量通过犯罪吸引子**间接负向**影响犯罪
- **开放性 ↔ 交通流量**：存在双向边，暗示隐藏混杂因素

##### (b) 犯罪生成器（Crime Generators）— Fig. 8(b)

| 因果路径 | 方向 | 含义 |
|----------|------|------|
| 犯罪生成器 → 犯罪 | **正向** | 犯罪生成器数量增加会增加犯罪机会 |
| 开放性 → 犯罪生成器 | **正向** | 开放性高的地方犯罪生成器更多 |

- **间接效应**：开放性通过犯罪生成器**间接正向**影响犯罪（"Openness → Crime Generator → Crime"）
- **犯罪吸引子 ↔ 犯罪生成器**：存在双向因果路径，暗示存在隐藏变量连接城市设施和犯罪事件
- **开放性 ↔ 交通流量**：存在双向边

##### (c) 犯罪威慑器（Crime Detractors）— Fig. 8(c)

| 因果路径 | 方向 | 含义 |
|----------|------|------|
| 警察局 → 犯罪 | **无明确因果关系** | 警察局数量与犯罪之间未发现因果效应 |
| 警察局 → 交通流量 | **正向** | 警察局存在增加交通流量 |

- 感知指标之间的交互：开放性负向影响围合感和交通流量；围合感正向影响交通流量；步行性正向影响围合感但负向影响交通流量

---

#### 4.1 核心发现总结

| 发现 | 具体内容 |
|------|----------|
| 街道感知特征 | **不直接影响**犯罪，而是通过城市设施**间接影响** |
| 犯罪吸引子和生成器 | 对犯罪有**正向**因果影响 |
| 犯罪威慑器（警察局） | 与犯罪**无明确因果关系** |
| 开放性 | 对不同类型设施的影响**方向相反**（负向影响吸引子，正向影响生成器） |

---

### 二、4.2. Causal effects of urban built environment on crime incidents

##### 计算前提

- 假设变量之间存在**线性关系**
- 利用**回归识别规则**（regression rule for identification）计算路径系数
- 路径系数乘积求和得到**平均因果效应（ACE）**

#### ACE量化结果（Table 3）

| 因果路径 | ACE值 | 含义 |
|----------|-------|------|
| 犯罪吸引子 → 犯罪 | **≈1.53** | 每增加1个犯罪吸引子，预计增加约1.53起犯罪事件 |
| 开放性 ↑10% → 犯罪（经由犯罪吸引子） | **-0.6** | 开放性增加10%，犯罪减少约0.6起 |
| 交通流量 ↑10% → 犯罪（经由犯罪吸引子） | **-0.38** | 交通流量增加10%，犯罪减少约0.38起 |
| 犯罪生成器 → 犯罪 | **≈1.62** | 每增加1个犯罪生成器，预计增加约1.62起犯罪事件 |
| 开放性 ↑10% → 犯罪（经由犯罪生成器） | **+0.11** | 开放性增加10%，犯罪增加约0.11起 |

#### 关键解读

| 要点 | 解读 |
|------|------|
| **犯罪生成器ACE > 犯罪吸引子ACE** | 犯罪生成器（1.62）的平均因果效应大于犯罪吸引子（1.53），原因：犯罪吸引子更容易吸引**警力部署和预防措施**，抵消部分犯罪效应 |
| **开放性的双重效应** | 对犯罪吸引子路径：开放性**降低**犯罪（增强监控 → 提高犯罪者被发现风险）；对犯罪生成器路径：开放性**增加**犯罪（吸引更多人流 → 增加潜在受害者和犯罪机会） |
| **交通流量的负向效应** | 通过犯罪吸引子路径：更多人流 → 更多"自然监控" → 犯罪减少 |

---

### 三、Results部分整体逻辑

```
4.1 因果发现（FCI算法 → 因果图）
    ├── 街道感知特征与犯罪：无直接因果边
    ├── 街道感知特征 + 犯罪吸引子 + 犯罪：存在间接路径
    ├── 街道感知特征 + 犯罪生成器 + 犯罪：存在间接路径
    └── 街道感知特征 + 犯罪威慑器 + 犯罪：无明确因果
                ↓
4.2 因果效应量化（ACE计算）
    ├── 犯罪吸引子 ACE ≈ 1.53
    ├── 犯罪生成器 ACE ≈ 1.62
    └── 开放性具有双重间接效应（方向相反）
```

**一句话总结**：Results部分的核心贡献是**两层递进发现**——第一层（4.1）证明街道感知特征不直接影响犯罪，而是通过城市设施间接影响；第二层（4.2）量化了间接效应的具体大小，并揭示了开放性对不同类型设施的**方向相反的双重效应**。
## 5. 讨论-Discussion
本文的核心贡献——证明了城市建成环境（尤其是街道感知特征）通过城市设施间接影响犯罪，且这种间接效应的方向和大小因设施类型而异，为城市犯罪预防提供了从"相关性"到"因果性"的实证依据和政策工具。
