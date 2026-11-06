# 来源与版本

本轮范围为北京时间 2026-11-06 至 11-07 凌晨。公开来源与本地证据分别登记，不以文件修改时间推断已读完。

## 原始公开资料

| 编号 | 资料 | 版本及定位 | 在本资料集中的用途 |
| --- | --- | --- | --- |
| C1 | [CMU 11-768 AI Agents](https://www.cmu-agents.com/) | 本地 Lecture 1–6；L2 60 页、L3 54 页、L4 46 页 | L2–4 完整中文对照笔记，L1 为整体地图；L5–6 待继续阅读 |
| P1 | [Attention Is All You Need](https://arxiv.org/html/1706.03762v7) | v7，§3 架构与注意力 | 两层导读和独立交互示例 |
| P2 | [Language Modeling Is Compression](https://arxiv.org/html/2309.10668v2) | v2，§2、§3、表 1 | 两层导读；摘要与表格差异单独注明 |
| P3 | [SkillsBench](https://arxiv.org/abs/2602.12670v4) | 本地 v4，首页摘要及评估设置 | 版本化的技能配对评价阅读卡 |
| P4 | [SWE-Skills-Bench](https://arxiv.org/abs/2603.15401v2) | v2，摘要与实验定义 | 单技能增量作用阅读卡 |
| A1 | [Assignment 1](https://github.com/cmu-agents/assignment-1/tree/67498d87e36f7b45a2a4ce82d65d1139fb6a51c0) | 固定源码提交 | 作业路线、进度边界与后续验收 |
| E1 | [Dify Issues](https://github.com/langgenius/dify/issues) | 动态入口，未核实具体机会当前状态 | 真实问题实践的延伸阅读 |

课程与论文仍归原作者；本资料集不再分发原 PDF。中文重述并非官方译文，教学图与交互为独立构造。

## 本地学习与验证证据

- `outputs/paper-reading`：本轮已有四份 HTML；入门版来自用户“再易懂一点”的反馈，进阶版保留公式和实验条件。
- 课程阅读聊天：提供第二、三、四课的中文逐页重述，已整理为独立 Markdown；没有公开整段聊天记录和内部工具日志。
- `outputs/assignment-1-任务拆解与skill建议.md`：较早的路线建议，其中“未安装”属于历史状态；公开实践笔记采用后来安装报告更新后的状态。
- `outputs/assignment-1-install-2026-11-07/安装结果与运行说明.md`、`pytest-baseline.xml`：本地安装与离线测试证据；敏感配置与原始日志未上传。
- `outputs/python-environments-2026-11-07/整理结果与使用说明.md`：环境采用方案和未验证范围，公开版省略个人路径与旧项目清单。
- 当天设计模式、回复助手讨论：只提取通用工程问题与合成示例，不公开任何真实聊天数据。
- Obsidian 的两份 CMU 速记与一份技能阅读速记：保留原话片段，逐条标明校正和待验证动作；内嵌截图不转载。

## 本地阅读 PDF 的 SHA-256

校验值用于识别本轮阅读文件，不表示已逐字对比在线版本。若原文更新，应创建新版本记录。

```text
lecture-02-tool-use.pdf
671b9d0c849150aa9b5d95a9655b892dbe5fa2d6fc7a6c704c0f8e3f876e74ad
lecture-03-long-context.pdf
cd08b3463430b78a144a24de611ec9a58befae32c5d2109471d89934fbf2f926
lecture-04-memory-and-skills.pdf
15165b0ab74f7ebe2704bbfbc341f2273d27e66041f3bfedf2c887c02e6a549d
2602.12670v4.pdf
e987ebc3f0084a1ffc8acbca58259e33120b95fcef3876abfad060e169cf210b
2603.15401v2.pdf
61120258c599e3b70c5d0151ee63ad2f96f51757fc6bf38f7f4d560edb460f1c
```
