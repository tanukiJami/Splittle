from django.urls import path
from . import views

urlpatterns = [
    path('view/', views.viewGroups, name='viewGroups'),
    path('create/', views.createGroup, name='createGroup'),
    path('view/', views.leaveGroup, name='leaveGroup'),
]
