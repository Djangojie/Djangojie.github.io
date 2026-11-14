# GitHub 项目与 Skills 雷达 · 2026-11-14

采集时间：2026-11-14T09:07:53+08:00。已核对说明，未安装或运行。

## 精选仓库累计 Star 排名

| 排名 | 仓库 | Star | 做了什么 |
| --- | --- | ---: | --- |
| 1 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | 263,223 | 带记忆、工具调用和技能机制的通用 Agent。 |
| 2 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | 210,415 | 把不同应用串成流程的可视化自动化平台，支持 AI 步骤和代码。 |
| 3 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | 195,252 | 将 PDF、PPT、Word、Excel 等材料转换为便于检索和分析的 Markdown。 |
| 4 | [langgenius/dify](https://github.com/langgenius/dify) | 161,121 | 搭建 AI 应用、知识库检索和 Agent 工作流的平台。 |
| 5 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | 144,584 | 汇集 AI Agent、技能与检索增强应用的示例代码。 |
| 6 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | 120,956 | 让 AI 通过代码操作浏览器，完成网页上的多步任务。 |
| 7 | [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | 79,576 | 面向初学者的 AI Agent 课程与代码示例。 |
| 8 | [astral-sh/ruff](https://github.com/astral-sh/ruff) | 51,227 | 检查 Python 代码中的常见问题并统一排版，规则可写入 pyproject.toml。 |
| 9 | [langfuse/langfuse](https://github.com/langfuse/langfuse) | 37,400 | 记录 Agent 的模型调用与执行轨迹，支持成本观察、数据集实验和评测。 |
| 10 | [marp-team/marp-cli](https://github.com/marp-team/marp-cli) | 3,919 | 将 Markdown 课件转为网页、PDF 或 PowerPoint。 |
| 11 | [langchain-ai/openevals](https://github.com/langchain-ai/openevals) | 1,252 | 为 LLM 应用提供可复用的评估器，支持 Python 和 TypeScript。 |

## Skills 推荐顺序

| 推荐顺序 | Skill | 做了什么 | 使用条件 |
| --- | --- | --- | --- |
| 1 | [systematic-debugging](https://github.com/obra/superpowers/blob/main/skills/systematic-debugging/SKILL.md) | 先复现、收集证据、找出根因，再修复问题。 | 较强的流程约束，小问题可按任务范围使用。 |
| 2 | [verification-before-completion](https://github.com/obra/superpowers/blob/main/skills/verification-before-completion/SKILL.md) | 要求完成声明附带最新验证证据。 | 可能增加检查步骤；须选择与改动相称的验证。 |
| 3 | [gh-fix-ci](https://github.com/openai/skills/blob/main/skills/.curated/gh-fix-ci/SKILL.md) | 读取 GitHub Actions 失败日志，定位 PR 自动检查失败。 | 需要 gh 登录及仓库访问；技能包含确认修复方案的步骤。 |
| 4 | [gh-address-comments](https://github.com/openai/skills/blob/main/skills/.curated/gh-address-comments/SKILL.md) | 整理 PR 的审阅意见并处理选定评论。 | 需要 gh 登录；技能会询问要处理哪些意见。 |
| 5 | [jupyter-notebook](https://github.com/openai/skills/blob/main/skills/.curated/jupyter-notebook/SKILL.md) | 通过模板生成和整理可复现的实验或教学笔记本。 | 运行需要 Python/Jupyter 依赖；必须区分已执行和仅生成。 |
| 6 | [playwright](https://github.com/openai/skills/blob/main/skills/.curated/playwright/SKILL.md) | 通过浏览器快照、导航和截图执行网页操作。 | 依赖 Node/npm 和浏览器；当前脚本使用 shell wrapper，Windows 适配需验证。 |
| 7 | [mcp-builder](https://github.com/anthropics/skills/blob/main/skills/mcp-builder/SKILL.md) | 指导构建 MCP 服务，让模型以工具方式访问外部系统。 | 需要编程和 SDK 环境；迁移到 Codex 时应核对宿主特有工具。 |
| 8 | [frontend-design](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md) | 指导网页的版式、字体和视觉风格设计。 | 属于设计指引；不保证可访问性或功能正确，仍需实际检查。 |
| 9 | [huashu-design](https://github.com/alchaincyf/huashu-design/blob/master/SKILL.md) | 用 HTML 设计幻灯片、原型和信息图，提供可编辑 PPTX 导出流程。 | 技能强制先给多个设计方向，会增加交互；完整依赖配套素材和脚本，需检查中文字体与 PPTX 导出保真度。MIT；模型调用可能收费。 |
| 10 | [presenton](https://github.com/presenton/skills/blob/main/skills/presenton/SKILL.md) | 通过 Presenton 的在线 API 生成可编辑 PPTX，也可导出 PDF 和 PNG。 | 需要兼容的 Agent、Python 辅助脚本和网络。流程可能上传用户提供的图片，并生成可分享预览链接。仓库为 Apache-2.0，服务额度和费用未核实。 |

## 排名说明

所选样本按 GitHub REST API 累计 stargazers_count 降序

按排错、验证、开源协作、实验与展示用途人工推荐；不是客观质量排行

仅统计技能所在仓库的 Star，不视为单个 Skill 的 Star

两期累计 Star 快照相隔约 21.1 小时，上期采集于 2026-11-13T11:59:12+08:00。本轮未采用 Trending 数据。

核对仓库元数据、README 和各 Skill 的 SKILL.md；未安装或运行推荐项
