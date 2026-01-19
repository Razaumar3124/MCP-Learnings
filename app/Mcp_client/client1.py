from fastmcp import Client, FastMCP
import asyncio

mcp = FastMCP("My Mcp Server")

async def main():
    async with Client("server.py") as client:
        tools = await client.list_tools()
        print(f"Available tools: {tools}")

if __name__ == "__main__":
    asyncio.run(main())