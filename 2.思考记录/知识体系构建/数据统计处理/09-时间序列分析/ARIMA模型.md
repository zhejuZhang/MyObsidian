# ARIMA模型

> 自回归积分移动平均模型，是时间序列预测的经典方法。

---

## 模型组成

### AR（自回归）

$$Y_t = c + \phi_1 Y_{t-1} + \phi_2 Y_{t-2} + \cdots + \phi_p Y_{t-p} + \varepsilon_t$$

- p：AR的阶数
- $\phi_i$：自回归系数
- 当前值依赖于过去p个值

### MA（移动平均）

$$Y_t = c + \varepsilon_t + \theta_1 \varepsilon_{t-1} + \theta_2 \varepsilon_{t-2} + \cdots + \theta_q \varepsilon_{t-q}$$

- q：MA的阶数
- $\theta_i$：移动平均系数
- 当前值依赖于过去q个误差

### I（积分/差分）

使非平稳数据变平稳的差分次数d。

---

## ARIMA(p,d,q)模型

$$\Delta^d Y_t = c + \phi_1 \Delta^d Y_{t-1} + \cdots + \phi_p \Delta^d Y_{t-p} + \varepsilon_t + \theta_1 \varepsilon_{t-1} + \cdots + \theta_q \varepsilon_{t-q}$$

### 特殊情况

| 模型 | 描述 |
|------|------|
| AR(1) | p=1, d=0, q=0 |
| MA(1) | p=0, d=0, q=1 |
| ARMA(1,1) | p=1, d=0, q=1 |
| 随机游走 | ARIMA(0,1,0) |

---

## Box-Jenkins方法

### 步骤

```
1. 识别（Identification）
   ├── 绘制时间图
   ├── ACF和PACF图
   └── 确定p, d, q
        │
2. 估计（Estimation）
   ├── 最大似然估计
   └── 最小二乘估计
        │
3. 诊断（Diagnostic）
   ├── 残差分析
   ├── Ljung-Box检验
   └── ACF/PACF检验
        │
4. 预测（Forecasting）
   └── 生成预测和置信区间
```

---

## 模型识别

### ACF和PACF的模式

| 模型 | ACF | PACF |
|------|-----|------|
| AR(p) | 拖尾（指数衰减） | p阶截尾 |
| MA(q) | q阶截尾 | 拖尾 |
| ARMA(p,q) | 拖尾 | 拖尾 |

### 差分次数d

- 观察时间图：有趋势 → 需要差分
- ACF缓慢衰减 → 需要差分
- ADF检验：非平稳 → 需要差分

---

## 季节性ARIMA

### SARIMA(p,d,q)(P,D,Q,s)

- (p,d,q)：非季节性部分
- (P,D,Q,s)：季节性部分
- s：季节周期（如月度数据s=12）

### 季节性成分

$$\Phi_P(B^s)\phi_p(B)(1-B^s)^D(1-B)^d Y_t = \Theta_Q(B^s)\theta_q(B)\varepsilon_t$$

---

## 模型诊断

### 残差检验

| 检验 | 目的 |
|------|------|
| Ljung-Box | 残差无自相关 |
| ACF图 | 残差无模式 |
| Q-Q图 | 残差正态性 |

### 信息准则

| 准则 | 公式 | 特点 |
|------|------|------|
| AIC | $-2\ln L + 2k$ | 常用 |
| BIC | $-2\ln L + k\ln n$ | 更保守 |
| AICc | AIC + 校正项 | 小样本 |

---

## 预测

### 点预测

$$\hat{Y}_{T+h|T} = E[Y_{T+h} | Y_1, \ldots, Y_T]$$

### 预测区间

$$\hat{Y}_{T+h|T} \pm z_{\alpha/2} \cdot \sigma_h$$

预测区间随预测步长增大而变宽。

---

## ARIMA的扩展

| 模型 | 特点 |
|------|------|
| ARIMAX | 包含外生变量 |
| GARCH | 条件异方差 |
| VAR | 多变量时间序列 |
| 状态空间模型 | 更灵活的框架 |

---

## 相关概念

- [[时间序列基础]] — 基本概念
- [[平稳性与差分]] — 平稳性检验和处理
- [[预测与评估]] — 预测方法和评估

---

## 常见误区

1. **不检验残差**：残差应近似白噪声
2. **过度差分**：差分过多会引入不必要的相关性
3. **忽视季节性**：季节性数据需要季节性模型
4. **样本外预测过度自信**：预测区间应考虑不确定性
