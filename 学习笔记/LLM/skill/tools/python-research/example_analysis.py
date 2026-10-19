"""
科研数据分析示例脚本
演示完整的数据分析流程：数据加载、清洗、分析、可视化、报告生成
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import warnings
warnings.filterwarnings('ignore')

# ============================================================
# 1. 设置随机种子（确保可复现性）
# ============================================================
def set_seed(seed=42):
    """设置随机种子"""
    np.random.seed(seed)
    return seed

set_seed(42)

# ============================================================
# 2. 学术风格配置
# ============================================================
def setup_academic_style():
    """配置学术图表风格"""
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

setup_academic_style()

# ============================================================
# 3. 数据加载
# ============================================================
def generate_sample_data(n_samples=500):
    """生成示例数据集"""
    np.random.seed(42)

    # 特征
    feature1 = np.random.randn(n_samples) * 2 + 5
    feature2 = np.random.randn(n_samples) * 1.5 + 3
    feature3 = np.random.randn(n_samples) * 3 + 10
    feature4 = feature1 * 0.5 + np.random.randn(n_samples) * 0.5

    # 类别标签（基于特征的组合）
    score = 0.3 * feature1 + 0.2 * feature2 + 0.1 * feature3 + np.random.randn(n_samples) * 0.5
    label = (score > np.median(score)).astype(int)

    df = pd.DataFrame({
        'feature1': feature1,
        'feature2': feature2,
        'feature3': feature3,
        'feature4': feature4,
        'label': label
    })

    return df

df = generate_sample_data(500)
print("=" * 50)
print("数据概览")
print("=" * 50)
print(f"数据形状: {df.shape}")
print(f"\n前5行:\n{df.head()}")
print(f"\n统计摘要:\n{df.describe()}")
print(f"\n缺失值:\n{df.isnull().sum()}")
print(f"\n类别分布:\n{df['label'].value_counts()}")

# ============================================================
# 4. 探索性数据分析 (EDA)
# ============================================================
def perform_eda(df, output_dir='results'):
    """执行探索性数据分析"""
    import os
    os.makedirs(output_dir, exist_ok=True)

    # 4.1 分布图
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    for idx, col in enumerate(['feature1', 'feature2', 'feature3', 'feature4']):
        ax = axes[idx // 2, idx % 2]
        ax.hist(df[col], bins=30, edgecolor='white', alpha=0.7)
        ax.set_xlabel(col)
        ax.set_ylabel('Frequency')
        ax.set_title(f'Distribution of {col}')
    plt.tight_layout()
    plt.savefig(f'{output_dir}/distributions.png')
    plt.close()

    # 4.2 相关性热力图
    fig, ax = plt.subplots(figsize=(8, 6))
    corr = df.select_dtypes(include=[np.number]).corr()
    sns.heatmap(corr, annot=True, fmt='.2f', cmap='RdBu_r',
                center=0, ax=ax, square=True)
    ax.set_title('Correlation Heatmap')
    plt.tight_layout()
    plt.savefig(f'{output_dir}/correlation_heatmap.png')
    plt.close()

    # 4.3 箱线图（按类别）
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    for idx, col in enumerate(['feature1', 'feature2', 'feature3', 'feature4']):
        ax = axes[idx // 2, idx % 2]
        df.boxplot(column=col, by='label', ax=ax)
        ax.set_xlabel('Label')
        ax.set_ylabel(col)
        ax.set_title(f'{col} by Label')
    plt.suptitle('')
    plt.tight_layout()
    plt.savefig(f'{output_dir}/boxplots_by_label.png')
    plt.close()

    print(f"EDA 图表已保存到 {output_dir}/")

perform_eda(df)

# ============================================================
# 5. 统计检验
# ============================================================
def statistical_tests(df):
    """执行统计检验"""
    print("\n" + "=" * 50)
    print("统计检验结果")
    print("=" * 50)

    group0 = df[df['label'] == 0]
    group1 = df[df['label'] == 1]

    features = ['feature1', 'feature2', 'feature3', 'feature4']

    results = []
    for feat in features:
        # 正态性检验
        _, p_norm0 = stats.shapiro(group0[feat].sample(min(50, len(group0))))
        _, p_norm1 = stats.shapiro(group1[feat].sample(min(50, len(group1))))

        # 根据正态性选择检验方法
        if p_norm0 > 0.05 and p_norm1 > 0.05:
            # 正态分布，使用t检验
            t_stat, p_value = stats.ttest_ind(group0[feat], group1[feat])
            test_name = 't-test'
        else:
            # 非正态，使用Mann-Whitney U检验
            u_stat, p_value = stats.mannwhitneyu(group0[feat], group1[feat])
            test_name = 'Mann-Whitney U'

        # 效应量 (Cohen's d)
        n0, n1 = len(group0), len(group1)
        var0, var1 = group0[feat].var(), group1[feat].var()
        pooled_std = np.sqrt(((n0-1)*var0 + (n1-1)*var1) / (n0+n1-2))
        cohens_d = (group0[feat].mean() - group1[feat].mean()) / pooled_std

        results.append({
            'Feature': feat,
            'Test': test_name,
            'p-value': p_value,
            'Cohen\'s d': cohens_d,
            'Significant': '***' if p_value < 0.001 else '**' if p_value < 0.01 else '*' if p_value < 0.05 else 'ns'
        })

    results_df = pd.DataFrame(results)
    print(results_df.to_string(index=False))
    return results_df

stats_results = statistical_tests(df)

# ============================================================
# 6. 机器学习分析
# ============================================================
def ml_analysis(df, output_dir='results'):
    """执行机器学习分析"""
    import os
    os.makedirs(output_dir, exist_ok=True)

    print("\n" + "=" * 50)
    print("机器学习分析")
    print("=" * 50)

    # 准备数据
    X = df.drop('label', axis=1).values
    y = df['label'].values

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # 标准化
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # 训练模型
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)

    # 交叉验证
    cv_scores = cross_val_score(model, X_train_scaled, y_train, cv=5, scoring='accuracy')
    print(f"\n交叉验证准确率: {cv_scores.mean():.4f} ± {cv_scores.std():.4f}")

    # 测试集评估
    y_pred = model.predict(X_test_scaled)
    print(f"\n测试集分类报告:")
    print(classification_report(y_test, y_pred))

    # 混淆矩阵
    cm = confusion_matrix(y_test, y_pred)
    fig, ax = plt.subplots(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax)
    ax.set_xlabel('Predicted')
    ax.set_ylabel('Actual')
    ax.set_title('Confusion Matrix')
    plt.tight_layout()
    plt.savefig(f'{output_dir}/confusion_matrix.png')
    plt.close()

    # 特征重要性
    feature_names = ['feature1', 'feature2', 'feature3', 'feature4']
    importances = model.feature_importances_

    fig, ax = plt.subplots(figsize=(8, 5))
    indices = np.argsort(importances)[::-1]
    ax.bar(range(len(importances)), importances[indices])
    ax.set_xticks(range(len(importances)))
    ax.set_xticklabels([feature_names[i] for i in indices])
    ax.set_ylabel('Importance')
    ax.set_title('Feature Importance')
    plt.tight_layout()
    plt.savefig(f'{output_dir}/feature_importance.png')
    plt.close()

    print(f"\nML 图表已保存到 {output_dir}/")

ml_analysis(df)

# ============================================================
# 7. 生成报告
# ============================================================
def generate_report(df, stats_results, output_dir='results'):
    """生成分析报告"""
    import os
    os.makedirs(output_dir, exist_ok=True)

    report = f"""# 数据分析报告

## 1. 数据概览
- 样本数: {len(df)}
- 特征数: {len(df.columns) - 1}
- 类别分布: {df['label'].value_counts().to_dict()}

## 2. 统计检验结果

| 特征 | 检验方法 | p值 | 效应量 | 显著性 |
|------|---------|-----|--------|--------|
"""
    for _, row in stats_results.iterrows():
        report += f"| {row['Feature']} | {row['Test']} | {row['p-value']:.4f} | {row[\"Cohen's d\"]:.4f} | {row['Significant']} |\n"

    report += """
## 3. 机器学习结果

使用随机森林分类器，5折交叉验证评估。

详见生成的图表：
- `confusion_matrix.png`: 混淆矩阵
- `feature_importance.png`: 特征重要性

## 4. 结论

基于统计检验和机器学习分析，得出以下结论：
1. 特征在不同类别间存在显著差异
2. 随机森林模型能够有效分类
3. 特征重要性分析揭示了关键特征
"""

    with open(f'{output_dir}/report.md', 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"报告已保存到 {output_dir}/report.md")

generate_report(df, stats_results)

print("\n" + "=" * 50)
print("分析完成！")
print("=" * 50)
