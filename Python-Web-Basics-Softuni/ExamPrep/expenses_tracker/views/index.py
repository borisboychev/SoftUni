from django.shortcuts import render

from expenses_tracker.models import Profile, Expense
from expenses_tracker.views.profiles import create_profile


def money_left():
    profile_budget = Profile.objects.all()[0].budget
    for expense in Expense.objects.all():
        profile_budget -= expense.price

    return profile_budget

def index(request):
    if Profile.objects.exists():
        context = {
            'profile': Profile.objects.all()[0],
            'expenses': Expense.objects.all(),
            'money_left': money_left(),
        }
        return render(request, 'home-with-profile.html', context)
    else:
        return create_profile(request)
