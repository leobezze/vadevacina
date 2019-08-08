from django.urls import path
from . import views


urlpatterns = [
    path('', views.posto_list, name='list'),
]