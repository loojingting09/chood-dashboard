"use client";
import { useEffect, useRef, useState } from "react";

export function CountUp({ value, dur = 1200, className }) {
  const str = String(value);
  const m = str.match(/-?[\d,]+\.?\d*/);
  const [val, setVal] = useState(0);
  const started = useRef(false);
  const target = m ? parseFloat(m[0].replace(/,/g, "")) : 0;
  useEffect(() => {
    if (!m || started.current) return;
    started.current = true;
    let raf, start;
    const step = (t) => {
      if (!start) start = t;
      const p = Math.min((t - start) / dur, 1);
      const e = 1 - Math.pow(1 - p, 3);
      setVal(target * e);
      if (p < 1) raf = requestAnimationFrame(step);
    };
    raf = requestAnimationFrame(step);
    return () => cancelAnimationFrame(raf);
  }, [target, dur, m]);
  if (!m) return <span className={className}>{str}</span>;
  const numStr = m[0].replace(/,/g, "");
  const decimals = (numStr.split(".")[1] || "").length;
  const prefix = str.slice(0, m.index);
  const suffix = str.slice(m.index + m[0].length);
  const shown =
    target >= 1000 ? Math.round(val).toLocaleString("en-US") : val.toFixed(decimals);
  return (
    <span className={className}>
      {prefix}
      {shown}
      {suffix}
    </span>
  );
}

// Reveal on scroll: adds .in when the element enters the viewport
export function Reveal({ children, className = "", delay = 0, as: Tag = "div" }) {
  const ref = useRef(null);
  const [seen, setSeen] = useState(false);
  useEffect(() => {
    const el = ref.current;
    if (!el || typeof IntersectionObserver === "undefined") {
      setSeen(true);
      return;
    }
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((e) => {
          if (e.isIntersecting) {
            setSeen(true);
            io.disconnect();
          }
        });
      },
      { threshold: 0.08, rootMargin: "0px 0px -8% 0px" }
    );
    io.observe(el);
    // safety: never let content stay hidden
    const t = setTimeout(() => setSeen(true), 1600);
    return () => {
      io.disconnect();
      clearTimeout(t);
    };
  }, []);
  return (
    <Tag
      ref={ref}
      className={`reveal ${seen ? "in" : ""} ${className}`}
      style={{ transitionDelay: `${delay}ms` }}
    >
      {children}
    </Tag>
  );
}
