from django.db import models


# Create your models here.
class Pet(models.Model):
    DOG = 'dog'
    CAT = 'cat'
    PARROT = 'parrot'
    UNKNOWN = 'unknown'

    PET_TYPES = (
        (DOG, 'dog'),
        (CAT, 'cat'),
        (PARROT, 'parrot'),
        (UNKNOWN, 'unknown'),
    )
    type = models.CharField(max_length=7, choices=PET_TYPES, default=UNKNOWN)
    name = models.CharField(max_length=7, blank=False)
    age = models.IntegerField(blank=False)
    description = models.TextField(blank=False)
    image_url = models.URLField(blank=False)


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.DO_NOTHING)
