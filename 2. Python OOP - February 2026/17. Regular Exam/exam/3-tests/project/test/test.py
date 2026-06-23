import unittest

from project.star_system import StarSystem

class TestStarSystem(unittest.TestCase):

    def setUp(self):
        self.valid_system = StarSystem(
            name="Solaris",
            star_type="Yellow dwarf",
            system_type="Single",
            num_planets=8,
            habitable_zone_range=(0.95, 1.67)
        )

    def test_init_valid(self):
        self.assertEqual("Solaris", self.valid_system.name)
        self.assertEqual("Yellow dwarf", self.valid_system.star_type)
        self.assertEqual("Single", self.valid_system.system_type)
        self.assertEqual(8, self.valid_system.num_planets)
        self.assertEqual((0.95, 1.67), self.valid_system.habitable_zone_range)

    def test_init_with_none_habitable_zone(self):
        system = StarSystem(
            name="Alpha",
            star_type="Red dwarf",
            system_type="Binary",
            num_planets=2,
            habitable_zone_range=None
        )
        self.assertIsNone(system.habitable_zone_range)

    def test_name_empty(self):
        with self.assertRaises(ValueError) as cm:
            StarSystem("", "Yellow dwarf", "Single", 1)
        self.assertEqual("Name must be a non-empty string.", str(cm.exception))

    def test_name_whitespace(self):
        with self.assertRaises(ValueError) as cm:
            StarSystem("   ", "Yellow dwarf", "Single", 1)
        self.assertEqual("Name must be a non-empty string.", str(cm.exception))

    def test_invalid_star_type(self):
        with self.assertRaises(ValueError) as cm:
            StarSystem("A", "Invalid", "Single", 1)
        self.assertIn("Star type must be one of", str(cm.exception))

    def test_invalid_system_type(self):
        with self.assertRaises(ValueError) as cm:
            StarSystem("A", "Yellow dwarf", "Invalid", 1)
        self.assertIn("System type must be one of", str(cm.exception))

    def test_negative_planets(self):
        with self.assertRaises(ValueError) as cm:
            StarSystem("A", "Yellow dwarf", "Single", -1)
        self.assertEqual("Number of planets must be a non-negative integer.", str(cm.exception))

    def test_invalid_habitable_range_length(self):
        with self.assertRaises(ValueError) as cm:
            StarSystem("A", "Yellow dwarf", "Single", 1, (1,))
        self.assertEqual(
            "Habitable zone range must be a tuple of two numbers (start, end) where start < end.",
            str(cm.exception)
        )

    def test_invalid_habitable_range_order(self):
        with self.assertRaises(ValueError) as cm:
            StarSystem("A", "Yellow dwarf", "Single", 1, (2, 1))
        self.assertEqual(
            "Habitable zone range must be a tuple of two numbers (start, end) where start < end.",
            str(cm.exception)
        )

    def test_is_habitable_true(self):
        self.assertTrue(self.valid_system.is_habitable)

    def test_is_habitable_false_no_range(self):
        system = StarSystem("A", "Yellow dwarf", "Single", 5, None)
        self.assertFalse(system.is_habitable)

    def test_is_habitable_false_no_planets(self):
        system = StarSystem("A", "Yellow dwarf", "Single", 0, (1, 2))
        self.assertFalse(system.is_habitable)

    def test_gt_valid(self):
        s1 = StarSystem("A", "Yellow dwarf", "Single", 5, (1, 5))
        s2 = StarSystem("B", "Yellow dwarf", "Single", 5, (1, 3))
        self.assertTrue(s1 > s2)

    def test_gt_equal(self):
        s1 = StarSystem("A", "Yellow dwarf", "Single", 5, (1, 3))
        s2 = StarSystem("B", "Yellow dwarf", "Single", 5, (1, 3))
        self.assertFalse(s1 > s2)

    def test_gt_not_habitable_self(self):
        s1 = StarSystem("A", "Yellow dwarf", "Single", 0, None)
        s2 = StarSystem("B", "Yellow dwarf", "Single", 5, (1, 3))
        with self.assertRaises(ValueError) as cm:
            s1 > s2
        self.assertEqual(
            "Comparison not possible: One or both systems lack a defined habitable zone or planets.",
            str(cm.exception)
        )

    def test_gt_not_habitable_other(self):
        s1 = StarSystem("A", "Yellow dwarf", "Single", 5, (1, 3))
        s2 = StarSystem("B", "Yellow dwarf", "Single", 0, None)
        with self.assertRaises(ValueError) as cm:
            s1 > s2
        self.assertEqual(
            "Comparison not possible: One or both systems lack a defined habitable zone or planets.",
            str(cm.exception)
        )

    def test_compare_star_systems_first_wins(self):
        s1 = StarSystem("A", "Yellow dwarf", "Single", 5, (1, 5))
        s2 = StarSystem("B", "Yellow dwarf", "Single", 5, (1, 3))
        result = StarSystem.compare_star_systems(s1, s2)
        self.assertEqual("A has a wider habitable zone than B.", result)

    def test_compare_star_systems_second_wins(self):
        s1 = StarSystem("A", "Yellow dwarf", "Single", 5, (1, 3))
        s2 = StarSystem("B", "Yellow dwarf", "Single", 5, (1, 5))
        result = StarSystem.compare_star_systems(s1, s2)
        self.assertEqual("B has a wider or equal habitable zone compared to A.", result)

    def test_compare_star_systems_equal(self):
        s1 = StarSystem("A", "Yellow dwarf", "Single", 5, (1, 3))
        s2 = StarSystem("B", "Yellow dwarf", "Single", 5, (1, 3))
        result = StarSystem.compare_star_systems(s1, s2)
        self.assertEqual("B has a wider or equal habitable zone compared to A.", result)

    def test_compare_star_systems_error(self):
        s1 = StarSystem("A", "Yellow dwarf", "Single", 0, None)
        s2 = StarSystem("B", "Yellow dwarf", "Single", 5, (1, 3))
        result = StarSystem.compare_star_systems(s1, s2)
        self.assertEqual(
            "Comparison not possible: One or both systems lack a defined habitable zone or planets.",
            result
        )

if __name__ == "__main__":
    unittest.main()