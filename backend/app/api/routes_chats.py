from fastapi import APIRouter, HTTPException, Depends
from app.models import schemas, db_models
from app.core.database import get_db
from sqlalchemy.orm import Session
from openai import OpenAI
import os
from app.core.logging_config import get_logger

logger = get_logger(__name__)

router = APIRouter(
    prefix="/api",
    tags=["chat"]
)

class QuestionRequest(schemas.QuestionRequest):
    question: str

"""
endpoint to persist user answers to the database
"""
@router.post("/answers")
async def save_answer(answer: schemas.AnswerCreate, db: Session = Depends(get_db)):
    try:
        new_answer = db_models.Answer(
            user_id=answer.user_id,
            question_key=answer.question_key,
            answer_text=answer.answer_text,
        )
        db.add(new_answer)
        db.commit()
        logger.info(f"Answer saved for user_id={answer.user_id}, question_key={answer.question_key}")
        return {"message": "Anwer saved"}
    except Exception as e:
        logger.error(f"Failed to save answer: {e}")
        raise HTTPException(status_code=500, detail="Failed to save answer.")

"""
endpoint to send a user question to the openai api and return the response
"""
@router.post("/question")
async def ask_question(data: QuestionRequest):
    try:
        logger.info(f"Sending question to OpenAI: {data.question}")
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
        logger.info("Received response from OpenAI.")
        return {"answer": answer}
    except Exception as e:
        print(f"OpenAI API error: {e}")
        raise HTTPException(status_code=500, detail="Could not generate AI answer.")
