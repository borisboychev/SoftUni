from django.urls import path

from app.views import index, create_recipe, edit_recipe, delete_recipe, details

urlpatterns = (
    path('', index, name='index'),
    path('create/', create_recipe, name='create recipe'),
    path('edit/<int:pk>/', edit_recipe, name='edit recipe'),
    path('delete/<int:pk>/', delete_recipe, name='delete recipe'),
    path('details/<int:pk>/', details, name='details'),
)