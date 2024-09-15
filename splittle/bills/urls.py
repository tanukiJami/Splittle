from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('group/<int:group_id>/bills/', views.bills, name='bills'),
]