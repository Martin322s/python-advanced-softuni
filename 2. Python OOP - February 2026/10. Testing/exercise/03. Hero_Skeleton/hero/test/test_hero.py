from project.hero import Hero
import unittest

class HeroTests(unittest.TestCase):
    def setUp(self):
        self.hero = Hero("Martin", 10, 100.0, 10.0)

    def test_constructor_sets_correct_values(self):
        self.assertEqual("Martin", self.hero.username)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(100.0, self.hero.health)
        self.assertEqual(10.0, self.hero.damage)

    def test_battle_raises_if_fight_yourself(self):
        enemy = Hero("Martin", 1, 10, 1)
        with self.assertRaises(Exception) as ctx:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight yourself", str(ctx.exception))

    def test_battle_raises_if_hero_health_zero_or_less(self):
        self.hero.health = 0
        enemy = Hero("Enemy", 1, 10, 1)
        with self.assertRaises(ValueError) as ctx:
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ctx.exception))

    def test_battle_raises_if_enemy_health_zero_or_less(self):
        enemy = Hero("Enemy", 1, 0, 1)
        with self.assertRaises(ValueError) as ctx:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight Enemy. He needs to rest", str(ctx.exception))

    def test_battle_returns_draw_when_both_die(self):
        hero = Hero("Hero", 1, 10, 10)     
        enemy = Hero("Enemy", 1, 10, 10)
        result = hero.battle(enemy)

        self.assertEqual("Draw", result)
        self.assertEqual(0, hero.health)
        self.assertEqual(0, enemy.health)

    def test_battle_returns_you_win_and_updates_stats(self):
        hero = Hero("Hero", 2, 50, 10)
        enemy = Hero("Enemy", 1, 10, 1) 

        result = hero.battle(enemy)

        self.assertEqual("You win", result)
        self.assertEqual(3, hero.level)
        self.assertEqual(54, hero.health)
        self.assertEqual(15, hero.damage)
        self.assertEqual(-10, enemy.health)

    def test_battle_returns_you_lose_and_updates_enemy_stats(self):
        hero = Hero("Hero", 1, 10, 1)
        enemy = Hero("Enemy", 2, 50, 10)

        result = hero.battle(enemy)

        self.assertEqual("You lose", result)
        self.assertEqual(-10, hero.health)
        self.assertEqual(3, enemy.level)
        self.assertEqual(54, enemy.health)
        self.assertEqual(15, enemy.damage)

    def test_str_returns_correct_format(self):
        expected = "Hero Martin: 10 lvl\nHealth: 100.0\nDamage: 10.0\n"
        self.assertEqual(expected, str(self.hero))


if __name__ == "__main__":
    unittest.main(verbosity=2)