import requests
import uuid

REGISTRY = "http://localhost:9000"


# Step 1: Discover agents
agents = requests.get(f"{REGISTRY}/agents").json()

print("Registered Agents")
print(agents)


# Step 2: Select research agent
agent = agents["research_agent"]

endpoint = agent["endpoint"]


# Step 3: Discover tools
tools = requests.get(endpoint.replace("/agent/task", "/tools")).json()

print("\nAvailable Tools")
print(tools)


# Step 4: Create task
task = {
    "message_id": str(uuid.uuid4()),
    "sender": "manager_agent",
    "receiver": "research_agent",
    "tool": "search",
    "input": {
        "query": "What is Graph RAG?"
    }
}


# Step 5: Send task
response = requests.post(endpoint, json=task)

print("\nAgent Response")
print(response.json())