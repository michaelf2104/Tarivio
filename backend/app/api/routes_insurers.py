from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import schemas, db_models
from app.core.database import get_db
from app.core.logging_config import get_logger

logger = get_logger(__name__)
router = APIRouter(
    prefix="/api",
    tags=["insurers"]
)

"""
endpoint to create a new insurer entry in the database
"""
@router.post("/insurers")
def create_insurer(insurer: schemas.InsurerCreate, db: Session = Depends(get_db)):
    try:
        new_insurer = db_models.Insurer(
            id=insurer.id,
            name=insurer.name
        )
        db.add(new_insurer)
        db.commit()
        db.refresh(new_insurer)
        logger.info(f"Insurer created with id={insurer.id}, name={insurer.name}")
        return new_insurer
    except Exception as e:
        logger.error(f"Failed to create insurer: {e}")
        raise HTTPException(status_code=500, detail="Failed to create insurer.")