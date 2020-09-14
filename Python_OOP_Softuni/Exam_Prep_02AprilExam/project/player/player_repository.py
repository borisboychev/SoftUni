from project.player.beginner import Beginner
from project.player.player import Player


class PlayerRepository:
    def __init__(self):
        self.count = 0
        self.players = []

    def add(self, player: Player):
        names = [p.username for p in self.players]
        if player.username in names:
            raise ValueError(f"Player {player.username} already exists!")

        self.players.append(player)
        self.count += 1

    def remove(self, player: str):
        if player == "":
            raise ValueError("Player cannot be an empty string!")
        player_to_remove = [p for p in self.players if p.username == player][0]
        self.players.remove(player_to_remove)
        self.count -= 1

    def find(self, username):
        p = [p for p in self.players if p.username == username][0]
        return p

# p1 = Beginner('test1')
# p2 = Beginner('test2')
# p3 = Beginner('test3')
#
# pr = PlayerRepository()
# pr.add(p1)
# pr.add(p2)
# pr.add(p3)
#
# print(pr.find('test1').username)
#
# print([x.username for x in pr.players])
# pr.remove('test1')
# print([x.username for x in pr.players])


