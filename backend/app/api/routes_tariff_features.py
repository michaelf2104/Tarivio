from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models import schemas, db_models
from app.core.logging_config import get_logger

logger = get_logger(__name__)
router = APIRouter(
    prefix="/api",
    tags=["tariff_features"]
)

@router.post("/tariff-features", response_model=schemas.TariffFeatureResponse)
def create_tariff_feature(feature: schemas.TariffFeatureCreate, db: Session = Depends(get_db)):
    try:
        new_feature = db_models.TariffFeature(
            tariff_id=feature.tariff_id,
            key=feature.key,
            name=feature.name,
            description_short=feature.description_short,
            description_long=feature.description_long,
            value=feature.value,
            value_type=feature.value_type
        )
        db.add(new_feature)
        db.commit()
        db.refresh(new_feature)
        logger.info(f"TariffFeature created: {feature.name} for tariff_id={feature.tariff_id}")
        return new_feature
    except Exception as e:
        logger.error(f"Failed to create tariff feature: {e}")
        raise HTTPException(status_code=500, detail="Could not create tariff feature")
