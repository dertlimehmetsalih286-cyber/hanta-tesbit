import { Switch, Route, Router as WouterRouter, Link, useLocation } from "wouter";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { Toaster } from "@/components/ui/toaster";
import { TooltipProvider } from "@/components/ui/tooltip";
import { Stethoscope, BarChart3, History, ShieldAlert } from "lucide-react";
import NotFound from "./pages/not-found";
import AnalyzerPage from "./pages/analyzer";
import HistoryPage from "./pages/history";
import StatsPage from "./pages/stats";

const queryClient = new QueryClient();

// Sol Menü ve Ana Düzen (Layout) Bileşeni
function Layout({ children }: { children: React.ReactNode }) {
  const [location] = useLocation();

  const links = [
    { href: "/", label: "Analyzer", icon: <Stethoscope className="w-4 h-4" /> },
    { href: "/history", label: "History", icon: <History className="w-4 h-4" /> },
    { href: "/stats", label: "Statistics", icon: <BarChart3 className="w-4 h-4" /> },
  ];

  return (
    <div className="min-h-[100dvh] flex flex-col md:flex-row bg-background">
      {/* SIDEBAR (SOL MENÜ) */}
      <aside className="w-full md:w-64 border-r border-border bg-card shrink-0 flex flex-col">
        {/* LOGO BÖLÜMÜ */}
        <div className="p-6 flex items-center gap-3 border-b border-border">
          <div className="w-10 h-10 rounded-xl bg-primary/10 text-primary flex items-center justify-center border border-primary/20">
            <ShieldAlert className="w-6 h-6" />
          </div>
          <div>
            <h1 className="font-bold text-lg text-foreground tracking-tight">Hantavirus</h1>
            <p className="text-sm text-muted-foreground -mt-1">Risk Analyzer</p>
          </div>
        </div>

        {/* MENÜ LİNKLERİ */}
        <nav className="p-4 flex-1 flex flex-col gap-1.5 overflow-y-auto mt-2">
          {links.map((link) => {
            const isActive = location === link.href;
            return (
              <Link key={link.href} href={link.href}
                className={`flex items-center gap-3.5 px-4 py-3 rounded-lg text-sm transition-colors ${
                  isActive ? "bg-primary text-primary-foreground font-semibold shadow-sm" : "text-slate-700 hover:bg-slate-100/70"
                }`}
              >
                {link.icon}
                <span>{link.label}</span>
              </Link>
            );
          })}
        </nav>

        {/* ALTTAKİ PROFİL BÖLÜMÜ */}
        <div className="p-4 border-t border-border mt-auto">
          <div className="bg-slate-100 p-4 rounded-xl flex items-center gap-3">
            <div className="w-10 h-10 rounded-full bg-slate-300 flex items-center justify-center text-slate-500 font-medium">H</div>
            <div>
              <p className="font-semibold text-sm">Hantavirus Risk</p>
              <p className="text-xs text-muted-foreground truncate">demo@workspace.com</p>
            </div>
          </div>
        </div>
      </aside>

      {/* ANA İÇERİK ALANI */}
      <main className="flex-1 overflow-y-auto relative bg-slate-50/50">
        <div className="max-w-6xl mx-auto p-6 md:p-10">{children}</div>
      </main>
    </div>
  );
}

// Yönlendirme (Router) Bileşeni
function Router() {
  return (
    <Layout>
      <Switch>
        <Route path="/" component={AnalyzerPage} />
        <Route path="/history" component={HistoryPage} />
        <Route path="/stats" component={StatsPage} />
        <Route component={NotFound} />
      </Switch>
    </Layout>
  );
}

// Ana Uygulama Başlangıç Dosyası
export default function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <TooltipProvider>
        <WouterRouter>
          <Router />
        </WouterRouter>
        <Toaster />
      </TooltipProvider>
    </QueryClientProvider>
  );
}
