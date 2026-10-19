# Python 科研工具使用教程

## 一、环境搭建

### 1.1 安装 Python
```bash
# 推荐使用 Miniconda
# 下载：https://docs.conda.io/en/latest/miniconda.html

# 或使用 pyenv
curl https://pyenv.run | bash
pyenv install 3.11.0
pyenv global 3.11.0
```

### 1.2 创建虚拟环境
```bash
# 使用 conda
conda create -n research python=3.11
conda activate research

# 或使用 venv
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

### 1.3 安装核心包
```bash
# 数据处理
pip install numpy pandas scipy

# 可视化
pip install matplotlib seaborn plotly

# 机器学习
pip install scikit-learn xgboost lightgbm

# 深度学习
pip install torch torchvision torchaudio
pip install transformers datasets

# 统计分析
pip install statsmodels pingouin

# 工具
pip install jupyter notebook ipython tqdm rich
```

### 1.4 requirements.txt
```txt
numpy>=1.24.0
pandas>=2.0.0
scipy>=1.10.0
matplotlib>=3.7.0
seaborn>=0.12.0
plotly>=5.13.0
scikit-learn>=1.2.0
xgboost>=1.7.0
lightgbm>=3.3.0
torch>=2.0.0
transformers>=4.30.0
statsmodels>=0.14.0
pingouin>=0.5.3
jupyter>=1.0.0
tqdm>=4.65.0
rich>=13.0.0
```

```bash
pip install -r requirements.txt
```

---

## 二、数据分析基础

### 2.1 Pandas 常用操作

```python
import pandas as pd
import numpy as np

# 读取数据
df = pd.read_csv('data.csv')
df = pd.read_excel('data.xlsx')
df = pd.read_json('data.json')

# 查看数据
df.head()           # 前5行
df.tail()           # 后5行
df.info()           # 数据类型和缺失值
df.describe()       # 统计摘要
df.shape            # 维度
df.columns          # 列名
df.dtypes           # 数据类型

# 数据选择
df['column']              # 选择列
df[['col1', 'col2']]     # 选择多列
df.iloc[0:10]             # 按行号选择
df.loc[0:10, 'col1':'col3']  # 按标签选择
df[df['col'] > 0.5]      # 条件筛选

# 数据清洗
df.dropna()                    # 删除缺失值
df.fillna(0)                   # 填充缺失值
df.fillna(method='ffill')     # 前向填充
df.drop_duplicates()          # 去重
df.drop(columns=['col'])      # 删除列

# 数据变换
df['new_col'] = df['col1'] + df['col2']  # 新列
df['col'] = np.log(df['col'] + 1)        # 对数变换
df['col'] = (df['col'] - df['col'].mean()) / df['col'].std()  # 标准化

# 聚合
df.groupby('category').agg({
    'value': ['mean', 'std', 'count']
})

# 数据透视表
pd.pivot_table(
    df, 
    values='value', 
    index='group', 
    columns='condition',
    aggfunc='mean'
)

# 合并
pd.merge(df1, df2, on='id', how='left')
pd.concat([df1, df2], axis=0)

# 导出
df.to_csv('output.csv', index=False)
df.to_excel('output.xlsx', index=False)
```

### 2.2 NumPy 常用操作

```python
import numpy as np

# 创建数组
arr = np.array([1, 2, 3, 4, 5])
arr = np.zeros((3, 4))
arr = np.ones((3, 4))
arr = np.random.randn(100, 10)
arr = np.arange(0, 100, 1)
arr = np.linspace(0, 1, 50)

# 数组操作
arr.shape           # 形状
arr.reshape(5, 20)  # 重塑
arr.T               # 转置
arr.flatten()       # 展平

# 数学运算
np.mean(arr)
np.std(arr)
np.sum(arr)
np.max(arr)
np.min(arr)
np.median(arr)
np.percentile(arr, [25, 50, 75])

# 线性代数
np.dot(A, B)        # 矩阵乘法
np.linalg.inv(A)    # 逆矩阵
np.linalg.eig(A)    # 特征值分解
np.linalg.svd(A)    # 奇异值分解
```

---

## 三、统计分析

### 3.1 假设检验

```python
from scipy import stats
import numpy as np

# 正态性检验
stat, p_value = stats.shapiro(data)
print(f"Shapiro-Wilk: stat={stat:.4f}, p={p_value:.4f}")

