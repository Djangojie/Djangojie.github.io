# GitHub 项目与 Skills 雷达 · 2026-11-08

采集时间：2026-11-08T11:43:00+08:00。已核对说明，未安装或运行。

## 精选仓库累计 Star 排名

| 排名 | 仓库 | Star | 做了什么 |
| --- | --- | ---: | --- |
| 1 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | 261,544 | 带记忆、工具调用和技能机制的通用 Agent。 |
| 2 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | 209,779 | 把不同应用串成流程的可视化自动化平台，支持 AI 步骤和代码。 |
| 3 | [langgenius/dify](https://github.com/langgenius/dify) | 160,637 | 搭建 AI 应用、知识库检索和 Agent 工作流的平台。 |
| 4 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | 144,130 | 汇集 AI Agent、技能与检索增强应用的示例代码。 |
| 5 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | 120,274 | 让 AI 通过代码操作浏览器，完成网页上的多步任务。 |
| 6 | [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | 79,133 | 面向初学者的 AI Agent 课程与代码示例。 |

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

## 排名说明

所选样本按 GitHub REST API 累计 stargazers_count 降序

按排错、验证、开源协作、实验与展示用途人工推荐；不是客观质量排行

仅统计技能所在仓库的 Star，不视为单个 Skill 的 Star

Trending 返回缓存页面，未采用其今日增长数；首日只有基线，不计算 24 小时增量

核对仓库元数据、README 和各 Skill 的 SKILL.md；未安装或运行推荐项
