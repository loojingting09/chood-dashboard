# -*- coding: utf-8 -*-
# ADDITIVE batch 3: append 3 new posts to posts.json (keep existing). No covers provided this batch.
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

NEW=[]

# ---- 蛋白饮做废19版 ----
NEW.append({
 "id":"protein-19-versions",
 "title":"为了一杯敢给大家喝的蛋白饮，做废了19版",
 "publishDate":"2026-09-21","type":"视频","status":"笔记状态正常","cover":None,
 "dataAsOf":"10-02 00:00",
 "headline":{"views":280,"likes":7,"comments":5},
 "diagnosis":{"window":"诊断统计笔记发布后14天内数据","style":"note",
   "metrics":[M("流量转化","封面点击率","11.6%","较好",60),M("开头吸引力","5秒完播率","45.3%","较好",74),
     M("互动表现","互动率","4.3%","较好",58),M("内容深度","平均观看时长","3.5秒","待提升",28),
     M("视频画质","画质得分","5.0","较好",72)],
   "fansGrowth":{"value":1,"median":0,"beat":"—"},
   "ai":"封面点击率 11.6% 与前 5 秒完播 45.3% 都不错，钩子有效；但平均观看仅 3.5 秒、只超 8% 同类——「研发故事」开头抓人、后段留不住。建议把 19 版试错的高潮前置，压缩中段。"},
 "overview":{
   "traffic":{"impressions":V(1367,"11.9%"),"views":V(280,"16.7%"),"coverCTR":V("11.6%","17%")},
   "impressionsTrend":imp_trend("09-21",11,1367),"impressionsTotal":1367,
   "hook":{"exit2s":V("31.2%","30.5%"),"complete5s":V("45.3%","47.5%")},
   "engagement":{"rate":V("4.3%","8.7%"),"likes":V(7,"50%"),"comments":V(5,"20%"),
     "collects":V(0,"0%"),"quoted":V(0,"0%"),"shares":V(1,"0%")},
   "engagementRateTrend":eng_trend([(9,12),(15,10),(2,6)]),
   "depth":{"avgWatch":V("3.5秒","3.1秒"),"newFans":1,"fullComplete":V("24.9%","24.6%"),"quality":5.0}},
 "traffic":{"asOf":"最多更新至笔记发布后14天","aiTitle":"视频推荐为主，公域曝光健康",
   "ai":"视频推荐过半、首页推荐三成，公域分发不错；问题在正片留存而非曝光。研发/试错题材自带信任感，建议保留但把节奏做紧。",
   "sources":[{"name":"视频推荐","pct":50.7},{"name":"首页推荐","pct":32.2},{"name":"个人主页","pct":5.1},{"name":"关注页面","pct":2.9},{"name":"搜索","pct":0.7},{"name":"其他来源","pct":8.4}],
   "channelDetail":{"channel":"视频推荐","expToViewRate":"100%","viewToEngRate":"2.1%",
     "impressions":V(140,"10.2%"),"views":V(140,"50.7%"),"avgWatch":"2.6秒","likes":2,"comments":0,"collects":0}},
 "audience":{"aiTitle":"海外年轻女性为主，35–44 岁占比偏高",
   "ai":"观众八成为女性、近九成在海外，25–34 岁为主力、35–44 岁占到 24%——研发/品质向内容吸引的人群更成熟。",
   "gender":{"male":19,"female":81},
   "age":[{"band":"<18","pct":3},{"band":"18-24","pct":13},{"band":"25-34","pct":55},{"band":"35-44","pct":24},{"band":">44","pct":4}],
   "city":[{"name":"海外","pct":86},{"name":"成都","pct":1},{"name":"上海","pct":1}],
   "cityTier":[{"name":"国外","pct":88},{"name":"新一线","pct":4},{"name":"一线城市","pct":2},{"name":"二线城市","pct":2},{"name":"五线城市","pct":1},{"name":"三线城市","pct":1}],
   "interests":[]},
 "content":None})

