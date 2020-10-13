from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.http import require_POST

from todos_app.forms import TodoForm, MyTodoForm
from todos_app.models import Todo


def index(request, form=None):
    context = {
        "todos": Todo.objects.all(),
        "todo_form": form,
        # 'todo_model_form': MyTodoForm()
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
        return redirect('todos index')

    return index(request, form)
