from django.urls import path

from expenses_app.views import index, edit, create_profile, expenses_profile

urlpatterns = [
    path('', index, name='home'),
    path('edit/<int:pk>', edit, name='edit'),
    path('create/', create_profile, name='create profile'),
    # path('delete/<int:pk', delete, name='delete'),
    path('profile/', expenses_profile, name='profile'),
    # path('profile/edit/', profile_edit, name='profile edit'),
    # path('profile/edit/', profile_delete, name='profile delete'),
]