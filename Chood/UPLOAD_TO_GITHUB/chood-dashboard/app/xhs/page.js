import Link from "next/link";
import { getAccount, getInsights, fmt } from "@/lib/data";
import { Donut } from "@/components/charts";
import { Kpi, Legend, AiInsight, SectionTitle } from "@/components/ui";
import AiInsights from "@/components/AiInsights";

function StatRows({ items }) {
  return (
    <div className="statrows">
      {items.map((it) => (
        <div className="statrow" key={it.label}>
          <span className="sr-label">{it.label}</span>
          <span className="sr-val num">{fmt(it.value)}</span>
          {it.wow && it.wow !== "—" ? (
            <span className={`sr-wow ${String(it.wow).startsWith("-") ? "down" : "up"}`}>{it.wow}</span>
          ) : (
            <span className="sr-wow muted">—</span>
          )}
        </div>
      ))}
    </div>
  );
}

export default function XhsAccountOverview() {
  const account = getAccount();
  const insights = getInsights();
  const o = account.overview;
  const w = o.watch;

  return (
    <div>
      <div className="page-head">
        <div className="crumb">小红书 · Xiaohongshu</div>
        <h1>账号概览</h1>
        <div className="meta">{account.handle} · {o.period}</div>
      </div>

      <div className="snap-note">
        <span className="snap-pill">数据快照 · 截至 2026-10-01</span>
        账号层面的「近7日 / 近30日」是小红书的<b>滚动窗口</b>，每天都会重新计算，因此这里是<b>截图当天</b>的快照，与 App 里此刻的实时数字会有正常差异。需要更新时，把最新的「账号概览 / 粉丝数据」截图发我即可。（每篇笔记的数据为发布后固定值，不受此影响。）
      </div>

      {/* -------- AI Insights teaser -------- */}
      <Link href="/xhs/insights" style={{ display: "block" }}>
        <AiInsights data={insights} compact />
        <div style={{ textAlign: "right", marginTop: 10 }}>
          <span className="ab-cta" style={{ background: "var(--chood)", color: "#fff" }}>查看完整 AI 分析 →</span>
        </div>
      </Link>

      {/* -------- 观看数据 -------- */}
      <SectionTitle title="观看数据" hint={o.period} />
      <div className="grid cols-6">
        <Kpi label="曝光数" value={w.impressions.value} wow={w.impressions.wow} hl />
        <Kpi label="观看数" value={fmt(w.views.value)} wow={w.views.wow} />
        <Kpi label="封面点击率" value={w.coverCTR.value} wow={w.coverCTR.wow} />
        <Kpi label="平均观看时长" value={w.avgWatch.value} wow={w.avgWatch.wow} />
        <Kpi label="视频完播率" value={w.completeRate.value} wow={w.completeRate.wow} />
        <Kpi label="观看总时长" value={w.totalWatch.value} wow={w.totalWatch.wow} />
      </div>

      <div className="grid cols-3" style={{ marginTop: 16 }}>
        <div className="card p">
          <div className="eyebrow" style={{ marginBottom: 12 }}>观看来源</div>
          <div style={{ display: "flex", alignItems: "center", gap: 16 }}>
            <Donut data={o.watchSources} size={150} />
            <div style={{ flex: 1 }}><Legend data={o.watchSources} /></div>
          </div>
        </div>
        <div className="card p">
          <div className="eyebrow" style={{ marginBottom: 12 }}>互动数据</div>
          <StatRows items={[
            { label: "点赞数", value: o.interaction.likes.value, wow: o.interaction.likes.wow },
            { label: "评论数", value: o.interaction.comments.value, wow: o.interaction.comments.wow },
            { label: "收藏数", value: o.interaction.collects.value, wow: o.interaction.collects.wow },
            { label: "分享数", value: o.interaction.shares.value, wow: o.interaction.shares.wow },
            { label: "被引用数", value: o.interaction.quoted.value, wow: o.interaction.quoted.wow },
          ]} />
        </div>
        <div className="card p">
          <div className="eyebrow" style={{ marginBottom: 12 }}>涨粉数据</div>
          <StatRows items={[
            { label: "涨粉数", value: o.growth.newFans.value, wow: o.growth.newFans.wow },
            { label: "新增关注", value: o.growth.newFollows.value, wow: o.growth.newFollows.wow },
            { label: "取消关注", value: o.growth.unfollows.value, wow: o.growth.unfollows.wow },
            { label: "主页访客", value: o.growth.homeVisitors.value, wow: o.growth.homeVisitors.wow },
            { label: "主页转粉率", value: o.growth.homeConvRate.value, wow: o.growth.homeConvRate.wow },
          ]} />
        </div>
      </div>

      {/* -------- 发布数据 -------- */}
      <SectionTitle title="发布数据" hint={o.period} />
      <div className="grid cols-4">
        <Kpi label="总发布" value={o.publish.total.value} wow={o.publish.total.wow} hl />
        <Kpi label="发布视频" value={o.publish.video.value} wow={o.publish.video.wow} />
        <Kpi label="发布图文" value={o.publish.image.value} wow={o.publish.image.wow} />
        <Kpi label="粉丝活跃时段" value={o.publish.activeHours} sub="建议发布时间" />
      </div>

      <div style={{ marginTop: 16 }}>
        <AiInsight title="账号增长解读" text={o.ai} />
      </div>

      <div className="nextlinks">
        <Link href="/xhs/fans" className="nextlink">
          <div>
            <div className="nl-k">粉丝数据 →</div>
            <div className="nl-s">总粉丝、增长趋势、来源结构</div>
          </div>
        </Link>
        <Link href="/xhs/posts" className="nextlink">
          <div>
            <div className="nl-k">笔记表现 →</div>
            <div className="nl-s">每篇笔记的曝光、互动与详情</div>
          </div>
        </Link>
      </div>
    </div>
  );
}
