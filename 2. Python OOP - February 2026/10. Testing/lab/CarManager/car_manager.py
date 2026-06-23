class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0
    
    @property
    def make(self):
        return self.__make
    
    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption
    
    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity
    
    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount
    
    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed

car = Car("a", "b", 1, 4)
car.make = ""
print(car)

import unittest

class CarTests(unittest.TestCase):
    def setUp(self):
        self.car = Car("BMW", "M3", 10, 60)

    def test_constructor_sets_correct_values(self):
        self.assertEqual("BMW", self.car.make)
        self.assertEqual("M3", self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(60, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_empty_raises_exception(self):
        with self.assertRaises(Exception) as ctx:
            self.car.make = ""
        self.assertEqual("Make cannot be null or empty!", str(ctx.exception))

    def test_make_none_raises_exception(self):
        with self.assertRaises(Exception) as ctx:
            self.car.make = None
        self.assertEqual("Make cannot be null or empty!", str(ctx.exception))

    def test_model_empty_raises_exception(self):
        with self.assertRaises(Exception) as ctx:
            self.car.model = ""
        self.assertEqual("Model cannot be null or empty!", str(ctx.exception))

    def test_model_none_raises_exception(self):
        with self.assertRaises(Exception) as ctx:
            self.car.model = None
        self.assertEqual("Model cannot be null or empty!", str(ctx.exception))

    def test_fuel_consumption_zero_raises_exception(self):
        with self.assertRaises(Exception) as ctx:
            self.car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ctx.exception))

    def test_fuel_consumption_negative_raises_exception(self):
        with self.assertRaises(Exception) as ctx:
            self.car.fuel_consumption = -1
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ctx.exception))

    def test_fuel_capacity_zero_raises_exception(self):
        with self.assertRaises(Exception) as ctx:
            self.car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ctx.exception))

    def test_fuel_capacity_negative_raises_exception(self):
        with self.assertRaises(Exception) as ctx:
            self.car.fuel_capacity = -10
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ctx.exception))

    def test_fuel_amount_negative_raises_exception(self):
        with self.assertRaises(Exception) as ctx:
            self.car.fuel_amount = -0.1
        self.assertEqual("Fuel amount cannot be negative!", str(ctx.exception))

    def test_refuel_zero_raises_exception(self):
        with self.assertRaises(Exception) as ctx:
            self.car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ctx.exception))

    def test_refuel_negative_raises_exception(self):
        with self.assertRaises(Exception) as ctx:
            self.car.refuel(-5)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ctx.exception))

    def test_refuel_increases_fuel_amount(self):
        self.car.refuel(10)
        self.assertEqual(10, self.car.fuel_amount)

    def test_refuel_caps_at_fuel_capacity(self):
        self.car.refuel(1000)
        self.assertEqual(self.car.fuel_capacity, self.car.fuel_amount)

    def test_refuel_adds_until_capacity_over_multiple_refuels(self):
        self.car.refuel(30)
        self.car.refuel(40)
        self.assertEqual(60, self.car.fuel_amount)

    def test_drive_raises_if_not_enough_fuel(self):
        with self.assertRaises(Exception) as ctx:
            self.car.drive(100)
        self.assertEqual("You don't have enough fuel to drive!", str(ctx.exception))

    def test_drive_reduces_fuel_amount_correctly(self):
        self.car.refuel(20)
        self.car.drive(100)
        self.assertEqual(10, self.car.fuel_amount)

    def test_drive_reduces_fuel_amount_for_fractional_distance(self):
        self.car.refuel(10)
        self.car.drive(50)
        self.assertEqual(5, self.car.fuel_amount)

    def test_drive_when_exact_fuel_is_available_leaves_zero(self):
        self.car.refuel(10)
        self.car.drive(100)
        self.assertEqual(0, self.car.fuel_amount)


if __name__ == "__main__":
    unittest.main()