from fastmcp import FastMCP, Context
from dataclasses import dataclass

mcp = FastMCP("Elicitation Server")

@dataclass
class UserInfo:
    name: str
    age: int
    
@mcp.tool()
async def collect_user_info(ctx: Context) -> str:
    """Collect user information through interactive prompts."""
    result = await ctx.elicit(
        message="Please provide your information",
        response_type=UserInfo
    )
    
    if result.action == "accept":
        user = result.data
        return f"Hello {user.name}, you are {user.age} years old."
    elif result.action == "decline":
        return "Information not provided"
    else:
        return "Operation Cancelled"
    
    
@mcp.tool()
async def set_priority(ctx: Context) -> str:
    """Set task priority level"""
    result = await ctx.elicit(
        "What priority level?",
        response_type=["low","medium","high"]
    )
    
    if result.action == "accept":
        return f"Priority set to: {result.data}"