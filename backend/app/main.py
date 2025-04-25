from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import openai
import os

# load .env file
load_dotenv()

# set open ai key
openai.api_key = os.getenv("OPENAI_API_KEY")


app = FastAPI()

app.add_middleware(
    CORSMiddleware, 
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# import router AFTER setting up cors!
from app.api.routes_chats import router as chat_router
app.include_router(chat_router)
        