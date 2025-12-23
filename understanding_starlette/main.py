from ast import main
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


async def homepage(request):
    return JSONResponse({"Hello": "World"})

# async def otherpage(request):
#     return JSONResponse({"other": "page"})

app = Starlette(debug=True, routes=[
     Route("/", homepage)])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)