from .models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        print('serializer Data',validated_data)
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ['username', 'email', 'password']