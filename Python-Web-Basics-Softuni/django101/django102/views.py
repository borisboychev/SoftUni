from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

""""Model Imports"""
from django102.models.game import Game
from django102.models.person import Person
from django102.models.player import Player


def index(request):
    users = User.objects.all()
    title = "Django101"
    context = {'title': title,
               'users': users,
               }
    return render(request, 'index.html', context)


def something(request):
    return HttpResponse('<u>It works</u>')


class UsersListView(ListView):
    model = User
    template_name = 'index2.html'
    queryset = User.objects.all().order_by('-username')

    def get_context_object_name(self, object_list):
        return 'users'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = "From Class View"
        return context


class GamesListView(ListView):
    model = Game
    template_name = 'games.html'

