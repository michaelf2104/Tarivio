from datetime import datetime
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from app.core.database import Base

class User(Base):
    __tablename__ = "users"
    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    email = Column(String, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    answers = relationship("Answer", back_populates="user")

class Answer(Base):
    __tablename__ = "answers"

    answer_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    question_key = Column(String, nullable=False)
    answer_text = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    # link to user
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"), nullable=False)
    user = relationship("User", back_populates="answers")