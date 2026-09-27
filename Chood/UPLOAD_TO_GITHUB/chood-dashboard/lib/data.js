import posts from "@/data/posts.json";
import account from "@/data/account.json";
import insights from "@/data/insights.json";

export function getAccount() {
  return account;
}

export function getInsights() {
  return insights;
}

export function getPosts() {
  // newest first
  return [...posts].sort((a, b) => (a.publishDate < b.publishDate ? 1 : -1));
}

export function getPost(id) {
  return posts.find((p) => p.id === id) || null;
}

// aggregate KPIs across all captured posts
export function getPostAggregates() {
  const list = posts;
  const sum = (fn) => list.reduce((t, p) => t + (fn(p) || 0), 0);
  const impressions = sum((p) => p.overview?.traffic?.impressions?.value);
  const views = sum((p) => p.overview?.traffic?.views?.value);
  const likes = sum((p) => p.overview?.engagement?.likes?.value);
  const comments = sum((p) => p.overview?.engagement?.comments?.value);
  const collects = sum((p) => p.overview?.engagement?.collects?.value);
  const shares = sum((p) => p.overview?.engagement?.shares?.value);
  const newFans = sum((p) => p.overview?.depth?.newFans);
  const interactions = likes + comments + collects + shares;
  return {
    count: list.length,
    impressions,
    views,
    likes,
    comments,
    collects,
    shares,
    interactions,
    newFans,
    avgCTR: impressions ? ((views / impressions) * 100).toFixed(1) + "%" : "—",
    avgEng: views ? ((interactions / views) * 100).toFixed(1) + "%" : "—",
  };
}

export const fmt = (n) =>
  typeof n === "number" ? n.toLocaleString("en-US") : n;
