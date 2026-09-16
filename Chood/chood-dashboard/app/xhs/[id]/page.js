import Link from "next/link";
import { notFound } from "next/navigation";
import { getPost, getPosts } from "@/lib/data";
import PostDetail from "@/components/PostDetail";

export function generateStaticParams() {
  return getPosts().map((p) => ({ id: p.id }));
}

export default function PostPage({ params }) {
  const post = getPost(params.id);
  if (!post) return notFound();
  return (
    <div>
      <div style={{ marginBottom: 14 }}>
        <Link href="/xhs" style={{ color: "var(--muted)", fontSize: 13 }}>← 返回数据看板</Link>
      </div>
      <PostDetail post={post} />
    </div>
  );
}
