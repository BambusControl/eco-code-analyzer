from typing import NamedTuple, Literal


# TODO add a line number of the problem


class Example(NamedTuple):
    inefficient: str
    efficient: str


class Suggestion(NamedTuple):
    name: str
    description: str
    category: str
    impact: Literal["high", "medium", "low"]
    example: Example
    environmental_impact: str
    references: set[str]
