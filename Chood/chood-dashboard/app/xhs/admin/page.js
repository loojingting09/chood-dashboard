"use client";
import { useState } from "react";
import posts from "@/data/posts.json";

export default function Admin() {
  const [files, setFiles] = useState([]);
  const [json, setJson] = useState(JSON.stringify(posts, null, 2));
  const [status, setStatus] = useState("");

  const onPick = (e) => {
    const list = Array.from(e.target.files || []).map((f) => ({
      name: f.name,
      url: URL.createObjectURL(f),
    }));
    setFiles(list);
  };

  const validate = () => {
    try {
      const parsed = JSON.parse(json);
      if (!Array.isArray(parsed)) throw new Error("Top level must be an array");
      setStatus(`✓ Valid JSON · ${parsed.length} note(s)`);
    } catch (err) {
      setStatus("✗ JSON error: " + err.message);
    }
  };

  const download = () => {
    const blob = new Blob([json], { type: "application/json" });
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = "posts.json";
    a.click();
  };

  return (
    <div style={{ maxWidth: 900 }}>
      <div className="page-head">
        <h1>Data Manager</h1>
        <div className="meta">Upload screenshots weekly to refresh the dashboard · zero cost, no image storage</div>
      </div>

      <div className="card p">
        <div className="eyebrow" style={{ marginBottom: 12 }}>Weekly update flow</div>
        <ol style={{ margin: 0, paddingLeft: 20, lineHeight: 2, color: "#5c5148" }}>
          <li>In the XHS app, open a note&apos;s analytics (作品分析) and screenshot the four tabs: Data Overview, Content, Traffic, Audience.</li>
          <li>Send the screenshots to your Claude workspace — Claude reads the numbers (no paid OCR, images are not stored).</li>
          <li>Claude updates the data file and redeploys; the dashboard refreshes.</li>
        </ol>
        <div className="notice" style={{ marginTop: 14 }}>
          <span>🔒</span>
          <div>The upload box below is for <strong>local preview only</strong>: images stay in your browser, are never uploaded to any server, and are not saved.</div>
        </div>
      </div>

      <div className="card p" style={{ marginTop: 16 }}>
        <div className="eyebrow" style={{ marginBottom: 12 }}>Screenshot preview (local)</div>
        <input type="file" accept="image/*" multiple onChange={onPick} />
        {files.length > 0 && (
          <div style={{ display: "flex", flexWrap: "wrap", gap: 10, marginTop: 14 }}>
            {files.map((f, i) => (
              // eslint-disable-next-line @next/next/no-img-element
              <img key={i} src={f.url} alt={f.name} style={{ width: 90, height: 160, objectFit: "cover", borderRadius: 8, border: "1px solid var(--line)" }} />
            ))}
          </div>
        )}
      </div>

      <div className="card p" style={{ marginTop: 16 }}>
        <div className="eyebrow" style={{ marginBottom: 12 }}>Data file · posts.json</div>
        <p style={{ color: "var(--muted)", fontSize: 13, marginTop: 0 }}>
          Advanced: edit the data directly. Once it validates, download <span className="mono">posts.json</span> and
          replace <span className="mono">data/posts.json</span> in the repo, then redeploy.
        </p>
        <textarea
          value={json}
          onChange={(e) => setJson(e.target.value)}
          spellCheck={false}
          className="mono"
          style={{ width: "100%", height: 280, borderRadius: 12, border: "1px solid var(--line)", padding: 12, fontSize: 12, resize: "vertical" }}
        />
        <div style={{ display: "flex", gap: 10, alignItems: "center", marginTop: 12 }}>
          <button onClick={validate} style={btn}>Validate JSON</button>
          <button onClick={download} style={{ ...btn, background: "var(--chood)", color: "#fff", border: "none" }}>Download posts.json</button>
          <span style={{ fontSize: 13, color: status.startsWith("✓") ? "var(--good)" : "var(--chood)" }}>{status}</span>
        </div>
      </div>
    </div>
  );
}

const btn = {
  background: "#fff",
  border: "1px solid var(--line)",
  borderRadius: 10,
  padding: "9px 16px",
  fontWeight: 600,
  cursor: "pointer",
  fontSize: 13,
};
