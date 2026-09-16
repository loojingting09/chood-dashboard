import "./globals.css";
import Sidebar from "@/components/Sidebar";

export const metadata = {
  title: "Chood Dashboard",
  description: "Chood internal data portal — XHS analytics",
};

export default function RootLayout({ children }) {
  return (
    <html lang="zh">
      <body>
        <div className="shell">
          <Sidebar />
          <main className="content">{children}</main>
        </div>
      </body>
    </html>
  );
}
