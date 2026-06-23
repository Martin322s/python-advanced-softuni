from project.vehicle import Vehicle
import unittest

class VehicleTests(unittest.TestCase):

    def setUp(self):
        self.vehicle = Vehicle(100, 200)

    def test_constructor_sets_correct_values(self):
        self.assertEqual(100, self.vehicle.fuel)
        self.assertEqual(100, self.vehicle.capacity)
        self.assertEqual(200, self.vehicle.horse_power)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive_reduces_fuel_correctly(self):
        self.vehicle.drive(10)
        self.assertEqual(87.5, self.vehicle.fuel)

    def test_drive_raises_if_not_enough_fuel(self):
        with self.assertRaises(Exception) as ctx:
            self.vehicle.drive(1000)
        self.assertEqual("Not enough fuel", str(ctx.exception))

    def test_refuel_increases_fuel(self):
        self.vehicle.fuel = 50
        self.vehicle.refuel(10)
        self.assertEqual(60, self.vehicle.fuel)

    def test_refuel_raises_if_over_capacity(self):
        with self.assertRaises(Exception) as ctx:
            self.vehicle.refuel(1)
        self.assertEqual("Too much fuel", str(ctx.exception))

    def test_str_returns_correct_format(self):
        expected = "The vehicle has 200 horse power with 100 fuel left and 1.25 fuel consumption"
        self.assertEqual(expected, str(self.vehicle))


if __name__ == "__main__":
    unittest.main(verbosity=2)