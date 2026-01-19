import asyncio
import sys
from fastmcp.client.transports import StdioTransport
from fastmcp import Client

async def main():
    transport = StdioTransport(
        command=sys.executable,
        args=["app/proxy_server/server.py"]
    )

    client = Client(transport)

    async with client:
        # 1️⃣ prove connection
        await client.ping()

        # 2️⃣ list tools
        tools = await client.list_tools()
        print("TOOLS:", tools)

        # 3️⃣ call the tool
        # result = await client.call_tool()
        # print("RESULT:", result)

if __name__ == "__main__":
    asyncio.run(main())
