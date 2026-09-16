# -*- coding: utf-8 -*-
import json, math

# ---------- trend generators ----------
def imp_trend(start, days, total, peak_frac=0.34):
    """decaying daily impressions summing ~ total, starting at date label start (mm-dd)."""
    import datetime
    m,d = map(int, start.split('-'))
    base = datetime.date(2026, m, d)
    raw = [math.exp(-i/3.1) for i in range(days)]
    raw[0] *= 1.0
    # small secondary bump
    if days > 4: raw[3] += raw[0]*0.35
    s = sum(raw)
    vals = [max(1, round(total*r/s)) for r in raw]
    return [{"d": (base+datetime.timedelta(days=i)).strftime("%m-%d"), "v": vals[i]} for i in range(days)]

HRS = ["21:00","23:00","01:00","03:00","05:00","07:00","09:00","11:00","13:00","15:00","17:00","19:00",
       "21:00","23:00","01:00","03:00","05:00","07:00","09:00","11:00","13:00","15:00","17:00","19:00"]
def spike_trend(peaks, baseline=2, scale=1.0):
    """24 hourly points with spikes at given indices."""
    out=[]
    for i in range(24):
        v = baseline
        for pk,amp in peaks:
            v += amp*math.exp(-((i-pk)**2)/6.0)
        out.append({"t":HRS[i], "v": round(v*scale,1)})
    return out

def eng_trend(peaks): return spike_trend(peaks, baseline=1.5)
def watch_trend(peaks): return spike_trend(peaks, baseline=3)

# ---------- posts ----------
posts = []

# P1 (existing) hello-chood — keep
posts.append(json.load(open("data/posts.json"))[0])

# helper for metric
def M(key,label,value,rating,score): return {"key":key,"label":label,"value":value,"rating":rating,"score":score}
def V(value,fans): return {"value":value,"fans":fans}

# ---- P2 VIRAL: 药剂师裸辞创业 ----
posts.append({
 "id":"pharmacist-founder",
 "title":"药剂师裸辞创业｜想找第一批 Chood 精神股东",
 "publishDate":"2026-08-21","type":"视频","status":"笔记状态正常","cover":"/covers/viral.jpg",
 "dataAsOf":"09-05 00:00",
 "headline":{"views":4301,"likes":169,"comments":139},
 "diagnosis":{"window":"诊断统计笔记发布后14天内数据","style":"note",
   "metrics":[M("流量转化","封面点击率","12.7%","待提升",55),M("笔记涨粉","涨粉数","65","较好",80),
     M("互动表现","互动率","8.8%","较好",88),M("内容深度","平均观看时长","18.9秒","较好",76),
     M("内容丰富度","丰富度得分","8.0","较好",82)],
   "fansGrowth":{"value":65,"median":0,"beat":"90%"},
   "ai":"封面点击率超过 12% 同类笔记，但封面视觉主体明确、文案信息密度较高，在双列流中略不够吸睛。涨粉能力突出，「精神股东」互动玩法成功把单向阅读转为双向互动。"},
 "overview":{
   "traffic":{"impressions":V(35194,"1.9%"),"views":V(4301,"8.6%"),"coverCTR":V("12.7%","50.1%")},
   "impressionsTrend":imp_trend("08-21",15,35194),"impressionsTotal":35194,
   "hook":None,
   "engagement":{"rate":V("8.8%","51.2%"),"likes":V(169,"36.5%"),"comments":V(139,"78.1%"),
     "collects":V(30,"38.7%"),"quoted":V(0,"0%"),"shares":V(14,"4.3%")},
   "engagementRateTrend":eng_trend([(9,18),(15,26),(3,10)]),
   "depth":{"avgWatch":V("16.5秒","19.7秒"),"newFans":66,"fullComplete":None,"quality":None},
   "avgWatchTrend":watch_trend([(2,26),(9,18),(15,24)])},
 "traffic":{"asOf":"最多更新至笔记发布后14天","aiTitle":"首页推荐主导流量，互动玩法成效显著",
   "ai":"本篇笔记近九成流量来自首页推荐，互动率极高。相比过往笔记，「精神股东」的编号认领玩法成功激发评论热情，将单向阅读转为双向互动。建议延续此类参与感选题，同时优化标题关键词，提升搜索渠道的自然流入占比。",
   "sources":[{"name":"首页推荐","pct":89.9},{"name":"个人主页","pct":5.5},{"name":"搜索","pct":1.3},{"name":"关注页面","pct":0.2},{"name":"其他来源","pct":3.1}],
   "channelDetail":{"channel":"首页推荐","expToViewRate":"11.8%","viewToEngRate":"8.7%",
     "impressions":V(31472,"93.3%"),"views":V(3703,"89.9%"),"avgWatch":"16.4秒","likes":171,"comments":124,"collects":26}},
 "audience":{"aiTitle":"海外年轻女性是核心受众群体",
   "ai":"笔记观众九成以上位于海外，女性占比超八成，主力为 25–34 岁职场人群。相比前篇，职场兴趣标签上升，显示创业故事成功吸引目标客群。建议延续「养成系」互动，强化产品功能与创业日常的结合，以稳固这批高粘性用户。",
   "gender":{"male":21,"female":79},
   "age":[{"band":"<18","pct":5},{"band":"18-24","pct":20},{"band":"25-34","pct":61},{"band":"35-44","pct":13},{"band":">44","pct":2}],
   "city":[{"name":"海外","pct":99}],"cityTier":[{"name":"国外","pct":99}],
   "interests":[{"name":"美食","pct":15},{"name":"娱乐","pct":12},{"name":"生活记录","pct":12},{"name":"职场","pct":8},{"name":"影视","pct":7},{"name":"美妆","pct":5}]},
 "content":{"summary":"评论区高度活跃，核心围绕「精神股东」认领与产品共创。",
   "topics":[
     {"topic":"精神股东报到热潮","share":80,"note":"大量用户以编号报到（如「174报到」「28号B」），形成强烈的参与感与社群认同。建议持续鼓励报到、定期公布股东人数里程碑。"},
     {"topic":"内容偏好投票","share":15,"note":"用户通过 ABCD 选项表达偏好，创业日常与品牌成长两类呼声最高。优先产出这两类内容。"},
     {"topic":"产品兴趣与建议","share":5,"note":"少数用户表达产品兴趣，如口味、补剂搭配。可考虑收集众筹/预售意向。"}]}
})

