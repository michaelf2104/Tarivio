from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models import schemas, db_models
from app.core.logging_config import get_logger

logger = get_logger(__name__)
router = APIRouter(
    prefix="/api",
    tags=["tariff_costs"]
)

@router.post("/tariff-costs", response_model=schemas.TariffCostResponse)
def create_tariff_cost(cost: schemas.TariffCostCreate, db: Session = Depends(get_db)):
    try:
        new_cost = db_models.TariffCost(
            tariff_id=cost.tariff_id,
            age_min=cost.age_min,
            age_max=cost.age_max,
            monthly_cost=cost.monthly_cost
        )
        db.add(new_cost)
        db.commit()
        db.refresh(new_cost)
        logger.info(f"TariffCost created for tariff_id={cost.tariff_id} ({cost.age_min}-{cost.age_max} Jahre)")
        return new_cost
    except Exception as e:
        logger.error(f"Failed to create tariff cost: {e}")
        raise HTTPException(status_code=500, detail="Could not create tariff cost")
