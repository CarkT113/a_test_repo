import type { Metadata } from "next";
import FXrates  from "@/components/charts/line/FXrates"
import InterestRates from "@/components/charts/line/InterestRates"
import React from "react";

export const metadata: Metadata = {
  title:
    "Next.js test Dashboard | ByCarlos - Next.js Dashboard Template",
  description: "This is Next.js test Dashboard Template By Carlos, a data analyst with over 6 years in SQL ingestion",
};

export default function reference() {
    return(
        <div className="grid grid-cols-7 gap-4 md:gap-4">
            <div className="col-span-5 xl:col-span-7">
                <FXrates />
            </div>
            <div className="col-span-5 xl:col-span-7">
                <InterestRates />
            </div>
        </div>
    )
}