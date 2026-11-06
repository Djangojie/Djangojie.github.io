# 从语言模型到可靠 Agent：学习资料集

本资料集把 2026-11-06 至 11-07 凌晨的一轮课程阅读、论文导读、交互页面、环境实践和工程讨论连起来。它是持续更新的学习记录，不是完成课程、论文复现或生产部署的证明。

## 一条主线

**模型怎样参考信息 → 怎样给出预测 → 怎样借工具行动 → 怎样管理历史 → 怎样复用经验 → 怎样验证系统。**

| 层次 | 要回答的问题 | 从这里开始 |
| --- | --- | --- |
| 模型基础 | 注意力到底在计算什么？ | [Attention 入门](guides/attention-reading.html)、[进阶](guides/attention-advanced.html) |
| 预测与压缩 | 预测概率为什么能决定编码长度？ | [压缩入门](guides/compression-reading.html)、[进阶](guides/compression-advanced.html) |
| 工具与执行 | 谁真正执行动作？参数、权限和失败怎么办？ | [第二课完整对照笔记](notes/lecture-02-tool-use.md) |
| 上下文 | 历史越来越长，怎样保留任务需要的信息？ | [第三课完整对照笔记](notes/lecture-03-long-context.md) |
| 记忆与技能 | 什么值得留下？何时复用？怎样维护？ | [第四课完整对照笔记](notes/lecture-04-memory-and-skills.md) |
| 证据与评价 | 技能有没有用，为什么不同基准会给出不同结果？ | [两组论文的阅读卡](notes/papers-and-evidence.md) |
| 工程实践 | 怎样拆依赖、环境和验收？ | [作业进度与实验计划](notes/assignment-and-environment.md) |
| 个人问题 | 为什么简单的回复任务会变成复杂软件？ | [问题与工程反思](notes/questions-and-engineering.md) |

在线入口：[学习导航](https://djangojie.github.io/research/agents/)，[本轮博客](https://djangojie.github.io/posts/from-attention-to-reliable-agents/)。GitHub 文件预览不会执行 HTML；在线页面或下载后本地打开均可交互。

## 阅读顺序

先用入门 HTML 建立直觉，再读进阶版公式和实验条件；之后按工具、上下文、记忆与技能读三份课程笔记，最后看工程反思和作业验收。无需先把所有公式背下来。

第一课在本轮起到整体地图的作用；已核对本地课件标题，但没有取得同等完整的第一课对照笔记。第五、六课只列为后续材料，不能把文件已下载算作已读完。FDE 实践资源作为延伸索引保留在反思文档中，具体机会状态须另行核验。

## 内容是谁写的，验证到哪里

- 用户提出阅读要求、理解障碍和工程问题；中文讲解、页面代码与本轮归纳由 AI 辅助形成。
- “来源事实”指指定版本原文或本地证据；“整理推论”是跨材料连接；“待验证”表示尚未通过实验。
- HTML 中是独立教学演示，没有调用真实模型，不代表已复现训练或基准结果。
- 作业环境已安装，TODO 尚未实现；完整离线基线有 11 项失败，远程集成未验证。
- 不上传私人聊天、学生资料、账号配置、环境快照或第三方论文和课件 PDF；原文统一从 [来源索引](sources.md) 访问。

## 维护方式

新增材料先登记来源和版本，再放到对应问题下；每篇笔记补“我能解释什么、还不确定什么、怎样验证”。后续实验使用独立结果表，记录模型、版本、任务、预算和失败，不能覆盖本轮的未完成状态。

重新生成四个 HTML：在本目录执行 `python scripts/build_beginner_guides.py`，只需 Python 标准库。该入口先生成进阶页面，再生成入门页面；单独运行 `build_reading_guides.py` 会让两个 reading 文件恢复为进阶内容。

发布清单及校验值见 [manifest.json](manifest.json)。
