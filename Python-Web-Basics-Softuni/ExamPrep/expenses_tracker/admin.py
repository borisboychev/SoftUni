from django.contrib import admin

# Register your models here.
from expenses_tracker.models import Expense, Profile

admin.site.register(Expense)
admin.site.register(Profile)
