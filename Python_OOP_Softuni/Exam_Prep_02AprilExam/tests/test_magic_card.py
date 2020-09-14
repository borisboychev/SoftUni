import unittest

from project.card.magic_card import MagicCard


class TestMagicCard(unittest.TestCase):
    def test_set_attr(self):
        tc = MagicCard('card')
        self.assertEqual(tc.name, 'card')
        self.assertEqual(tc.damage_points, 5)
        self.assertEqual(tc.health_points, 80)
        self.assertEqual(tc.__class__.__name__, 'MagicCard')

    def test_empty_string_name_raises(self):
        with self.assertRaises(ValueError) as content:
            c = MagicCard("")

        self.assertEqual(str(content.exception), "Card's name cannot be an empty string.")

    def test_damage_points_less_than_0_raises(self):
        c = MagicCard("test")

        with self.assertRaises(ValueError) as content:
            c.damage_points = -1

        self.assertEqual(str(content.exception), "Card's damage points cannot be less than zero.")

    def test_health_points_less_than_0_raises(self):
        c = MagicCard('test')

        with self.assertRaises(ValueError) as content:
            c.health_points = -1

        self.assertEqual(str(content.exception), "Card's HP cannot be less than zero.")
