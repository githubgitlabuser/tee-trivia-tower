import { useState } from "react";

export default function StartRound() {
  const [question, setQuestion] = useState<string | null>(null);
  const [hash, setHash] = useState<string | null>(null);

  async function fetchQuestion() {
    // const res = await fetch("/api/proxy"); // see next.config.js rewrite
    const res = await fetch("/api/question");
    const data = await res.json();
    setQuestion(data.question);
    setHash(data.hash);
    localStorage.setItem("currentHash", data.hash);
  }

  return (
    <div className="flex flex-col items-center gap-4">
      <button
        className="px-6 py-2 rounded-xl bg-blue-600 text-white"
        onClick={fetchQuestion}
      >
        Start / Next Question
      </button>
      {question && <p className="text-xl">{question}</p>}
    </div>
  );
}
