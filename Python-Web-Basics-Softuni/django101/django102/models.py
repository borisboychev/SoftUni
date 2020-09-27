from django.db.models import Model, CharField

from django.db import models


class Game(Model):
    name = CharField(max_length=30)
    level_of_difficulty = models.IntegerField()
