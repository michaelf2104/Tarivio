from datetime import datetime
from sqlalchemy import Column, String, DateTime, ForeignKey, Integer, Float, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from app.core.database import Base

class User(Base):
    __tablename__ = "users"
    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    birthdate = Column(DateTime, nullable=False)
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

class Insurer(Base):
    __tablename__ = "insurers"
    id = Column(String, primary_key=True, index=True)  
    name = Column(String, unique=True)
    tariffs = relationship("Tariff", back_populates="insurer")

class Tariff(Base):
    __tablename__ = "tariffs"
    id = Column(String, primary_key=True, index=True) 
    name = Column(String)
    type = Column(String)  # "basetarif" or "addontarif"
    cost = Column(Float)
    deductible = Column(String)
    selfpay_type = Column(String)
    selfpay_amount = Column(Float)
    insurer_id = Column(String, ForeignKey("insurers.id"))
    insurer = relationship("Insurer", back_populates="tariffs")
    features = Column(JSON, nullable=True)

class TariffCombination(Base):
    __tablename__ = "tariff_combinations"
    id = Column(String, primary_key=True, index=True)  
    basetarif_id = Column(String, ForeignKey("tariffs.id"))
    addontarif_id = Column(String, ForeignKey("tariffs.id"))

class Pflegepflichtversicherung(Base):
    __tablename__ = "ppv"  # pflegepflichtversicherung
    id = Column(String, primary_key=True, index=True) 
    insurer_id = Column(String, ForeignKey("insurers.id"), nullable=False)
    min_age = Column(Integer, nullable=False)
    max_age = Column(Integer, nullable=False)
    cost = Column(Float, nullable=False)
    special_conditions = Column(JSON, nullable=True)

    insurer = relationship("Insurer")
