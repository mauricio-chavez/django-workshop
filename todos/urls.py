"""TODOs app URLs config"""

from django.urls import path

from . import views


urlpatterns = [
    path('', views.list, name='list'),
    path('create', views.create, name='create'),
    path('fulfill/<int:pk>', views.fulfill, name='fulfill'),
    path('delete/<int:pk>', views.delete, name='delete'),
]
