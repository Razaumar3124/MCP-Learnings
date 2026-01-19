import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient

SERVERS = {
    "math": {
        "transport": "stdio",
        "command": "C:\\Users\\Abdurrazzak Shaikh\\AppData\\Local\\Programs\\Python\\Python313\\Scripts",
        "args": [
            "run",
            "fastmcp",
            "run",
            "D:\Rnt_Tasks\Model-Context-Protocol-MCP\app\4_Mcp_math_server_own_Mcp_client\server.py"
        ]
    }
}

async def main():
    client = MultiServerMCPClient(SERVERS)
    tools = client.get_tools()
    print(tools)
    
if __name__ == "__main__":
    asyncio.run(main())