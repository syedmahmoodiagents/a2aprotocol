import os
from dotenv import load_dotenv
load_dotenv()
os.getenv("HF_TOKEN")

from fastmcp import FastMCP
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import HumanMessage, SystemMessage

mcp = FastMCP("research_agent_tools")

llm = ChatHuggingFace(
    llm=HuggingFaceEndpoint(
        repo_id="openai/gpt-oss-20b",
        task="text-generation"
    )
)


@mcp.tool()
def web_search(query: str):

    messages = [
        SystemMessage(content="Explain the topic clearly in 3 sentences."),
        HumanMessage(content=query)
    ]

    response = llm.invoke(messages)

    return response.content


@mcp.tool()
def summarize(text: str):

    messages = [
        SystemMessage(content="Summarize the text briefly."),
        HumanMessage(content=text)
    ]

    response = llm.invoke(messages)

    return response.content