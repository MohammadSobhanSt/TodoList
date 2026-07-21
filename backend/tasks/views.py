from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from . import serializers
from .models import Task


class CreateTasksView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.TaskSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
 

class TaskListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.TaskListSerializer
    
    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)


class TaskUpdateView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)


class TaskDeleteView(RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)