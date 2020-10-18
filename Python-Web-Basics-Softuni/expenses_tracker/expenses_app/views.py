from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.http import require_POST

from expenses_app.forms import ProfileForm, ExpensesForm
from expenses_app.models import Expenses, Profile


def money_left(profile, expenses):
    all_expenses = 0
    budget = 0
    for expense in expenses:
        all_expenses += expense.price

    for p in profile:
        budget = p.budget

    money_remaining = budget - all_expenses
    return money_remaining


def profile_budget():
    return [p.budget for p in Profile.objects.all()][0]


def index(request, profile_form=None, expenses_form=None, pk=None, profile=None):
    context = {
        'expenses': Expenses.objects.all(),
        'profile': profile,
        'profile_form': profile_form,
        'expenses_form': expenses_form,
        'pk': pk,
        'money_left': money_left(Profile.objects.all(), Expenses.objects.all()),
        'profile_budget': profile_budget()
    }

    if len(Profile.objects.all()) == 0:
        return render(request, 'home-no-profile.html', context)
    else:
        return render(request, 'home-with-profile.html', context)


def expenses_profile(request):
    context = {
        'expenses': Expenses.objects.all(),
        'profile': Profile.objects.all(),
        'profile_form': ProfileForm(),
        'expenses_form': ExpensesForm(),
    }
    return render(request, 'profile.html', context)


@require_POST
def create_profile(request):
    profile_form = ProfileForm(request.POST)

    if profile_form.is_valid():
        profile_new = Profile(first_name=profile_form.cleaned_data['first_name'],
                              last_name=profile_form.cleaned_data['last_name'],
                              budget=profile_form.cleaned_data['budget'])
        profile_new.save()

        index(request, profile_form=profile_form, profile=profile_new)

        return redirect('home')


def edit(request, pk=None):
    expense = Expenses.objects.get(pk=pk)
    if request.method == 'GET':
        form = Expenses(initial=expense.__dict__)
        return index(request, form)
    else:
        pass
