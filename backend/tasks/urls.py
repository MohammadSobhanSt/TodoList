from django.urls import path
from . import views


app_name = "tasks"
urlpatterns = [
    path("new-task/", views.CreateTasksView.as_view(), name="new-task"),
    path("list/", views.TaskListView.as_view(), name="task-list"),
    path("edit/<int:pk>/", views.TaskUpdateView.as_view(), name="task-update"),
    path("delete/<int:pk>/", views.TaskDeleteView.as_view(), name="task-delete"),
]