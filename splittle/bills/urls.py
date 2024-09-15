from django.urls import path
from . import views

urlpatterns = [
    path('group/<int:group_id>/bills/', views.bills, name='bills'),
    path('group/<int:group_id>/create_bill/', views.create_bill, name='create_bill'),
    path('group/<int:group_id>/bills/<int:bill_id>/details/', views.bill_details, name='bill_details')
]