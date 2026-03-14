from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Any
from tools import web_search, summarize

app = FastAPI()

class TaskRequest(BaseModel):
    message_id: str
    sender: str
    receiver: str
    type: str
    task: Dict[str, Any]


@app.get("/agent/info")
def agent_info():
    return {
        "agent_id": "research_agent",
        "capabilities": ["web_search", "summarize"],
        "endpoint": "http://localhost:8000/agent/task"
    }


@app.post("/agent/task")
def run_task(req: TaskRequest):

    try:
        print("Incoming request:", req)

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

    except Exception as e:
        print("SERVER ERROR:", str(e))
        return {"error": str(e)}