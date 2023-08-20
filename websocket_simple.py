from fastapi import FastAPI, WebSocket,WebSocketDisconnect
import json

app = FastAPI()

class ConnectionManager:
    def __init__(self):
        self.active_connections = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    async def disconnect(self, websocket: WebSocket):
        await websocket.close()
        self.active_connections.remove(websocket)

    async def send_custom_dict(self, custom_dict: dict):
        message = json.dumps(custom_dict)
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            # Define your own custom dictionary
            custom_dict = {"key1": "value1", "key2": "value2"}
            await manager.send_custom_dict(custom_dict)
    except WebSocketDisconnect:
        await manager.disconnect(websocket)
