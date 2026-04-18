from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: float) -> str:
        return None

    @abstractmethod
    def refuel(self, fuel: float) -> None:
        return None

class Car(Vehicle):
    AC_EXTRA = 0.9

    def drive(self, distance: float) -> str:
        needed = distance * (self.fuel_consumption + self.AC_EXTRA)

        if self.fuel_quantity >= needed:
            self.fuel_quantity -= needed
            return f"Car travelled {distance:g} km"

        return "Car needs refueling"

    def refuel(self, fuel: float) -> None:
        self.fuel_quantity += fuel


class Truck(Vehicle):
    AC_EXTRA = 1.6
    REFUEL_EFFICIENCY = 0.95

    def drive(self, distance: float) -> str:
        needed = distance * (self.fuel_consumption + self.AC_EXTRA)

        if self.fuel_quantity >= needed:
            self.fuel_quantity -= needed
            return f"Truck travelled {distance:g} km"

        return "Truck needs refueling"

    def refuel(self, fuel: float) -> None:
        self.fuel_quantity += fuel * self.REFUEL_EFFICIENCY
