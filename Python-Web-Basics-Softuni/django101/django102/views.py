from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView

""""Model Imports"""
from django102.models.game import Game
from django102.models.person import Person
from django102.models.player import Player


def index(request):
    title = "Django101"
    users = User.objects.all()
    games = Game.objects.all_with_players_count()
    context = {'title': title,
               'users': users,
               'games': games
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


def create_game(request):
    game = Game(
        name='LoL',
        level_of_difficulty=2,
    )
    game.save()
    return redirect(request, 'index')
