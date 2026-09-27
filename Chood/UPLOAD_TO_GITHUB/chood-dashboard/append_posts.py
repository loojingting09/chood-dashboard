# -*- coding: utf-8 -*-
# ADDITIVE: loads existing posts.json (6 posts) and appends 5 new posts. Existing untouched.
import json, math, datetime

def imp_trend(start, days, total):
    m,d = map(int, start.split('-')); base = datetime.date(2026, m, d)
    raw = [math.exp(-i/3.1) for i in range(days)]
    if days > 4: raw[3] += raw[0]*0.35
    s = sum(raw); vals = [max(1, round(total*r/s)) for r in raw]
    return [{"d": (base+datetime.timedelta(days=i)).strftime("%m-%d"), "v": vals[i]} for i in range(days)]

HRS = ["21:00","23:00","01:00","03:00","05:00","07:00","09:00","11:00","13:00","15:00","17:00","19:00",
       "21:00","23:00","01:00","03:00","05:00","07:00","09:00","11:00","13:00","15:00","17:00","19:00"]
def spike(peaks, baseline, scale=1.0):
    out=[]
    for i in range(24):
        v=baseline
        for pk,amp in peaks: v += amp*math.exp(-((i-pk)**2)/6.0)
        out.append({"t":HRS[i],"v":round(v*scale,1)})
    return out
def eng_trend(peaks): return spike(peaks,1.5)
def watch_trend(peaks): return spike(peaks,3)
def M(key,label,value,rating,score): return {"key":key,"label":label,"value":value,"rating":rating,"score":score}
def V(value,fans): return {"value":value,"fans":fans}

NEW = []

# ---- 甜品: 小孩子才做选择 (曝光 reconstructed 1723 from channel share) ----
NEW.append({
 "id":"dessert-protein",
 "title":"小孩子才做选择，我甜品和蛋白都要 😋",
 "publishDate":"2026-09-13","type":"视频","status":"笔记状态正常","cover":"/covers/dessert-protein.jpg",
 "dataAsOf":"09-27 00:00",
 "headline":{"views":375,"likes":13,"comments":3},
 "diagnosis":{"window":"诊断统计笔记发布后14天内数据","style":"note",
   "metrics":[M("流量转化","封面点击率","11.8%","较好",60),M("开头吸引力","5秒完播率","45.0%","较好",74),
     M("互动表现","互动率","6.2%","较好",70),M("内容深度","平均观看时长","13.4秒","较好",82),
     M("视频画质","画质得分","5.0","较好",72)],
   "fansGrowth":{"value":0,"median":0,"beat":"—"},
   "ai":"平均观看时长 13.4 秒、超过 88% 同类，完播与画质俱佳；这类「高蛋白甜品/食谱」内容的留存明显优于账号均值，是最值得放大的选题方向。"},
 "overview":{
   "traffic":{"impressions":V(1723,"—"),"views":V(375,"—"),"coverCTR":V("11.8%","—")},
   "impressionsTrend":imp_trend("09-13",13,1723),"impressionsTotal":1723,
   "hook":{"exit2s":V("—","—"),"complete5s":V("45.0%","—")},
   "engagement":{"rate":V("6.2%","17.4%"),"likes":V(13,"46.2%"),"comments":V(3,"33.3%"),
     "collects":V(6,"16.7%"),"quoted":V(0,"0%"),"shares":V(0,"0%")},
   "engagementRateTrend":eng_trend([(20,20),(6,8),(2,6)]),
   "depth":{"avgWatch":V("13.4秒","7.7秒"),"newFans":0,"fullComplete":V("27.1%","30.9%"),"quality":5.0},
   "avgWatchTrend":watch_trend([(2,14),(20,20),(9,6)])},
 "traffic":{"asOf":"最多更新至笔记发布后14天","aiTitle":"视频推荐为主，公域推荐占三成",
   "ai":"超过一半流量来自「视频推荐」，加上「首页推荐」近三成，公域占比健康；说明这条高完播的食谱内容拿到了算法分发。建议围绕「高蛋白甜品」做成系列，稳定喂给推荐池。",
   "sources":[{"name":"视频推荐","pct":55},{"name":"首页推荐","pct":29},{"name":"个人主页","pct":10.2},{"name":"搜索","pct":0.8},{"name":"关注页面","pct":0.8},{"name":"其他来源","pct":4.2}],
   "channelDetail":{"channel":"视频推荐","expToViewRate":"100%","viewToEngRate":"2%",
     "impressions":V(205,"11.9%"),"views":V(205,"55%"),"avgWatch":"4.2秒","likes":3,"comments":1,"collects":0}},
 "audience":{"aiTitle":"海外年轻女性为主，兴趣集中在美食",
   "ai":"观众九成为女性、近九成在海外，25–34 岁为主力，兴趣高度集中在美食与生活记录——与「甜品食谱」选题高度契合。",
   "gender":{"male":7,"female":93},
   "age":[{"band":"<18","pct":7},{"band":"18-24","pct":27},{"band":"25-34","pct":49},{"band":"35-44","pct":13},{"band":">44","pct":4}],
   "city":[{"name":"海外","pct":88}],"cityTier":[{"name":"国外","pct":91},{"name":"新一线","pct":2},{"name":"三线城市","pct":1},{"name":"二线城市","pct":1},{"name":"一线城市","pct":1}],
   "interests":[{"name":"美食","pct":17},{"name":"娱乐","pct":14},{"name":"生活记录","pct":11},{"name":"影视","pct":11}]},
 "content":None})

