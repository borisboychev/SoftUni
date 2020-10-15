from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=20)
    pages = models.IntegerField(default=1)
    description = models.TextField(max_length=100)
    author = models.CharField(max_length=20)