# 方差齐性检验
stat, p_value = stats.levene(group1, group2, group3)
print(f"Levene: stat={stat:.4f}, p={p_value:.4f}")

# t检验
# 独立样本t检验
t_stat, p_value = stats.ttest_ind(group1, group2)
print(f"Independent t-test: t={t_stat:.4f}, p={p_value:.4f}")

# 配对样本t检验
t_stat, p_value = stats.ttest_rel(before, after)
print(f"Paired t-test: t={t_stat:.4f}, p={p_value:.4f}")

# 单样本t检验
t_stat, p_value = stats.ttest_1samp(data, popmean=0)
print(f"One-sample t-test: t={t_stat:.4f}, p={p_value:.4f}")

# 方差分析 (ANOVA)
f_stat, p_value = stats.f_oneway(group1, group2, group3)
print(f"ANOVA: F={f_stat:.4f}, p={p_value:.4f}")

# 非参数检验
# Mann-Whitney U检验
u_stat, p_value = stats.mannwhitneyu(group1, group2)
print(f"Mann-Whitney U: U={u_stat:.4f}, p={p_value:.4f}")

# Kruskal-Wallis检验
h_stat, p_value = stats.kruskal(group1, group2, group3)
print(f"Kruskal-Wallis: H={h_stat:.4f}, p={p_value:.4f}")

# 卡方检验
chi2, p_value, dof, expected = stats.chi2_contingency(contingency_table)
print(f"Chi-square: chi2={chi2:.4f}, p={p_value:.4f}")
```

### 3.2 效应量计算

```python
import numpy as np
from scipy import stats

def cohens_d(group1, group2):
    """计算 Cohen's d 效应量"""
    n1, n2 = len(group1), len(group2)
    var1, var2 = np.var(group1, ddof=1), np.var(group2, ddof=1)
    pooled_std = np.sqrt(((n1-1)*var1 + (n2-1)*var2) / (n1+n2-2))
    return (np.mean(group1) - np.mean(group2)) / pooled_std

def eta_squared(f_stat, df_between, df_total):
    """计算 Eta-squared (ANOVA 效应量)"""
    return (f_stat * df_between) / (f_stat * df_between + df_total - df_between)

# 使用
d = cohens_d(group1, group2)
print(f"Cohen's d: {d:.4f}")

# 效应量解释
# d < 0.2: 极小效应
# 0.2 <= d < 0.5: 小效应
# 0.5 <= d < 0.8: 中等效应
# d >= 0.8: 大效应
```

### 3.3 样本量计算

```python
from scipy.stats import norm
import numpy as np

def sample_size_ttest(d, alpha=0.05, power=0.80):
    """计算两独立样本t检验所需样本量
    
    Args:
        d: Cohen's d 效应量
        alpha: 显著性水平
        power: 统计功效 (1-β)
    
    Returns:
        每组所需样本量
    """
    z_alpha = norm.ppf(1 - alpha/2)
    z_beta = norm.ppf(power)
    n = 2 * ((z_alpha + z_beta) / d) ** 2
    return int(np.ceil(n))

def sample_size_correlation(r, alpha=0.05, power=0.80):
    """计算相关系数检验所需样本量
    
    Args:
        r: 预期相关系数
        alpha: 显著性水平
        power: 统计功效
    
    Returns:
        所需样本量
    """
    z_alpha = norm.ppf(1 - alpha/2)
    z_beta = norm.ppf(power)
    z_r = 0.5 * np.log((1+r)/(1-r))  # Fisher's z变换
    n = ((z_alpha + z_beta) / z_r) ** 2 + 3
    return int(np.ceil(n))

# 使用
n = sample_size_ttest(d=0.5)
print(f"检测中等效应 (d=0.5) 需要每组 {n} 人")

n = sample_size_correlation(r=0.3)
print(f"检测中等相关 (r=0.3) 需要 {n} 人")
```

### 3.4 置信区间

```python
import numpy as np
from scipy import stats

def mean_ci(data, confidence=0.95):
    """计算均值的置信区间"""
    n = len(data)
    mean = np.mean(data)
    se = stats.sem(data)
    h = se * stats.t.ppf((1 + confidence) / 2, n - 1)
    return mean - h, mean + h

