// frontend/src/pages/api/question.ts
import type { NextApiRequest, NextApiResponse } from "next";

export default async function handler(_: NextApiRequest, res: NextApiResponse) {
  const base =
    process.env.ROFL_URL || // set by docker-compose
    "http://localhost:8000"; // when you run Next on host

  try {
    const r = await fetch(`${base}/question`);
    if (!r.ok) throw new Error(`ROFL returned ${r.status}`);
    const data = await r.json();
    res.status(200).json(data);
  } catch (e: any) {
    res.status(502).json({ error: e.message || "ROFL offline?" });
  }
}
