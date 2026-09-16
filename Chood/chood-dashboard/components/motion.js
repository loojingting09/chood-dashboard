"use client";
import { useEffect, useRef, useState } from "react";

// Numbers render their exact final value immediately — never an animated
// partial value — so every figure is always correct at a glance and in
// screenshots. (The "high-tech" motion lives in Reveal, hover lifts, the
// animated gradient banner and the live dots, not in the numbers.)
export function CountUp({ value, className }) {
  return <span className={className}>{String(value)}</span>;
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
