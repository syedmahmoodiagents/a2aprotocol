import os
from dotenv import load_dotenv
load_dotenv()
os.getenv("HF_TOKEN")

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.messages import HumanMessage, SystemMessage

llm = ChatHuggingFace(llm=HuggingFaceEndpoint(repo_id='openai/gpt-oss-20b'))

from fastmcp import FastMCP

mcp = FastMCP("research-agent-tools")

@mcp.tool()
def web_search(query: str):
    """
    Search and explain a topic
    """
    
    messages = [
        SystemMessage(content="Explain briefly in 3-4 sentences."),
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