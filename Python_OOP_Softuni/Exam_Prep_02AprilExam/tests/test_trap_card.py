import unittest

from project.card.trap_card import TrapCard


class TestTrapCard(unittest.TestCase):
    def test_set_attr(self):
        tc = TrapCard('card')
        self.assertEqual(tc.name, 'card')
        self.assertEqual(tc.damage_points, 120)
        self.assertEqual(tc.health_points, 5)
        self.assertEqual(tc.__class__.__name__, 'TrapCard')

    def test_empty_string_name_raises(self):

        with self.assertRaises(ValueError) as content:
            c = TrapCard("")

        self.assertEqual(str(content.exception), "Card's name cannot be an empty string.")

    def test_damage_points_less_than_0_raises(self):
        c = TrapCard("test")

        with self.assertRaises(ValueError) as content:
            c.damage_points = -1

        self.assertEqual(str(content.exception), "Card's damage points cannot be less than zero.")

    def test_health_points_less_than_0_raises(self):
        c = TrapCard('test')

        with self.assertRaises(ValueError) as content:
            c.health_points = -1

        self.assertEqual(str(content.exception), "Card's HP cannot be less than zero.")
