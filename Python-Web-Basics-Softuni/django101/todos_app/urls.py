from django.urls import path

from todos_app.views import index, create_todo, edit_todo, delete_todo, mark_done

urlpatterns = [
    path('', index, name='todos'),
    path('create/', create_todo, name='create'),
    path('edit/<int:pk>', edit_todo, name='edit'),
    path('delete/<int:pk>', delete_todo, name='delete'),
    path('mark-done/<int:pk>', mark_done, name='mark done'),
]