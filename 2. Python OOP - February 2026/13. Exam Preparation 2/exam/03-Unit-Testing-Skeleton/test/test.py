import unittest
from project.climbing_robot import ClimbingRobot

class TestClimbingRobot(unittest.TestCase):
    def setUp(self):
        self.robot = ClimbingRobot(category="Mountain", part_type="Arm", capacity=100, memory=200)

    def test_init_sets_all_attributes(self):
        self.assertEqual("Mountain", self.robot.category)
        self.assertEqual("Arm", self.robot.part_type)
        self.assertEqual(100, self.robot.capacity)
        self.assertEqual(200, self.robot.memory)
        self.assertEqual([], self.robot.installed_software)

    def test_category_setter_valid_values(self):
        for cat in ClimbingRobot.ALLOWED_CATEGORIES:
            r = ClimbingRobot(category=cat, part_type="X", capacity=1, memory=1)
            self.assertEqual(cat, r.category)

    def test_category_setter_invalid_raises_value_error_with_correct_message(self):
        with self.assertRaises(ValueError) as ex:
            ClimbingRobot(category="Sea", part_type="X", capacity=1, memory=1)

        self.assertEqual(
            f"Category should be one of {ClimbingRobot.ALLOWED_CATEGORIES}",
            str(ex.exception)
        )

    def test_get_used_capacity_when_no_software_returns_zero(self):
        self.assertEqual(0, self.robot.get_used_capacity())

    def test_get_used_memory_when_no_software_returns_zero(self):
        self.assertEqual(0, self.robot.get_used_memory())

    def test_get_available_capacity_when_no_software_returns_full_capacity(self):
        self.assertEqual(100, self.robot.get_available_capacity())

    def test_get_available_memory_when_no_software_returns_full_memory(self):
        self.assertEqual(200, self.robot.get_available_memory())

    def test_used_and_available_capacity_and_memory_with_installed_software(self):
        self.robot.installed_software = [
            {"name": "A", "capacity_consumption": 10, "memory_consumption": 20},
            {"name": "B", "capacity_consumption": 15, "memory_consumption": 30},
        ]
        self.assertEqual(25, self.robot.get_used_capacity())
        self.assertEqual(75, self.robot.get_available_capacity())
        self.assertEqual(50, self.robot.get_used_memory())
        self.assertEqual(150, self.robot.get_available_memory())

    def test_install_software_success_appends_and_returns_success_message(self):
        sw = {"name": "GripAI", "capacity_consumption": 30, "memory_consumption": 50}
        result = self.robot.install_software(sw)

        self.assertEqual("Software 'GripAI' successfully installed on Mountain part.", result)
        self.assertEqual(1, len(self.robot.installed_software))
        self.assertEqual(sw, self.robot.installed_software[0])

        self.assertEqual(30, self.robot.get_used_capacity())
        self.assertEqual(50, self.robot.get_used_memory())
        self.assertEqual(70, self.robot.get_available_capacity())
        self.assertEqual(150, self.robot.get_available_memory())

    def test_install_software_fails_when_not_enough_capacity_does_not_append(self):
        sw = {"name": "HeavyPack", "capacity_consumption": 101, "memory_consumption": 1}
        result = self.robot.install_software(sw)

        self.assertEqual("Software 'HeavyPack' cannot be installed on Mountain part.", result)
        self.assertEqual([], self.robot.installed_software)

    def test_install_software_fails_when_not_enough_memory_does_not_append(self):
        sw = {"name": "BigBrain", "capacity_consumption": 1, "memory_consumption": 201}
        result = self.robot.install_software(sw)

        self.assertEqual("Software 'BigBrain' cannot be installed on Mountain part.", result)
        self.assertEqual([], self.robot.installed_software)

    def test_install_software_fails_when_capacity_ok_but_memory_not_ok(self):
        sw = {"name": "MemFail", "capacity_consumption": 100, "memory_consumption": 999}
        result = self.robot.install_software(sw)

        self.assertEqual("Software 'MemFail' cannot be installed on Mountain part.", result)
        self.assertEqual(0, len(self.robot.installed_software))

    def test_install_software_fails_when_memory_ok_but_capacity_not_ok(self):
        sw = {"name": "CapFail", "capacity_consumption": 999, "memory_consumption": 200}
        result = self.robot.install_software(sw)

        self.assertEqual("Software 'CapFail' cannot be installed on Mountain part.", result)
        self.assertEqual(0, len(self.robot.installed_software))

    def test_install_software_exact_fit_succeeds(self):
        sw = {"name": "ExactFit", "capacity_consumption": 100, "memory_consumption": 200}
        result = self.robot.install_software(sw)

        self.assertEqual("Software 'ExactFit' successfully installed on Mountain part.", result)
        self.assertEqual(0, self.robot.get_available_capacity())
        self.assertEqual(0, self.robot.get_available_memory())

    def test_multiple_installations_accumulate_usage_correctly(self):
        sw1 = {"name": "A", "capacity_consumption": 10, "memory_consumption": 20}
        sw2 = {"name": "B", "capacity_consumption": 15, "memory_consumption": 30}
        sw3 = {"name": "C", "capacity_consumption": 60, "memory_consumption": 100}

        self.robot.install_software(sw1)
        self.robot.install_software(sw2)
        self.robot.install_software(sw3)

        self.assertEqual(3, len(self.robot.installed_software))
        self.assertEqual(85, self.robot.get_used_capacity())
        self.assertEqual(15, self.robot.get_available_capacity())
        self.assertEqual(150, self.robot.get_used_memory())
        self.assertEqual(50, self.robot.get_available_memory())


if __name__ == "__main__":
    unittest.main()