from django.urls import path

from todos_app.views import index, create_todo

urlpatterns = [
    path('', index, name='todos index'),
    path('create/', create_todo, name='create todo'),
]