from django.shortcuts import render, redirect

from expenses_tracker.forms.expense import ExpenseForm
from expenses_tracker.models import Expense


def create_expense(request):
    if request.method == "GET":
        context = {
            'form': ExpenseForm(),
        }
        return render(request, 'expense-create.html', context)
    else:
        form = ExpenseForm(request.POST)

        if form.is_valid():
            expense = Expense(title=form.cleaned_data["title"],
                              description=form.cleaned_data["description"],
                              image_url=form.cleaned_data["image_url"],
                              price=form.cleaned_data["price"])
            expense.save()
            return redirect('index')
        context = {
            'form': ExpenseForm(),
        }
        return render(request, 'expense-create.html', context)


def edit_expense(request, pk):
    expense = Expense.objects.get(pk=pk)

    if request.method == "GET":
        context = {
            'form': ExpenseForm(instance=expense),
        }
        return render(request, 'expense-edit.html', context)
    else:
        form = ExpenseForm(request.POST)

        if form.is_valid():
            expense.title = form.cleaned_data["title"]
            expense.description = form.cleaned_data["description"]
            expense.image_url = form.cleaned_data["image_url"]
            expense.price = form.cleaned_data["price"]
            expense.save()
            return redirect('index')
        context = {
            'form': ExpenseForm(instance=expense),
        }
        return render(request, 'expense-edit.html', context)


def delete_expense(request, pk):
    expense = Expense.objects.get(pk=pk)

    if request.method == "GET":
        form = ExpenseForm(instance=expense)
        form.fields['title'].widget.attrs['disabled'] = True
        form.fields['description'].widget.attrs['disabled'] = True
        form.fields['image_url'].widget.attrs['disabled'] = True
        form.fields['price'].widget.attrs['disabled'] = True
        context = {
            'form': form,
        }
        return render(request, 'expense-delete.html', context)
    else:
        expense.delete()
        return redirect('index')
