from django.db import models


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=30, blank=False)
    description = models.TextField()
    is_done = models.BooleanField(blank=False)
