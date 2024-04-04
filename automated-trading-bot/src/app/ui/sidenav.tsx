import Link from "next/link";
import { PowerIcon } from "@heroicons/react/24/outline";
import TrdrLogo from "@/app/ui/trdr-logo";

export default function SideNav() {
  return (
    <div className="flex h-full flex-col px-3 py-4 md:px-2">
      <Link
        className="mb-2 flex h-20 items-end justify-start rounded-md bg-green-800/90 hover:border-gray-300 hover:bg-green-800/80 p-4 md:h-40"
        href="/"
      >
        <div className="w-32 text-white md:w-40">
          <TrdrLogo />
        </div>
      </Link>
    </div>
  );
}
