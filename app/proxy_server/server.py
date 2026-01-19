from fastmcp import FastMCP

mcp = FastMCP("CalculatorServer")

@mcp.tool
def add(a: int, b: int) -> int:
    """Addition of two numbers"""
    return a + b

if __name__ == "__main__":
    mcp.run()
