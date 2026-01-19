import asyncio
from dotenv import load_dotenv

from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI

load_dotenv()

SERVER = {
    "StructuredOutputServer": {
        "transport": "stdio",
        "command": "C:\\Users\\Abdurrazzak Shaikh\\.local\\bin\\uv.exe",
        "args": [
            "run",
            "fastmcp",
            "run",
            "D:\\Rnt_Tasks\\Model-Context-Protocol-MCP\\app\\Structured_output_in_mcp\\structured_output1.py"
        ],
    }
}


async def main():
    # 1️⃣ Connect to MCP server
    client = MultiServerMCPClient(SERVER)

    # 2️⃣ Load MCP tools (these are LangChain tools already)
    tools = await client.get_tools()

    # Map tools by name for execution later
    tool_map = {tool.name: tool for tool in tools}

    # 3️⃣ Create Gemini model
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0,
    )

    # 4️⃣ Bind tools (PASS THE LIST, NOT ONE TOOL)
    llm_with_tools = llm.bind_tools(tools)

    # 5️⃣ Send user input
    response = await llm_with_tools.ainvoke(
        "These earbuds are very bad!"
    )

    # 6️⃣ Check if model wants a tool call
    if response.tool_calls:
        tool_call = response.tool_calls[0]

        tool_name = tool_call["name"]
        tool_args = tool_call["args"]
        tool_id = tool_call["id"]

        # 7️⃣ Execute MCP tool
        tool = tool_map[tool_name]
        tool_result = await tool.ainvoke(tool_args)

        # 8️⃣ Send tool result back to the model
        final_response = await llm_with_tools.ainvoke(
            [
                response,
                {
                    "role": "tool",
                    "tool_call_id": tool_id,
                    "content": tool_result,
                },
            ]
        )

        # 9️⃣ FINAL OUTPUT
        print("\n=== FINAL MODEL OUTPUT ===")
        print(final_response.content)

    else:
        # Model answered directly (no tool)
        print("\n=== MODEL OUTPUT ===")
        print(response.content)


if __name__ == "__main__":
    asyncio.run(main())
