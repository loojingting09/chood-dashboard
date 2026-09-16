"use client";
import {
  ResponsiveContainer,
  PieChart,
  Pie,
  Cell,
  AreaChart,
  Area,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  RadarChart,
  PolarGrid,
  PolarAngleAxis,
  Radar,
} from "recharts";
import { DONUT_COLORS } from "@/lib/colors";

export { DONUT_COLORS };

export function Donut({ data, size = 176 }) {
  return (
    <div style={{ width: size, height: size, flex: "none" }}>
      <ResponsiveContainer width="100%" height="100%">
        <PieChart>
          <Pie
            data={data}
            dataKey="pct"
            nameKey="name"
            cx="50%"
            cy="50%"
            innerRadius={size * 0.3}
            outerRadius={size * 0.46}
            paddingAngle={2}
            stroke="none"
            startAngle={90}
            endAngle={-270}
          >
            {data.map((_, i) => (
              <Cell key={i} fill={DONUT_COLORS[i % DONUT_COLORS.length]} />
            ))}
          </Pie>
          <Tooltip formatter={(v, n) => [`${v}%`, n]} />
        </PieChart>
      </ResponsiveContainer>
    </div>
  );
}

export function RadarPanel({ data, height = 260 }) {
  return (
    <div style={{ width: "100%", height }}>
      <ResponsiveContainer width="100%" height="100%">
        <RadarChart data={data} outerRadius="72%">
          <PolarGrid stroke="#e6e6ec" />
          <PolarAngleAxis
            dataKey="axis"
            tick={{ fontSize: 12, fill: "#6a6a74" }}
          />
          <Radar
            dataKey="value"
            stroke="#FF2442"
            fill="#FF2442"
            fillOpacity={0.18}
            strokeWidth={2}
          />
        </RadarChart>
      </ResponsiveContainer>
    </div>
  );
}

export function AreaTrend({
  data,
  xKey,
  yKey,
  height = 200,
  unit = "",
  yPct = false,
}) {
  return (
    <div style={{ width: "100%", height }}>
      <ResponsiveContainer width="100%" height="100%">
        <AreaChart data={data} margin={{ top: 8, right: 10, left: -6, bottom: 0 }}>
          <defs>
            <linearGradient id={`g-${yKey}`} x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stopColor="#FF2442" stopOpacity={0.35} />
              <stop offset="100%" stopColor="#FF2442" stopOpacity={0.02} />
            </linearGradient>
          </defs>
          <CartesianGrid vertical={false} stroke="#f0f0f3" />
          <XAxis
            dataKey={xKey}
            tick={{ fontSize: 11, fill: "#a0a0aa" }}
            axisLine={false}
            tickLine={false}
            interval="preserveStartEnd"
            minTickGap={24}
          />
          <YAxis
            tick={{ fontSize: 11, fill: "#a0a0aa" }}
            axisLine={false}
            tickLine={false}
            width={40}
            tickFormatter={(v) => (yPct ? `${v}%` : v)}
          />
          <Tooltip
            formatter={(v) => [`${v}${unit}`, ""]}
            labelStyle={{ color: "#6a6a74" }}
          />
          <Area
            type="monotone"
            dataKey={yKey}
            stroke="#FF2442"
            strokeWidth={2.4}
            fill={`url(#g-${yKey})`}
          />
        </AreaChart>
      </ResponsiveContainer>
    </div>
  );
}
