## 论文信息

标题：Spatial heterogeneity of forest carbon stocks in the Xiangjiang river Basin urban agglomeration: analysis and assessment based on the multiscale geographically weighted regression (MGWR) model

作者：Yingfeng Kuang, Xiaolong Chen

期刊：Frontiers in Environmental Science (Q1, IF ~3.7)

年份：2025

DOI：https://doi.org/10.3389/fenvs.2025.1573438

引用量：7

key：MGWR, Spatial heterogeneity, Forest carbon stocks, Geographically weighted regression, Urban agglomeration

## 研究问题

- 解决什么问题：What
    - 湘江流域城市群森林碳储量的空间异质性分析
    - 传统 OLS 模型无法捕捉森林碳储量在不同空间位置的异质性关系
    - 需要一种更可靠的方法来准确估计大尺度森林碳储量的空间分布

- 解决问题思路：
    - 基于湖南省第 10 次连续森林资源清查数据和气候数据
    - 筛选 5 个关键变量：平均胸径、林分密度、平均林龄、平均树高、年均降水量
    - 构建 OLS 模型和 4 种 GWR 模型（GWR-Gaussian、GWR-Bi-square、MGWR-Gaussian、MGWR-Bi-square）
    - 通过模型拟合和独立样本检验比较，选择最优模型

- 核心创新：Innovation
    - 首次将 MGWR 模型应用于湘江流域城市群森林碳储量空间分布估计
    - 系统比较了 OLS、GWR、MGWR 三类模型的性能
    - MGWR 模型允许不同变量有不同的带宽，更好地捕捉多尺度空间异质性
    - 揭示了森林碳储量"东高西低、南高北低"的空间分布格局

- 结论：Conclusion
    - 4 种 GWR 模型均优于 OLS 模型（RSS 更小、R² 更大、AIC 更低）
    - MGWR (Gaussian) 模型拟合效果最优：RSS 减少 25927.06，R² 提高 0.113，AIC 降低 76.4
    - GWR (Gaussian) 模型独立样本检验最优：RMSE 降低 1.95，MAE 降低 1.09
    - 森林碳储量呈现显著的空间非平稳性
    - 5 个变量在不同空间位置对碳储量的影响程度和方向不同

- 重要语句：Quote
    - "The MGWR model better captures the spatial heterogeneity of variables"
    - "The four GWR models outperform the OLS model in terms of model fit and independent samples test"

- 缺点：Limitation
    - 仅使用一期截面数据，未考虑时间维度
    - 未纳入土地利用变化、城市化等社会经济变量
    - 样本量（431 个样地）相对有限
    - 未讨论模型的空间预测不确定性

- 启发：Inspiration
    - MGWR 相比 GWR 的优势在于允许不同变量有不同的空间尺度
    - 空间异质性分析需要选择合适的空间回归模型
    - 森林碳储量的空间分布受多种因素共同影响

- 与我的研究关系：relationship
    - MGWR 是空间异质性分析的先进方法，可推广到其他空间分析场景
    - 模型比较框架（OLS vs GWR vs MGWR）可借鉴
    - 空间非平稳性检验方法对空间数据建模有指导意义
