"""Build a static GitHub radar from a reviewed JSON snapshot (standard library only)."""
import argparse
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'research' / 'github-radar'


def esc(value):
    return html.escape(str(value), quote=True)


def chart(rows, title, subtitle):
    width, top, step = 1000, 125, 70
    height = top + len(rows) * step + 42
    maximum = max(r['stars'] for r in rows)
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
             f'<title id="title">{esc(title)}</title><desc id="desc">{esc(subtitle)}。' + '；'.join(f"{esc(r['repo'])}: {r['stars']:,} Stars" for r in rows) + '</desc>',
             f'<rect width="100%" height="100%" rx="20" fill="#f5f3ed"/>',
             '<g font-family="Segoe UI,Microsoft YaHei,Arial,sans-serif" fill="#152d35">',
             f'<text x="28" y="42" font-size="25" font-weight="700">{esc(title)}</text>',
             f'<text x="28" y="72" font-size="15" fill="#52676d">{esc(subtitle)}</text>']
    for i, row in enumerate(rows):
        y = top + step * i
        length = round(row['stars'] / maximum * 460, 1)
        parts += [f'<text x="28" y="{y + 20}" font-size="16">{i+1:02d}  {esc(row["repo"])}</text>',
                  f'<rect x="395" y="{y}" width="460" height="30" rx="5" fill="#e0e5df"/>',
                  f'<rect x="395" y="{y}" width="{length}" height="30" rx="5" fill="{["#1c6970", "#40858a", "#639da0"][min(i, 2)]}"/>',
                  f'<text x="875" y="{y + 21}" font-size="17">{row["stars"]:,}</text>']
    parts.append('</g></svg>')
    return '\n'.join(parts)