# ---- 品牌过生日 ----
NEW.append({
 "id":"brand-birthday",
 "title":"第一次给自己的品牌过生日，原来是这种感觉",
 "publishDate":"2026-09-19","type":"视频","status":"笔记状态正常","cover":"/covers/brand-birthday.jpg",
 "dataAsOf":"09-27 00:00",
 "headline":{"views":392,"likes":37,"comments":5},
 "diagnosis":{"window":"诊断统计笔记发布后14天内数据","style":"note",
   "metrics":[M("流量转化","封面点击率","11.3%","较好",58),M("开头吸引力","5秒完播率","37.2%","较好",60),
     M("互动表现","互动率","10.8%","待提升",55),M("内容深度","平均观看时长","7.0秒","较好",50),
     M("视频画质","画质得分","4.1","较好",62)],
   "fansGrowth":{"value":1,"median":0,"beat":"—"},
   "ai":"品牌一周年内容带来全账号第二高互动（37 赞 / 5 评论），互动率 10.8% 接近同类中位；情感向的品牌里程碑选题能有效撬动老观众参与，适合作为固定的品牌节点内容。"},
 "overview":{
   "traffic":{"impressions":V(1184,"17.1%"),"views":V(392,"13.4%"),"coverCTR":V("11.3%","11.8%")},
   "impressionsTrend":imp_trend("09-19",8,1184),"impressionsTotal":1184,
   "hook":{"exit2s":V("19.1%","15.5%"),"complete5s":V("37.2%","44.6%")},
   "engagement":{"rate":V("10.8%","23.1%"),"likes":V(37,"29.7%"),"comments":V(5,"20%"),
     "collects":V(0,"0%"),"quoted":V(0,"0%"),"shares":V(0,"0%")},
   "engagementRateTrend":eng_trend([(8,22),(15,14),(2,8)]),
   "depth":{"avgWatch":V("7秒","4.2秒"),"newFans":1,"fullComplete":V("23.3%","36.5%"),"quality":4.1}},
 "traffic":{"asOf":"最多更新至笔记发布后14天","aiTitle":"视频推荐主导，情感选题带动互动",
   "ai":"超七成流量来自「视频推荐」，公域分发充足；情感向的周年内容把点赞率显著拉高。建议把品牌里程碑（周年、销量节点、上新）做成固定的情感锚点内容。",
   "sources":[{"name":"视频推荐","pct":75.3},{"name":"首页推荐","pct":9.8},{"name":"个人主页","pct":7.5},{"name":"关注页面","pct":2.1},{"name":"搜索","pct":0.5},{"name":"其他来源","pct":4.8}],
   "channelDetail":{"channel":"视频推荐","expToViewRate":"100%","viewToEngRate":"—",
     "impressions":V(293,"24.7%"),"views":V(293,"75.3%"),"avgWatch":"2.8秒","likes":36,"comments":2,"collects":0}},
 "audience":{"aiTitle":"海外年轻女性为主，生活记录/娱乐兴趣突出",
   "ai":"观众九成以上为女性、九成在海外，25–34 岁占 64%；兴趣以生活记录与娱乐为主，情感共鸣型内容命中核心人群。",
   "gender":{"male":7,"female":93},
   "age":[{"band":"<18","pct":3},{"band":"18-24","pct":19},{"band":"25-34","pct":64},{"band":"35-44","pct":11},{"band":">44","pct":3}],
   "city":[{"name":"海外","pct":93}],"cityTier":[{"name":"国外","pct":93},{"name":"新一线","pct":2},{"name":"一线城市","pct":2},{"name":"二线城市","pct":1}],
   "interests":[{"name":"生活记录","pct":15},{"name":"娱乐","pct":15},{"name":"美食","pct":13},{"name":"影视","pct":12}]},
 "content":None})

