from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models import schemas, db_models

router = APIRouter(
    prefix="/api",
    tags=["pflegepflichtversicherungen"]
)

@router.post("/ppv", response_model=schemas.PflegepflichtversicherungResponse)
def create_pvns(ppv: schemas.PflegepflichtversicherungCreate, db: Session = Depends(get_db)):
    try:
        new_ppv = db_models.Pflegepflichtversicherung(
            id=ppv.id,
            insurer_id=ppv.insurer_id,
            min_age=ppv.min_age,
            max_age=ppv.max_age,
            cost=ppv.cost,
            special_conditions=ppv.special_conditions
        )
        db.add(new_ppv)
        db.commit()
        db.refresh(new_ppv)
        return new_ppv
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