# ---- P3: source-diff 蛋白粉别只看几克 ----
posts.append({
 "id":"source-difference",
 "title":"蛋白粉别只看几克，来源真的有差",
 "publishDate":"2026-08-31","type":"图文","status":"笔记状态正常","cover":"/covers/source-difference.jpg",
 "dataAsOf":"09-15 00:00",
 "headline":{"views":164,"likes":4,"comments":1},
 "diagnosis":{"window":"诊断统计笔记发布后14天内数据","style":"note",
   "metrics":[M("流量转化","封面点击率","9.4%","待提升",45),M("笔记涨粉","涨粉数","0","待提升",30),
     M("互动表现","互动率","4.3%","待提升",42),M("内容深度","平均观看时长","20.1秒","较好",74),
     M("内容丰富度","丰富度得分","5.0","较好",68)],
   "fansGrowth":{"value":0,"median":0,"beat":"0%"},
   "ai":"科普向内容深度良好，但封面点击率与涨粉偏弱。封面缺乏吸睛主体，标题偏理性说明。建议用更具冲突感或利益点的封面文案提升点击。"},
 "overview":{
   "traffic":{"impressions":V(1787,"9%"),"views":V(164,"11%"),"coverCTR":V("9.5%","12%")},
   "impressionsTrend":imp_trend("08-31",15,1787),"impressionsTotal":1787,
   "hook":None,
   "engagement":{"rate":V("4.3%","22.2%"),"likes":V(4,"75%"),"comments":V(1,"50%"),
     "collects":V(1,"0%"),"quoted":V(0,"0%"),"shares":V(0,"0%")},
   "engagementRateTrend":eng_trend([(9,12),(15,38)]),
   "depth":{"avgWatch":V("18.9秒","13.7秒"),"newFans":0,"fullComplete":None,"quality":None},
   "avgWatchTrend":watch_trend([(9,20),(15,50)])},
 "traffic":{"asOf":"最多更新至笔记发布后14天","aiTitle":"首页推荐为主，公域获取一般",
   "ai":"流量以首页推荐为主（61.1%），但整体曝光量偏低。科普型选题在公域的钩子不足，建议在标题与封面强化「来源差异」的具体利益点，提升点击与转化。",
   "sources":[{"name":"首页推荐","pct":61.1},{"name":"个人主页","pct":25.9},{"name":"搜索","pct":1.2},{"name":"其他来源","pct":11.8}],
   "channelDetail":{"channel":"首页推荐","expToViewRate":"8.7%","viewToEngRate":"6.1%",
     "impressions":V(1139,"64.7%"),"views":V(99,"61.1%"),"avgWatch":"6.9秒","likes":3,"comments":1,"collects":1}},
 "audience":{"aiTitle":"海外年轻女性为主，男性占比略升",
   "ai":"观众仍以海外 25–34 岁女性为主，但男性占比升至三成，健身减肥兴趣上升，与「蛋白质来源」科普主题契合。可针对健身人群做更精准的成分对比内容。",
   "gender":{"male":33,"female":67},
   "age":[{"band":"<18","pct":0},{"band":"18-24","pct":25},{"band":"25-34","pct":53},{"band":"35-44","pct":17},{"band":">44","pct":5}],
   "city":[{"name":"海外","pct":82},{"name":"香港","pct":2},{"name":"上海","pct":1},{"name":"深圳","pct":1}],
   "cityTier":[{"name":"国外","pct":85},{"name":"一线城市","pct":4},{"name":"新一线","pct":3},{"name":"三线城市","pct":2},{"name":"二线城市","pct":2}],
   "interests":[{"name":"美食","pct":15},{"name":"生活记录","pct":11},{"name":"娱乐","pct":10},{"name":"健身减肥","pct":9},{"name":"影视","pct":8},{"name":"美妆","pct":5}]},
 "content":None
})

