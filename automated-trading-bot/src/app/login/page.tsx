import TrdrLogo from "../ui/trdr-logo";
import LoginForm from "@/app/ui/forms/login-form";

export default function LoginPage() {
  return (
    <main className="flex items-center justify-center md:h-screen">
      <div className="relative mx-auto flex w-full max-w-[400px] flex-col space-y-2.5 p-4 md:-mt-32">
        <a
          href="/"
          className="flex h-20 w-full items-end rounded-lg bg-green-800/90 p-3 md:h-36"
        >
          <div className="w-32 text-white md:w-36">
            <TrdrLogo />
          </div>
        </a>
        <LoginForm />
      </div>
    </main>
  );
}
