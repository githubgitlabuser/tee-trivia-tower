import Head from "next/head";
import StartRound from "@/components/StartRound";
import AnswerBox from "@/components/AnswerBox";
import ScoreBoard from "@/components/ScoreBoard";

export default function Home() {
  return (
    <>
      <Head><title>TEE Trivia Tower</title></Head>
      <main className="flex flex-col gap-8 items-center p-8">
        <h1 className="text-4xl font-bold">TEE Trivia Tower 🏰</h1>
        <StartRound />
        <AnswerBox />
        <ScoreBoard />
      </main>
    </>
  );
}
