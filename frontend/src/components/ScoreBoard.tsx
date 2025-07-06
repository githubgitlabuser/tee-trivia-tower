import { useEffect, useState } from "react";

export default function ScoreBoard() {
  const [score, setScore] = useState<number>(0);
  useEffect(() => {
    setScore(Number(localStorage.getItem("score") || 0));
    const i = setInterval(() => setScore(Number(localStorage.getItem("score") || 0)), 1000);
    return () => clearInterval(i);
  }, []);
  return <p className="text-lg">Score: {score}</p>;
}
