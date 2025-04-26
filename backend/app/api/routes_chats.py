from fastapi import APIRouter, HTTPException, Depends
from app.models import schemas, db_models
from app.services.storage import save_answer_to_db
from app.core.database import get_db
from sqlalchemy.orm import Session
from openai import OpenAI
import os

router = APIRouter(
    prefix="/api",
    tags=["chat"]
)

class QuestionRequest(schemas.QuestionRequest):
    question: str

@router.post("/answers")
async def receive_answer(data: schemas.AnswerCreate, db: Session = Depends(get_db)):
    try:
        save_answer_to_db(db, data.user_id, data.question_key, data.answer_text)
    except Exception as e:
        print(f"Fehler beim Speichern: {e}")
        raise HTTPException(status_code=500, detail="Error while saving answer")
    return {"status": "saved"}

@router.get("/summary")
async def get_summary(user_id: str, db: Session = Depends(get_db)):
    answers = (
        db.query(db_models.Answer)
        .filter(db_models.Answer.user_id == user_id)
        .order_by(db_models.Answer.timestamp)
        .all()
    )
    return {
        "summary": "\n".join(
            [f"{a.question_key}: {a.answer_text}" for a in answers]
        )
    }

@router.post("/question")
async def ask_question(data: QuestionRequest):
    try:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "Du bist ein Versicherungs-Experte für private Krankenversicherungen."
                },
                {
                    "role": "user",
                    "content": data.question
                }
            ]
        )
        answer = response.choices[0].message.content.strip()
        return {"answer": answer}
    except Exception as e:
        print(f"OpenAI API error: {e}")
        raise HTTPException(status_code=500, detail="KI-Antwort konnte nicht generiert werden.")
