from pydantic import BaseModel
from typing import Dict, Any

class TaskRequest(BaseModel):
    message_id: str
    sender: str
    receiver: str
    type: str
    task: Dict[str, Any]


class TaskResponse(BaseModel):
    message_id: str
    status: str
    result: Dict[str, Any]