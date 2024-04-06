// This file contains data type definitions.

export type User = {
  email: string;
  password: string;
};

export type Stock = {
  ticker: string;
  shares: number;
  price: number;
  total: number;
  holding: "holding" | "notHolding";
};
