from fastapi import APIRouter, WebSocket
import asyncio

router = APIRouter()
connections = []


@router.websocket("/stream")
async def stream(websocket: WebSocket):
    await websocket.accept()
    connections.append(websocket)

    try:
        while True:
            await asyncio.sleep(1)
    except:
        connections.remove(websocket)
