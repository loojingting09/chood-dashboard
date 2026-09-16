# -*- coding: utf-8 -*-
import json
posts = json.load(open("data/posts.json"))

def num(x):
    if isinstance(x,(int,float)): return x
    return float(str(x).replace('%','').replace('秒','').replace(',',''))

def pv(p,*keys):
    d=p
    for k in keys: d=d[k]
    return d

rows=[]
for p in posts:
    o=p["overview"]; e=o["engagement"]
    imp=o["traffic"]["impressions"]["value"]; views=o["traffic"]["views"]["value"]
    inter=e["likes"]["value"]+e["comments"]["value"]+e["collects"]["value"]+e["shares"]["value"]
    rows.append({"id":p["id"],"title":p["title"],"date":p["publishDate"],
      "imp":imp,"views":views,"likes":e["likes"]["value"],"comments":e["comments"]["value"],
      "collects":e["collects"]["value"],"shares":e["shares"]["value"],"inter":inter,
      "eng":round(inter/views*100,1) if views else 0,
      "ctr":num(o["traffic"]["coverCTR"]["value"]),
      "watch":num(o["depth"]["avgWatch"]["value"]),
      "newFans":o["depth"]["newFans"],"cover":p.get("cover")})

tot=lambda k: sum(r[k] for r in rows)
T={"imp":tot("imp"),"views":tot("views"),"inter":tot("inter"),"newFans":tot("newFans"),
   "likes":tot("likes"),"comments":tot("comments"),"collects":tot("collects"),"shares":tot("shares")}

# aggregated traffic-source mix weighted by views
mix={}
for p in posts:
    views=p["overview"]["traffic"]["views"]["value"]
    for s in p["traffic"]["sources"]:
        mix[s["name"]]=mix.get(s["name"],0)+s["pct"]/100*views
mixtot=sum(mix.values())
source_mix=sorted([{"name":k,"pct":round(v/mixtot*100,1)} for k,v in mix.items()], key=lambda x:-x["pct"])

viral=max(rows,key=lambda r:r["views"])
def share(k): return round(viral[k]/T[k]*100)

# gender/audience consistency
fem=[p["audience"]["gender"]["female"] for p in posts]
overseas=[p["audience"]["city"][0]["pct"] for p in posts]

views_by_post=sorted(rows,key=lambda r:-r["views"])

insights={
 "generatedFor":"6 篇笔记 · 2026-08-19 → 09-07",
 "asOf":"09-16",
 "headline":"账号已跑通「养成系 + 创业纪实」内容方向，并出现首个爆款。当前增长高度依赖单篇爆文，下一步是把爆款的互动玩法沉淀为可复制的栏目。",
 "portfolio":[
   {"label":"累计曝光","value":f"{T['imp']:,}","note":"6 篇累计"},
   {"label":"累计观看","value":f"{T['views']:,}","note":f"爆款占 {share('views')}%"},
   {"label":"累计互动","value":f"{T['inter']:,}","note":f"爆款占 {share('inter')}%"},
   {"label":"累计涨粉","value":f"{T['newFans']:,}","note":f"爆款占 {share('newFans')}%"}],
 "cards":[
  {"tone":"good","icon":"🚀","title":"爆款验证了「精神股东」互动玩法",
   "body":f"《药剂师裸辞创业》以 {viral['imp']:,} 曝光、{viral['views']:,} 观看、{viral['eng']}% 互动率成为首个爆款，贡献了全账号 {share('newFans')}% 的涨粉。编号「报到」的参与感设计带来 {viral['comments']} 条评论——是其他笔记的数十倍。这是最值得复制的资产。"},
  {"tone":"warn","icon":"⚠️","title":"增长过度集中在单篇",
   "body":f"爆款贡献了 {share('views')}% 的观看与 {share('inter')}% 的互动，其余 5 篇多在 150–250 观看区间徘徊。账号需要第 2、第 3 个「可复制爆点」来降低对单篇的依赖。"},
  {"tone":"good","icon":"🎯","title":"受众画像高度一致，精准触达目标人群",
   "body":f"6 篇笔记的观众都是「海外（{min(overseas)}–{max(overseas)}%）+ 女性（{min(fem)}–{max(fem)}%）+ 25–34 岁」，兴趣稳定落在美食 / 生活记录 / 娱乐。内容-人群匹配度很高，说明选题方向正确。"},
  {"tone":"neutral","icon":"📡","title":"流量结构：视频推荐是基本盘，首页推荐是爆发口",
   "body":f"日常笔记主要吃「视频推荐」的算法分发（约 60–69%），反馈平稳但天花板有限；唯一破圈的爆款拿到了 90% 的「首页推荐」。想要放大声量，关键在于持续产出能进入首页推荐公域池的强钩子内容。"},
  {"tone":"warn","icon":"🖼️","title":"封面点击率与涨粉是共同短板",
   "body":"除爆款外，封面点击率普遍在 9–10%，涨粉多为 0。内容深度（平均观看 12–20 秒）其实不弱，问题出在「入口」——封面与前 3 秒钩子没有把泛流量留下来。"}],
 "recommendations":[
  {"title":"把「精神股东」做成固定栏目","body":"每期公布股东编号与人数里程碑，鼓励评论区报到；用创业进度 + 用户共创驱动持续互动，复制爆款的参与感机制。"},
  {"title":"封面与前 3 秒专项优化","body":"统一采用「人物出镜 + 冲突/利益点文案」的封面模板，视频前 3 秒直给结论或悬念，目标把封面点击率从 ~9% 提升到 12%+、5 秒完播率提升到 45%+。"},
  {"title":"围绕高完播题材做系列","body":"「创业幕后」「省时早餐场景」完播率与黏性最高，固定更新节奏并在结尾加关注引导，把高完播的泛流量沉淀成粉丝。"},
  {"title":"补齐搜索关键词布局","body":"在标题与正文嵌入「功能蛋白」「代餐」「早餐」等搜索热词，提升搜索渠道自然流入，减少对算法推荐的单一依赖。"}],
 "viewsByPost":[{"name":r["title"][:10],"views":r["views"],"cover":r["cover"]} for r in views_by_post],
 "sourceMix":source_mix,
 "scatter":[{"title":r["title"][:12],"eng":r["eng"],"views":r["views"],"newFans":r["newFans"]} for r in rows]
}
json.dump(insights, open("data/insights.json","w"), ensure_ascii=False, separators=(',',':'))
print("insights written")
print("totals",T)
print("viral share views",share('views'),"inter",share('inter'),"newFans",share('newFans'))
print("source_mix",source_mix)