# ---- 1岁生日不收礼 (图文, breakout) ----
NEW.append({
 "id":"anniversary-giveaway",
 "title":"1岁生日不收礼，这次换我们送你们 🎂🎁",
 "publishDate":"2026-09-20","type":"图文","status":"笔记状态正常","cover":None,
 "dataAsOf":"10-02 00:00",
 "headline":{"views":1283,"likes":78,"comments":120},
 "diagnosis":{"window":"诊断统计笔记发布后14天内数据","style":"note",
   "metrics":[M("流量转化","封面点击率","12.0%","待提升",55),M("笔记涨粉","涨粉数","39","较好",80),
     M("互动表现","互动率","19.3%","较好",90),M("内容深度","平均观看时长","9.6秒","待提升",48),
     M("内容丰富度","丰富度得分","11.0","较好",85)],
   "fansGrowth":{"value":39,"median":0,"beat":"—"},
   "ai":"全账号互动密度最高的一篇：19.3% 互动率、120 条评论、+39 涨粉（近 30 日涨粉第一）。生日抽奖的「给粉丝送礼」机制把祝福直接转成评论与关注。唯一短板是封面点击率 12%、略低于同类中位——入口还能更强。"},
 "overview":{
   "traffic":{"impressions":V(11485,"3.7%"),"views":V(1283,"11.2%"),"coverCTR":V("12%","28.7%")},
   "impressionsTrend":imp_trend("09-20",12,11485),"impressionsTotal":11485,
   "hook":None,
   "engagement":{"rate":V("19.3%","81.1%"),"likes":V(78,"50%"),"comments":V(120,"37.2%"),
     "collects":V(49,"65.3%"),"quoted":V(0,"0%"),"shares":V(4,"50%")},
   "engagementRateTrend":eng_trend([(8,30),(15,20),(2,10)]),
   "depth":{"avgWatch":V("9.6秒","18.7秒"),"newFans":39,"fullComplete":None,"quality":None}},
 "traffic":{"asOf":"最多更新至笔记发布后14天","aiTitle":"首页推荐主导，抽奖机制引爆互动",
   "ai":"近九成流量来自首页推荐——抽奖+生日的强钩子进入了公域大池，互动率 16.8% 远高于日常。这类「给粉丝发福利」的节点内容最能把公域流量转成评论与关注，值得固定做（周年/销量节点/上新）。",
   "sources":[{"name":"首页推荐","pct":86.5},{"name":"个人主页","pct":3.1},{"name":"关注页面","pct":1.6},{"name":"搜索","pct":0.9},{"name":"其他来源","pct":7.9}],
   "channelDetail":{"channel":"首页推荐","expToViewRate":"10.6%","viewToEngRate":"16.8%",
     "impressions":V(10422,"90.7%"),"views":V(1103,"86.5%"),"avgWatch":"8.1秒","likes":78,"comments":64,"collects":43}},
 "audience":{"aiTitle":"海外年轻女性高度集中，女性占 98%",
   "ai":"女性占 98%、海外占 98%，25–34 岁为主；生日福利内容几乎全部命中核心女性粉丝，是巩固粘性的最佳载体。",
   "gender":{"male":2,"female":98},
   "age":[{"band":"<18","pct":3},{"band":"18-24","pct":27},{"band":"25-34","pct":54},{"band":"35-44","pct":13},{"band":">44","pct":2}],
   "city":[{"name":"海外","pct":98}],"cityTier":[{"name":"国外","pct":99}],
   "interests":[{"name":"美食","pct":18},{"name":"生活记录","pct":12},{"name":"娱乐","pct":11},{"name":"美妆","pct":7}]},
 "content":{"summary":"评论区被生日祝福刷屏，并延伸到抽奖互动——是全账号互动密度最高的一篇。",
   "topics":[
     {"topic":"生日祝福刷屏","share":95,"note":"评论区被「Happy Birthday Chood」刷屏，用户纷纷送上祝福，表达对品牌的支持与喜爱。建议及时感谢粉丝祝福，可制作感谢视频或图文，增强粉丝粘性。"},
     {"topic":"抽奖互动热情","share":5,"note":"部分用户询问抽奖细节、表达对生日礼物的期待（如「sauna 加按摩🔥」）。建议及时回复抽奖疑问，增加互动趣味性。"}]}})

