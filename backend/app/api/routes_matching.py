from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from typing import Dict
from pydantic import BaseModel

router = APIRouter(
    prefix="/api",
    tags=["matching"]
)

class MatchingRequest(BaseModel):
    user_answers: Dict[str, str]
    yearly_visits: int
