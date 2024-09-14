from django.urls import path
from . import views

urlpatterns = [
    path("", views.landingPage, name = "Landing Page"),
    path("register/", views.register, name = "Register" ),
    path("", views.login, name = "Login")
]