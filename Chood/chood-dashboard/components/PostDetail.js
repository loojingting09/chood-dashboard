"use client";
import { useState } from "react";
import { Donut, RadarPanel, AreaTrend } from "@/components/charts";
import { Kpi, HBars, GenderBar, Legend, AiInsight, RatingPill, PostCover } from "@/components/ui";
import { fmt } from "@/lib/data";

const TABS = ["数据概览", "内容分析", "流量分析", "观众分析"];

export default function PostDetail({ post }) {
  const [tab, setTab] = useState("数据概览");
  const o = post.overview;
  const t = post.traffic;
  const a = post.audience;
  const radar = post.diagnosis.metrics.map((m) => ({ axis: m.key, value: m.score }));

  return (
    <div>
      <div className="card p" style={{ marginBottom: 18 }}>
        <div className="post-head">
          <PostCover cover={post.cover} title={post.title} className="cover" size="big" />
          <div style={{ flex: 1 }}>
            <h1>{post.title}</h1>
            <span className="status">
              <span className="tick">✓</span> {post.status}
            </span>
            <div className="qstats">
              <span>观看 <b className="num">{fmt(post.headline.views)}</b></span>
              <span>点赞 <b className="num">{post.headline.likes}</b></span>
              <span>评论 <b className="num">{post.headline.comments}</b></span>
              <span style={{ color: "var(--muted)" }}>{post.publishDate} · {post.type}</span>
            </div>
          </div>
        </div>
      </div>

      <div className="tabs">
        {TABS.map((tb) => (
          <button key={tb} className={tab === tb ? "active" : ""} onClick={() => setTab(tb)}>
            {tb}
          </button>
        ))}
      </div>

      {tab === "数据概览" && <Overview post={post} o={o} radar={radar} />}
      {tab === "内容分析" && (post.content ? <ContentAnalysis c={post.content} /> : <ContentPending />)}
      {tab === "流量分析" && <Traffic t={t} />}
      {tab === "观众分析" && <Audience a={a} />}
    </div>
  );
}

