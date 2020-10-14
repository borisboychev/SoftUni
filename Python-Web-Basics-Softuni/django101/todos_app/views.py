from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.http import require_POST

from todos_app.forms import TodoForm, MyTodoForm
from todos_app.models import Todo


def index(request, form=None, form_action='create', pk=None):
    if not form:
        form = TodoForm()
    context = {
        'todos': Todo.objects.all().order_by('title'),
        'todo_form': form,
        'form_action': form_action,
        'pk': pk,
    }

    return render(request, 'todos_app/index.html', context)


@require_POST
def create_todo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        todo = Todo(title=form.cleaned_data['title'],
                    description=form.cleaned_data['description'],
                    is_done=False)
        todo.save()
        return redirect('todos')

    return index(request, form)


def edit_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.method == 'GET':
        form = TodoForm(initial=todo.__dict__)
        return index(request, form)
    else:
        form = TodoForm(request.POST)
        if form.is_valid():
            todo.title = form.cleaned_datap['title']
            todo.description = form.cleaned_data['description']
            todo.save()
        return index(request, form, 'edit', pk=pk)


def delete_todo(request):
    pass


@require_POST
def mark_done(request, pk):
    todo = Todo.objects.get(pk=pk)

    todo.is_done = not todo.is_done
    todo.save()

    return redirect('todos')
