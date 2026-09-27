import Link from "next/link";
import { getPosts, getPostAggregates, fmt } from "@/lib/data";
import { Kpi, SectionTitle, PostCover } from "@/components/ui";

export default function XhsPosts() {
  const posts = getPosts();
  const agg = getPostAggregates();
  return (
    <div>
      <div className="page-head">
        <div className="crumb">小红书 · Xiaohongshu</div>
        <h1>笔记表现</h1>
        <div className="meta">已收录 {posts.length} 篇 · 汇总数据</div>
      </div>

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

      <div className="nextlinks">
        <Link href="/xhs" className="nextlink">
          <div>
            <div className="nl-k">← 账号概览</div>
            <div className="nl-s">账号诊断与近 7 日表现</div>
          </div>
        </Link>
        <Link href="/xhs/insights" className="nextlink">
          <div>
            <div className="nl-k">AI Insights →</div>
            <div className="nl-s">跨 6 篇笔记的智能分析与建议</div>
          </div>
        </Link>
      </div>
    </div>
  );
}
