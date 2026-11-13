---
layout: page
title: 高校科研项目与论文
permalink: /research/vocal-ai/
---

我在上海理工大学参与计算声学与 AI 美育研究，关注如何把声乐专家使用的技巧维度转化为可分析的音频特征、可检验的模型和可用的反馈。

## Diva 宝贝 · 智能声乐评测

**从声乐技巧建模到赛事辅助评分。** 我在高校科研项目中承担音频数据处理、评测模型调优及部署支持。团队采用全维动态卷积与密集连接，提取复杂频谱中的多尺度特征，并以专家评分作为比对和校准依据。

2025 年 11 月，Diva 用于中德智声国际音乐节复赛（中国区决赛）。校方报道显示，参赛者来自国内外 20 余所高校与艺术机构，现场采用 12 位专家评委与 Diva 辅助评分的机制。团队已申请 6 项软件著作权和 3 项专利。[上海理工大学报道](https://www.usst.edu.cn/2025/1124/c1615a66257/page.htm)

## BelcantoEdu · 可控美声歌声生成

面向声乐教学示例，我参与研发基于条件扩散的歌声生成研究原型。项目基于开源 Audio Diffusion，用十维美声技巧向量对去噪过程施加条件，并探索在保留目标音色的同时迁移技巧，结合分类评估与人工听评检验生成效果。

[项目源码与上游说明](https://github.com/Djangojie/BelcantoEdu) · [早期写作笔记]({{ '/posts/my-paper-post/' | relative_url }})

## 代表性论文

以下成果均有 Kejie Ye 署名。Scientific Reports 论文作者列表中有上海理工大学、上海音乐学院和西湖大学的合作者，本人署名单位为上海理工大学。

### [Dense dynamic convolutional network for Bel canto vocal technique assessment](https://doi.org/10.1038/s41598-025-98726-1)

**Scientific Reports · 2025**

DDNet 将全维动态卷积与密集连接用于声乐技巧评估，论文报告该任务 Top-1 准确率为 90.11%。本人贡献为正式分析与论文审阅修订。

### [Acoustic Structure of Laryngeal-Position Stability, Resonance, and Vocal Openness in Classical Singing and Their Associations with Machine-Learning-based Pedagogical Ratings](https://doi.org/10.1016/j.jvoice.2026.09.015)

**Journal of Voice · 2026 年在线发表**

团队用声学特征和支持向量机预测专家评分，并按歌者隔离训练与验证。

### [Classic Vocal Performance Training Through C-VaC Method: Study of Core Muscle Stability Warm-Up Techniques via Computer-Aided Analysis](https://doi.org/10.1016/j.jvoice.2024.10.014)

**Journal of Voice · 2024 年在线发表**

研究用音准、频率微扰、振幅微扰等声学指标比较不同热身方式。

### [Transfer Learning in Vocal Education: Technical Evaluation of Limited Samples Describing Mezzo-soprano](https://arxiv.org/abs/2410.23325)

**arXiv · 2024 · 预印本**

研究用预训练模型处理女中音技巧评估中的小样本问题。
