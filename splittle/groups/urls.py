from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewGroups, name='viewGroups'),
    path('', views.createGroup, name='createGroup'),
]
