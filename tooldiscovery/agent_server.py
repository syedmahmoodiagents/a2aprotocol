import requests
from fastapi import FastAPI
from schema import TaskRequest, TaskResponse

app = FastAPI()

REGISTRY = "http://localhost:9000"


AGENT_INFO = {
    "agent_id": "research_agent",
    "name": "Research Agent",
    "endpoint": "http://localhost:8001/agent/task",
    "tools": ["search", "summarize"]
}


# Register agent on startup
@app.on_event("startup")
def register_agent():

    requests.post(
        f"{REGISTRY}/register",
        json=AGENT_INFO
    )


# Tool discovery
@app.get("/tools")
def get_tools():
    return {
        "agent_id": AGENT_INFO["agent_id"],
        "tools": AGENT_INFO["tools"]
    }


# Task execution
@app.post("/agent/task")
def execute_task(task: TaskRequest):

    if task.tool == "search":

        query = task.input["query"]

        result = {
            "answer": f"Search result for {query}"
        }

    elif task.tool == "summarize":

        text = task.input["text"]

        result = {
            "summary": text[:50]
        }

    else:

        result = {"error": "Unknown tool"}

    return TaskResponse(
        message_id=task.message_id,
        status="completed",
        result=result
    )