import Link from "next/link";
import { getAccount, fmt } from "@/lib/data";
import { Donut, AreaTrend } from "@/components/charts";
import { Kpi, Legend, SectionTitle } from "@/components/ui";

export default function XhsFans() {
  const account = getAccount();
  return (
    <div>
      <div className="page-head">
        <div className="crumb">小红书 · Xiaohongshu</div>
        <h1>粉丝数据</h1>
        <div className="meta">{account.handle} · {account.fans.period}</div>
      </div>

      <div className="snap-note">
        <span className="snap-pill">数据快照 · 截至 2026-09-14 · 近30日</span>
        新增 / 流失粉丝为<b>近30日滚动窗口</b>数值（每日刷新）。若在 App 切换到「近7日」，数字会明显更小——这是不同统计周期，并非错误。需要更新时，发我最新的粉丝数据截图即可。
      </div>

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
          <AreaTrend data={account.fans.growthCurve} xKey="d" yKey="v" height={240} unit=" 粉丝" />
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

      <div className="nextlinks">
        <Link href="/xhs" className="nextlink">
          <div>
            <div className="nl-k">← 账号概览</div>
            <div className="nl-s">账号诊断与近 7 日表现</div>
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
