from fastapi import FastAPI

app = FastAPI()

agent_registry = {}


@app.post("/register")
def register_agent(agent: dict):

    agent_registry[agent["agent_id"]] = agent

    return {"status": "registered"}


@app.get("/agents")
def list_agents():

    return agent_registry