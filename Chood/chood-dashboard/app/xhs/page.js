import Link from "next/link";
import { getAccount, getPosts, getPostAggregates, getInsights, fmt } from "@/lib/data";
import { Donut, RadarPanel, AreaTrend } from "@/components/charts";
import { Kpi, Legend, AiInsight, SectionTitle, PostCover } from "@/components/ui";
import AiInsights from "@/components/AiInsights";

export default function XhsOverview() {
  const account = getAccount();
  const posts = getPosts();
  const agg = getPostAggregates();
  const insights = getInsights();

  const radar = account.overview.diagnosis.map((d) => ({
    axis: d.key,
    value: d.beat,
  }));

  return (
    <div>
      <div className="page-head">
        <h1>小红书数据看板</h1>
        <div className="meta">{account.handle}</div>
      </div>

      {/* -------- AI Insights teaser -------- */}
      <Link href="/xhs/insights" style={{ display: "block" }}>
        <AiInsights data={insights} compact />
        <div style={{ textAlign: "right", marginTop: 10 }}>
          <span className="ab-cta" style={{ background: "var(--chood)", color: "#fff" }}>查看完整 AI 分析 →</span>
        </div>
      </Link>

      {/* -------- Account diagnosis -------- */}
      <SectionTitle title="账号概览" hint={account.overview.period} />
      <div className="grid cols-2">
        <div className="card p">
          <div className="eyebrow" style={{ marginBottom: 6 }}>账号诊断 · 你的数据 vs 同类创作者</div>
          <RadarPanel data={radar} />
          <div className="hbars" style={{ marginTop: 8 }}>
            {account.overview.diagnosis.map((d) => (
              <div className="hbar-row" key={d.key} style={{ gridTemplateColumns: "72px 1fr 96px" }}>
                <span className="lab">{d.key}</span>
                <div className="hbar-track">
                  <div className="hbar-fill" style={{ width: `${d.beat}%` }} />
                </div>
                <span className="pct num" style={{ width: 96 }}>
                  {fmt(d.value)} · 超{d.beat}%
                </span>
              </div>
            ))}
          </div>
        </div>
        <div className="grid" style={{ gridTemplateColumns: "1fr 1fr", alignContent: "start" }}>
          <Kpi label="曝光数" value={fmt(account.overview.kpis.impressions.value)} wow={account.overview.kpis.impressions.wow} hl />
          <Kpi label="观看数" value={fmt(account.overview.kpis.views.value)} wow={account.overview.kpis.views.wow} />
          <Kpi label="封面点击率" value={account.overview.kpis.coverCTR.value} wow={account.overview.kpis.coverCTR.wow} />
          <Kpi label="近7日发布" value={account.overview.diagnosis.find((d) => d.key === "发布数")?.value ?? "—"} sub="篇笔记" />
          <div className="span-2">
            <AiInsight title="账号增长解读" text={account.overview.ai} />
          </div>
        </div>
      </div>

      {/* -------- Fans -------- */}
      <SectionTitle title="粉丝数据" hint={account.fans.period} />
      <div className="grid cols-6">
        <Kpi label="总粉丝" value={fmt(account.fans.base.total)} hl />
        <Kpi label="新增粉丝" value={fmt(account.fans.base.new)} />
        <Kpi label="流失粉丝" value={fmt(account.fans.base.lost)} />
        <Kpi label="活跃粉丝占比" value={account.fans.base.activePct} />
        <Kpi label="日均观看粉丝" value={account.fans.base.dailyViewers} />
        <Kpi label="日均互动粉丝" value={account.fans.base.dailyEngagers} />
      </div>
      <div className="grid cols-3" style={{ marginTop: 16 }}>
        <div className="card p span-2">
          <div className="eyebrow" style={{ marginBottom: 10 }}>粉丝增长趋势</div>
          <AreaTrend data={account.fans.growthCurve} xKey="d" yKey="v" height={220} unit=" 粉丝" />
        </div>
        <div className="card p">
          <div className="eyebrow" style={{ marginBottom: 10 }}>新增粉丝来源</div>
          <div style={{ display: "flex", alignItems: "center", gap: 16 }}>
            <Donut data={account.fans.newFanSources} size={150} />
            <div style={{ flex: 1 }}>
              <Legend data={account.fans.newFanSources} />
            </div>
          </div>
        </div>
      </div>

      {/* -------- Posts -------- */}
      <SectionTitle title="笔记表现" hint={`已收录 ${posts.length} 篇 · 汇总数据`} />
      <div className="grid cols-6" style={{ marginBottom: 16 }}>
        <Kpi label="累计曝光" value={fmt(agg.impressions)} hl />
        <Kpi label="累计观看" value={fmt(agg.views)} />
        <Kpi label="累计互动" value={fmt(agg.interactions)} />
        <Kpi label="累计涨粉" value={fmt(agg.newFans)} />
        <Kpi label="平均点击率" value={agg.avgCTR} />
        <Kpi label="平均互动率" value={agg.avgEng} />
      </div>
      <div className="card p">
        <table className="ptable">
          <thead>
            <tr>
              <th style={{ width: 60 }}>封面</th>
              <th>笔记</th>
              <th className="num">曝光</th>
              <th className="num">观看</th>
              <th className="num">点赞</th>
              <th className="num">评论</th>
              <th className="num">收藏</th>
              <th className="num">互动率</th>
              <th className="num">涨粉</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            {posts.map((p) => (
              <tr key={p.id}>
                <td>
                  <PostCover cover={p.cover} title={p.title} className="pc-cover" size="sm" />
                </td>
                <td>
                  <div className="t-title">{p.title}</div>
                  <div className="t-date">{p.publishDate} · {p.type}</div>
                </td>
                <td className="num">{fmt(p.overview.traffic.impressions.value)}</td>
                <td className="num">{fmt(p.overview.traffic.views.value)}</td>
                <td className="num">{p.overview.engagement.likes.value}</td>
                <td className="num">{p.overview.engagement.comments.value}</td>
                <td className="num">{p.overview.engagement.collects.value}</td>
                <td className="num">{p.overview.engagement.rate.value}</td>
                <td className="num">{p.overview.depth.newFans}</td>
                <td><Link href={`/xhs/${p.id}`} style={{ color: "var(--xhs)", fontWeight: 600 }}>详情 →</Link></td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
