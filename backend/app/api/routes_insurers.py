from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import schemas, db_models
from app.core.database import get_db

router = APIRouter(
    prefix="/api",
    tags=["insurers"]
)

@router.post("/insurers")
def create_insurer(insurer: schemas.InsurerCreate, db: Session = Depends(get_db)):
    new_insurer = db_models.Insurer(
        id=insurer.id,
        name=insurer.name
    )
    db.add(new_insurer)
    db.commit()
    db.refresh(new_insurer)
    return new_insurer