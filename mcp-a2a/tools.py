from fastmcp import FastMCP

mcp = FastMCP("research-agent-tools")

@mcp.tool()
def web_search(query: str):
    """
    Search information on the web
    """
    return f"Search result for: {query}"

@mcp.tool()
def summarize(text: str):
    """
    Summarize text
    """
    return text[:60]