from tempfile import template
from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView
urlpatterns = [
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
]
