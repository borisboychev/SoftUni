from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from pythons_core.decorators import  groups_required

from .forms import PythonCreateForm
from .models import Python


# Create your views here.
@login_required(login_url='login')
def index(req):
    pythons = Python.objects.all()
    return render(req, 'index.html', {'pythons': pythons})


@groups_required(groups=['regular user'])
def create(req):
    if req.method == 'GET':
        context = {
            'form' :PythonCreateForm(),
            'current_page': 'create',
        }
        return render(req, 'create.html', context)
    else:
        data = req.POST
        form = PythonCreateForm(data)
        print(form)
        if form.is_valid():
            python = form.save()
            python.save()
            return redirect('index')
