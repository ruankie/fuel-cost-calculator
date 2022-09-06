import argparse


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


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t", "--tank", type=float, help="tank size in L", required=True
    )
    parser.add_argument(
        "-d",
        "--distance",
        type=float,
        help="distance traveled on full tank in km",
        required=True,
    )
    parser.add_argument(
        "-f",
        "--fuel",
        type=float,
        help="fuel cost in base currency per L",
        required=True,
    )
    parser.add_argument("-b", "--base", help="base currency symbol", default="ZAR")
    args = parser.parse_args()

    calc = FuelCostCalculator(
        tank_size=args.tank,
        distance_on_tank=args.distance,
        fuel_cost=args.fuel,
        base_currency=args.base,
    )

    cost = calc.calculate_cost_per_km()
    print(f"Cost per km: {calc.base_currency} {round(cost, 2)}")