function Overview({ post, o, radar }) {
  const d = post.diagnosis;
  const e = o.engagement;
  return (
    <div>
      {/* diagnosis */}
      <div className="card p">
        <div className="eyebrow" style={{ marginBottom: 6 }}>
          笔记诊断 · <span style={{ color: "var(--muted-2)" }}>{d.window}</span>
        </div>
        <div className="grid cols-2">
          <RadarPanel data={radar} />
          <div className="hbars" style={{ alignSelf: "center" }}>
            {d.metrics.map((m) => (
              <div key={m.key} style={{ display: "flex", justifyContent: "space-between", alignItems: "center", gap: 10 }}>
                <span style={{ fontSize: 13, color: "#4a4a54" }}>
                  <b>{m.key}</b> · {m.label} {m.value}
                </span>
                <RatingPill rating={m.rating} />
              </div>
            ))}
            <div style={{ borderTop: "1px solid var(--line)", paddingTop: 10, fontSize: 13, color: "#4a4a54" }}>
              笔记涨粉 <b>{d.fansGrowth.value}</b> · 同类中位数 {d.fansGrowth.median} · 超过 <b style={{ color: "var(--xhs)" }}>{d.fansGrowth.beat}</b> 同类
            </div>
          </div>
        </div>
        <div style={{ marginTop: 14 }}>
          <AiInsight title="AI 诊断解读" text={d.ai} />
        </div>
      </div>

      {/* 笔记数据 */}
      <div className="section-title"><h2>笔记数据</h2><span className="hint">数据更新至 {post.dataAsOf}</span></div>

      <div className="eyebrow">1 · 流量转化</div>
      <div className="grid cols-3" style={{ margin: "10px 0 14px" }}>
        <Kpi label="曝光数" value={fmt(o.traffic.impressions.value)} sub={`粉丝占 ${o.traffic.impressions.fans}`} hl />
        <Kpi label="观看数" value={fmt(o.traffic.views.value)} sub={`粉丝占 ${o.traffic.views.fans}`} live />
        <Kpi label="封面点击率" value={o.traffic.coverCTR.value} sub={`粉丝 ${o.traffic.coverCTR.fans}`} />
      </div>
      <div className="card p" style={{ marginBottom: 22 }}>
        <div className="eyebrow" style={{ marginBottom: 10 }}>曝光数趋势图 · 累计 {fmt(o.impressionsTotal)}</div>
        <AreaTrend data={o.impressionsTrend} xKey="d" yKey="v" height={200} unit=" 曝光" />
      </div>

      {o.hook && (
        <>
          <div className="eyebrow">2 · 开头吸引力</div>
          <div className="grid cols-3" style={{ margin: "10px 0 22px" }}>
            <Kpi label="2秒退出率" value={o.hook.exit2s.value} sub={`粉丝 ${o.hook.exit2s.fans}`} />
            <Kpi label="5秒完播率" value={o.hook.complete5s.value} sub={`粉丝 ${o.hook.complete5s.fans}`} hl />
          </div>
        </>
      )}

      <div className="eyebrow">{o.hook ? "3" : "2"} · 互动表现</div>
      <div className="grid cols-3" style={{ margin: "10px 0 14px" }}>
        <Kpi label="互动率" value={e.rate.value} sub={`粉丝占 ${e.rate.fans}`} hl />
        <Kpi label="点赞数" value={e.likes.value} sub={`粉丝占 ${e.likes.fans}`} live />
        <Kpi label="评论数" value={e.comments.value} sub={`粉丝占 ${e.comments.fans}`} live />
        <Kpi label="收藏数" value={e.collects.value} sub={`粉丝占 ${e.collects.fans}`} live />
        <Kpi label="被引用数" value={e.quoted.value} sub={`粉丝占 ${e.quoted.fans}`} />
        <Kpi label="分享数" value={e.shares.value} sub={`粉丝占 ${e.shares.fans}`} live />
      </div>
      <div className="card p" style={{ marginBottom: 22 }}>
        <div className="eyebrow" style={{ marginBottom: 10 }}>互动率趋势图 · 按小时（发布后72小时）</div>
        <AreaTrend data={o.engagementRateTrend} xKey="t" yKey="v" height={190} unit="%" yPct />
      </div>

      <div className="eyebrow">{o.hook ? "4" : "3"} · 内容深度</div>
      <div className="grid cols-3" style={{ margin: "10px 0 14px" }}>
        <Kpi label="平均观看时长" value={o.depth.avgWatch.value} sub={`粉丝 ${o.depth.avgWatch.fans}`} hl />
        {o.depth.fullComplete && <Kpi label="全片完播率" value={o.depth.fullComplete.value} sub={`粉丝 ${o.depth.fullComplete.fans}`} />}
        {o.depth.quality != null && <Kpi label="视频画质得分" value={o.depth.quality} />}
        <Kpi label="涨粉数" value={o.depth.newFans} />
      </div>
      <div className="card p">
        <div className="eyebrow" style={{ marginBottom: 10 }}>平均观看时长趋势图 · 按小时（发布后72小时）</div>
        <AreaTrend data={o.avgWatchTrend} xKey="t" yKey="v" height={190} unit=" 秒" />
      </div>
    </div>
  );
}

function ContentPending() {
  return (
    <div className="card p">
      <div className="notice">
        <span>ℹ️</span>
        <div>
          <b>内容分析数据待补充。</b> 这一栏对应小红书 App 的「内容分析」标签（完播、内容标签等）。
          下次上传这篇笔记的「内容分析」截图，即可自动补齐这一栏。
        </div>
      </div>
    </div>
  );
}

