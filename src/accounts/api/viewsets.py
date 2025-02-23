from rest_framework.viewsets import ModelViewSet
from accounts.api import serializers
from django.contrib.auth import get_user_model
from accounts import models


class UserModelViewSet(ModelViewSet):
    serializer_class = serializers.UserModelSerializer

    def get_queryset(self):
        return get_user_model().objects.all()


class ProfileModelViewSet(ModelViewSet):
    serializer_class = serializers.ProfileModelSerializer

    def get_queryset(self):
        return models.Profile.objects.all()
