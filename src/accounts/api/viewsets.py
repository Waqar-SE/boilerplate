from rest_framework.viewsets import ModelViewSet, GenericViewSet, mixins
from accounts.api import serializers
from django.contrib.auth import get_user_model
from accounts import models
from rest_framework.decorators import action
from rest_framework.response import Response


class SignUpViewSet(GenericViewSet, mixins.CreateModelMixin):
    serializer_class = serializers.SignUpSerializer

    @action(
        detail=False,
        serializer_class=serializers.SendOTPSerializer,
        methods=["POST"],
        url_path="otp/send/",
        url_name="send-otp",
    )
    def send_otp(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, 201)

    @action(
        detail=False,
        serializer_class=serializers.VerifyOTPSerializer,
        methods=["POST"],
        url_path="otp/verify/",
        url_name="verify-otp",
    )
    def verify_otp(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, 200)


class AuthenticationViewSet:
    def login(self):
        pass

    def logout(self):
        pass


class ResetPasswordViewSet(GenericViewSet):
    def forget_password(self):
        pass

    def reset_password(self):
        pass


class PersonalProfileViewSet(
    GenericViewSet,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
):
    def get(self):
        pass

    def update(self):
        pass

    def change_password(self):
        pass


class UserModelViewSet(ModelViewSet):
    serializer_class = serializers.UserModelSerializer

    def get_queryset(self):
        return get_user_model().objects.all()


class ProfileModelViewSet(ModelViewSet):
    serializer_class = serializers.ProfileModelSerializer

    def get_queryset(self):
        return models.Profile.objects.all()
