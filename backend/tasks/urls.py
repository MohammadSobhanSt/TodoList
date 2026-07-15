from django.urls import path
from . import views


app_name = "tasks"
urlpatterns = [
    path("new-task/", views.CreateTasksView.as_view(), name="new-task"),
]