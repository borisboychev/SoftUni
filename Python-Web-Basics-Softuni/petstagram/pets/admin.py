from django.contrib import admin

# Register your models here.
from pets.models import Pet, Like

admin.site.register(Pet)
admin.site.register(Like)