def proportion_ci(successes, n, confidence=0.95):
    """计算比例的置信区间"""
    p = successes / n
    z = stats.norm.ppf((1 + confidence) / 2)
    se = np.sqrt(p * (1-p) / n)
    return p - z*se, p + z*se

# 使用
ci = mean_ci(data)
print(f"均值 95% CI: [{ci[0]:.4f}, {ci[1]:.4f}]")

ci = proportion_ci(80, 100)
print(f"比例 95% CI: [{ci[0]:.4f}, {ci[1]:.4f}]")
```

---

## 四、可视化

### 4.1 Matplotlib 学术风格

```python
import matplotlib.pyplot as plt
import numpy as np

# 学术风格配置
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif'],
    'font.size': 12,
    'axes.labelsize': 14,
    'axes.titlesize': 16,
    'xtick.labelsize': 11,
    'ytick.labelsize': 11,
    'legend.fontsize': 11,
    'figure.figsize': (8, 6),
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.grid': True,
    'grid.alpha': 0.3,
})

# 柱状图
def plot_bar_comparison(methods, scores, filename='bar.png'):
    """绘制方法对比柱状图"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    colors = ['#94a3b8'] * (len(methods) - 1) + ['#1e40af']
    bars = ax.bar(methods, scores, color=colors, edgecolor='white', linewidth=2)
    
    for bar, score in zip(bars, scores):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01,
                f'{score:.2f}', ha='center', va='bottom', fontweight='bold')
    
    ax.set_ylabel('Accuracy')
    ax.set_ylim(0.7, 1.0)
    ax.set_title('Method Comparison')
    
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

# 折线图
def plot_learning_curves(train_losses, val_losses, filename='curves.png'):
    """绘制学习曲线"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    epochs = range(1, len(train_losses) + 1)
    ax.plot(epochs, train_losses, 'b-', label='Training Loss')
    ax.plot(epochs, val_losses, 'r--', label='Validation Loss')
    
    ax.set_xlabel('Epoch')
    ax.set_ylabel('Loss')
    ax.set_title('Learning Curves')
    ax.legend()
    
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

# 箱线图
def plot_boxplot(data_dict, filename='boxplot.png'):
    """绘制箱线图"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    data = list(data_dict.values())
    labels = list(data_dict.keys())
    
    bp = ax.boxplot(data, labels=labels, patch_artist=True)
    
    colors = ['#94a3b8'] * (len(data) - 1) + ['#1e40af']
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
    
    ax.set_ylabel('Score')
    ax.set_title('Score Distribution')
    
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
```

### 4.2 Seaborn 统计图

```python
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# 设置风格
sns.set_theme(style="whitegrid", font_scale=1.2)

# 箱线图 + 散点
def plot_boxplot_with_points(df, x, y, filename='boxplot.png'):
    """带散点的箱线图"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    palette = ['#94a3b8'] * (df[x].nunique() - 1) + ['#1e40af']
    
    sns.boxplot(data=df, x=x, y=y, palette=palette, ax=ax)
    sns.stripplot(data=df, x=x, y=y, color='black', 
                  alpha=0.3, size=4, ax=ax)
    
    ax.set_title('Score Distribution by Method')
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

# 热力图
def plot_correlation_heatmap(df, filename='heatmap.png'):
    """相关性热力图"""
    fig, ax = plt.subplots(figsize=(10, 8))
    
    corr = df.select_dtypes(include=[np.number]).corr()
    
    sns.heatmap(corr, annot=True, fmt='.2f', cmap='RdBu_r',
                center=0, ax=ax, square=True)
    
    ax.set_title('Correlation Heatmap')
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
```

### 4.3 Plotly 交互式图表

```python
import plotly.graph_objects as go
import plotly.express as px

# 柱状图
def plot_interactive_bar(methods, scores, filename='bar.html'):
    """交互式柱状图"""
    colors = ['#94a3b8'] * (len(methods) - 1) + ['#1e40af']
    
    fig = go.Figure(data=[
        go.Bar(x=methods, y=scores, marker_color=colors,
               text=[f'{s:.2f}' for s in scores],
               textposition='outside')
    ])
    
    fig.update_layout(
        title='Method Comparison',
        xaxis_title='Method',
        yaxis_title='Accuracy',
        yaxis=dict(range=[0.7, 1.0]),
        plot_bgcolor='white',
        font=dict(family="Arial", size=14),
    )
    
    fig.write_html(filename)

