from fastapi import FastAPI
from schema import TaskRequest, TaskResponse

app = FastAPI()

AGENT_INFO = {
    "agent_id": "research_agent",
    "name": "Research Agent",
    "capabilities": ["search", "summarize"],
    "endpoint": "http://localhost:8000/agent/task"
}

@app.get("/agent/info")
def agent_info():
    return AGENT_INFO


@app.post("/agent/task")
def execute_task(task: TaskRequest):

    task_name = task.task.get("name")
    task_input = task.task.get("input")

    if task_name == "search":
        query = task_input["query"]

        result = {
            "answer": f"Search result for '{query}'"
        }

    elif task_name == "summarize":
        text = task_input["text"]

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