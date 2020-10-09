from django.db.models import Model

from django.db import models

from django102.models.player import Player


class GameManager(models.Manager):
    def all_with_players_count(self):
        games = self.all() \
            .annotate(players_count=models.Count('players'))
        return games

class Game(Model):
    objects = GameManager()
    DIFFICULTY_LEVELS = (
        (1, 'Easy'),
        (2, 'Medium'),
        (3, 'Hard'),
        (4, 'Veteran'),
    )
    name = models.CharField(max_length=30, blank=False, default='')
    level_of_difficulty = models.IntegerField(
        blank=False,
        choices=DIFFICULTY_LEVELS,
        default=1,
    )
    players = models.ManyToManyField(Player)
