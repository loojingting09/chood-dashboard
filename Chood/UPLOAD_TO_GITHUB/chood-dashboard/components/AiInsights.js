import { Donut, DONUT_COLORS } from "@/components/charts";
import { Legend } from "@/components/ui";
import { CountUp, Reveal } from "@/components/motion";

export default function AiInsights({ data, compact }) {
  const maxViews = Math.max(...data.viewsByPost.map((v) => v.views), 1);
  return (
    <div>
      <Reveal>
        <div className="ai-banner">
          <div className="ai-glow" />
          <div className="ab-badge">✦ AI 分析 · Cross-post intelligence</div>
          <h2>{data.headline}</h2>
          <p>基于 {data.generatedFor} · 生成于 {data.asOf}</p>
        </div>
      </Reveal>

      <div className="portfolio" style={{ marginTop: 18 }}>
        {data.portfolio.map((k, i) => (
          <Reveal key={i} delay={i * 60}>
            <div className="pf">
              <div className="v num"><CountUp value={k.value} /></div>
              <div className="l">{k.label}</div>
              <div className="n">{k.note}</div>
            </div>
          </Reveal>
        ))}
      </div>

      {!compact && (
        <>
          <div className="section-title"><h2>关键洞察</h2><span className="hint">AI 从 6 篇笔记中提炼</span></div>
          <div className="grid cols-2">
            {data.cards.map((c, i) => (
              <Reveal key={i} delay={i * 70}>
                <div className={`insight-card ${c.tone}`}>
                  <div className="ic-ico">{c.icon}</div>
                  <div>
                    <h3>{c.title}</h3>
                    <p>{c.body}</p>
                  </div>
                </div>
              </Reveal>
            ))}
          </div>

          <div className="grid cols-2" style={{ marginTop: 24 }}>
            <Reveal>
              <div className="card p">
                <div className="eyebrow" style={{ marginBottom: 12 }}>观看量 · 按笔记</div>
                {data.viewsByPost.map((v, i) => (
                  <div className="vbar-row" key={i}>
                    <span className="nm">{v.name}</span>
                    <div className="vbar-track">
                      <div className="vbar-fill" style={{ width: `${(v.views / maxViews) * 100}%` }} />
                    </div>
                    <span className="vv num"><CountUp value={v.views} /></span>
                  </div>
                ))}
              </div>
            </Reveal>
            <Reveal delay={80}>
              <div className="card p">
                <div className="eyebrow" style={{ marginBottom: 12 }}>整体流量来源 · 加权占比</div>
                <div style={{ display: "flex", alignItems: "center", gap: 16 }}>
                  <Donut data={data.sourceMix} size={168} />
                  <div style={{ flex: 1 }}><Legend data={data.sourceMix} /></div>
                </div>
              </div>
            </Reveal>
          </div>

          <div className="section-title"><h2>下一步建议</h2><span className="hint">Recommended actions</span></div>
          <Reveal>
            <div className="card p">
              {data.recommendations.map((r, i) => (
                <div className="rec" key={i} style={i === 0 ? { borderTop: "none", paddingTop: 0 } : {}}>
                  <div className="rn">{i + 1}</div>
                  <div>
                    <h4>{r.title}</h4>
                    <p>{r.body}</p>
                  </div>
                </div>
              ))}
            </div>
          </Reveal>
        </>
      )}
    </div>
  );
}
