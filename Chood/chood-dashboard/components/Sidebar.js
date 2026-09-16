"use client";
import Link from "next/link";
import { usePathname } from "next/navigation";

const TOP = [{ href: "/", label: "Home", icon: "◇" }];

const XHS_CHILDREN = [
  { href: "/xhs", label: "账号概览", en: "Overview", exact: true },
  { href: "/xhs/fans", label: "粉丝数据", en: "Fans" },
  { href: "/xhs/posts", label: "笔记表现", en: "Posts" },
];

const AFTER = [
  { href: "/xhs/insights", label: "AI Insights", icon: "✦" },
  { href: "/xhs/admin", label: "Data Manager", icon: "⬆" },
];

export default function Sidebar() {
  const path = usePathname();
  const isActive = (href, exact) =>
    exact || href === "/"
      ? path === href
      : path === href || path.startsWith(href + "/");
  const inXhsData = XHS_CHILDREN.some((c) =>
    c.exact ? path === c.href : path === c.href || path.startsWith(c.href + "/")
  ) || /^\/xhs\/[^/]+$/.test(path); // post detail pages

  return (
    <aside className="sidebar">
      <div className="brandmark">
        <div className="logo">C</div>
        <div>
          <div className="name">Chood</div>
          <div className="sub">Dashboard</div>
        </div>
      </div>
      <div className="nav-label">Workspace</div>
      <nav className="nav">
        {TOP.map((it) => (
          <Link key={it.href} href={it.href} className={isActive(it.href) ? "active" : ""}>
            <span>{it.icon}</span>
            {it.label}
          </Link>
        ))}

        {/* Xiaohongshu group — the raw data dashboards */}
        <div className={`nav-group ${inXhsData ? "open" : ""}`}>
          <div className="nav-group-head">
            <span className="dot" /> Xiaohongshu (XHS)
          </div>
          <div className="nav-children">
            {XHS_CHILDREN.map((c) => (
              <Link
                key={c.href}
                href={c.href}
                className={isActive(c.href, c.exact) ? "active" : ""}
              >
                <span className="cn">{c.label}</span>
                <span className="en">{c.en}</span>
              </Link>
            ))}
          </div>
        </div>

        {AFTER.map((it) => (
          <Link key={it.href} href={it.href} className={isActive(it.href) ? "active" : ""}>
            <span>{it.icon}</span>
            {it.label}
          </Link>
        ))}
      </nav>
      <div className="sidebar-foot">
        Chood internal dashboard<br />
        Source: Xiaohongshu Creator Platform<br />
        Confidential · Internal use
      </div>
    </aside>
  );
}
