from typing import NamedTuple


# TODO add a line number of the problem


class Example(NamedTuple):
    inefficient: str
    efficient: str


class Suggestion(NamedTuple):
    name: str
    description: str
    category: str
    impact: str
    example: Example
    environmental_impact: str
    references: str
