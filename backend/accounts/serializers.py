from rest_framework import serializers
from django.contrib.auth.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password', 'placeholder': 'Password'},
        label = 'Password'
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password', 'placeholder': 'Confirm Password'},
        label = 'Confirm Password'
    )

    class Meta:
            model = User
            fields = ["username", "password1", "password2"]
    
    def validate(self, attrs):
        if attrs["password1"] != attrs["password2"]:
            raise serializers.ValidationError({"password2": "Passwords don't match."})
        return attrs

    def create(self, data):
        data.pop("password2")

        return User.objects.create_user(
            username=data["username"],
            password=data["password1"]
        )