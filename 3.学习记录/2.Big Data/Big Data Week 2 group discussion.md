### 1. What questions could you answer with this dataset?
**你可以使用此数据集回答什么问题？**
- **Identifying active travel hotspots and planning infrastructure (识别慢行交通热点与规划基础设施):**
    - **English:** Utilizing the hourly count of users at street level, we can precisely identify the most popular cycling and running routes. This provides empirical evidence for municipal departments to plan, optimize, or expand cycle lanes and greenways.
    - **中文:** 利用街道级别的每小时用户计数，我们可以精确识别最受欢迎的骑行和跑步路线。这为市政部门规划、优化或扩建自行车道和绿道提供了实证依据。
- **Analysing network efficiency and traffic bottlenecks (分析路网效率与交通瓶颈):**
    - **English:** By analysing the "wait times at intersections" data, we can evaluate which traffic lights or junctions cause the most significant delays for non-motorized transport. This helps in optimizing traffic signal timings for cyclists.
    - **中文:** 通过分析“路口等待时间”数据，我们可以评估哪些红绿灯或交叉路口对非机动车造成的延误最严重。这有助于为骑行者优化交通信号灯配时。
- **Understanding commuting patterns and spatial connectivity (理解通勤模式与空间连通性):**
    - **English:** The Origin/Destination (O/D) data, resolved to census output areas, allows us to analyse commuting corridors during peak hours. It reveals the strength of "active travel" connections between specific residential areas and commercial zones.
    - **中文:** 精确到人口普查输出区的起讫点 (O/D) 数据，使我们能够分析高峰时段的通勤走廊。它揭示了特定居住区与商业区之间“主动出行”联系的紧密程度。
- **Longitudinal evaluation of infrastructure investments (基础设施投资的纵向评估):**
    - **English:** Given the longitudinal nature of the data (e.g., Glasgow 2013-2020), we can conduct "before and after" studies to evaluate the effectiveness of new cycling infrastructure investments by comparing traffic volumes over time.
    - **中文:** 鉴于数据的纵向特征（例如格拉斯哥 2013-2020 年的数据），我们可以通过对比不同时期的交通量，进行“前后对比”研究，从而评估新建骑行基础设施投资的有效性。
### 2. Are there other questions that would require traditional forms of data (Survey/Census)?
**是否有其他问题需要依赖传统形式的数据（调查/人口普查）？**
- **Understanding "Who" is cycling - Addressing Representativeness Bias (了解“谁”在骑行——解决代表性偏差问题):**
    
    - **English:** Strava data suffers from significant representativeness bias. It primarily captures a specific demographic (often younger, fitter, or tech-savvy individuals) and misses populations like the elderly, children, or lower-income commuters. To understand the true socio-economic profile (age, gender, income) of cyclists, we _must_ rely on traditional Census or household survey data.
        
    - **中文:** Strava 数据存在严重的代表性偏差。它主要捕捉特定人群（通常是更年轻、更健康或精通技术的人），而遗漏了老年人、儿童或低收入通勤者等群体。为了了解骑行者真实的社会经济特征（年龄、性别、收入），我们_必须_依赖传统的人口普查或家庭调查数据。
        
- **Investigating "Why" people don't cycle - Capturing Motivations and Barriers (调查人们“为什么”不骑行——捕捉动机和障碍):**
    
    - **English:** Big data like Strava only shows "revealed behaviour" (those who already cycle). It cannot tell us why people in a specific neighbourhood _choose not to_ cycle (e.g., safety concerns, lack of bike storage, or affordability). To capture these subjective motivations and barriers, traditional qualitative or quantitative survey methods are essential.
        
    - **中文:** 像 Strava 这样的大数据只显示“已发生的行为”（那些已经骑行的人）。它无法告诉我们为什么特定社区的人们_选择不_骑行（例如，安全担忧、缺乏自行车存放处或负担不起）。为了捕捉这些主观的动机和障碍，传统的定性或定量调查方法是必不可少的。
        
- **Calculating accurate Mode Share (计算准确的交通出行分担率):**
    
    - **English:** Strava data only provides absolute counts of its active users. It cannot reveal what proportion "cycling" represents within the overall transport mix of a city (compared to driving or public transit). Calculating macroscopic mode share requires representative traditional travel surveys (like a National Travel Survey).
        
    - **中文:** Strava 数据仅提供其活跃用户的绝对数量。它无法揭示“骑行”在城市整体交通结构中所占的比例（与开车或公共交通相比）。计算宏观的交通出行分担率需要具有代表性的传统旅行调查（如国家旅行调查）。