# ---- 这一年，CHOOD 最珍贵的 ----
NEW.append({
 "id":"one-year-reflection",
 "title":"这一年，CHOOD 最珍贵的，不是卖出了多少盒",
 "publishDate":"2026-09-26","type":"视频","status":"笔记状态正常","cover":None,
 "dataAsOf":"10-02 00:00",
 "headline":{"views":143,"likes":5,"comments":1},
 "diagnosis":{"window":"诊断统计笔记发布后14天内数据","style":"note",
   "metrics":[M("流量转化","封面点击率","9.9%","较好",56),M("开头吸引力","5秒完播率","28.7%","待提升",42),
     M("互动表现","互动率","3.5%","较好",55),M("内容深度","平均观看时长","6.2秒","待提升",42),
     M("视频画质","画质得分","5.0","较好",72)],
   "fansGrowth":{"value":0,"median":0,"beat":"—"},
   "ai":"情感总结向内容：前 5 秒完播仅 28.7%、只超 34% 同类——开头偏慢，没在黄金 5 秒给出钩子。品牌价值观表达可保留，但需要更强的开场。观看数不足 200，小红书暂未提供评论 AI 分析。"},
 "overview":{
   "traffic":{"impressions":V(524,"18.9%"),"views":V(143,"20.6%"),"coverCTR":V("9.9%","13%")},
   "impressionsTrend":imp_trend("09-26",6,524),"impressionsTotal":524,
   "hook":{"exit2s":V("37.6%","32.4%"),"complete5s":V("28.7%","36.8%")},
   "engagement":{"rate":V("3.5%","10.3%"),"likes":V(5,"75%"),"comments":V(1,"0%"),
     "collects":V(0,"0%"),"quoted":V(0,"0%"),"shares":V(0,"0%")},
   "engagementRateTrend":eng_trend([(9,10),(2,6),(15,6)]),
   "depth":{"avgWatch":V("6.2秒","7.5秒"),"newFans":0,"fullComplete":V("19.3%","23.7%"),"quality":5.0}},
 "traffic":{"asOf":"最多更新至笔记发布后14天","aiTitle":"视频推荐主导，情感向内容公域有量",
   "ai":"七成流量来自视频推荐，公域有量但互动弱（互动率 1%）。情感总结内容更适合做阶段性复盘，不宜频繁，且开头要更快进入主题。",
   "sources":[{"name":"视频推荐","pct":72.3},{"name":"首页推荐","pct":19.9},{"name":"个人主页","pct":2.1},{"name":"关注页面","pct":1.4},{"name":"其他来源","pct":4.3}],
   "channelDetail":{"channel":"视频推荐","expToViewRate":"100%","viewToEngRate":"1%",
     "impressions":V(102,"19.5%"),"views":V(102,"72.3%"),"avgWatch":"5秒","likes":0,"comments":0,"collects":0}},
 "audience":{"aiTitle":"海外年轻女性为主，35–44 岁占比偏高",
   "ai":"女性占九成、海外占近九成，25–34 岁为主、35–44 岁占 20%；兴趣更偏娱乐与影视，情感向内容吸引的人群略有不同。",
   "gender":{"male":10,"female":90},
   "age":[{"band":"<18","pct":5},{"band":"18-24","pct":11},{"band":"25-34","pct":64},{"band":"35-44","pct":20}],
   "city":[{"name":"海外","pct":88}],"cityTier":[{"name":"国外","pct":92},{"name":"新一线","pct":3},{"name":"二线城市","pct":1}],
   "interests":[{"name":"娱乐","pct":15},{"name":"影视","pct":15},{"name":"生活记录","pct":12},{"name":"美食","pct":12},{"name":"二次元","pct":4},{"name":"美妆","pct":4},{"name":"情感","pct":4}]},
 "content":None})

posts=json.load(open("data/posts.json"))
existing={p["id"] for p in posts}
added=[]
for p in NEW:
    if p["id"] in existing: print("SKIP dup:",p["id"]); continue
    posts.append(p); added.append(p["id"])
json.dump(posts, open("data/posts.json","w"), ensure_ascii=False, separators=(",",":"))
print("total:",len(posts),"| added:",added)
