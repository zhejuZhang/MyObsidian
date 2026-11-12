
**解决什么问题:** 识别城市建成环境与犯罪之间的因果关系
**解决问题思路:** 利用两种新的城市大数据形式——街景图像和兴趣点,通过结构因果模型考察城市建成环境与犯罪之间的 因果关系


**结论:** 街道感知特征不会直接影响犯罪,而是通过城市 设施间接产生影响 & 街道感知特征对犯罪的影响取决于所涉及的城市设施类型
**重要语句:** 
**缺点:** 
**启发:** 

- 阅读日期：2026年11月12日
- 书目信息：He, Z., Meng, W., Yao, J., Gong, Y., Wu, L. and Tao, L. (2026) ‘Measuring the causal effect of urban environments on crime with street view images and points of interest’, *Cities*, 168, 106399. [DOI 与出版入口](https://doi.org/10.1016/j.cities.2025.106399)。
- 已读范围：全文
- 作者的研究问题：Using two new forms of urban big data, the street view images and points of interest, this research examines the causal relationship between urban built environment and crime with structural causal models.
- 数据、地点、时期：
	- crime incidents, road networks, SVIs and POIs
	![[Pasted image 20261112133837.png]]
	- Manhattan, New York City.
	- 2018-2020

- 方法与关键假设：
	- **方法:**
		- 使用SCMs推导涉及环境特征 (即城市设施和街道感知特征)与犯罪相关的因果图。最后,通过回归 模型和识别回归规则
		- The research framework, presented in Fig. 1, consists of three steps. First, the urban built environment was quantified based on POIs and SVIs. Second, the casual graphs involving environmental characteristics (i.e., the urban facilities and street perception characteristics) and crime were derived using SCMs. Finally, the average casual effects were estimated by regression model and regression rule for identification
		- 
		- 语义分割从SVIs中提取元素
		- 用FCN-8从提取建成环境特征
		- 快速因果推理(FCI)算法来识别环境特征与犯罪发生之间的因果关系
			- FCN是SCMs中的一个经典模型
			- FCI 算法包括两个主要步骤:骨架图构建和边定向。
	- 
	- **关键假设:**
		- 假设环境特征之间存在线性关系,且所有选定的变量形成一个线性 系统,那么城市建成环境对犯罪的影响可以进一步进行定量测量。在本 研究中,仅测量了环境特征对犯罪的影响。

- 主要发现或概念贡献：
	- 本研究的结果揭示了连 接特定建成环境特征与犯罪的(直接和间接)影响路径。
		- 街道感知特征并不直接影响犯罪,而是通过其与城市设施的相互作用间接 影响犯罪(图8)。例如,路径 “开放度 (O) → 犯罪生成器 (G) →犯罪 (C)” 说明了开放度通过犯罪生成器对犯罪的间接影响。
		- 这一发现表明, 城市设施在塑造犯罪动态方面比街道感知特征发挥着更重要的作用.
		- 
		- 直接:
			- 城市设施主要 反映了居民的日常活动,为潜在作案者和受害者创造了相遇的机会—这是犯罪机会的基本条件。
		- 间接:
			- 街道感知特征与环境监护联系更 紧密,表明了不同的被发现的风险。因此,街道感知特征可能间接放大 或减少与城市设施相关的犯罪风险(何等人,2022)。因此,街道感知 特征(例如,开放度)通过城市设施间接影响犯罪风险。
	- 街道感知特征对犯罪的影响因城市设施的类型而异
		- 开放度对监视的 积极影响可能被其促进行人流量增加的作用所抵消,从而导致犯罪案件增加。
	- 
	- 研究成果对城市设计和犯罪预防实践具有启示意义。
		- 首先,发现的 因果图能更好地揭示多种环境特征对犯罪的影响路径。发现的因果路径 有助于通过周密有效的设计来降低犯罪风险,从而减少直接因果因素的 影响。例如,通过了解城市设施在塑造犯罪动态中扮演更重要的角色, 我们可以在设计城市建成环境时,更侧重调整城市设施的布局(如犯罪 吸引点和犯罪生成点),以实现犯罪减少。其次,因果效应定量反映了 特定环境特征所关联的实际犯罪风险。通过识别高犯罪风险区域,如本 研究中的犯罪生成点(例如学校和超市),我们可以策略性地部署增强 型犯罪监视设备(例如高精度摄像头)并增加警力巡逻,以降低潜在犯 罪风险

- 作者自己承认的限制：
	1. 首先,它仅关注物理城市建成环境, 由SVIs和POIs表示,而没有考虑其他影响因素。事实上,城市建成环境 与犯罪之间存在复杂的相互作用。犯罪可能受到各种因素的影响,包括 建成环境特征、自然环境条件、社会经济条件,甚至人类行为因素。未来,我们旨在开发额外的指标来表征城市环境。
	2. 其次,本研究将盗窃和抢劫归类为财产犯罪进行调查。然而,不同类型的犯罪事件实际上可能 具有不同的潜在影响因素。在未来的研究中,我们将对每种具体的犯罪 类型进行更详细的分析。
	3. 最后, ACE衡量的是城市建成环境对犯罪在整个研究区域内的平均影响,忽略了城市建成环境与犯罪之间因果关系中的空间异质性。未来,我们将探 索城市建成环境对犯罪因果效应的空间异质性。

- 我需要检验的问题：
- 能支持的论断与原文位置：
- 不能支持的论断或适用边界：
- 与另一篇文献的共识、差异或互补：













