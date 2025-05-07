from datetime import datetime
from sqlalchemy import Column, String, DateTime, ForeignKey, Integer, Float, JSON, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from app.core.database import Base
from .enum_declaration import TariffLevel, ValueType

class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    birthdate = Column(DateTime, nullable=False)
    email = Column(String, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    answers = relationship("Answer", back_populates="user")


class Answer(Base):
    __tablename__ = "answer"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    question_key = Column(String, nullable=False)
    answer_text = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="answers")


class Insurer(Base):
    __tablename__ = "insurer"
    id = Column(String, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)


class Tariff(Base):
    __tablename__ = "tariff"
    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    insurer_id = Column(String, ForeignKey("insurer.id"), nullable=False)
    level = Column(Enum(TariffLevel), nullable=False)
    features = relationship("TariffFeature", back_populates="tariff")
    cost = relationship("TariffCost", back_populates="tariff")


class TariffFeature(Base):
    __tablename__ = "tariff_feature"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    tariff_id = Column(String, ForeignKey("tariff.id"), nullable=False)
    key = Column(String, nullable=False)
    name = Column(String, nullable=False)
    description_short = Column(String, nullable=False)
    description_long = Column(String, nullable=False)
    value = Column(String, nullable=False)
    value_type = Column(Enum(ValueType), nullable=False)
    tariff = relationship("Tariff", back_populates="features")


class TariffCost(Base):
    __tablename__ = "tariff_cost"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    tariff_id = Column(String, ForeignKey("tariff.id"), nullable=False)
    age_min = Column(Integer, nullable=False)
    age_max = Column(Integer, nullable=False)
    monthly_cost = Column(Float, nullable=False)
    tariff = relationship("Tariff", back_populates="cost")


class Pflegepflichtversicherung(Base):
    __tablename__ = "ppv"  # pflegepflichtversicherung
    id = Column(String, primary_key=True, index=True) 
    insurer_id = Column(String, ForeignKey("insurer.id"), nullable=False)
    cost = Column(Float, nullable=False)
    special_conditions = Column(JSON, nullable=True)
    insurer = relationship("Insurer")
