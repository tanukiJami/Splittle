from django.urls import path
from . import views

urlpatterns = [
    path("", views.landingPage, name = "Landing Page"),
    path("register/", views.register, name = "Register" ),
    path("login/", views.login, name = "Login"),
]