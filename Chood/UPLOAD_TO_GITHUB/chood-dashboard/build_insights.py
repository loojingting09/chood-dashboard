# -*- coding: utf-8 -*-
# Rebuilds insights.json from posts.json (numbers computed) + refreshed narrative (11 posts).
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
vv, ve, vi, vf = (viral["overview"]["traffic"]["views"]["value"],
                  viral["overview"]["traffic"]["impressions"]["value"],
                  inter(viral), viral["overview"]["depth"]["newFans"])
pv = lambda a,b: f"{round(100*a/b)}%"

def fmt(n): return f"{n:,}"

# viewsByPost (all, desc)
vbp = sorted(
    [{"name": p["title"][:11], "views": p["overview"]["traffic"]["views"]["value"], "cover": p.get("cover")} for p in posts],
    key=lambda x: -x["views"])

# view-weighted source mix (posts with traffic data)
agg, wsum = {}, 0
for p in posts:
    tr = p.get("traffic")
    if not tr: continue
    w = p["overview"]["traffic"]["views"]["value"]; wsum += w
    for s in tr["sources"]:
        agg[s["name"]] = agg.get(s["name"], 0) + s["pct"] * w
mix = sorted(([{"name": n, "pct": round(v/wsum, 1)} for n, v in agg.items()]), key=lambda x: -x["pct"])

insights = {
 "generatedFor": f"{len(posts)} 篇笔记 · 2026-08-19 → 09-19",
 "asOf": "09-27",
 "headline": "账号跑通了「养成系 + 创业纪实」方向，单篇爆款仍贡献约六成观看；新一批日常、食谱与品牌节点内容稳定落在 95–392 观看，开始形成第二梯队——但还没跑出第二个爆点。",
 "portfolio": [
   {"label": "累计曝光", "value": fmt(exp), "note": f"{len(posts)} 篇累计"},
   {"label": "累计观看", "value": fmt(views), "note": f"爆款占 {pv(vv,views)}"},
   {"label": "累计互动", "value": fmt(inter_t), "note": f"爆款占 {pv(vi,inter_t)}"},
   {"label": "累计涨粉", "value": fmt(fans), "note": f"爆款占 {pv(vf,fans)}"},
 ],
 "cards": [
   {"tone":"good","icon":"🚀","title":"爆款仍是最大资产，但占比在健康下降",
    "body":f"《药剂师裸辞创业》以 35,194 曝光、4,301 观看贡献了全账号 {pv(vv,views)} 的观看（此前为 77%）——新内容正在分担增长。编号「报到」的「精神股东」玩法带来 139 条评论，仍是最值得复制的互动资产。"},
   {"tone":"good","icon":"🎂","title":"品牌节点 + 情感选题是新的高互动点",
    "body":"《第一次给品牌过生日》以 392 观看、10.8% 互动率成为全账号第二高互动（37 赞）。情感向的品牌里程碑（周年、销量节点、上新）能有效撬动老观众参与，适合做成固定的品牌节点内容。"},
   {"tone":"good","icon":"🍮","title":"高蛋白甜品 / 食谱内容留存最好",
    "body":"《甜品和蛋白都要》平均观看时长 13.4 秒、超过 88% 同类，完播 27%，是新一批里内容深度最强的一条。这类「好吃又不越界」的食谱内容最能留住泛流量，值得做成系列。"},
   {"tone":"neutral","icon":"🔎","title":"图文科普靠「主页 + 搜索」，是可沉淀的资产",
    "body":"《把成分表丢给 ChatGPT》个人主页 + 搜索占近 46%，与视频依赖公域推荐的逻辑不同。这类科普/测评图文更适合嵌入「成分」「代餐」「蛋白」等搜索词，做成能长期被搜到的内容。"},
   {"tone":"warn","icon":"⚠️","title":"第二梯队尚未破圈，入口仍是短板",
    "body":f"除爆款外，其余 10 篇多在 95–392 观看；封面点击率普遍 7–13%、涨粉多为 0。内容留存其实不弱（多条完播 22–45%），问题依旧出在「封面 + 前 3 秒」这个入口没接住泛流量。"},
   {"tone":"warn","icon":"🎬","title":"预告造势有效，但正片留存要跟上",
    "body":"《偷偷准备了很久》拿到近八成视频推荐曝光，前 5 秒完播 42%，但平均观看仅 4.2 秒——悬念拉开后正片没接住。预告应更短、直接指向「明天是什么」，并在 24 小时内发正片承接这波流量。"},
 ],
 "recommendations": [
   {"title":"把「精神股东」做成固定栏目",
    "body":"每期公布股东编号与人数里程碑，鼓励评论区报到；用创业进度 + 用户共创驱动持续互动，把爆款的参与感机制沉淀成可复制的栏目。"},
   {"title":"双赛道内容矩阵：高完播食谱 + 品牌情感节点",
    "body":"食谱类（如高蛋白甜品）负责留存与泛流量，品牌/情感节点（周年、上新）负责互动与老粉唤醒；两条线交替更新，降低对单篇爆款的依赖。"},
   {"title":"封面与前 3 秒专项优化",
    "body":"统一「人物出镜 + 冲突/利益点文案」封面模板，视频前 3 秒直给结论或悬念，目标把封面点击率从多数的 7–13% 提升到 12%+、5 秒完播率提升到 45%+。"},
   {"title":"图文科普做搜索沉淀",
    "body":"把测评/科普图文标题正文嵌入「功能蛋白」「代餐」「成分」「早餐」等搜索热词，提升个人主页与搜索的自然流入，形成可长期被搜到的内容资产。"},
   {"title":"预告—正片联动",
    "body":"预告只保留一个悬念钩子并控制在极短时长，发布后 24 小时内发正片承接；用预告造势、用正片兑现，避免曝光空转。"},
 ],
 "viewsByPost": vbp,
 "sourceMix": mix,
}
json.dump(insights, open("data/insights.json","w"), ensure_ascii=False, separators=(",",":"))
print("insights rebuilt · exp",exp,"views",views,"inter",inter_t,"fans",fans)
print("viral shares: views",pv(vv,views),"inter",pv(vi,inter_t),"fans",pv(vf,fans))
print("viewsByPost",len(vbp),"sourceMix",[ (m['name'],m['pct']) for m in mix])
