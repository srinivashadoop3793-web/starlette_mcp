from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route, Mount
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("sse-demo")

#add mcp tools
@mcp.tool()
def add(a: int, b: int) -> int:
    """_Add two numberss"""
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """_Multiply two numbers"""
    return a * b

@mcp.tool()
def echo(message: str)-> str:
    """Greeting message"""
    return f"you are called a {message}"


#create starlette app
app = Starlette(routes=[
Mount("/", app = mcp.sse_app())
])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
