from django.contrib import admin

# Register your models here.
from expenses_app.models import Expenses, Profile

admin.site.register(Expenses)
admin.site.register(Profile)
