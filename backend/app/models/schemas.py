from pydantic import BaseModel
from typing import Optional
from uuid import UUID

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
        orm_mode = True

class TariffBase(BaseModel):
    id: str
    name: str
    type: str  # "basetarif" or "addontarif"
    cost: float
    deductible: str
    selfpay_type: str
    selfpay_amount: float
    insurer_id: str
    features: Optional[dict] = None

class TariffCreate(TariffBase):
    pass

class TariffResponse(TariffBase):
    class Config:
        orm_mode = True

class TariffCombinationBase(BaseModel):
    id: str
    basetarif_id: str
    addontarif_id: str

class TariffCombinationCreate(TariffCombinationBase):
    pass

class TariffCombinationResponse(TariffCombinationBase):
    class Config:
        orm_mode = True

class PflegepflichtversicherungBase(BaseModel):
    id: str
    insurer_id: str
    min_age: int
    max_age: int
    cost: float
    special_conditions: Optional[dict] = None

class PflegepflichtversicherungCreate(PflegepflichtversicherungBase):
    pass

class PflegepflichtversicherungResponse(PflegepflichtversicherungBase):
    class Config:
        orm_mode = True

