// pages/api/users.ts
import type { NextApiRequest, NextApiResponse } from 'next';
import prisma from '../../lib/prisma'; // Assuming your Prisma client is in lib/prisma.ts

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
    if (req.method === 'GET') {
        const users = await prisma.staffs.findMany();
        res.status(200).json(users);
    } else {
        res.setHeader('Allow', ['GET']);
        res.status(405).end(`Method ${req.method} Not Allowed`);
   }
}