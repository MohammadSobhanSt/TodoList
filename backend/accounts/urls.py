from django.urls import path
from . import views


app_name = "accounts"
urlpatterns = [
    path("signup/", views.RegistrationView.as_view(), name="registration"),
    path("login/", views.LoginView.as_view(), name="login"),
]