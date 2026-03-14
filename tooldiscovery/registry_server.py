from fastapi import FastAPI
from schema import AgentRegistration

app = FastAPI()

AGENTS = {}


@app.post("/register")
def register_agent(agent: AgentRegistration):

    AGENTS[agent.agent_id] = agent

    return {
        "status": "registered",
        "agent_id": agent.agent_id
    }


@app.get("/agents")
def list_agents():
    return AGENTS


@app.get("/agents/{agent_id}")
def get_agent(agent_id: str):

    if agent_id not in AGENTS:
        return {"error": "agent not found"}

    return AGENTS[agent_id]