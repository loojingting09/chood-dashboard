import Link from "next/link";
import { getInsights } from "@/lib/data";
import AiInsights from "@/components/AiInsights";

export default function InsightsPage() {
  const data = getInsights();
  return (
    <div>
      <div style={{ marginBottom: 14 }}>
        <Link href="/xhs" style={{ color: "var(--muted)", fontSize: 13 }}>← 返回数据看板</Link>
      </div>
      <div className="page-head">
        <h1>AI Insights</h1>
        <div className="meta">Cross-post intelligence · 跨笔记智能分析</div>
      </div>
      <AiInsights data={data} />
    </div>
  );
}
