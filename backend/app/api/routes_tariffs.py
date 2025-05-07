from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models import schemas, db_models
from app.core.logging_config import get_logger 

logger = get_logger(__name__)
router = APIRouter(
    prefix="/api",
    tags=["tariffs"]
)

@router.post("/tariffs", response_model=schemas.TariffResponse)
def create_tariff(tariff: schemas.TariffCreate, db: Session = Depends(get_db)):
    try:
        new_tariff = db_models.Tariff(
            id=tariff.id,
            name=tariff.name,
            insurer_id=tariff.insurer_id,
            level=tariff.level,
        )
        db.add(new_tariff)
        db.commit()
        db.refresh(new_tariff)
        logger.info(f"Tariff created with id={tariff.id}, name={tariff.name}")
        return new_tariff
    except Exception as e:
        logger.error(f"Failed to create tariff: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    

