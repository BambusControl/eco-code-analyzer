from typing import TypedDict


class AnalysisResult(TypedDict):
    energy_efficiency: float
    resource_usage: float
    io_efficiency: float
    algorithm_efficiency: float
    custom_rules: float