# 散点图
def plot_interactive_scatter(df, x, y, color=None, filename='scatter.html'):
    """交互式散点图"""
    fig = px.scatter(df, x=x, y=y, color=color,
                     hover_data=df.columns)
    
    fig.update_layout(
        title=f'{x} vs {y}',
        plot_bgcolor='white',
        font=dict(family="Arial", size=14),
    )
    
    fig.write_html(filename)
```

---

## 五、机器学习

### 5.1 Scikit-learn 基础

```python
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (accuracy_score, precision_recall_fscore_support,
                             classification_report, confusion_matrix)
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
import numpy as np

# 数据准备
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 特征标准化
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 模型训练
models = {
    'LR': LogisticRegression(max_iter=1000),
    'SVM': SVC(kernel='rbf'),
    'RF': RandomForestClassifier(n_estimators=100),
    'GBDT': GradientBoostingClassifier(n_estimators=100),
}

results = {}
for name, model in models.items():
    # 交叉验证
    cv_scores = cross_val_score(model, X_train_scaled, y_train, cv=5)
    
    # 训练和预测
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    
    # 评估
    acc = accuracy_score(y_test, y_pred)
    precision, recall, f1, _ = precision_recall_fscore_support(
        y_test, y_pred, average='weighted'
    )
    
    results[name] = {
        'cv_mean': cv_scores.mean(),
        'cv_std': cv_scores.std(),
        'test_acc': acc,
        'test_f1': f1,
    }
    
    print(f"\n{name}:")
    print(f"  CV: {cv_scores.mean():.4f} ± {cv_scores.std():.4f}")
    print(f"  Test Acc: {acc:.4f}, F1: {f1:.4f}")

# 结果表格
import pandas as pd
results_df = pd.DataFrame(results).T
print("\n" + results_df.to_string())
```

### 5.2 交叉验证

```python
from sklearn.model_selection import (
    KFold, StratifiedKFold, RepeatedStratifiedKFold,
    cross_validate
)

# K折交叉验证
kfold = KFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=kfold, scoring='accuracy')

# 分层K折（推荐用于分类）
skfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=skfold, scoring='accuracy')

# 重复分层K折（更稳健）
rskfold = RepeatedStratifiedKFold(n_splits=5, n_repeats=3, random_state=42)
scores = cross_val_score(model, X, y, cv=rskfold, scoring='accuracy')

# 多指标评估
scoring = ['accuracy', 'precision_weighted', 'recall_weighted', 'f1_weighted']
cv_results = cross_validate(model, X, y, cv=skfold, scoring=scoring)

for metric in scoring:
    key = f'test_{metric}'
    print(f"{metric}: {cv_results[key].mean():.4f} ± {cv_results[key].std():.4f}")
```

### 5.3 超参数调优

```python
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from scipy.stats import randint, uniform

# 网格搜索
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 7, None],
    'min_samples_split': [2, 5, 10],
}

grid_search = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1,
    verbose=1
)
grid_search.fit(X_train, y_train)

print(f"Best params: {grid_search.best_params_}")
print(f"Best score: {grid_search.best_score_:.4f}")

# 随机搜索（更高效）
param_distributions = {
    'n_estimators': randint(50, 500),
    'max_depth': [3, 5, 7, 10, None],
    'min_samples_split': randint(2, 20),
    'min_samples_leaf': randint(1, 10),
}

random_search = RandomizedSearchCV(
    RandomForestClassifier(random_state=42),
    param_distributions,
    n_iter=100,
    cv=5,
    scoring='accuracy',
    n_jobs=-1,
    random_state=42,
    verbose=1
)
random_search.fit(X_train, y_train)

print(f"Best params: {random_search.best_params_}")
print(f"Best score: {random_search.best_score_:.4f}")
```

---

## 六、深度学习 (PyTorch)

### 6.1 数据加载

```python
import torch
from torch.utils.data import Dataset, DataLoader
import numpy as np

class CustomDataset(Dataset):
    def __init__(self, X, y):
        self.X = torch.FloatTensor(X)
        self.y = torch.LongTensor(y)
    
    def __len__(self):
        return len(self.y)
    
    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]

# 创建数据集
train_dataset = CustomDataset(X_train, y_train)
test_dataset = CustomDataset(X_test, y_test)

