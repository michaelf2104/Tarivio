from app.models.db_models import Answer
from app.core.database import SessionLocal

def save_answer_to_db(customer_id: str, question: str, answer: str):
    db = SessionLocal()
    try:
        new_entry = Answer(
            customer_id=customer_id,
            question=question,
            answer=answer
        )
        db.add(new_entry)
        db.commit()
    except Exception as e:
        db.rollback()
    finally:
        db.close()
