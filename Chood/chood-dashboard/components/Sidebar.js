"use client";
import Link from "next/link";
import { usePathname } from "next/navigation";

const items = [
  { href: "/", label: "Home", icon: "◇" },
  { href: "/xhs", label: "Xiaohongshu (XHS)", dot: true },
  { href: "/xhs/insights", label: "AI Insights", icon: "✦" },
  { href: "/xhs/admin", label: "Data Manager", icon: "⬆" },
];

export default function Sidebar() {
  const path = usePathname();
  const isActive = (href) =>
    href === "/" ? path === "/" : path === href || path.startsWith(href + "/");
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
        {items.map((it) => (
          <Link key={it.href} href={it.href} className={isActive(it.href) ? "active" : ""}>
            {it.dot ? <span className="dot" /> : <span>{it.icon}</span>}
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
