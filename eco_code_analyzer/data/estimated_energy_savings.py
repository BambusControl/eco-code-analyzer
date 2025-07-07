from typing import TypedDict


class EstimatedEnergySavings(TypedDict):
    energy_kwh_per_year: float
    co2_kg_per_year: float
    trees_equivalent: float
