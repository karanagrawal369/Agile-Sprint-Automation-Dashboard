import asyncio
from datetime import datetime

class WebSocketLogger:
    _instance = None
    _clients = set()

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(WebSocketLogger, cls).__new__(cls)
        return cls._instance

    @classmethod
    async def register_client(cls, websocket):
        cls._clients.add(websocket)

    @classmethod
    def remove_client(cls, websocket):
        cls._clients.remove(websocket)

    @classmethod
    async def log(cls, agent_name, step_type, message):
        """
        Broadcasts the log message to all connected web browsers.
        """
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        # Structure data for the frontend
        log_entry = {
            "timestamp": timestamp,
            "agent": agent_name,
            "type": step_type,
            "message": message
        }

        # Send to all connected clients (browsers)
        if cls._clients:
            # We use a copy to avoid modification during iteration
            for client in list(cls._clients):
                try:
                    await client.send_json(log_entry)
                except:
                    cls.remove_client(client)