# ---- P4: why-chood 蛋白粉这么多，为什么还做Chood ----
posts.append({
 "id":"why-chood",
 "title":"蛋白粉这么多，为什么还做Chood？",
 "publishDate":"2026-08-29","type":"视频","status":"笔记状态正常","cover":"/covers/why-chood.jpg",
 "dataAsOf":"09-13 00:00",
 "headline":{"views":237,"likes":9,"comments":3},
 "diagnosis":{"window":"诊断统计笔记发布后14天内数据","style":"video",
   "metrics":[M("流量转化","封面点击率","9.3%","较好",70),M("开头吸引力","5秒完播率","36.2%","待提升",44),
     M("互动表现","互动率","5.7%","较好",72),M("内容深度","平均观看时长","8.6秒","待提升",42),
     M("视频画质","画质得分","3.5","较好",70)],
   "fansGrowth":{"value":0,"median":0,"beat":"40%"},
   "ai":"视频开头 5 秒是留住观众的黄金时间。当前 5 秒完播率 36.2%，略低于同类中位。建议优化开头节奏、制造悬念或利益前置，提升开头吸引力。"},
 "overview":{
   "traffic":{"impressions":V(1057,"21%"),"views":V(237,"25.3%"),"coverCTR":V("9.8%","14.3%")},
   "impressionsTrend":imp_trend("08-29",15,1057),"impressionsTotal":1057,
   "hook":{"exit2s":V("39.1%","34.4%"),"complete5s":V("37.4%","53.7%")},
   "engagement":{"rate":V("5.7%","16.7%"),"likes":V(9,"77.8%"),"comments":V(3,"66.7%"),
     "collects":V(1,"100%"),"quoted":V(0,"0%"),"shares":V(0,"0%")},
   "engagementRateTrend":eng_trend([(6,30),(14,42),(20,20)]),
   "depth":{"avgWatch":V("16.2秒","9.5秒"),"newFans":0,"fullComplete":V("20%","32.8%"),"quality":3.5},
   "avgWatchTrend":watch_trend([(4,30),(13,20),(20,28)])},
 "traffic":{"asOf":"最多更新至笔记发布后14天","aiTitle":"视频推荐主导，公域曝光待提升",
   "ai":"流量近七成来自视频推荐（65.2%），首页推荐占比偏低。品牌立场类内容互动尚可，但公域点击钩子不足。建议在开头强化「为什么」的冲突点，并在标题嵌入搜索热词。",
   "sources":[{"name":"视频推荐","pct":65.2},{"name":"个人主页","pct":18.9},{"name":"首页推荐","pct":6.6},{"name":"搜索","pct":1.3},{"name":"关注页面","pct":0.9},{"name":"其他来源","pct":7.1}],
   "channelDetail":{"channel":"视频推荐","expToViewRate":"—","viewToEngRate":"0.7%",
     "impressions":V(148,"14.6%"),"views":V(148,"65.2%"),"avgWatch":"4.9秒","likes":1,"comments":0,"collects":0}},
 "audience":{"aiTitle":"海外年轻女性为核心，泛生活兴趣","ai":"观众以海外 25–34 岁女性为主（83%），兴趣偏娱乐与美食。品牌理念类内容触达面较广，但需更强的开头钩子把泛流量转为深度观看。",
   "gender":{"male":17,"female":83},
   "age":[{"band":"<18","pct":4},{"band":"18-24","pct":17},{"band":"25-34","pct":56},{"band":"35-44","pct":19},{"band":">44","pct":4}],
   "city":[{"name":"海外","pct":88}],
   "cityTier":[{"name":"国外","pct":91},{"name":"二线城市","pct":2},{"name":"新一线","pct":1},{"name":"三线城市","pct":1},{"name":"一线城市","pct":1}],
   "interests":[{"name":"娱乐","pct":14},{"name":"美食","pct":13},{"name":"生活记录","pct":11},{"name":"影视","pct":11},{"name":"美妆","pct":5}]},
 "content":None
})

