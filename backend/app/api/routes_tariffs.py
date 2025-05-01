from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models import schemas, db_models

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
            type=tariff.type,
            cost=tariff.cost,
            deductible=tariff.deductible,
            selfpay_type=tariff.selfpay_type,
            selfpay_amount=tariff.selfpay_amount,
            insurer_id=tariff.insurer_id,
            features=tariff.features
        )
        db.add(new_tariff)
        db.commit()
        db.refresh(new_tariff)
        return new_tariff
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

