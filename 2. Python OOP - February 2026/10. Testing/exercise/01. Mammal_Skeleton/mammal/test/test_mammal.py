import unittest
from project.mammal import Mammal

class MammalTests(unittest.TestCase):

    def setUp(self):
        self.mammal = Mammal("Leo", "Lion", "Roar")

    def test_constructor_sets_correct_values(self):
        self.assertEqual("Leo", self.mammal.name)
        self.assertEqual("Lion", self.mammal.type)
        self.assertEqual("Roar", self.mammal.sound)

    def test_kingdom_is_set_correctly(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_make_sound_returns_correct_string(self):
        result = self.mammal.make_sound()
        self.assertEqual("Leo makes Roar", result)

    def test_info_returns_correct_string(self):
        result = self.mammal.info()
        self.assertEqual("Leo is of type Lion", result)


if __name__ == "__main__":
    unittest.main(verbosity=2)