from django.db.models import Model, CharField


class Game(Model):
    name = CharField(max_length=30)
