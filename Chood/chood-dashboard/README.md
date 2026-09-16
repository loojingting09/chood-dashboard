# Chood 数据门户 (Chood Data Portal)

Internal analytics portal for Chood. v1 ships the **小红书 (XHS)** module: account-level
overview, follower data, and per-post analytics (数据概览 / 内容分析 / 流量分析 / 观众分析).

## Stack
- Next.js 14 (App Router), React 18, Recharts
- **No database, no paid API, no image storage.** All data lives in `data/*.json`.

## Data model
- `data/account.json` — 账号概览 + 粉丝数据
- `data/posts.json` — array of notes; each note carries its four analysis sections
- `public/covers/` — note cover images

## Updating each week (zero-cost flow)
1. In the XHS app, open a note's 作品分析 and screenshot the four tabs.
2. Send the screenshots to your Claude workspace — Claude reads the numbers (no paid OCR,
   images are not stored) and updates `data/posts.json` (+ a cropped cover in `public/covers/`).
3. Redeploy. The `/xhs/admin` page also lets you edit/validate/download `posts.json` by hand.

## Local dev
```bash
npm install
npm run dev
```

## Deploy
Deploys to Vercel as a standard Next.js app — no environment variables required.

## Handoff / transfer
Fully portable: it's a plain repo with data in-repo and no secrets. Transfer the repo and the
Vercel project to Chood's account at any time.

## Phase 2 (optional, later)
Self-serve in-app screenshot upload → automatic extraction. That requires (a) a database to
persist writes and (b) a vision API key with billing — the only part that would incur cost.
