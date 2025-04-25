from pydantic import BaseModel

class AnswerCreate(BaseModel):
    user_id: str
    question_key: str
    answer_text: str

class AnswerResponse(BaseModel):
    question_key: str
    answer_text: str

class SummaryResponse(BaseModel):
    summary: str

class AnswerCreate(BaseModel):
    customer_id: str
    question_key: str
    answer_text: str

class QuestionRequest(BaseModel):
    question: str