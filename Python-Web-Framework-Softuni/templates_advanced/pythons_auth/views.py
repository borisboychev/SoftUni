from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect


# Create your views here.

def login_user(request):
    username = 'boris3'
    password = 'RUkg2k1o13zZ'
    user = authenticate(username=username, password=password)
    if user:
        login(request, user)
    return redirect('index')


def logout_user(request):
    logout(request)
    return redirect('index')