### 1. What questions could you answer with this dataset?

**你们可以用这个数据集回答什么问题？（大数据的优势）**

你可以从**路网效率**和**城市慢行交通规划**的角度切入：

- **Identifying traffic bottlenecks and assessing intersection efficiency (识别交通瓶颈与评估路口效率):**
    
    - **English:** Utilizing the unique data field "wait times at intersections," we can pinpoint exactly which traffic lights or junctions cause the most significant delays for cyclists and runners. This provides empirical evidence to optimize traffic signal timings and improve active travel infrastructure.
        
    - **中文:** 利用“路口等待时间”这一独特字段，我们可以精准定位哪些红绿灯或交叉路口对骑行者和跑步者造成了最严重的延误。这为优化交通信号灯配时、改善慢行交通基础设施提供了实证依据。
        
- **Analysing commuting corridors and spatial connectivity (分析通勤走廊与空间连通性):**
    
    - **English:** With the Origin/Destination (O/D) data resolved to census output areas, we can trace macro-level commuting corridors during peak hours. This reveals the actual travel demand and spatial connectivity between specific residential zones and employment centres.
        
    - **中文:** 借助解析到人口普查输出区级别的起讫点 (O/D) 数据，我们能够追踪高峰时段宏观的通勤走廊。这揭示了特定居住区与就业中心之间真实的出行需求和空间连通性。
        
- **Evaluating infrastructure investments longitudinally (纵向评估基础设施投资效果):**
    
    - **English:** Given the long temporal extent of the data (e.g., Glasgow 2013-2020), we can conduct longitudinal "before-and-after" studies. For instance, evaluating how the construction of a new cycle lane has changed local cycling volumes over several years.
        
    - **中文:** 鉴于数据具有较长的时间跨度（如格拉斯哥 2013-2020 年数据），我们可以进行纵向的“前后对比”研究。例如，评估一条新建自行车道的落成在几年内如何改变了当地的骑行流量。
        

### 2. Are there other questions that would require traditional forms of data?

**有哪些问题需要依赖传统形式的数据（如问卷调查/人口普查）？（大数据的局限性）**

这是 Nick Bailey 教授本周理论课的核心考点，一定要抛出 **“代表性偏差 (Representativeness bias)”** 这个学术概念！

- **Understanding "Who" is missing – Addressing representativeness bias (了解“谁”被遗漏了——解决代表性偏差):**
    
    - **English:** Strava data suffers from severe representativeness bias. It primarily captures younger, fitter, tech-savvy demographics, systematically excluding the elderly, low-income groups, or children cycling to school. To understand the true socio-demographic profile of active travellers, we _must_ rely on traditional Census or household survey data.
        
    - **中文:** Strava 数据存在严重的代表性偏差。它主要捕捉到了年轻、体能较好、精通技术的人群，而系统性地排除了老年人、低收入群体或骑车上学的儿童。为了了解慢行交通者真实的社会人口学特征，我们_必须_依赖传统的人口普查或家庭调查数据。
        
- **Investigating "Why" people don't cycle – Capturing hidden barriers (调查人们“为什么”不骑行——捕捉隐形障碍):**
    
    - **English:** Big data like Strava only captures "revealed behaviour" (those already cycling). It is completely blind to the motivations of non-cyclists. If we want to know _why_ people in a deprived neighbourhood choose not to cycle (e.g., perceived danger, lack of bike storage, or affordability), we must use traditional qualitative interviews or quantitative survey methods.
        
    - **中文:** 像 Strava 这样的大数据只捕捉到了“已发生的行为”（那些已经在骑行的人）。它对非骑行者的动机一无所知。如果我们想知道_为什么_某个贫困社区的人们选择不骑行（例如，觉得危险、缺乏自行车停放处或经济负担不起），我们必须使用传统的定性访谈或定量问卷调查方法。
        
- **Calculating objective mode share (计算客观的交通出行分担率):**
    
    - **English:** Strava only gives us absolute counts of its active users, but it cannot tell us what proportion "cycling" represents out of all daily trips in Glasgow (compared to driving, buses, or walking). Calculating an accurate mode share requires representative traditional travel surveys (e.g., the National Travel Survey).
        
    - **中文:** Strava 只能为我们提供其活跃用户的绝对计数，但它无法告诉我们“骑行”在格拉斯哥所有日常出行中所占的比例（相较于开车、乘坐公交或步行）。计算准确的交通出行分担率需要具有代表性的传统出行调查（如国家出行调查）。