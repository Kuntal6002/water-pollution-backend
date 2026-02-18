from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.water import WaterIn, PredictionResponse, WaterHistory
from app.services.inference_service import InferenceService
from app.services.water_service import create_reading
from app.db.models import WaterReading

router = APIRouter()
inference_service = InferenceService()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/ingest", response_model=PredictionResponse)
def ingest(data: WaterIn, db: Session = Depends(get_db)):
    prediction, confidence, version = inference_service.predict(data.dict())
    create_reading(db, data, prediction, confidence, version)

    return {"prediction": prediction, "confidence": confidence}


@router.get("/latest", response_model=WaterHistory)
def latest(db: Session = Depends(get_db)):
    return db.query(WaterReading).order_by(
        WaterReading.created_at.desc()
    ).first()


@router.get("/history")
def history(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(WaterReading).offset(skip).limit(limit).all()