# ---- 早餐: 今天没有认真生活 (only 数据概览 provided) ----
NEW.append({
 "id":"morning-cup",
 "title":"今天没有认真生活，但认真喝了一杯早餐",
 "publishDate":"2026-09-15","type":"视频","status":"笔记状态正常","cover":"/covers/morning-cup.jpg",
 "dataAsOf":"09-27 00:00",
 "headline":{"views":95,"likes":3,"comments":0},
 "diagnosis":{"window":"诊断统计笔记发布后14天内数据","style":"note",
   "metrics":[M("流量转化","封面点击率","7.1%","待提升",40),M("开头吸引力","5秒完播率","41.1%","较好",62),
     M("互动表现","互动率","3.2%","待提升",38),M("内容深度","平均观看时长","6.6秒","待提升",42),
     M("视频画质","画质得分","—","中等",50)],
   "fansGrowth":{"value":0,"median":0,"beat":"—"},
   "ai":"本篇仅提供「数据概览」截图：封面点击率 7.1% 与互动率 3.2% 偏低，但前 5 秒完播 41.1% 尚可——问题集中在「封面入口」而非内容本身。流量来源与观众画像待补充截图后完善。"},
 "overview":{
   "traffic":{"impressions":V(647,"24.6%"),"views":V(95,"43.6%"),"coverCTR":V("7.1%","8.4%")},
   "impressionsTrend":imp_trend("09-15",11,647),"impressionsTotal":647,
   "hook":{"exit2s":V("33.3%","32%"),"complete5s":V("41.1%","39.2%")},
   "engagement":{"rate":V("3.2%","2.4%"),"likes":V(3,"33.3%"),"comments":V(0,"0%"),
     "collects":V(0,"0%"),"quoted":V(0,"0%"),"shares":V(0,"0%")},
   "engagementRateTrend":eng_trend([(18,12),(20,10),(6,4)]),
   "depth":{"avgWatch":V("6.6秒","7.1秒"),"newFans":0,"fullComplete":V("29.9%","29.4%"),"quality":None}},
 "traffic":None,
 "audience":None,
 "content":None})

