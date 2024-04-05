"use client";

import {
  RocketLaunchIcon,
  UserIcon,
  PresentationChartLineIcon,
} from "@heroicons/react/24/outline";
import Link from "next/link";
import { usePathname } from "next/navigation";
import clsx from "clsx";

const links = [
  { name: "Home", href: "/dashboard", icon: UserIcon },
  {
    name: "Bots",
    href: "/dashboard/bots",
    icon: RocketLaunchIcon,
  },
  {
    name: "History",
    href: "/dashboard/history",
    icon: PresentationChartLineIcon,
  },
];

export default function NavLinks() {
  const pathname = usePathname();
  return (
    <>
      {links.map((link) => {
        const LinkIcon = link.icon;
        return (
          <Link
            key={link.name}
            href={link.href}
            className={clsx(
              "flex h-[48px] grow items-center justify-center gap-2 rounded-md bg-gray-50 p-3 text-sm font-medium hover:bg-green-100/75 hover:text-green-800/90 md:flex-none md:justify-start md:p-2 md:px-3",
              {
                "bg-green-100/75 text-green-800/90": pathname === link.href,
              },
            )}
          >
            <LinkIcon className="w-6" />
            <p className="hidden md:block">{link.name}</p>
          </Link>
        );
      })}
    </>
  );
}
