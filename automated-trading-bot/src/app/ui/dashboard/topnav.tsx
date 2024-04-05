import Link from "next/link";
import { PowerIcon } from "@heroicons/react/24/outline";
import TrdrLogo from "@/app/ui/trdr-logo";
import NavLinks from "./nav-links";

export default function TopNav() {
  return (
    <div className="flex w-full flex-row px-3 py-4 md:px-2 md:space-x-4">
      <Link
        className="mb-2 flex h-20 items-end justify-start rounded-md bg-green-800/90 hover:border-gray-300 hover:bg-green-800/80 p-4 md:h-40"
        href="/"
      >
        <div className="w-32 text-white md:w-40">
          <TrdrLogo />
        </div>
      </Link>
      <div className="flex grow flex-col justify-between space-x-2 md:flex-row md:space-x-2 md:space-y-0">
        <NavLinks />
      </div>
    </div>
  );
}
