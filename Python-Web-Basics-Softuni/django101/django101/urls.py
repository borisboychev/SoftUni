from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('/102', include('django102.urls')) adds prefix 102
    path('', include('django102.urls')),
    path('admin/', admin.site.urls),
    path('todos/', include('todos_app.urls')),
    path('books/', include('books.urls'))

]
