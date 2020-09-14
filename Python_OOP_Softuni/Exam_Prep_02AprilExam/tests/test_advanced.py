import unittest

from project.player.advanced import Advanced


class TestAdvanced(unittest.TestCase):
    def test_set_attr(self):
        p1 = Advanced('player1')
        self.assertEqual('player1', p1.username)
        self.assertEqual(250, p1.health)
        self.assertEqual("Advanced", p1.__class__.__name__)
        self.assertEqual("CardRepository", p1.card_repository.__class__.__name__)
        self.assertFalse(p1.is_dead)

    def test_empty_string_username_raises(self):
        with self.assertRaises(ValueError) as content:
            p1 = Advanced("")

        self.assertEqual(str(content.exception), "Player's username cannot be an empty string.")

    def test_health_less_than_0_raises(self):
        p1 = Advanced('test')

        with self.assertRaises(ValueError) as content:
            p1.health = -1

        self.assertEqual(str(content.exception), "Player's health bonus cannot be less than zero.")

    def test_is_dead(self):
        p1 = Advanced("test")

        self.assertFalse(p1.is_dead)
        p1.health = 0
        self.assertTrue(p1.is_dead)

    def test_take_damage(self):
        p1 = Advanced("test")
        p1.take_damage(50)
        self.assertEqual(p1.health, 200)