# 创建数据加载器
train_loader = DataLoader(
    train_dataset, 
    batch_size=32, 
    shuffle=True, 
    num_workers=4
)
test_loader = DataLoader(
    test_dataset, 
    batch_size=64, 
    shuffle=False, 
    num_workers=4
)
```

### 6.2 模型定义

```python
import torch.nn as nn

class MLP(nn.Module):
    def __init__(self, input_dim, hidden_dims, output_dim, dropout=0.5):
        super().__init__()
        
        layers = []
        prev_dim = input_dim
        for dim in hidden_dims:
            layers.extend([
                nn.Linear(prev_dim, dim),
                nn.BatchNorm1d(dim),
                nn.ReLU(),
                nn.Dropout(dropout),
            ])
            prev_dim = dim
        
        layers.append(nn.Linear(prev_dim, output_dim))
        self.model = nn.Sequential(*layers)
    
    def forward(self, x):
        return self.model(x)

# 初始化
model = MLP(
    input_dim=X_train.shape[1],
    hidden_dims=[256, 128, 64],
    output_dim=len(np.unique(y_train)),
    dropout=0.5
)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = model.to(device)
```

### 6.3 训练循环

```python
import torch.optim as optim
from tqdm import tqdm

def train_epoch(model, dataloader, criterion, optimizer, device):
    model.train()
    total_loss = 0
    correct = 0
    total = 0
    
    for X_batch, y_batch in tqdm(dataloader, desc='Training'):
        X_batch, y_batch = X_batch.to(device), y_batch.to(device)
        
        optimizer.zero_grad()
        outputs = model(X_batch)
        loss = criterion(outputs, y_batch)
        loss.backward()
        optimizer.step()
        
        total_loss += loss.item() * len(y_batch)
        _, predicted = outputs.max(1)
        correct += predicted.eq(y_batch).sum().item()
        total += len(y_batch)
    
    return total_loss / total, correct / total

@torch.no_grad()
def evaluate(model, dataloader, criterion, device):
    model.eval()
    total_loss = 0
    correct = 0
    total = 0
    
    for X_batch, y_batch in dataloader:
        X_batch, y_batch = X_batch.to(device), y_batch.to(device)
        
        outputs = model(X_batch)
        loss = criterion(outputs, y_batch)
        
        total_loss += loss.item() * len(y_batch)
        _, predicted = outputs.max(1)
        correct += predicted.eq(y_batch).sum().item()
        total += len(y_batch)
    
    return total_loss / total, correct / total

# 训练
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)
scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, patience=5)

best_val_acc = 0
for epoch in range(100):
    train_loss, train_acc = train_epoch(model, train_loader, criterion, optimizer, device)
    val_loss, val_acc = evaluate(model, test_loader, criterion, device)
    
    scheduler.step(val_loss)
    
    if val_acc > best_val_acc:
        best_val_acc = val_acc
        torch.save(model.state_dict(), 'best_model.pth')
    
    if (epoch + 1) % 10 == 0:
        print(f"Epoch {epoch+1}: "
              f"Train Loss={train_loss:.4f}, Acc={train_acc:.4f} | "
              f"Val Loss={val_loss:.4f}, Acc={val_acc:.4f}")
```

---

## 七、实验管理

### 7.1 配置管理

```python
from dataclasses import dataclass, field
from typing import List
import json

@dataclass
class ExperimentConfig:
    # 数据
    data_path: str = 'data.csv'
    test_size: float = 0.2
    random_state: int = 42
    
    # 模型
    model_name: str = 'MLP'
    hidden_dims: List[int] = field(default_factory=lambda: [256, 128, 64])
    dropout: float = 0.5
    
    # 训练
    batch_size: int = 32
    learning_rate: float = 0.001
    epochs: int = 100
    
    # 输出
    output_dir: str = 'results/'
    
    def save(self, path):
        with open(path, 'w') as f:
            json.dump(self.__dict__, f, indent=2)
    
    @classmethod
    def load(cls, path):
        with open(path) as f:
            config = json.load(f)
        return cls(**config)

# 使用
config = ExperimentConfig(
    hidden_dims=[512, 256, 128],
    learning_rate=0.0005,
    epochs=50
)
config.save('config.json')
```

### 7.2 结果记录

```python
import json
import os
from datetime import datetime

