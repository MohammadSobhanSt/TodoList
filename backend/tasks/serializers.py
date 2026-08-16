from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    start_time = serializers.DateField(required=False)
    deadline = serializers.DateField(required=False, allow_null=True)

    class Meta:
        model = Task
        fields = ["pk", "title", "completed", "description", "start_time", "deadline"]


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["pk", "title", "completed", "description", "start_time", "deadline"]
