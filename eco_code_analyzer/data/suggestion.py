from typing import TypedDict

class Suggestion(TypedDict):
    name: str
    description: str
    category: str
    impact: str
    example: str
    environmental_impact: str
    references: str