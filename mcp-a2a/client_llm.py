import requests
import uuid

SERVER = "http://localhost:8000"

# Discover the agent
try:
    info_response = requests.get(f"{SERVER}/agent/info")
    info_response.raise_for_status()

    agent_info = info_response.json()

    print("Agent discovered:")
    print(agent_info)

except Exception as e:
    print("Agent discovery failed:", e)
    exit()


# Build A2A message
message = {
    "message_id": str(uuid.uuid4()),
    "sender": "manager_agent",
    "receiver": agent_info["agent_id"],
    "type": "task",
    "task": {
        "name": "web_search",
        "input": {
            "query": "What is Agentic AI?"
        }
    }
}

# Send task to agent
try:

    response = requests.post(
        agent_info["endpoint"],
        json=message,
        timeout=30
    )

    print("\nHTTP Status:", response.status_code)

except requests.exceptions.RequestException as e:
    print("Request failed:", e)
    exit()


# Parse server response
try:

    data = response.json()

    print("\nFull response:")
    print(data)

    if "result" in data:
        print("\nResult:")
        print(data["result"])
    else:
        print("\nNo result field returned by server.")

except ValueError:

    print("\nServer did not return JSON.")
    print("Raw response:")
    print(response.text)