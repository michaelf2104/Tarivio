from app.models import db_models
from sqlalchemy.orm import Session

def save_answer_to_db(db: Session, customer_id: str, question_key: str, answer_text: str):
    user = db.query(db_models.User).filter(db_models.User.user_id == customer_id).first()
    if not user:
        user = db_models.User(user_id=customer_id)
        db.add(user)
        db.commit()

    new_answer = db_models.Answer(
        user_id=customer_id,
        question_key=question_key,
        answer_text=answer_text
    )
    db.add(new_answer)
    db.commit()
