from django.urls import path

from books.views import index, create, edit

urlpatterns = [
    path('', index, name='books index'),
    path('create/', create, name='books create'),
    path('edit/<int:pk>', edit, name='books edit')
]