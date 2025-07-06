import { useState } from "react";
import confetti from "canvas-confetti";

export default function AnswerBox() {
  const [answer, setAnswer] = useState("");

  function checkAnswer() {
    const hash = localStorage.getItem("currentHash");
    const attempt = crypto.subtle.digest
      ? crypto.subtle.digest("SHA-256", new TextEncoder().encode(answer.toLowerCase()))
      : Promise.resolve(new ArrayBuffer(0));

    attempt.then(buf => {
      const h = Array.from(new Uint8Array(buf))
        .map(b => b.toString(16).padStart(2, "0"))
        .join("");
      if (h === hash) {
        confetti();
        const score = Number(localStorage.getItem("score") || 0) + 1;
        localStorage.setItem("score", String(score));
        alert("Correct! 🎉");
      } else {
        alert("Try again!");
      }
    });
  }

  return (
    <div className="flex gap-2">
      <input
        className="border rounded-xl px-3 py-2"
        value={answer}
        onChange={e => setAnswer(e.target.value)}
        placeholder="Your answer..."
      />
      <button className="bg-green-600 text-white px-4 rounded-xl" onClick={checkAnswer}>
        Submit
      </button>
    </div>
  );
}
