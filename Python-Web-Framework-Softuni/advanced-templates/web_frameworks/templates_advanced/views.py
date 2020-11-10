from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from templates_advanced.forms import TodoForm
from templates_advanced.models import Todo


def index(request):
    contxt = {
        'todos': Todo.objects.all(),
        'form': TodoForm
    }
    return render(request, 'templates_advanced/index.html', contxt)