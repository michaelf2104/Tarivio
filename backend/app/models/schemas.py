from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from app.models.enum_declaration import TariffLevel, ValueType


class AnswerCreate(BaseModel):
    user_id: UUID
    question_key: str
    answer_text: str

class AnswerResponse(BaseModel):
    question_key: str
    answer_text: str

class SummaryResponse(BaseModel):
    summary: str

class QuestionRequest(BaseModel):
    question: str

class InsurerBase(BaseModel):
    id: str
    name: str

class InsurerCreate(InsurerBase):
    pass

class InsurerResponse(InsurerBase):
    class Config:
        from_attributes = True

class TariffBase(BaseModel):
    id: str
    name: str
    insurer_id: str
    level: TariffLevel

class TariffCreate(TariffBase):
    pass

class TariffResponse(TariffBase):
    class Config:
        from_attributes = True

class TariffFeatureBase(BaseModel):
    tariff_id: str
    key: str
    name: str
    description_short: str
    description_long: str
    value: str
    value_type: ValueType

class TariffFeatureCreate(TariffFeatureBase):
    pass 

class TariffFeatureResponse(TariffFeatureBase):
    class Config:
        from_attributes = True  

class TariffCostBase(BaseModel):
    tariff_id: str
    age_min: int
    age_max: int
    monthly_cost: float

class TariffCostCreate(TariffCostBase):
    pass


class TariffCostResponse(TariffCostBase):
    class Config:
        from_attributes = True


class PflegepflichtversicherungBase(BaseModel):
    id: str
    insurer_id: str
    cost: float
    special_conditions: Optional[dict] = None

class PflegepflichtversicherungCreate(PflegepflichtversicherungBase):
    pass

class PflegepflichtversicherungResponse(PflegepflichtversicherungBase):
    class Config:
        orm_mode = True

