from pydantic import BaseModel
from fastmcp import FastMCP, Context

mcp = FastMCP()


class SentimentResult(BaseModel):
    sentiment: str
    confidence: float
    reasoning: str


@mcp.tool
async def analyze_sentiment(text: str, ctx: Context) -> SentimentResult:
    """Analyze text sentiment with structured output."""

    sample = await ctx.sample(   # ✅ YOU MISSED THIS
        messages=f"Analyze the sentiment of: {text}",
        result_type=SentimentResult,
    )

    return sample.result         # ✅ REAL VALUE, NOT COROUTINE


if __name__ == "__main__":
    mcp.run()
