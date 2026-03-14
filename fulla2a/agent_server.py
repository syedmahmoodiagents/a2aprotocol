import requests
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Any

from tools import web_search, summarize

REGISTRY = "http://localhost:9000/register"

app = FastAPI()


class TaskRequest(BaseModel):
    message_id: str
    sender: str
    receiver: str
    type: str
    task: Dict[str, Any]


AGENT_INFO = {
    "agent_id": "research_agent",
    "name": "Research Agent",
    "capabilities": ["web_search", "summarize"],
    "endpoint": "http://localhost:8000/agent/task"
}


@app.on_event("startup")
def register_agent():

    try:
        requests.post(REGISTRY, json=AGENT_INFO)
        print("Agent registered")
    except:
        print("Registry not available")


@app.post("/agent/task")
def run_task(req: TaskRequest):

    task_name = req.task["name"]
    task_input = req.task["input"]

    if task_name == "web_search":
        result = web_search(**task_input)

    elif task_name == "summarize":
        result = summarize(**task_input)

    else:
        result = "Unknown task"

    return {
        "message_id": req.message_id,
        "status": "completed",
        "result": result
    }