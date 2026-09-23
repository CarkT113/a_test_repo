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


export default function test112() {
  
  const [staffs, setStaffs] = useState([]);

  useEffect(() => {
    fetch('/api/staffs/')
      .then((response) => response.json())
      .then((data) => setStaffs(data))
  }, []);

  return (
    <div>
      <Table>
        {/*Header*/}
        <TableHeader>
          <TableRow>
            <TableCell isHeader>
              Staff ID
            </TableCell>
            <TableCell isHeader>
              Staff Name
            </TableCell>
            <TableCell isHeader>
              Staff Age
            </TableCell>
          </TableRow>
        </TableHeader>

        {/*Body*/}
        <TableBody>
          {staffs.map((staff: any) => (
          <TableRow key = {staff.staffid}>
            <TableCell>
              {staff.staffid}
            </TableCell>
            <TableCell>
              {staff.name}
            </TableCell>
            <TableCell>
              {staff.age}
            </TableCell>
          </TableRow>
        ))}
        </TableBody>
      </Table>
    </div>
  )
}