def build(data):
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / 'snapshots').mkdir(exist_ok=True)
    date = data['checked_at'][:10]
    payload = json.dumps(data, ensure_ascii=False, indent=2) + '\n'
    (OUT / 'data.json').write_text(payload, encoding='utf-8')
    (OUT / 'snapshots' / f'{date}.json').write_text(payload, encoding='utf-8')
    repos = sorted(data['repositories'], key=lambda r: (-r['stars'], r['repo']))
    sources = sorted(data['skill_sources'], key=lambda r: (-r['stars'], r['repo']))
    (OUT / 'repositories.svg').write_text(chart(repos, '热门仓库 · 累计 Star 排名', f'{date} / 精选样本 / 线性刻度，起点为 0'), encoding='utf-8')
    (OUT / 'skill-sources.svg').write_text(chart(sources, 'Skills 来源仓库 · 热度排名', f'{date} / 仓库 Star 不代表单个 Skill 的热度或质量'), encoding='utf-8')
    repo_rows = ''.join(f'<tr><td class="rank">{i+1:02d}</td><td><a href="{esc(r["url"])}">{esc(r["repo"])}</a><p>{esc(r["description"])}</p></td><td class="number">{r["stars"]:,}</td><td>{esc(r["pushed_at"][:10])}<small>UTC · 最近推送</small></td><td>{esc(r["relevance"])}<small>下一步：{esc(r["next_step"])}</small><details><summary>使用前了解</summary>{esc(r["limitations"])}<br><a href="{esc(r["readme_url"])}">README</a> · <a href="{esc(r["metadata_url"])}">元数据来源</a></details></td></tr>' for i, r in enumerate(repos))
    skill_rows = ''.join(f'<tr><td class="rank">{s["rank"]:02d}</td><td><a href="{esc(s["url"])}">{esc(s["name"])}</a><small>{esc(s["repo"])}</small></td><td>{esc(s["description"])}</td><td>{esc(s["relevance"])}<small>{esc(s["limitations"])}</small></td></tr>' for s in data['skills'])
    doc = '''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>GitHub 项目与 Skills 雷达 · Django</title><meta name="description" content="AI Agent、自动化与开发效率：精选热门仓库累计 Star 排名、图表与实用 Skills。">
<style>
:root{color-scheme:light;--bg:#f5f3ed;--ink:#152d35;--muted:#52676d;--accent:#176e75;--line:#d6ded7}*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.7 system-ui,'Microsoft YaHei',sans-serif}main{max-width:1220px;margin:auto;padding:30px 32px 64px}a{color:var(--accent);text-underline-offset:4px}nav{display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap;border-bottom:1px solid var(--line);padding-bottom:20px}.brand{font-weight:750;letter-spacing:.04em}header{padding:52px 0 32px;max-width:910px}.kicker{color:var(--accent);font-weight:650}h1{font-size:clamp(34px,5.5vw,64px);line-height:1.17;letter-spacing:-.035em;margin:14px 0 20px}header p{font-size:19px;color:var(--muted);max-width:750px}.stats{display:flex;gap:48px;flex-wrap:wrap;margin-top:30px}.stats b{display:block;font-size:32px;line-height:1.25}.stats span{color:var(--muted);font-size:14px}.notice{border-left:4px solid var(--accent);background:#e7ede6;padding:16px 22px;margin:22px 0 36px}section{padding:26px 0;border-top:1px solid var(--line)}h2{font-size:27px;line-height:1.3;margin:12px 0}h3{margin-bottom:4px}section>p{color:var(--muted)}.chart{display:block;width:100%;height:auto;max-width:1000px;margin:24px auto}.table-wrap{overflow-x:auto;border:1px solid var(--line);border-radius:10px;background:#fffefb}table{border-collapse:collapse;width:100%;font-size:14px}th{text-align:left;background:#e7ede6;color:var(--muted);font-size:13px}td,th{padding:18px 15px;border-bottom:1px solid var(--line);vertical-align:top}tr:last-child td{border-bottom:0}td p{margin:8px 0 0;color:var(--muted)}td a{font-weight:650;overflow-wrap:anywhere}.rank{font-size:21px;color:var(--accent);font-weight:700}.number{font-variant-numeric:tabular-nums;white-space:nowrap;font-weight:700}small{display:block;margin-top:8px;color:var(--muted);font-size:12px}details{margin-top:10px}summary{cursor:pointer;color:var(--accent)}.search{display:flex;align-items:center;gap:14px;margin:25px 0 14px;flex-wrap:wrap}input{font:inherit;padding:10px 14px;min-width:240px;border:1px solid #90a6a5;border-radius:6px;background:#fffefb}.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin:24px 0}.card{border-top:3px solid var(--accent);padding:15px 18px;background:#e7ede6}.card p{font-size:14px;color:var(--muted)}footer{border-top:1px solid var(--line);margin-top:30px;padding-top:25px;color:var(--muted);font-size:13px}li{margin:10px 0}button{font:inherit}.empty{display:none;color:var(--muted)}@media(max-width:700px){main{padding:22px 18px 45px}header{padding-top:32px}.stats{gap:28px}.cards{grid-template-columns:1fr}table{min-width:730px}h2{font-size:24px}td,th{padding:13px 12px}.chart{min-height:160px}}@media(prefers-reduced-motion:no-preference){a{transition:color .15s}a:hover{color:#113b40}}@media print{input,.search,nav{display:none}main{padding:0}.table-wrap{overflow:visible}table{min-width:0}.cards{break-inside:avoid}}
</style></head><body><main>
<nav aria-label="导航"><a class="brand" href="/">DJANGO / 项目观察</a><div><a href="#repositories">仓库榜</a> · <a href="#skills">Skills 推荐</a> · <a href="#method">排名说明</a></div></nav>
<header><div class="kicker">GITHUB RADAR · 每日精选</div><h1>找到值得读的代码，<br>也找到能用上的技能。</h1><p>关注 AI Agent、开发效率与自动化。用累计热度筛选项目，再用具体用途判断值不值得花时间。</p><div class="stats"><div><b>__REPOS__</b><span>精选仓库</span></div><div><b>__SKILLS__</b><span>实用 Skills</span></div><div><b>__DATE__</b><span>本次快照 · 北京时间</span></div></div></header>
<div class="notice"><strong>这是精选样本排名，不是 GitHub 全站榜单。</strong>仓库按累计 Star 排序；Skills 按用途推荐。增长须按实际快照间隔计算。推荐项已核对说明，尚未安装或运行。</div>
<section><h2>先看这三个用途</h2><p><a href="topics/ppt-and-wechat/">新专题：PPT 美化与微信回复助手 · 排名、功能与选择建议 →</a></p><div class="cards"><article class="card"><h3>排错与验收</h3><p>先看 systematic-debugging 和 verification-before-completion，把“找到根因”和“拿出证据”变成固定步骤。</p></article><article class="card"><h3>学习 Agent</h3><p>用微软入门课程建立结构，再从 awesome-llm-apps 选一个最小例子，记录输入、工具和成功标准。</p></article><article class="card"><h3>做一次小实验</h3><p>观察 Hermes 的记忆与技能机制，或用 Browser Use 操作一个公开页面。先测一个任务，再考虑长期使用。</p></article></div></section>
<div class="search"><label for="search">筛选清单</label><input id="search" type="search" placeholder="例如：排错、浏览器、MCP" autocomplete="off"><span id="result-count" role="status" aria-live="polite"></span></div>
<section id="repositories"><h2>01 / 热门仓库排名</h2><p>按本次样本的累计 Star 降序排列。Star 是受关注程度的线索，不代表质量、近期增速或适合所有任务。</p><img class="chart" src="repositories.svg" alt="精选仓库的累计 Star 横向条形图，具体数值见下表" width="1000" height="587"><div class="table-wrap"><table><caption>__DATE__ 精选仓库累计 Star 排名</caption><thead><tr><th scope="col">排名</th><th scope="col">仓库 / 做了什么</th><th scope="col">累计 Star</th><th scope="col">最近活动</th><th scope="col">用途与边界</th></tr></thead><tbody>__REPO_ROWS__</tbody></table></div><p class="empty">没有匹配的仓库。</p></section>
<section id="skills"><h2>02 / 实用 Skills 推荐</h2><p>Skill 是给 Agent 使用的一组任务说明和配套资源。以下按排错、验证、协作、实验与展示用途排序，属于编辑推荐，不是效果测评，也没有单个 Skill 的 Star 统计。</p><div class="table-wrap"><table><caption>Skills 的推荐顺序与用途</caption><thead><tr><th scope="col">推荐顺序</th><th scope="col">Skill / 来源</th><th scope="col">做了什么</th><th scope="col">适用场景与条件</th></tr></thead><tbody>__SKILL_ROWS__</tbody></table></div><p class="empty">没有匹配的 Skill。</p><h3>这些 Skills 来自哪些热门仓库？</h3><p>下面统计整个来源仓库的累计 Star，不能分摊到单个 Skill。</p><img class="chart" src="skill-sources.svg" alt="Skills 来源仓库累计 Star 排名，数据可从 JSON 下载" width="1000" height="377"></section>
<section id="method"><h2>03 / 数据、口径与验证范围</h2><ul><li>采集时间：<time>__CHECKED__</time>。仓库 Star、最近推送及归档状态来自 GitHub REST API；功能介绍来自仓库 README 与各技能的 SKILL.md。</li><li>本次聚焦 AI Agent、自动化、开发效率和学习，未穷尽所有热门项目。技能推荐顺序反映上述用途，不是客观质量评分。</li><li>GitHub Trending 返回缓存页面，本次没有采用其“今日增长”。以后只有可比且有时间戳的快照才计算变化，并注明实际间隔。</li><li>本次只做资料核对，未安装推荐项，未验证运行效果、安全性或生产可靠性。开源代码、模型 API 和云服务可能采用不同收费与授权方式。</li><li>计划每日更新；页面始终显示实际采集时间。抓取失败时保留最近成功版本，不用旧数据冒充当天结果。</li></ul><p><a href="data.json">下载最新 JSON</a> · <a href="snapshots/__DATE__.json">查看本次快照</a> · <a href="https://github.com/Djangojie/Djangojie.github.io/tree/main/research/github-radar">查看版本与历史</a></p></section>
<footer>公开来源整理 · AI 辅助筛选与编排 · 不构成项目实测背书。<br>图表和表格共用同一份快照，图表均从 0 开始，避免夸大差异。</footer>
</main><script>
const input=document.getElementById('search');
function filter(){const q=input.value.trim().toLocaleLowerCase();let visible=0;for(const id of ['repositories','skills']){const section=document.getElementById(id);let count=0;for(const row of section.querySelectorAll('tbody tr')){const show=row.textContent.toLocaleLowerCase().includes(q);row.hidden=!show;if(show)count++;}section.querySelector('.empty').style.display=count?'none':'block';visible+=count;}document.getElementById('result-count').textContent=q?`找到 ${visible} 条匹配`:'';}
input.addEventListener('input',filter);
</script></body></html>'''
    replacements = {'__REPOS__': str(len(repos)), '__SKILLS__': str(len(data['skills'])), '__DATE__': date, '__CHECKED__': esc(data['checked_at']), '__REPO_ROWS__': repo_rows, '__SKILL_ROWS__': skill_rows}
    for key, value in replacements.items():
        doc = doc.replace(key, value)
    (OUT / 'index.html').write_text(doc, encoding='utf-8')
    report = f'# GitHub 项目与 Skills 雷达 · {date}\n\n采集时间：{data["checked_at"]}。已核对说明，未安装或运行。\n\n## 精选仓库累计 Star 排名\n\n| 排名 | 仓库 | Star | 做了什么 |\n| --- | --- | ---: | --- |\n'
    for i, r in enumerate(repos):
        report += f'| {i+1} | [{r["repo"]}]({r["url"]}) | {r["stars"]:,} | {r["description"]} |\n'
    report += '\n## Skills 推荐顺序\n\n| 推荐顺序 | Skill | 做了什么 | 使用条件 |\n| --- | --- | --- | --- |\n'
    for s in data['skills']:
        report += f'| {s["rank"]} | [{s["name"]}]({s["url"]}) | {s["description"]} | {s["limitations"]} |\n'
    report += '\n## 排名说明\n\n' + '\n\n'.join(data['methodology'].values()) + '\n'
    (OUT / 'report.md').write_text(report, encoding='utf-8')
    print(f'Built {len(repos)} repositories, {len(data["skills"])} skills: {OUT}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('snapshot', type=Path)
    args = parser.parse_args()
    snapshot = json.loads(args.snapshot.read_text(encoding='utf-8'))
    assert snapshot['schema_version'] == 1
    assert len({r['repo'] for r in snapshot['repositories']}) == len(snapshot['repositories'])
    assert len({s['url'] for s in snapshot['skills']}) == len(snapshot['skills'])
    assert all(isinstance(r['stars'], int) and r['stars'] >= 0 for r in snapshot['repositories'])
    build(snapshot)
