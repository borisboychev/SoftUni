from django.urls import path, include

from pets.views import pets_index, see_details, like, create_pet, delete_pet, edit_pet

urlpatterns = (
    path('', pets_index, name='pets index'),
    path('details/<int:pk>/', see_details, name='details'),
    path('like/<int:pk>/', like, name='like'),
    path('create/', create_pet, name='create pet'),
    path('delete/<int:pk>/', delete_pet, name='delete pet'),
    path('edit/<int:pk>/', edit_pet, name='edit pet'),
)
