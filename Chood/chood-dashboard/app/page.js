import Link from "next/link";
import { getAccount, getPostAggregates, getPosts, fmt } from "@/lib/data";
import { CountUp } from "@/components/motion";

export default function Home() {
  const account = getAccount();
  const agg = getPostAggregates();
  const posts = getPosts();
  return (
    <div className="portal">
      <div className="hero">
        <h1>Chood Dashboard</h1>
        <p>
          One place to track Chood&apos;s performance across channels. The Xiaohongshu (XHS)
          module is live, covering the account and every post in detail.
        </p>
      </div>

      <Link href="/xhs" className="card module-card" style={{ marginTop: 22 }}>
        <div className="mc-left">
          <div className="badge" style={{ display: "flex", alignItems: "center", gap: 7 }}><span className="livedot" /> MODULE · LIVE</div>
          <div>
            <h3>Xiaohongshu</h3>
            <div className="en">XHS · Analytics</div>
          </div>
        </div>
        <div className="mc-right">
          <div className="mc-stats">
            <div className="s">
              <div className="v num"><CountUp value={account.fans.base.total} /></div>
              <div className="l">Total followers</div>
            </div>
            <div className="s">
              <div className="v num"><CountUp value={fmt(agg.impressions)} /></div>
              <div className="l">Impressions (recorded)</div>
            </div>
            <div className="s">
              <div className="v num"><CountUp value={posts.length} /></div>
              <div className="l">Notes</div>
            </div>
          </div>
          <span className="enter">Enter dashboard →</span>
        </div>
      </Link>
    </div>
  );
}
