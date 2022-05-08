from rest_framework import serializers
from .models import CustomUser


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=50)

    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError('Email is exists.')
        return value

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError(
                'The size of password must be 8 or more.')
        return value

    def save(self, **kwargs):
        email = self.validated_data['email']
        username = self.validated_data['username']
        password = self.validated_data['password']
        CustomUser.objects.create(
            email=email, username=username, password=password)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate_email(self, value):
        if not CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError('The email is not exists.')
        return value


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()
