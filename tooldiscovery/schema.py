from pydantic import BaseModel
from typing import Dict, Any, List


class AgentRegistration(BaseModel):
    agent_id: str
    name: str
    endpoint: str
    tools: List[str]


class TaskRequest(BaseModel):
    message_id: str
    sender: str
    receiver: str
    tool: str
    input: Dict[str, Any]


class TaskResponse(BaseModel):
    message_id: str
    status: str
    result: Dict[str, Any]