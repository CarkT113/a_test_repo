"use client";
import React from "react";
import { useEffect, useState } from 'react'
import {
  Table,
  TableBody,
  TableCell,
  TableHeader,
  TableRow,
} from "../ui/table";
//set up function to retrieve data

export default function countriesTable() {
  
  const [countries, setCountries] = useState([]);

  useEffect(() => {
    fetch('/api/countries/')
      .then((response) => response.json())
      .then((data) => setCountries(data))
  }, []);

  return (
    <div>
      <Table>
        {/*Header*/}
        <TableHeader>
          <TableRow>
            <TableCell isHeader>
              Country Code
            </TableCell>
            <TableCell isHeader>
              Country Name
            </TableCell>
          </TableRow>
        </TableHeader>

        {/*Body*/}
        <TableBody>
          {countries.map((country: any) => (
          <TableRow key = {country.country_code}>
            <TableCell>
              {country.country_code}
            </TableCell>
            <TableCell>
              {country.country_name}
            </TableCell>
          </TableRow>
        ))}
        </TableBody>
      </Table>
    </div>
  )
}