from django.urls import path
from . import views


app_name = "accounts"
urlpatterns = [
    path("", views.RegistrationView.as_view(), name="registration")
]