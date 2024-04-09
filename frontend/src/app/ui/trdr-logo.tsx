import { ArrowTrendingUpIcon } from "@heroicons/react/24/outline";

export default function TrdrLogo() {
  return (
    <div className={`flex flex-row items-center leading-none text-white`}>
      <ArrowTrendingUpIcon className="h-12 w-12 rotate-[15deg]" />
      <p className="text-[44px]">trdr</p>
    </div>
  );
}
