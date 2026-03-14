import requests
import uuid

REGISTRY = "http://localhost:9000"


# Step 1: discover agents
agents = requests.get(f"{REGISTRY}/agents").json()

print("Registered Agents")
print(agents)


# Step 2: select research agent
agent = agents["research_agent"]

endpoint = agent["endpoint"]


# Step 3: create task
task = {
    "message_id": str(uuid.uuid4()),
    "sender": "manager_agent",
    "receiver": "research_agent",
    "task": "search",
    "input": {
        "query": "What is Agentic AI?"
    }
}


# Step 4: send task
response = requests.post(endpoint, json=task)

print("\nAgent Response")
print(response.json())