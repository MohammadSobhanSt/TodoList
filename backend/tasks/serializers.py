from rest_framework import serializers
from .models import Task


class CreateTaskSerializer(serializers.ModelSerializer):
    start_time = serializers.DateField(required=False)
    deadline = serializers.DateField(required=False)
    
    class Meta:
        model = Task
        fields = ["title", "description", "start_time", "deadline"]