from tempfile import template
from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView
urlpatterns = [
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
]
