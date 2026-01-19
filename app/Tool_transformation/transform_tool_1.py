from fastmcp import FastMCP
from fastmcp.tools import Tool
import random

mcp = FastMCP("Dice server")

@mcp.tool()
def roll_dice(n_dice: int) -> list[int]:
    """Roll n_dice 6-sided dice and return the results."""
    return [random.randint(1,6) for _ in range(n_dice)]

roll_dice_tool = Tool.from_tool(
    roll_dice,
    name="Roll dice",
    description=f"""
    Simulates rolling `n_dice` standard six-sided dice (d6).

    For each die, an independent random integer between 1 and 6 (inclusive)
    is generated. The function returns a list containing the individual
    outcomes of each die roll. The length of the returned list is exactly
    equal to `n_dice`.

    Parameters:
        n_dice (int): The number of six-sided dice to roll. Must be a
            non-negative integer.

    Returns:
        list[int]: A list of integers in the range 1–6 (inclusive),
        representing the result of each die roll.
    """
)

mcp.add_tool(roll_dice_tool)

if __name__ == "__main__":
    mcp.run()