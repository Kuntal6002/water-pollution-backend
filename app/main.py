from fastapi import FastAPI
from app.api.routes import router as api_router
from app.api.websocket import router as ws_router
from app.db.base import Base
from app.db.session import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(api_router)
app.include_router(ws_router)
