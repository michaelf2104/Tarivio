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
from app.api.routes_tariffs import router as tariffs_router
from app.api.routes_insurers import router as insurers_router
from app.api.routes_matching import router as matching_router
from app.api.routes_ppv import router as ppv_router
from app.api.routes_tariff_features import router as tariff_feature_router
from app.api.routes_tariff_costs import router as tariff_costs_router

app.include_router(chat_router)
app.include_router(matching_router)
app.include_router(tariffs_router)
app.include_router(insurers_router)
app.include_router(ppv_router)
app.include_router(tariff_feature_router)
app.include_router(tariff_costs_router)
