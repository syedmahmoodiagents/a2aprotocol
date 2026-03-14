import requests
import uuid

REGISTRY = "http://localhost:9000"

agents = requests.get(f"{REGISTRY}/agents").json()

print("Registered Agents")
print(agents)

agent = agents["research_agent"]
endpoint = agent["endpoint"]

task = {
    "message_id": str(uuid.uuid4()),
    "sender": "manager_agent",
    "receiver": "research_agent",
    "task": "search",
    "input": {
        "query": "What is Agentic AI?"
    }
}

response = requests.post(endpoint, json=task)

print("\nAgent Response")
print(response.json())