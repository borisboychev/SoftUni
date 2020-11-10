from django.db import models


# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length=12, blank=False)
    state = models.BooleanField(default=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return f'{self.text} - {self.state}'

