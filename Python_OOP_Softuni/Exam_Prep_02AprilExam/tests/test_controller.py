import unittest

from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.controller import Controller
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class TestControllers(unittest.TestCase):
    def test_init_attr(self):
        controller = Controller()
        self.assertEqual(controller.player_repository.__class__.__name__, "PlayerRepository")
        self.assertEqual(controller.card_repository.__class__.__name__ , "CardRepository")

    def test_add_player_beginner(self):
        controller = Controller()
        type = "Beginner"
        name = 'test'
        add = controller.add_player(type, name)
        self.assertEqual(add, f"Successfully added player of type {type} with username: {name}")

    def test_add_player_advanced(self):
        controller = Controller()
        type = "Advanced"
        name = 'test'
        add = controller.add_player(type, name)
        self.assertEqual(add, f"Successfully added player of type {type} with username: {name}")

    def test_add_card_trap(self):
        controller = Controller()
        type = 'Trap'
        name = 'test'
        add = controller.add_card(type, name)

        self.assertEqual(add, f"Successfully added card of type {type}Card with name: {name}")

    def test_add_card_magic(self):
        controller = Controller()
        type = 'Magic'
        name = 'test'
        add = controller.add_card(type, name)

        self.assertEqual(add, f"Successfully added card of type {type}Card with name: {name}")

    def test_add_player_card(self):
        controller = Controller()
        controller.player_repository.add(Beginner('player'))
        controller.card_repository.add(MagicCard('magic'))
        username = 'player'
        card_name = 'magic'

        result = controller.add_player_card(username, card_name)

        self.assertEqual(result, f"Successfully added card: {card_name} to user: {username}")

    def test_fight(self):
        controller = Controller()
        controller.player_repository.add(Advanced('player1'))
        controller.player_repository.add(Advanced('player2'))
        controller.card_repository.add(MagicCard('magic1'))
        controller.card_repository.add(MagicCard('magic2'))

        controller.add_player_card("player1", "magic1")
        controller.add_player_card("player2", "magic2")

        attack_name = "player1"
        enemy_name = "player2"
        result = controller.fight(attack_name, enemy_name)

        self.assertEqual(result, f"Attack user health {controller.player_repository.find(attack_name).health}"
                                 f" - Enemy user health {controller.player_repository.find(enemy_name).health}")


    def test_report(self):
        controller = Controller()
        controller.player_repository.add(Advanced('player1'))
        controller.card_repository.add(MagicCard('magic1'))
        controller.add_player_card("player1", "magic1")

        result = controller.report()

        self.assertEqual(result, f"Username: player1 - Health: 250 - Cards: 1\n### Card: magic1 - Damage: 5")