# ---- 偷偷准备了很久 (teaser) ----
NEW.append({
 "id":"teaser-launch",
 "title":"偷偷准备了很久，明天就是这一天了 🥹",
 "publishDate":"2026-09-18","type":"视频","status":"笔记状态正常","cover":"/covers/teaser-launch.jpg",
 "dataAsOf":"09-27 00:00",
 "headline":{"views":238,"likes":10,"comments":1},
 "diagnosis":{"window":"诊断统计笔记发布后14天内数据","style":"note",
   "metrics":[M("流量转化","封面点击率","7.8%","待提升",42),M("开头吸引力","5秒完播率","42.1%","较好",60),
     M("互动表现","互动率","5.0%","待提升",40),M("内容深度","平均观看时长","4.2秒","待提升",30),
     M("视频画质","画质得分","5.0","较好",72)],
   "fansGrowth":{"value":0,"median":0,"beat":"—"},
   "ai":"预告/悬念型内容，前 5 秒完播 42% 说明钩子有效，但平均观看仅 4.2 秒、只超 16% 同类——悬念拉开后正片留存不足。作为「造势」内容可用，但需搭配次日正片才能兑现流量。"},
 "overview":{
   "traffic":{"impressions":V(802,"19.8%"),"views":V(238,"15.5%"),"coverCTR":V("7.8%","9.1%")},
   "impressionsTrend":imp_trend("09-18",9,802),"impressionsTotal":802,
   "hook":{"exit2s":V("41.9%","43.5%"),"complete5s":V("42.1%","43.8%")},
   "engagement":{"rate":V("5%","8.1%"),"likes":V(10,"30%"),"comments":V(1,"0%"),
     "collects":V(0,"0%"),"quoted":V(0,"0%"),"shares":V(0,"0%")},
   "engagementRateTrend":eng_trend([(9,14),(15,10),(20,8)]),
   "depth":{"avgWatch":V("4.2秒","9.1秒"),"newFans":0,"fullComplete":V("22.5%","27.1%"),"quality":5.0}},
 "traffic":{"asOf":"最多更新至笔记发布后14天","aiTitle":"视频推荐主导，预告内容公域曝光高",
   "ai":"近八成流量来自「视频推荐」，预告内容拿到了大量公域曝光，但正片留存不足导致转化有限。预告应更短、更聚焦「明天是什么」，把悬念直接指向次日正片。",
   "sources":[{"name":"视频推荐","pct":79.4},{"name":"首页推荐","pct":5.5},{"name":"个人主页","pct":4.2},{"name":"搜索","pct":0.8},{"name":"关注页面","pct":0.4},{"name":"其他来源","pct":9.7}],
   "channelDetail":{"channel":"视频推荐","expToViewRate":"100%","viewToEngRate":"4.2%",
     "impressions":V(189,"23.6%"),"views":V(189,"79.4%"),"avgWatch":"3.3秒","likes":8,"comments":0,"collects":0}},
 "audience":{"aiTitle":"海外年轻女性为主",
   "ai":"观众九成为女性、近八成在海外，25–34 岁占 57%；兴趣以美食为首。人群与账号一致，说明预告触达的是自己的核心受众。",
   "gender":{"male":10,"female":90},
   "age":[{"band":"<18","pct":6},{"band":"18-24","pct":24},{"band":"25-34","pct":57},{"band":"35-44","pct":12},{"band":">44","pct":2}],
   "city":[{"name":"海外","pct":77}],"cityTier":[{"name":"国外","pct":79},{"name":"三线城市","pct":5},{"name":"新一线","pct":3},{"name":"一线城市","pct":3},{"name":"四线城市","pct":3},{"name":"二线城市","pct":2}],
   "interests":[{"name":"美食","pct":15}]},
 "content":None})

