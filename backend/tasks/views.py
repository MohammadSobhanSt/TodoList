from rest_framework.generics import CreateAPIView
from . import serializers


class CreateTasksView(CreateAPIView):
    serializer_class = serializers.CreateTaskSerializer