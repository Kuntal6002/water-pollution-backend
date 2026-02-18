from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy.sql import func
from app.db.base import Base


class WaterReading(Base):
    __tablename__ = "water_readings"

    id = Column(Integer, primary_key=True, index=True)

    ph = Column(Float, nullable=False)
    turbidity = Column(Float, nullable=False)
    tds = Column(Float, nullable=False)
    temperature = Column(Float, nullable=False)
    dissolved_oxygen = Column(Float, nullable=False)

    prediction = Column(String, nullable=False)
    confidence = Column(Float, nullable=False)
    model_version = Column(String, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
