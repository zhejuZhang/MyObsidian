# Python统计分析

> Python是通用编程语言，在数据科学领域日益流行。

---

## Python的优势

| 优势 | 描述 |
|------|------|
| 通用语言 | 可用于各种任务 |
| 生态丰富 | 大量库 |
| 易于部署 | 生产环境友好 |
| 机器学习 | scikit-learn, TensorFlow |
| 大数据 | PySpark, Dask |

---

## 核心库

| 库 | 用途 |
|------|------|
| NumPy | 数值计算 |
| Pandas | 数据处理 |
| SciPy | 科学计算 |
| Statsmodels | 统计模型 |
| Scikit-learn | 机器学习 |
| Matplotlib | 基础可视化 |
| Seaborn | 统计可视化 |
| Plotly | 交互可视化 |

---

## 数据处理

### Pandas

```python
import pandas as pd

# 读取数据
df = pd.read_csv("data.csv")
df = pd.read_excel("data.xlsx")

# 基本操作
df.head()
df.info()
df.describe()

# 数据处理
df[df['age'] > 18]
df[['name', 'age']]
df.assign(income_k=df['income'] / 1000)
df.groupby('gender')['income'].mean()
```

### 数据清洗

```python
# 缺失值
df.isnull().sum()
df.fillna(df.mean())
df.dropna()

# 重复值
df.duplicated().sum()
df.drop_duplicates()

# 异常值
Q1 = df['value'].quantile(0.25)
Q3 = df['value'].quantile(0.75)
IQR = Q3 - Q1
df[(df['value'] >= Q1-1.5*IQR) & (df['value'] <= Q3+1.5*IQR)]
```

---

## 描述性统计

```python
import numpy as np
from scipy import stats

# 基本统计量
np.mean(x)
np.median(x)
np.std(x)
np.var(x)

# 分布统计
stats.describe(x)
stats.skew(x)  # 偏度
stats.kurtosis(x)  # 峰度

# 相关系数
np.corrcoef(x, y)
df.corr()
```

---

## 假设检验

```python
from scipy import stats

# t检验
stats.ttest_1samp(x, popmean=0)  # 单样本
stats.ttest_ind(x, y)  # 独立样本
stats.ttest_rel(x, y)  # 配对样本

# 方差分析
stats.f_oneway(group1, group2, group3)

# 卡方检验
stats.chi2_contingency(table)

# 非参数检验
stats.mannwhitneyu(x, y)  # Mann-Whitney
stats.kruskal(group1, group2, group3)  # Kruskal-Wallis
stats.wilcoxon(x, y)  # Wilcoxon
```

---

## 回归分析

### Statsmodels

```python
import statsmodels.api as sm

# 线性回归
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
print(model.summary())
predictions = model.predict(X_new)

# 逻辑回归
model = sm.Logit(y, X).fit()
print(model.summary())
```

### Scikit-learn

```python
from sklearn.linear_model import LinearRegression, LogisticRegression

# 线性回归
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

# 逻辑回归
model = LogisticRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

---

## 可视化

### Matplotlib

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.scatter(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot')
plt.show()
```

### Seaborn

```python
import seaborn as sns

# 散点图
sns.scatterplot(data=df, x='x', y='y', hue='group')

# 直方图
sns.histplot(data=df, x='value', kde=True)

# 箱线图
sns.boxplot(data=df, x='group', y='value')

# 相关热力图
sns.heatmap(df.corr(), annot=True)
```

---

## 机器学习

### Scikit-learn

```python
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# 数据准备
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 标准化
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 建模
model = RandomForestClassifier()
model.fit(X_train_scaled, y_train)

# 评估
predictions = model.predict(X_test_scaled)
accuracy_score(y_test, predictions)
cross_val_score(model, X, y, cv=5)
```

---

## Python vs R

| 维度 | Python | R |
|------|--------|---|
| 统计分析 | ✓ | ✓ 更强 |
| 机器学习 | ✓ 更强 | ✓ |
| 深度学习 | ✓ 更强 | 弱 |
| 可视化 | ✓ | ✓ 更强 |
| 数据处理 | ✓ | ✓ |
| 生产部署 | ✓ 更强 | 弱 |
| 学习曲线 | 低 | 中 |

---

## 相关概念

- [[R语言统计分析]] — R的统计分析
- [[其他统计软件]] — 其他工具

---

## 常见误区

1. **不用向量化**：NumPy的向量化比循环快
2. **不用管道**：应使用方法链或pipe
3. **忽视文档**：库的文档很详细
4. **不管理环境**：应使用venv或conda
