import PageBreadcrumb from "@/components/common/PageBreadCrumb";
import ComponentCard from "@/components/common/ComponentCard";
import DynamicCountries from "@/components/tables/DynamicCountries";
import { Metadata } from "next";
import React from "react";


export const metadata: Metadata = {
  title: "Next.js Line Chart | TailAdmin - Next.js Dashboard Template",
  description:
    "This is Next.js Line Chart page for TailAdmin - Next.js Tailwind CSS Admin Dashboard Template",
};

export default async function countries() {
  return (
    <div>
      <PageBreadcrumb pageTitle="Index - Country" />
      <div className="space-y-6">
        <ComponentCard title="test for import" className="text-center">
          <div>
            <p>texts are imported directly from the database</p>
            <DynamicCountries />
          </div>
        </ComponentCard>
      </div>
    </div>
  );
}