# ---- 把CHOOD成分表丢给ChatGPT (图文) ----
NEW.append({
 "id":"chatgpt-ingredients",
 "title":"把CHOOD成分表丢给ChatGPT，结果它不按套路出牌",
 "publishDate":"2026-09-12","type":"图文","status":"笔记状态正常","cover":"/covers/chatgpt-ingredients.jpg",
 "dataAsOf":"09-27 00:00",
 "headline":{"views":119,"likes":5,"comments":2},
 "diagnosis":{"window":"诊断统计笔记发布后14天内数据","style":"note",
   "metrics":[M("流量转化","封面点击率","13.0%","待提升",62),M("笔记涨粉","涨粉数","1","待提升",45),
     M("互动表现","互动率","8.6%","较好",78),M("内容深度","平均观看时长","14.8秒","待提升",50),
     M("内容丰富度","丰富度得分","11.0","较好",85)],
   "fansGrowth":{"value":1,"median":0,"beat":"7%"},
   "ai":"图文形式，互动率 8.6% 与内容丰富度 11.0 均属较好；「把成分表丢给 ChatGPT」的测评角度自带话题性，且个人主页 + 搜索流量占比高（近 46%），适合作为可被搜索沉淀的科普型内容持续做。"},
 "overview":{
   "traffic":{"impressions":V(987,"13.1%"),"views":V(119,"28.4%"),"coverCTR":V("13%","25.6%")},
   "impressionsTrend":imp_trend("09-12",15,987),"impressionsTotal":987,
   "hook":None,
   "engagement":{"rate":V("8.6%","15.2%"),"likes":V(5,"60%"),"comments":V(2,"33.3%"),
     "collects":V(1,"100%"),"quoted":V(0,"0%"),"shares":V(0,"0%")},
   "engagementRateTrend":eng_trend([(9,16),(15,12),(20,10)]),
   "depth":{"avgWatch":V("14.8秒","25.5秒"),"newFans":1,"fullComplete":None,"quality":None}},
 "traffic":{"asOf":"最多更新至笔记发布后14天","aiTitle":"个人主页与搜索主导，科普内容可沉淀",
   "ai":"流量结构与视频不同：个人主页近四成、搜索 + 关注合计约一成，说明这类科普/测评图文更依赖主页访客与搜索沉淀，而非公域爆发。建议在标题正文嵌入「成分」「代餐」「蛋白」等搜索词，做成可长期被搜到的内容资产。",
   "sources":[{"name":"个人主页","pct":39.7},{"name":"首页推荐","pct":34.5},{"name":"搜索","pct":6},{"name":"关注页面","pct":4.3},{"name":"其他来源","pct":15.5}],
   "channelDetail":{"channel":"个人主页","expToViewRate":"21.3%","viewToEngRate":"10.9%",
     "impressions":V(216,"21.9%"),"views":V(46,"39.7%"),"avgWatch":"12.6秒","likes":3,"comments":1,"collects":1}},
 "audience":{"aiTitle":"海外年轻女性为主，25–34 岁高度集中",
   "ai":"观众八成以上为女性、96% 在海外，25–34 岁占 69%；科普型内容吸引的仍是核心的成熟女性人群，适合承接产品成分与功效教育。",
   "gender":{"male":17,"female":83},
   "age":[{"band":"<18","pct":4},{"band":"18-24","pct":13},{"band":"25-34","pct":69},{"band":"35-44","pct":12},{"band":">44","pct":3}],
   "city":[{"name":"海外","pct":96},{"name":"杭州","pct":1},{"name":"无锡","pct":1},{"name":"北京","pct":1}],
   "cityTier":[{"name":"国外","pct":96},{"name":"新一线","pct":1},{"name":"一线城市","pct":1},{"name":"二线城市","pct":1}],
   "interests":[{"name":"美食","pct":17},{"name":"娱乐","pct":12},{"name":"生活记录","pct":9}]},
 "content":None})

# ---- merge additively ----
posts = json.load(open("data/posts.json"))
existing_ids = {p["id"] for p in posts}
added=[]
for p in NEW:
    if p["id"] in existing_ids:
        print("SKIP dup:", p["id"]); continue
    posts.append(p); added.append(p["id"])
json.dump(posts, open("data/posts.json","w"), ensure_ascii=False, separators=(",",":"))
print("total posts:", len(posts), "| added:", added)
