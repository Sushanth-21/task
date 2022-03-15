from dataclasses import fields
import email
from rest_framework import serializers
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'is_staff', 'is_superuser')
        extra_kwargs = {'password': {'write_only': True}, }

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'], password=validated_data['password'], email=validated_data['email'], is_staff=validated_data['is_staff'], is_superuser=validated_data['is_superuser'])
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')
