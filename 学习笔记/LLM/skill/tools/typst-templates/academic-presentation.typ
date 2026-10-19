// 学术报告 Typst 幻灯片模板
// 使用方法：typst compile academic-presentation.typ slides.pdf

#import "@preview/touying:0.5.2": *
#import themes.metropolis: *
#import "@preview/cetz:0.2.2": *

// ============================================================
// 主题配置
// ============================================================
#show: metropolis-theme.with(
  aspect-ratio: "16-9",
  footer: self => self.info.institute,
  config-info(
    title: [基于深度学习的文本分类研究],
    subtitle: [学术报告],
    author: [作者姓名],
    date: datetime.today(),
    institute: [某某大学计算机学院],
  ),
  config-colors(
    primary: rgb("#1e40af"),
    primary-light: rgb("#3b82f6"),
    secondary: rgb("#1e293b"),
    neutral: rgb("#ffffff"),
    neutral-light: rgb("#f8fafc"),
    neutral-dark: rgb("#1e293b"),
  ),
)

// ============================================================
// 封面
// ============================================================
#title-slide()

// ============================================================
// 目录
// ============================================================
#slide[
  == 目录

  #outline()
]

// ============================================================
// 第一部分：引言
// ============================================================
= 引言

== 研究背景

- 文本分类是自然语言处理的基础任务
- 传统方法依赖人工特征工程
- 深度学习方法展现出强大潜力

#v(1em)

#quote[
  如何设计更有效的深度学习模型来提升文本分类性能？
]

#speaker-note[
  详细说明现有方法的局限性，引出研究动机。
  强调深度学习在 NLP 领域的发展趋势。
]

== 研究目标

#quote[
  提出一种基于 Transformer 的文本分类方法，提升分类准确率并降低人工特征工程成本。
]

*主要创新点*：

+ 动态注意力机制
+ 多尺度特征融合
+ 对比学习损失函数

== 相关工作

#figure(
  table(
    columns: 3,
    align: center,
    table.header[方法][优点][缺点],
    [TextCNN], [速度快], [捕获长距离依赖能力弱],
    [LSTM], [序列建模强], [并行化困难],
    [BERT], [预训练强大], [计算成本高],
  ),
  caption: [现有方法对比],
)

// ============================================================
// 第二部分：方法
// ============================================================
= 研究方法

== 模型架构

#slide[
  === 模型结构

  + 预训练编码器 (BERT)
  + 动态注意力池化层
  + 多尺度特征融合
  + 分类头 (MLP)

  === 训练策略

  - 学习率：$2 times 10^(-5)$
  - Batch size：32
  - Epochs：10
][
  #canvas({
    import draw: *

    // 定义样式
    let box(pos, name, content, color: blue) = {
      rect(
        pos,
        (pos.at(0) + 2.5, pos.at(1) + 0.8),
        name: name,
        fill: color.lighten(80%),
        stroke: color,
        radius: 4pt,
      )
      content(name, text(size: 14pt, content))
    }

    // 绘制节点
    box((0, 0), "input", "输入")
    box((0, -2), "bert", "BERT", color: green)
    box((0, -4), "attn", "注意力", color: orange)
    box((0, -6), "fusion", "融合", color: purple)
    box((0, -8), "output", "输出", color: red)

    // 绘制箭头
    line("input", "bert", mark: (end: ">"))
    line("bert", "attn", mark: (end: ">"))
    line("attn", "fusion", mark: (end: ">"))
    line("fusion", "output", mark: (end: ">"))
  })
]

== 损失函数

总损失函数：

$
  cal(L) = cal(L)_"CE" + lambda cal(L)_"CL"
$

其中对比学习损失：

$
  cal(L)_"CL" = -log frac(exp(sim(z_i, z_j) \/ tau), sum_(k=1)^(2N) bb(1)_(k != i) exp(sim(z_i, z_k) \/ tau))
$

- $cal(L)_"CE"$：交叉熵损失
- $cal(L)_"CL"$：对比学习损失
- $lambda$：平衡系数
- $tau$：温度参数

// ============================================================
// 第三部分：实验
// ============================================================
= 实验

== 数据集

#figure(
  table(
    columns: 4,
    align: center,
    table.header[数据集][训练集][测试集][类别数],
    [AG News], [120K], [7.6K], [4],
    [IMDB], [25K], [25K], [2],
    [SST-2], [67K], [1.8K], [2],
  ),
  caption: [实验数据集统计],
)

*评估指标*：
- 准确率 (Accuracy)
- 精确率 (Precision)
- 召回率 (Recall)
- F1 分数

== 实验结果

#figure(
  table(
    columns: 4,
    align: center,
    table.header[方法][AG News][IMDB][SST-2],
    [TextCNN], [91.2%], [89.5%], [90.1%],
    [LSTM], [92.1%], [90.3%], [91.2%],
    [BERT-base], [94.5%], [93.2%], [93.5%],
    [*Ours*], [*96.1%*], [*95.3%*], [*95.8%*],
  ),
  caption: [各方法在不同数据集上的准确率],
)

#alert[
  我们的方法在所有数据集上均取得最优结果，平均提升 1.6%。
]

#speaker-note[
  重点解释为什么我们的方法更好，突出创新点的贡献。
]

== 消融实验

#figure(
  table(
    columns: 3,
    align: center,
    table.header[模型变体][AG News][平均],
    [Full Model], [*96.1%*], [*95.7%*],
    [w/o Attention], [95.2%], [94.8%],
    [w/o Multi-scale], [95.5%], [95.1%],
    [w/o Contrastive], [95.8%], [95.3%],
  ),
  caption: [消融实验结果],
)

- 注意力机制贡献最大 (+0.9%)
- 多尺度融合次之 (+0.6%)
- 对比学习损失 (+0.4%)

// ============================================================
// 第四部分：结论
// ============================================================
= 结论

== 主要贡献

+ *提出了动态注意力池化机制*
  - 自适应地关注重要文本片段
  - 提升特征表示质量

+ *设计了多尺度特征融合模块*
  - 捕获不同粒度的语义信息
  - 增强模型表达能力

+ *引入对比学习损失函数*
  - 学习更鲁棒的特征表示
  - 提升泛化能力

+ 在三个基准数据集上取得 SOTA

== 未来工作

- *多语言扩展*
  - 支持更多语言的文本分类
  - 探索跨语言迁移学习

- *效率优化*
  - 模型压缩和量化
  - 知识蒸馏

- *应用拓展*
  - 情感分析
  - 命名实体识别
  - 问答系统

== 代码示例

```python
import torch
from transformers import BertModel

class TextClassifier(torch.nn.Module):
    def __init__(self, num_classes):
        super().__init__()
        self.bert = BertModel.from_pretrained('bert-base')
        self.attention = DynamicAttention()
        self.classifier = torch.nn.Linear(768, num_classes)

    def forward(self, input_ids, attention_mask):
        outputs = self.bert(input_ids, attention_mask)
        pooled = self.attention(outputs.last_hidden_state)
        return self.classifier(pooled)
```

// ============================================================
// 致谢
// ============================================================
#focus-slide[
  谢谢！ \
  Q&A

  #v(1em)

  联系方式：email@example.com \
  GitHub：github.com/username
]
