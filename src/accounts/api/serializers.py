from rest_framework import serializers
from django.contrib.auth import get_user_model
from accounts import models

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'

class ProfileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = '__all__'