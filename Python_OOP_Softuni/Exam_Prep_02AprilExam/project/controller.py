from project.battle_field import BattleField
from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class Controller:
    def __init__(self):
        self.player_repository = PlayerRepository()
        self.card_repository = CardRepository()

    def add_player(self, type, username):
        if type == "Beginner":
            created_player = Beginner(username)
        else:
            created_player = Advanced(username)

        self.player_repository.add(created_player)

        return f"Successfully added player of type {type} with username: {username}"

    def add_card(self, type, name):
        if type == "Trap":
            created_card = TrapCard(name)
        else:
            created_card = MagicCard(name)
        self.card_repository.add(created_card)

        return f"Successfully added card of type {type}Card with name: {name}"

    def add_player_card(self, username, card_name):
        player = self.player_repository.find(username)
        card = self.card_repository.find(card_name)
        player.card_repository.add(card)
        return f"Successfully added card: {card_name} to user: {username}"

    def fight(self,attack_name, enemy_name):
        attacker = self.player_repository.find(attack_name)
        enemy = self.player_repository.find(enemy_name)

        bf = BattleField()
        bf.fight(attacker, enemy)
        return f"Attack user health {attacker.health} - Enemy user health {enemy.health}"

    def report(self):
        result = ''
        player = 0
        for p in self.player_repository.players:
            result += f"Username: {p.username} - Health: {p.health} - Cards: {p.card_repository.count}\n"
            player += 1
            for i in range(p.card_repository.count):
                if i == p.card_repository.count-1 and player == self.player_repository.count:
                    result += f"### Card: {p.card_repository.cards[i].name} - Damage: {p.card_repository.cards[i].damage_points}"
                else:
                    result += f"### Card: {p.card_repository.cards[i].name} - Damage: {p.card_repository.cards[i].damage_points}\n"

        return result



# p1 = Beginner('player1')
# p2 = Advanced("player2")
# tc = TrapCard("trapcard1")
# mc = MagicCard('magiccard1')
#
# pr = PlayerRepository()
#
# pr.add(p1)
# pr.add(p2)
#
# print(pr.find('player1').username)
#
# p1.card_repository.add(tc)
# p2.card_repository.add(mc)
#
#
# controller = Controller()
#
# print(controller.add_player('Advanced', 'test1'))
# print(controller.add_player('Beginner', 'test2'))
# print(controller.add_card('Magic', 'magic1'))
# print(controller.add_card('Trap', 'trap1'))
# print(controller.add_player_card('test1', 'magic1'))
# print(controller.add_player_card('test2', 'trap1'))
# print([f"{p.username},{p.health}" for p in controller.player_repository.players])
# print(controller.fight('test1', 'test2'))
#
# print(controller.report())
#
# controller.player_repository.remove('test1')
# print('---------------------------------------------------')
# print([p.username for p in controller.player_repository.players])
#
# print([c.name for c in controller.card_repository.cards])
# controller.card_repository.remove('magic1')
# print([c.name for c in controller.card_repository.cards])

