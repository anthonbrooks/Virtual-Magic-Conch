from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.services.search import search_web
from backend.services.scraper import gather_context
from backend.services.ai import ask_ai
from pydantic import BaseModel

from my_module.functions import magic_conch

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:5173",
    "https://virtual-magic-conch.onrender.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    text: str

@app.post("/chat")
def chat(message: Message):
    try:
        user_text = message.text

        # Try Magic Conch first
        conch_answer = magic_conch(user_text)
        if conch_answer:  # if your function returns a non-empty answer
            return {"reply": conch_answer}

        # Otherwise use AI/web search
        urls = search_web(user_text)

        context = gather_context(urls)

        answer = ask_ai(user_text, context)

        return {"reply": answer}
    except Exception as e:
        print("Error in /chat:", e)
        return {"reply": f"Error: {e}"}