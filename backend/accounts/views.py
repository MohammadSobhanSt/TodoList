from rest_framework.views import status
from rest_framework.generics import CreateAPIView
from . import serializers


class RegistrationView(CreateAPIView):
    serializer_class = serializers.RegistrationSerializer