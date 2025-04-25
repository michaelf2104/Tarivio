from fastapi import APIRouter, HTTPException
from ..models import schemas, db_models
from ..core.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends

router = APIRouter()

@router.post("/answers")
async def submit_answer(answer: schemas.AnswerCreate, db: Session = Depends(get_db)):
    user = db.query(db_models.User).filter(db_models.User.id == answer.user_id).first()
    if not user:
        user = db_models.User(id=answer.user_id)
        db.add(user)
        db.commit()

    db_answer = db_models.Answer(
        user_id=answer.user_id,
        question_key=answer.question_key,
        answer_text=answer.answer_text
    )
    db.add(db_answer)
    db.commit()
    return {"message": "Answer saved"}

@router.get("/summary")
async def get_summary(customer_id: str, db: Session = Depends(get_db)):
    answers = db.query(db_models.Answer).filter(db_models.Answer.user_id == customer_id).all()
    return {
        "summary": "\n".join(
            [f"{a.question_key}: {a.answer_text}" for a in answers]
        )
    }