function ContentAnalysis({ c }) {
  return (
    <div>
      <AiInsight title="评论总结" text={c.summary} time="该结果基于评论区内容由 AI 归纳" />
      <div className="section-title"><h2>评论话题分布</h2><span className="hint">用户在聊什么</span></div>
      <div style={{ display: "flex", flexDirection: "column", gap: 14 }}>
        {c.topics.map((tp, i) => (
          <div className="card p" key={i}>
            <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 8 }}>
              <b style={{ fontSize: 15 }}>话题{["一", "二", "三", "四", "五"][i]}：{tp.topic}</b>
              <span className="pill good">占比 {tp.share}%</span>
            </div>
            <div className="hbar-track" style={{ marginBottom: 10 }}>
              <div className="hbar-fill" style={{ width: `${tp.share}%` }} />
            </div>
            <p style={{ margin: 0, fontSize: 13.5, color: "#5c5148", lineHeight: 1.65 }}>{tp.note}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

function Traffic({ t }) {
  const c = t.channelDetail;
  return (
    <div>
      <AiInsight title={t.aiTitle} text={t.ai} time="该结果于 09-15 生成，24小时后可重新分析" />
      <div className="grid cols-2" style={{ marginTop: 18 }}>
        <div className="card p">
          <div className="eyebrow" style={{ marginBottom: 10 }}>观看来源 · {t.asOf}</div>
          <div style={{ display: "flex", alignItems: "center", gap: 18 }}>
            <Donut data={t.sources} size={176} />
            <div style={{ flex: 1 }}>
              <Legend data={t.sources} />
            </div>
          </div>
        </div>
        <div className="card p">
          <div className="eyebrow" style={{ marginBottom: 10 }}>此渠道详细数据 · {c.channel}</div>
          <div className="funnel">
            <div className="fr">
              <span className="lab">曝光数</span>
              <div className="fbar" style={{ width: "100%" }} />
            </div>
            <div className="conv">转化率 {c.expToViewRate}</div>
            <div className="fr">
              <span className="lab">观看数</span>
              <div className="fbar" style={{ width: "36%" }} />
            </div>
            <div className="conv">互动率 {c.viewToEngRate}</div>
            <div className="fr">
              <span className="lab">互动数</span>
              <div className="fbar" style={{ width: "9%" }} />
            </div>
          </div>
          <div className="mini-grid">
            <div className="mini"><div className="ml">曝光数 · 占总曝光 {c.impressions.share}</div><div className="mv num">{fmt(c.impressions.value)}</div></div>
            <div className="mini"><div className="ml">观看数 · 占总观看 {c.views.share}</div><div className="mv num">{fmt(c.views.value)}</div></div>
            <div className="mini"><div className="ml">平均观看时长</div><div className="mv">{c.avgWatch}</div></div>
            <div className="mini"><div className="ml">点赞 / 评论 / 收藏</div><div className="mv num">{c.likes} / {c.comments} / {c.collects}</div></div>
          </div>
        </div>
      </div>
    </div>
  );
}

function Audience({ a }) {
  return (
    <div>
      <AiInsight title={a.aiTitle} text={a.ai} time="该结果于 09-15 生成" />
      <div className="grid cols-2" style={{ marginTop: 18 }}>
        <div className="card p">
          <div className="eyebrow" style={{ marginBottom: 14 }}>性别分布</div>
          <GenderBar male={a.gender.male} female={a.gender.female} />
          <div className="eyebrow" style={{ margin: "22px 0 14px" }}>年龄分布</div>
          <HBars items={a.age} />
        </div>
        <div className="card p">
          <div className="eyebrow" style={{ marginBottom: 14 }}>城市分布</div>
          <HBars items={a.city} />
          <div className="eyebrow" style={{ margin: "22px 0 14px" }}>城市等级</div>
          <HBars items={a.cityTier} />
        </div>
      </div>
      <div className="card p" style={{ marginTop: 16 }}>
        <div className="eyebrow" style={{ marginBottom: 14 }}>兴趣分布</div>
        <HBars items={a.interests} />
      </div>
    </div>
  );
}
