import Link from "next/link";
import { getAccount, getInsights, fmt } from "@/lib/data";
import { RadarPanel } from "@/components/charts";
import { Kpi, AiInsight, SectionTitle } from "@/components/ui";
import AiInsights from "@/components/AiInsights";

export default function XhsAccountOverview() {
  const account = getAccount();
  const insights = getInsights();

  const radar = account.overview.diagnosis.map((d) => ({
    axis: d.key,
    value: d.beat,
  }));

  return (
    <div>
      <div className="page-head">
        <div className="crumb">小红书 · Xiaohongshu</div>
        <h1>账号概览</h1>
        <div className="meta">{account.handle} · {account.overview.period}</div>
      </div>

      <div className="snap-note">
        <span className="snap-pill">数据快照 · 截至 2026-09-14</span>
        「近7日 / 近30日」是小红书的<b>滚动窗口</b>，每天都会重新计算，因此这里的账号数值是<b>截图当天</b>的快照，与 App 里此刻的实时数字会有正常差异。需要更新时，把最新的「账号概览 / 粉丝数据」截图发我即可。（每篇笔记的数据为发布后固定值，不受此影响。）
      </div>

      {/* -------- AI Insights teaser -------- */}
      <Link href="/xhs/insights" style={{ display: "block" }}>
        <AiInsights data={insights} compact />
        <div style={{ textAlign: "right", marginTop: 10 }}>
          <span className="ab-cta" style={{ background: "var(--chood)", color: "#fff" }}>查看完整 AI 分析 →</span>
        </div>
      </Link>

      {/* -------- Account diagnosis -------- */}
      <SectionTitle title="账号诊断" hint={account.overview.period} />
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
