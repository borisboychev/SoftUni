import unittest

from project.battle_field import BattleField
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner


class TestBattlefield(unittest.TestCase):
    def test_fight_when_attacker_is_dead(self):
        attacker = Beginner('attacker')
        enemy = Advanced("enemy")

        attacker.take_damage(50)
        bf = BattleField()

        with self.assertRaises(ValueError) as content:
            bf.fight(attacker, enemy)

        self.assertEqual("Player is dead!", str(content.exception))

    def test_fight_when_enemy_is_dead(self):
        attacker = Beginner('attacker')
        enemy = Advanced("enemy")

        enemy.take_damage(250)
        bf = BattleField()

        with self.assertRaises(ValueError) as content:
            bf.fight(attacker, enemy)

        self.assertEqual("Player is dead!", str(content.exception))

    def test_fight_when_players_are_not_dead_attacker_health(self):
        attacker = Beginner('attacker')
        enemy = Advanced("enemy")
        trap = TrapCard("trap")
        magic = MagicCard('magic')
        attacker.card_repository.add(trap)
        enemy.card_repository.add(magic)
        bf = BattleField()

        bf.fight(attacker, enemy)


        self.assertEqual(attacker.health, 90)

    def test_fight_when_players_are_not_dead_enemy_health(self):
        attacker = Beginner('attacker')
        enemy = Advanced("enemy")
        trap = TrapCard("trap")
        magic = MagicCard('magic')
        attacker.card_repository.add(trap)
        enemy.card_repository.add(magic)
        bf = BattleField()

        bf.fight(attacker, enemy)

        self.assertEqual(enemy.health, 180)

    def test_fight_when_attacker_gets_killed(self):
        attacker = Beginner('attacker')
        enemy = Advanced("enemy")
        trap = TrapCard("trap")
        magic = MagicCard('magic')
        attacker.card_repository.add(magic)
        enemy.card_repository.add(trap)

        attacker.health = 1
        bf = BattleField()
        bf.fight(attacker, enemy)

        attacker.health -= 1
        self.assertTrue(attacker.is_dead)

    def test_fight_when_enemy_gets_killed(self):
        enemy = Beginner('enemy')
        attacker = Advanced("attacker")
        trap = TrapCard("trap")
        magic = MagicCard('magic')
        attacker.card_repository.add(trap)
        enemy.card_repository.add(magic)

        enemy.health = 1
        bf = BattleField()
        bf.fight(attacker, enemy)

        enemy.health -= 1
        self.assertTrue(enemy.is_dead)