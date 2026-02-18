from sqlalchemy.orm import Session
from app.db.models import WaterReading


def create_reading(db: Session, data, prediction, confidence, model_version):
    reading = WaterReading(
        **data.dict(),
        prediction=prediction,
        confidence=confidence,
        model_version=model_version
    )
    db.add(reading)
    db.commit()
    db.refresh(reading)
    return reading
