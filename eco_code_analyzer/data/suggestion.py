from typing import NamedTuple, Literal


# TODO add a line number of the problem


class Example(NamedTuple):
    inefficient: str
    efficient: str


class Suggestion(NamedTuple):
    name: str
    description: str
    category: Literal[
        "energy_efficiency", "memory_usage", "io_efficiency", "algorithm_efficiency"
    ]
    impact: Literal["high", "medium", "low"]
    example: Example
    references: set[str]
