class FuelCostCalculator:
    def __init__(
        self,
        tank_size: float,
        distance_on_tank: float,
        fuel_cost: float,
        base_currency="ZAR",
    ) -> None:
        self.tank_size = tank_size  # L
        self.distance_on_tank = distance_on_tank  # km
        self.fuel_cost = fuel_cost  # ZAR/L
        self.base_currency = base_currency  # ZAR

    def calculate_cost_per_km(self) -> float:
        """Return cost (in base currency) per km driven."""
        efficiency = self.tank_size / self.distance_on_tank  # L/km
        return self.fuel_cost * efficiency  # ZAR/km
