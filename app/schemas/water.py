from pydantic import BaseModel, Field


class WaterIn(BaseModel):
    ph: float = Field(..., ge=0, le=14)
    turbidity: float = Field(..., ge=0)
    tds: float = Field(..., ge=0)
    temperature: float = Field(..., ge=-10, le=100)
    dissolved_oxygen: float = Field(..., ge=0)


class PredictionResponse(BaseModel):
    prediction: str
    confidence: float


class WaterHistory(BaseModel):
    id: int
    ph: float
    turbidity: float
    tds: float
    temperature: float
    dissolved_oxygen: float
    prediction: str
    confidence: float

    class Config:
        orm_mode = True
