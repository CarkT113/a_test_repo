//app router
import { NextResponse } from 'next/server';
import prisma from '../../lib/prisma'; // Adjust path as needed

export async function GET() {
    const staffs = await prisma.vwucinterestratesevenyrs.findMany();
    return NextResponse.json(staffs);
}