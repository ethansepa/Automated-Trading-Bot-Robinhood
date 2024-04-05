import TopNav from "../ui/dashboard/topnav";

export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <div className="flex w-screen h-screen flex-row md:flex-col md:overflow-hidden">
      <div className="w-full flex-none md:w-64">
        <TopNav />
      </div>
      <div className="flex-grow p-6 md:overflow-y-auto md:p-12">{children}</div>
    </div>
  );
}
