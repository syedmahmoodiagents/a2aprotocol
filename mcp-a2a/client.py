import requests
import uuid

SERVER = "http://localhost:8000"

info = requests.get(f"{SERVER}/agent/info").json()

print("Agent discovered:")
print(info)


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
    f"{SERVER}/agent/task",
    json=message
)

print("Status:", response.status_code)
print("Raw response:", response.text)

data = response.json()

print("Parsed response:")
print(data)

print("\nResult:")
print(data["result"])