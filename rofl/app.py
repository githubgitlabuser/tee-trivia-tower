from fastapi import FastAPI
from pydantic import BaseModel
import hashlib, random

# from sapphirepy.rofl import sign_bytes

app = FastAPI(title="TEE Trivia Tower – ROFL")

# ▶ 50 Q/A – extend or swap freely
TRIVIA = [
    ("What is the capital of France?", "Paris"),
    ("Who wrote '1984'?", "George Orwell"),
    ("2 + 2 * 2 = ?", "6"),
    ("What gas do plants breathe in?", "Carbon Dioxide"),
    ("Who painted the Mona Lisa?", "Leonardo da Vinci"),
    ("Fastest land animal?", "Cheetah"),
    ("Largest ocean on Earth?", "Pacific"),
    ("What planet is known as the Red Planet?", "Mars"),
    ("What is H2O commonly called?", "Water"),
    ("First president of the USA?", "George Washington"),
    ("Largest mammal?", "Blue Whale"),
    ("Tallest mountain?", "Mount Everest"),
    ("Speed of light ~ ___ km/s?", "300000"),
    ("Currency of Japan?", "Yen"),
    ("Chemical symbol for Gold?", "Au"),
    ("Smallest prime number?", "2"),
    ("Who discovered penicillin?", "Alexander Fleming"),
    ("Pythagoras theorem applies to what shape?", "Right Triangle"),
    ("Which language has the most native speakers?", "Mandarin"),
    ("What year did WW2 end?", "1945"),
    ("Primary gas in Earth’s atmosphere?", "Nitrogen"),
    ("How many bones in adult human?", "206"),
    ("Author of Harry Potter?", "J.K. Rowling"),
    ("First man in space?", "Yuri Gagarin"),
    ("In computing, what does CPU stand for?", "Central Processing Unit"),
    ("What does HTML stand for?", "HyperText Markup Language"),
    ("Which element’s symbol is ‘Fe’?", "Iron"),
    ("Hardest natural substance?", "Diamond"),
    ("Who is known as the father of computers?", "Charles Babbage"),
    ("Largest desert?", "Sahara"),
    ("What does DNA stand for?", "Deoxyribonucleic Acid"),
    ("Which planet has the most moons?", "Saturn"),
    ("Fahrenheit 451 author?", "Ray Bradbury"),
    ("Smallest continent?", "Australia"),
    ("Lightest element?", "Hydrogen"),
    ("Founder of Microsoft?", "Bill Gates"),
    ("How many players in a football (soccer) team?", "11"),
    ("What instrument has 88 keys?", "Piano"),
    ("Largest volcano in the solar system?", "Olympus Mons"),
    ("Main language in Brazil?", "Portuguese"),
    ("What is the boiling point of water °C?", "100"),
    ("Who painted Starry Night?", "Vincent van Gogh"),
    ("What year did the Titanic sink?", "1912"),
    ("Heaviest terrestrial animal?", "African Elephant"),
    ("Atomic number of Oxygen?", "8"),
    ("Who developed the theory of relativity?", "Albert Einstein"),
    ("Great Barrier Reef is off which country?", "Australia"),
    ("How many hearts does an octopus have?", "3"),
    ("What is the square root of 81?", "9")
]

class QuestionPayload(BaseModel):
    question: str
    hash: str

def sign_answer(answer: str) -> str:
    """Dummy TEE-style hash: replace with py-oasis-sdk signer if desired."""
    digest = hashlib.sha256(answer.lower().encode()).hexdigest()
    return digest  # would be signature bytes in a real ROFL app
    # sig: bytes = sign_bytes(answer.lower().encode())   # enclave-sealed signature
    # return {"question": q, "sig": sig.hex()}

@app.get("/question", response_model=QuestionPayload)
def get_question():
    q, a = random.choice(TRIVIA)
    return {"question": q, "hash": sign_answer(a)}
