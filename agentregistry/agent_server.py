import requests
from fastapi import FastAPI
from schema import TaskRequest, TaskResponse

app = FastAPI()

REGISTRY = "http://localhost:9000"


AGENT_INFO = {
    "agent_id": "research_agent",
    "name": "Research Agent",
    "endpoint": "http://localhost:8001/agent/task"
}


# Register agent on startup
@app.on_event("startup")
def register_agent():

    requests.post(
        f"{REGISTRY}/register",
        json=AGENT_INFO
    )


# Task execution
@app.post("/agent/task")
def execute_task(task: TaskRequest):

    if task.task == "search":

        query = task.input["query"]

        result = {
            "answer": f"Search result for {query}"
        }

    elif task.task == "summarize":

        text = task.input["text"]

        result = {
            "summary": text[:50]
        }

    else:

        result = {"error": "Unknown task"}

    return TaskResponse(
        message_id=task.message_id,
        status="completed",
        result=result
    )