"""Render reviewed topical GitHub research as a blog page and two SVG charts."""
import argparse
import json
from datetime import datetime
from pathlib import Path

from build_github_radar import ROOT, chart


def build(data):
    out = ROOT / 'research' / 'github-radar' / 'topics'
    out.mkdir(parents=True, exist_ok=True)
    date = data['checked_at'][:10]
    (out / 'ppt-wechat.json').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    body = f'''---
layout: page
title: PPT 美化与微信回复助手：热门项目专题
permalink: /research/github-radar/topics/ppt-and-wechat/
---

[返回 GitHub 雷达](/research/github-radar/)

**现有 PPT 精修先看 OfficeCLI；按模板重做先看 PPT Master 或 Presenton。个人微信回复建议可参考 WeReply，但它远没有热门机器人框架成熟。**

采集时间：{data['checked_at']}。以下按精选样本累计 Star 排名，Star 表示关注度，不表示效果或可靠性。{data['validation']}

## PPT：直接修改、重新生成、网页演示要分开看

“可导出 PPTX”不等于“能保留原有所有元素无损美化”。模型、中文字体、图表与动画兼容性都要用实际文件检查。

![PPT 相关精选仓库累计 Star 排名](/research/github-radar/topics/ppt.svg)

'''
    for cat, heading, file in [('ppt', '', 'ppt.svg'), ('wechat', '微信：个人回复助手与机器人是两种产品', 'wechat.svg')]:
        rows = sorted([r for r in data['repositories'] if r['category'] == cat], key=lambda r: (-r['stars'], r['repo']))
        title = 'PPT 相关仓库 · 累计 Star' if cat == 'ppt' else '微信相关仓库 · 累计 Star'
        (out / file).write_text(chart(rows, title, f'{date} / 精选样本；不是效果排名'), encoding='utf-8')
        if heading:
            body += f'\n## {heading}\n\nCowAgent 等热门项目主要用来把 AI 接入聊天渠道；当前 CowAgent 的 weixin 通道是在你的会话列表新增一个机器人助手，不能据此推断它会读取并代回所有好友聊天。\n\n**如果目标是“帮我想怎么回”，应优先看生成草稿、由人确认发送的设计。**这类精确匹配项目的 Star 很少，本次保留真实关注数，不把它们包装成热门成熟产品。\n\n![微信相关精选仓库累计 Star 排名，低 Star 项目详见表格](/research/github-radar/topics/wechat.svg)\n\n'
        body += '| 排名 | 仓库 | 累计 Star | 做了什么 / 交付形式 | 适用场景与限制 |\n| --- | --- | ---: | --- | --- |\n'
        for i, r in enumerate(rows):
            body += f'| {i+1} | [{r["repo"]}]({r["url"]}) | {r["stars"]:,} | {r["description"]}<br>**形式：**{r["output"]} | {r["use"]}<br>**限制：**{r["limitations"]}<br>最近推送：{r["pushed_at"][:10]}（UTC） |\n'
    body += '''
## 选型建议

| 你想完成什么 | 优先查看 | 先做的验证 |
| --- | --- | --- |
| 保留一份已有 PPT 的内容，统一字号、颜色、位置 | OfficeCLI | 复制 3 页真实稿，检查文字、图表、母版是否保留 |
| 根据材料重做一份可编辑 PPT | PPT Master、Presenton | 同一份内容生成 3 页，在 PowerPoint/WPS 里手工编辑确认 |
| 想要漂亮的杂志风或瑞士风演示 | guizang-ppt-skill | 确认交付 HTML 是否符合场地和编辑要求 |
| 研究 Agent 怎样审查和修正幻灯片 | PPTAgent | 在 WSL 等文档支持环境验证依赖和视觉审查流程 |
| 在 Windows 微信聊天中获得几条候选回复 | WeReply 的交互设计 | 先验证当前微信版本能否读取和填入，不自动发送 |
| 在微信里找一个 AI 聊天入口 | CowAgent | 确认机器人会话范围、登录条件和消息权限 |
| 做企业微信或公众号的自动问答 | LangBot、Kirara AI | 确认所需渠道、触发规则与模型费用 |

## 没有列为优先推荐的旧方案

'''
    for r in data['excluded']:
        body += f'- [{r["repo"]}]({r["url"]})：{r["stars"]:,} Star。{r["reason"]}\n'
    body += '''
## 使用边界与来源

微信回复内容可能涉及私人聊天；使用云模型通常会将选取的上下文发送给配置的 API。当前只做公开仓库调研，没有读取私人聊天、登录微信或自动发送消息，也不能承诺任何第三方方案“不会封号”。

代码授权与云服务收费分别查看。特别注意 wxauto 的 README 使用声明与 API 返回许可证之间存在需要核实的差异；PPTist 和 guizang-ppt-skill 使用 AGPL-3.0。开放源码不代表所有商业使用都没有条件。

每一行的仓库链接提供 README 与代码；Star、归档状态和最近推送来自 GitHub API。[查看原始采集数据](/research/github-radar/topics/ppt-wechat.json)。补充核对：

'''
    for url in data['extra_sources']:
        body += f'- [项目说明]({url})\n'
    (out / 'ppt-and-wechat.md').write_text(body, encoding='utf-8')
    return body


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('snapshot', type=Path)
    args = parser.parse_args()
    data = json.loads(args.snapshot.read_text(encoding='utf-8'))
    assert len({r['repo'] for r in data['repositories']}) == len(data['repositories'])
    build(data)
    print('Built PPT and WeChat topic: 13 repositories, 1 archived exclusion, 2 charts')
