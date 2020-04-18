"""GDG TODOs URL Configuration"""

from django.contrib import admin
from django.urls import path, include

from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('todos/', include(('todos.urls', 'todos'), namespace='todos')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
]
