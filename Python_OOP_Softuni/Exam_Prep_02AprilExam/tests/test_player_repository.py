import unittest

from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class TestPlayerRepository(unittest.TestCase):
    def test_init_attr(self):
        pr = PlayerRepository()
        self.assertEqual(pr.count, 0)
        self.assertEqual(pr.players, [])

    def test_add_existing_player_raises(self):
        pr = PlayerRepository()
        p1 = Beginner('player1')
        p2 = Beginner('player1')
        pr.add(p1)

        with self.assertRaises(ValueError) as content:
            pr.add(p2)

        self.assertEqual(str(content.exception), f"Player {p2.username} already exists!")

    def test_add_with_valid_data(self):
        pr = PlayerRepository()
        p = Beginner('player1')
        pr.add(p)

        result = [p]

        self.assertEqual(pr.players, result)
        self.assertEqual(pr.count, 1)

    def test_remove_with_empty_string_raises(self):
        pr = PlayerRepository()

        with self.assertRaises(ValueError) as content:
            pr.remove("")

        self.assertEqual(str(content.exception), "Player cannot be an empty string!")

    def test_remove_with_valid_data(self):
        pr = PlayerRepository()
        pr.add(Beginner('player1'))

        result = []
        pr.remove("player1")

        self.assertEqual(pr.players, result)
        self.assertEqual(pr.count, 0)

    def test_find(self):
        pr = PlayerRepository()
        p = Beginner('player')
        pr.add(p)

        result = p

        self.assertEqual(pr.find('player'), result)
