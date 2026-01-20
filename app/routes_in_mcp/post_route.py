from fastmcp import FastMCP
from starlette.requests import Request
from starlette.responses import JSONResponse, PlainTextResponse

mcp = FastMCP("Post route server")

@mcp.custom_route("/health", methods=["POST"])
async def health(request: Request) -> JSONResponse:
    data = await request.json()
    print(data)
    return JSONResponse({"status": "ok"})

@mcp.custom_route("/number", methods=["POST"])
async def number_route(request: Request):
    body = await request.body()
    text = body.decode("utf-8").strip()
    another_text = body.decode("utf-8")
    print(text)
    print(another_text)

    if not text.isdigit():
        return PlainTextResponse(
            "Body must contain a single integer",
            status_code=400
        )

    number = int(text)
    print("Received number:", number)
    
    return PlainTextResponse(f"Received number: {number}")

if __name__ == "__main__":
    mcp.run(transport="http")