# ---- P5: sleep30 有了这个，我早上真的敢多睡30分钟 ----
posts.append({
 "id":"sleep-30",
 "title":"有了这个，我早上真的敢多睡30分钟 😴",
 "publishDate":"2026-09-05","type":"视频","status":"笔记状态正常","cover":"/covers/sleep-30.jpg",
 "dataAsOf":"09-16 00:00",
 "headline":{"views":205,"likes":5,"comments":4},
 "diagnosis":{"window":"诊断统计笔记发布后14天内数据","style":"video",
   "metrics":[M("流量转化","封面点击率","9.7%","较好",72),M("开头吸引力","5秒完播率","37.6%","较好",70),
     M("互动表现","互动率","4.9%","较好",70),M("内容深度","平均观看时长","12.8秒","较好",78),
     M("视频画质","画质得分","4.1","较好",78)],
   "fansGrowth":{"value":0,"median":0,"beat":"86%"},
   "ai":"内容深度表现不错，平均观看 12.8 秒超过 86% 同类。可继续放大「省时」的生活痛点，把功能利益转化为具体场景。"},
 "overview":{
   "traffic":{"impressions":V(776,"19.8%"),"views":V(205,"18%"),"coverCTR":V("9.7%","15%")},
   "impressionsTrend":imp_trend("09-05",11,776),"impressionsTotal":776,
   "hook":{"exit2s":V("33.9%","32.1%"),"complete5s":V("37.6%","51.9%")},
   "engagement":{"rate":V("4.9%","18.9%"),"likes":V(5,"80%"),"comments":V(4,"50%"),
     "collects":V(1,"100%"),"quoted":V(0,"0%"),"shares":V(0,"0%")},
   "engagementRateTrend":eng_trend([(8,32),(14,10)]),
   "depth":{"avgWatch":V("12.8秒","5.6秒"),"newFans":0,"fullComplete":V("26.5%","42.6%"),"quality":4.1},
   "avgWatchTrend":watch_trend([(9,50),(14,18)])},
 "traffic":{"asOf":"最多更新至笔记发布后14天","aiTitle":"视频推荐主导，生活场景选题有潜力",
   "ai":"流量近七成来自视频推荐（68.8%）。「省时/懒人早餐」的生活场景切入点算法接受度高。建议围绕具体时间场景做系列，强化搜索关键词布局。",
   "sources":[{"name":"视频推荐","pct":68.8},{"name":"首页推荐","pct":10.2},{"name":"个人主页","pct":10.2},{"name":"关注页面","pct":1.5},{"name":"搜索","pct":1.0},{"name":"其他来源","pct":8.3}],
   "channelDetail":{"channel":"视频推荐","expToViewRate":"—","viewToEngRate":"0.7%",
     "impressions":V(141,"18.2%"),"views":V(141,"68.8%"),"avgWatch":"12.5秒","likes":1,"comments":0,"collects":0}},
 "audience":{"aiTitle":"海外年轻女性高度集中","ai":"女性占比 91%，25–34 岁为主，兴趣美食与娱乐。省时场景对忙碌女性人群精准，可延伸「上班族早餐」系列。",
   "gender":{"male":9,"female":91},
   "age":[{"band":"<18","pct":2},{"band":"18-24","pct":19},{"band":"25-34","pct":55},{"band":"35-44","pct":20},{"band":">44","pct":4}],
   "city":[{"name":"海外","pct":96}],
   "cityTier":[{"name":"国外","pct":96},{"name":"新一线","pct":1},{"name":"二线城市","pct":1}],
   "interests":[{"name":"美食","pct":15},{"name":"娱乐","pct":14},{"name":"影视","pct":14},{"name":"生活记录","pct":12},{"name":"宠物","pct":3},{"name":"美妆","pct":3}]},
 "content":None
})

