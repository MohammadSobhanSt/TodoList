from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers


class RegistrationView(CreateAPIView):
    serializer_class = serializers.RegistrationSerializer


class LoginView(APIView):
    serializer_class = serializers.LoginSerializer

    def post(self, request):
        if not request.user.is_authenticated:
            serializer = self.serializer_class(data=request.data)

            if serializer.is_valid():
                username = serializer.validated_data.get("username")
                password = serializer.validated_data.get("password")

                user = authenticate(username=username, password=password)

                if user:
                    login(request, user)
                    return Response(
                        {"message": "Login successful"}, status=status.HTTP_200_OK
                    )
                else:
                    return Response(
                        {"error": "Invalid credentials"},
                        status=status.HTTP_401_UNAUTHORIZED,
                    )

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(
            {"error": "You are already logged in."}, status=status.HTTP_400_BAD_REQUEST
        )


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response(
            {"success": "You logged out successfully."},
            status=status.HTTP_204_NO_CONTENT,
        )
