from app.models import db_models
from sqlalchemy.orm import Session
from fastapi import HTTPException
import uuid

def save_answer_to_db(db: Session, user_id: str, question_key: str, answer_text: str):
    try:
        user_uuid = uuid.UUID(user_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid UUID format")
    users = db.query(db_models.User).all()
    print("alle user in der db:", users)
    user = db.query(db_models.User).filter(db_models.User.user_id == user_uuid).first()
    if not user:
        raise HTTPException(status_code=400, detail="User does not exist")

    new_answer = db_models.Answer(
        user_id=user_uuid,
        question_key=question_key,
        answer_text=answer_text
    )
    db.add(new_answer)
    db.commit()
