from rest_framework import serializers

from .models import CustomAccountManager, NewUser


class CustomAccountManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomAccountManager
        fields = '__all__'


class NewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = '__all__'
