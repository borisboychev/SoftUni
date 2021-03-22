from django.db import models

# Create your models here.
from django.db.models import TextField

from pets.models import Pet


class Comment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    comment = TextField()
    test = models.CharField(max_length=2)