import requests
import uuid

SERVER = "http://localhost:8000"

info = requests.get(f"{SERVER}/agent/info").json()

print("Discovered Agent:")
print(info)


message = {
    "message_id": str(uuid.uuid4()),
    "sender": "manager_agent",
    "receiver": "research_agent",
    "type": "task",
    "task": {
        "name": "search",
        "input": {
            "query": "What is Agentic AI?"
        }
    }
}


response = requests.post(
    f"{SERVER}/agent/task",
    json=message
)

print("\nResponse:")
print(response.json())