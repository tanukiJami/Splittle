from django.urls import path
from . import views

urlpatterns = [
    path('bill/<int:bill_id>/assign_users/', views.assign_users_to_items, name='assign_users_to_items'),
]