from typing import TypedDict

class Weights(TypedDict):
    energy_efficiency: float
    resource_usage: float
    io_efficiency: float
    algorithm_efficiency: float
    custom_rules: float

class Thresholds(TypedDict):
    eco_score: float
    category_score: float

class Coefficients(TypedDict):
    energy_consumption_per_cpu_cycle: float
    co2_emissions_per_kwh: float
    base_energy_consumption_per_year: float
    base_co2_emissions_per_year: float
    trees_equivalent_factor: float

class AppConfig(TypedDict):
    weights: Weights
    thresholds: Thresholds
    coefficients: Coefficients
    custom_rules: list # This is a list of dictionaries, but for simplicity, we'll keep it as a list for now.