import { CurrencyDollarIcon } from "@heroicons/react/24/outline";

const iconMap = {
  money: CurrencyDollarIcon,
};

export default async function CardWrapper() {
  const tempTotal = 1000; //TODO: placeholder
  const tempAvailable = 1000; //TODO: placeholder
  return (
    <>
      <Card title="Total" value={tempTotal} type="money" />
      <Card title="Available" value={tempAvailable} type="money" />
    </>
  );
}

export function Card({
  title,
  value,
  type,
}: {
  title: string;
  value: number | string;
  type: "money";
}) {
  const Icon = iconMap[type];

  return (
    <div className="rounded-xl bg-gray-50 p-2 shadow-sm">
      <div className="flex p-4">
        {Icon ? <Icon className="h-5 w-5 text-gray-700" /> : null}
        <h3 className="ml-2 text-sm font-medium">{title}</h3>
      </div>
      <p className="runcate rounded-xl bg-white px-4 py-8 text-center text-2xl">
        {value}
      </p>
    </div>
  );
}
