# -*- coding: utf-8 -*-
# Rebuilds insights.json from posts.json (numbers computed) + refreshed narrative (14 posts).
import json
posts = json.load(open("data/posts.json"))

def inter(p):
    e = p["overview"]["engagement"]
    return sum(e[k]["value"] for k in ["likes","comments","collects","shares","quoted"])

exp = sum(p["overview"]["traffic"]["impressions"]["value"] for p in posts)
views = sum(p["overview"]["traffic"]["views"]["value"] for p in posts)
inter_t = sum(inter(p) for p in posts)
fans = sum(p["overview"]["depth"]["newFans"] for p in posts)

viral = next(p for p in posts if p["id"] == "pharmacist-founder")
vv, vi, vf = viral["overview"]["traffic"]["views"]["value"], inter(viral), viral["overview"]["depth"]["newFans"]
pv = lambda a,b: f"{round(100*a/b)}%"
def fmt(n): return f"{n:,}"

vbp = sorted(
    [{"name": p["title"][:11], "views": p["overview"]["traffic"]["views"]["value"], "cover": p.get("cover")} for p in posts],
    key=lambda x: -x["views"])

agg, wsum = {}, 0
for p in posts:
    tr = p.get("traffic")
    if not tr: continue
    w = p["overview"]["traffic"]["views"]["value"]; wsum += w
    for s in tr["sources"]:
        agg[s["name"]] = agg.get(s["name"], 0) + s["pct"] * w
mix = sorted(([{"name": n, "pct": round(v/wsum, 1)} for n, v in agg.items()]), key=lambda x: -x["pct"])

insights = {
 "generatedFor": f"{len(posts)} 篇笔记 · 2026-08-19 → 09-26",
 "asOf": "10-02",
 "headline": "账号已跑出两个破圈点——创业纪实爆款与一周年抽奖——两者合计贡献约 65% 的观看；日常、食谱与品牌节点内容稳定填充第二梯队。增长正从「单篇依赖」转向「爆款 + 节点」的双引擎，下一步是把节点玩法做成可复制的节奏。",
 "portfolio": [
   {"label": "累计曝光", "value": fmt(exp), "note": f"{len(posts)} 篇累计"},
   {"label": "累计观看", "value": fmt(views), "note": f"爆款占 {pv(vv,views)}"},
   {"label": "累计互动", "value": fmt(inter_t), "note": f"爆款占 {pv(vi,inter_t)}"},
   {"label": "累计涨粉", "value": fmt(fans), "note": f"爆款占 {pv(vf,fans)}"},
 ],
 "cards": [
   {"tone":"good","icon":"🎂","title":"一周年抽奖是第二个破圈点，也是涨粉王",
    "body":"《1岁生日不收礼》以 11,485 曝光、1,283 观看、19.3% 互动率成为全账号互动密度最高的一篇（120 条评论、+39 涨粉，近 30 日涨粉第一）。「给粉丝送礼」的抽奖机制把公域流量直接转成评论与关注——这是继「精神股东」后第二个被验证的可复制玩法。"},
   {"tone":"good","icon":"🚀","title":"创业爆款仍是最大单篇，但占比健康下降",
    "body":f"《药剂师裸辞创业》4,301 观看、贡献 {pv(vv,views)} 的观看（此前 77% → 63% → 现 {pv(vv,views)}）。两个破圈点加上稳定的第二梯队，账号对单篇的依赖正在下降。"},
   {"tone":"good","icon":"🍮","title":"高蛋白甜品 / 食谱内容留存最好",
    "body":"《甜品和蛋白都要》平均观看 13.4 秒、超 88% 同类，是所有内容里深度最强的一条。食谱类负责「留存与泛流量」，是双引擎之外最稳的内容底盘，值得做成系列。"},
   {"tone":"neutral","icon":"📡","title":"节点内容吃首页推荐，日常内容吃视频推荐",
    "body":"两个破圈点（创业爆款、生日抽奖）都靠「首页推荐」进入公域大池（86–90%）；日常/食谱/研发内容主要吃「视频推荐」（50–79%）。想放大声量，关键是持续产出能进首页推荐池的强钩子（冲突、福利、情绪）。"},
   {"tone":"warn","icon":"⚠️","title":"封面点击率与人均观看是共同短板",
    "body":"账号近 30 日封面点击率 11.9%（-7%）、人均观看 12 秒（-19%）双双回落；多数第二梯队笔记封面点击率在 7–13%、涨粉为 0。量起来了，但「入口质量」在被稀释——封面与前 3 秒仍是最该补的环节。"},
   {"tone":"warn","icon":"🎬","title":"预告 / 情感向内容留存不足",
    "body":"《偷偷准备了很久》《这一年…》等预告与情感总结内容前 5 秒尚可，但平均观看只有 4–6 秒、正片留存弱。这类内容适合点缀造势，不宜频繁，且开头要更快进入主题。"},
 ],
 "recommendations": [
   {"title":"把「节点福利」做成固定日历",
    "body":"周年、销量里程碑、上新、节日都用「给粉丝送礼 / 抽奖」机制承接，复制生日抽奖的互动与涨粉效果；每次明确福利、门槛与截止，用评论区报名驱动互动。"},
   {"title":"双引擎 + 食谱底盘的内容矩阵",
    "body":"破圈引擎（创业纪实 / 节点福利）负责声量与涨粉，食谱类负责留存与日常流量，两条线交替更新，降低对单篇爆款的依赖。"},
   {"title":"封面与前 3 秒专项优化",
    "body":"统一「人物出镜 + 冲突/利益点文案」封面模板，视频前 3 秒直给结论或悬念，目标把封面点击率从 7–13% 提升到 12%+、5 秒完播率提升到 45%+。"},
   {"title":"图文科普做搜索沉淀",
    "body":"把测评/科普图文（如「成分表丢给 ChatGPT」）标题正文嵌入「功能蛋白」「代餐」「成分」等搜索词，提升个人主页与搜索的自然流入，形成可长期被搜到的内容资产。"},
   {"title":"承接主页流量、提升转粉率",
    "body":"近 30 日主页访客 607、转粉率仅 3.8%。优化主页简介、置顶爆款与福利笔记、统一封面风格，把「来逛主页」的人更多转成关注。"},
 ],
 "viewsByPost": vbp,
 "sourceMix": mix,
}
json.dump(insights, open("data/insights.json","w"), ensure_ascii=False, separators=(",",":"))
print("insights rebuilt · exp",exp,"views",views,"inter",inter_t,"fans",fans)
print("viral views share",pv(vv,views),"| anniversary views", next(p['overview']['traffic']['views']['value'] for p in posts if p['id']=='anniversary-giveaway'))
print("sourceMix",[(m['name'],m['pct']) for m in mix])