class ExperimentLogger:
    def __init__(self, output_dir='results'):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        self.results = []
    
    def log(self, epoch, metrics):
        metrics['epoch'] = epoch
        metrics['timestamp'] = datetime.now().isoformat()
        self.results.append(metrics)
    
    def save(self, filename='results.json'):
        path = os.path.join(self.output_dir, filename)
        with open(path, 'w') as f:
            json.dump(self.results, f, indent=2)
    
    def get_best(self, metric='val_acc', mode='max'):
        if mode == 'max':
            return max(self.results, key=lambda x: x[metric])
        else:
            return min(self.results, key=lambda x: x[metric])

# 使用
logger = ExperimentLogger('results/exp1')

for epoch in range(100):
    # 训练...
    logger.log(epoch, {
        'train_loss': train_loss,
        'train_acc': train_acc,
        'val_loss': val_loss,
        'val_acc': val_acc,
    })

logger.save()
best = logger.get_best('val_acc')
print(f"Best epoch: {best['epoch']}, Val Acc: {best['val_acc']:.4f}")
```

### 7.3 Weights & Biases 集成

```python
import wandb

# 初始化
wandb.init(
    project="my-research",
    name="experiment-1",
    config={
        "learning_rate": 0.001,
        "epochs": 100,
        "batch_size": 32,
        "model": "MLP",
    }
)

# 训练循环中记录
for epoch in range(100):
    # 训练...
    wandb.log({
        "train_loss": train_loss,
        "train_acc": train_acc,
        "val_loss": val_loss,
        "val_acc": val_acc,
        "epoch": epoch,
    })

# 保存模型
wandb.save('best_model.pth')
wandb.finish()
```

---

## 八、实用工具函数

### 8.1 随机种子

```python
import torch
import numpy as np
import random

def set_seed(seed=42):
    """设置随机种子确保可复现性"""
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
```

### 8.2 计时器

```python
import time
from contextlib import contextmanager

@contextmanager
def timer(name):
    """计时上下文管理器"""
    start = time.time()
    yield
    elapsed = time.time() - start
    print(f"{name}: {elapsed:.2f}s")

# 使用
with timer("数据加载"):
    data = load_data()

with timer("模型训练"):
    model.train()
```

### 8.3 日志工具

```python
import logging

def setup_logging(log_file='train.log'):
    """配置日志"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

# 使用
logger = setup_logging()
logger.info("开始训练")
logger.info(f"Epoch {epoch}: loss={loss:.4f}")
```

---

## 九、项目结构模板

```
research_project/
├── README.md
├── requirements.txt
├── config.json
├── train.py
├── evaluate.py
├── data/
│   ├── raw/
│   └── processed/
├── src/
│   ├── __init__.py
│   ├── dataset.py
│   ├── model.py
│   ├── trainer.py
│   └── utils.py
├── notebooks/
│   ├── 01_eda.ipynb
│   └── 02_analysis.ipynb
├── results/
│   ├── models/
│   └── figures/
└── tests/
    └── test_model.py
```

---

## 十、常见问题

### Q1: 如何加速数据加载？
```python
# 使用多进程加载
DataLoader(dataset, num_workers=4, pin_memory=True)

# 使用预加载
DataLoader(dataset, prefetch_factor=2)
```

### Q2: 如何处理类别不平衡？
```python
# 方法1：加权损失函数
weights = torch.FloatTensor([1.0, 5.0])  # 少数类权重更高
criterion = nn.CrossEntropyLoss(weight=weights)

# 方法2：过采样/欠采样
from imblearn.over_sampling import SMOTE
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_train, y_train)
```

### Q3: 如何保存和加载模型？
```python
# 保存
torch.save(model.state_dict(), 'model.pth')

# 加载
model.load_state_dict(torch.load('model.pth'))
model.eval()
```

### Q4: 如何使用GPU？
```python
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = model.to(device)
data = data.to(device)
```

---

## 十一、相关资源

- [Pandas 文档](https://pandas.pydata.org/docs/)
- [Matplotlib 文档](https://matplotlib.org/stable/)
- [Scikit-learn 文档](https://scikit-learn.org/stable/)
- [PyTorch 文档](https://pytorch.org/docs/stable/)
- [Weights & Biases](https://wandb.ai/)
