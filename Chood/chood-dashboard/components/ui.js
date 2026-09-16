import { DONUT_COLORS } from "@/lib/colors";
import { CountUp } from "@/components/motion";

export function SectionTitle({ title, hint }) {
  return (
    <div className="section-title">
      <h2>{title}</h2>
      {hint ? <span className="hint">{hint}</span> : null}
    </div>
  );
}

export function RatingPill({ rating }) {
  const good = rating === "较好" || rating === "优秀";
  return <span className={`pill ${good ? "good" : "warn"}`}>{rating}</span>;
}

export function Kpi({ label, value, sub, hl, live, wow }) {
  return (
    <div className={`card kpi ${hl ? "hl" : ""}`}>
      <div className="k-label">
        {label}
        {live ? <span className="tag-live">实时</span> : null}
      </div>
      <div className="k-val num"><CountUp value={value} /></div>
      {sub ? <div className="k-sub">{sub}</div> : null}
      {wow ? (
        <div className="k-sub">
          环比{" "}
          <span className={`wow ${wow.startsWith("-") ? "down" : "up"}`}>{wow}</span>
        </div>
      ) : null}
    </div>
  );
}

export function HBars({ items }) {
  const max = Math.max(...items.map((i) => i.pct), 1);
  return (
    <div className="hbars">
      {items.map((it, idx) => (
        <div className="hbar-row" key={idx}>
          <span className="lab">{it.lab || it.name || it.band}</span>
          <div className="hbar-track">
            <div className="hbar-fill" style={{ width: `${(it.pct / max) * 100}%` }} />
          </div>
          <span className="pct num">{it.pct}%</span>
        </div>
      ))}
    </div>
  );
}

export function GenderBar({ male, female }) {
  return (
    <div className="gender">
      <div className="gender-track">
        <div className="m" style={{ width: `${male}%` }} />
        <div className="f" style={{ width: `${female}%` }} />
      </div>
      <div className="gender-legend">
        <span>
          <span className="dot-m" />男性 <b>{male}%</b>
        </span>
        <span>
          <span className="dot-f" />女性 <b>{female}%</b>
        </span>
      </div>
    </div>
  );
}

export function Legend({ data }) {
  return (
    <div className="legend">
      {data.map((d, i) => (
        <div className={`legend-row ${i === 0 ? "top" : ""}`} key={i}>
          <span className="sw" style={{ background: DONUT_COLORS[i % DONUT_COLORS.length] }} />
          <span className="nm">{d.name}</span>
          <span className="pc num">{d.pct}%</span>
        </div>
      ))}
    </div>
  );
}

export function PostCover({ cover, title, className = "", size = "sm" }) {
  if (cover) {
    // eslint-disable-next-line @next/next/no-img-element
    return <img className={className} src={cover} alt="" />;
  }
  const ch = (title || "C").trim().charAt(0);
  return (
    <div className={`${className} covertile ${size}`}>
      <span>{ch}</span>
    </div>
  );
}

export function AiInsight({ title, text, time }) {
  return (
    <div className="ai">
      <div className="ai-h">
        {title}
        <span className="ai-badge">AI</span>
      </div>
      <p>{text}</p>
      {time ? <div className="ai-time">{time}</div> : null}
    </div>
  );
}
