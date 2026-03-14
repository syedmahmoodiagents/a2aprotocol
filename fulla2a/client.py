import requests
import uuid

REGISTRY = "http://localhost:9000/agents"

agents = requests.get(REGISTRY).json()

print("Registered agents:")
print(agents)

research_agent = agents["research_agent"]

message = {
    "message_id": str(uuid.uuid4()),
    "sender": "manager_agent",
    "receiver": "research_agent",
    "type": "task",
    "task": {
        "name": "web_search",
        "input": {
            "query": "What is Agentic AI?"
        }
    }
}

response = requests.post(
    research_agent["endpoint"],
    json=message
)

data = response.json()

print("\nResult:")
print(data["result"])