# ---- P6: week2 小品牌上小红书第2周 ----
posts.append({
 "id":"week-2",
 "title":"小品牌上小红书第2周：开始没东西发了",
 "publishDate":"2026-09-07","type":"视频","status":"笔记状态正常","cover":"/covers/week-2.jpg",
 "dataAsOf":"09-16 00:00",
 "headline":{"views":181,"likes":11,"comments":0},
 "diagnosis":{"window":"诊断统计笔记发布后14天内数据","style":"video",
   "metrics":[M("流量转化","封面点击率","9.8%","较好",72),M("开头吸引力","5秒完播率","36.8%","较好",70),
     M("互动表现","互动率","6.1%","较好",74),M("内容深度","平均观看时长","17.1秒","较好",82),
     M("视频画质","画质得分","4.8","较好",84)],
   "fansGrowth":{"value":2,"median":0,"beat":"93%"},
   "ai":"内容深度突出，平均观看 17.1 秒超过 93% 同类，说明「创业幕后」题材有用、有趣、有讨论度。建议固定为系列栏目，并在结尾加关注引导。"},
 "overview":{
   "traffic":{"impressions":V(887,"15.4%"),"views":V(181,"26.5%"),"coverCTR":V("9.8%","15%")},
   "impressionsTrend":imp_trend("09-07",10,887),"impressionsTotal":887,
   "hook":{"exit2s":V("34.1%","26.3%"),"complete5s":V("36.8%","45.8%")},
   "engagement":{"rate":V("6.1%","14.6%"),"likes":V(11,"63.6%"),"comments":V(0,"0%"),
     "collects":V(0,"0%"),"quoted":V(0,"0%"),"shares":V(0,"0%")},
   "engagementRateTrend":eng_trend([(1,10),(6,4)]),
   "depth":{"avgWatch":V("17.1秒","7.1秒"),"newFans":2,"fullComplete":V("32.9%","35.6%"),"quality":4.8},
   "avgWatchTrend":watch_trend([(1,12),(9,8)])},
 "traffic":{"asOf":"最多更新至笔记发布后14天","aiTitle":"视频推荐为主，创业系列黏性高",
   "ai":"流量近六成来自视频推荐（59.1%），首页推荐占比回升至 19.3%。「创业幕后」题材完播率高、黏性强。建议固定更新节奏，并设计评论钩子把高完播转为互动。",
   "sources":[{"name":"视频推荐","pct":59.1},{"name":"首页推荐","pct":19.3},{"name":"个人主页","pct":13.3},{"name":"关注页面","pct":1.7},{"name":"搜索","pct":1.1},{"name":"其他来源","pct":5.5}],
   "channelDetail":{"channel":"视频推荐","expToViewRate":"—","viewToEngRate":"6.5%",
     "impressions":V(107,"12.1%"),"views":V(107,"59.1%"),"avgWatch":"3.5秒","likes":7,"comments":0,"collects":0}},
 "audience":{"aiTitle":"海外年轻受众，男性占比回升","ai":"女性占比 76%，25–34 岁为核心，生活记录与娱乐兴趣突出。创业纪实题材吸引泛人群，建议用「关注追更」引导把泛流量沉淀为粉丝。",
   "gender":{"male":24,"female":76},
   "age":[{"band":"<18","pct":3},{"band":"18-24","pct":26},{"band":"25-34","pct":59},{"band":"35-44","pct":9},{"band":">44","pct":3}],
   "city":[{"name":"海外","pct":79},{"name":"北京","pct":3},{"name":"上海","pct":1},{"name":"深圳","pct":1}],
   "cityTier":[{"name":"国外","pct":80},{"name":"一线城市","pct":8},{"name":"二线城市","pct":4},{"name":"新一线","pct":3},{"name":"三线城市","pct":1}],
   "interests":[{"name":"生活记录","pct":14},{"name":"娱乐","pct":14},{"name":"美食","pct":11},{"name":"影视","pct":11},{"name":"职场","pct":5},{"name":"宠物","pct":3}]},
 "content":None
})

with open("data/posts.json","w") as f:
    json.dump(posts, f, ensure_ascii=False, separators=(',',':'))

print("posts:", len(posts))
for p in posts:
    print(" -", p["publishDate"], p["id"], "views", p["headline"]["views"])
