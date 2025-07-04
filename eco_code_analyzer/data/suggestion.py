from typing import TypedDict

# TODO add a line number of the problem
class Suggestion(TypedDict):
    name: str
    description: str
    category: str
    impact: str
    example_bad: str
    example_good: str
    environmental_impact: str
    references: str