from rest_framework import serializers
from django.contrib.auth import get_user_model
from accounts import models


class SignUpProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = ["office_number"]


class SignUpOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Organization
        fields = ["name", "address"]


class SignUpSerializer(serializers.ModelSerializer):
    profiles = SignUpProfileSerializer(write_only=True)
    organization = SignUpOrganizationSerializer(
        source="profiles.organization", write_only=True
    )

    class Meta:
        model = get_user_model()
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "profiles",
            "organization",
        ]

    def create(self, validated_data):
        profile_data = validated_data.pop("profiles", {})
        organization = models.Organization.objects.create(
            **profile_data.pop("organization")
        )
        user = super().create(validated_data)
        models.Profile.objects.create(
            organization=organization, user=user, **profile_data
        )
        return user


class SendOTPSerializer(serializers.ModelSerializer):
    validation_error_message = "Email or Phone number must be provided to receive OTP"

    email = serializers.EmailField(required=False, source="user.email")
    phone_number = serializers.CharField(required=False, source="user.phone_number")

    class Meta:
        model = models.OTP
        fields = ["email", "phone_number"]

    def validate(self, attrs):
        user = attrs.get("user")
        if "email" in user or "phone_number" in user:
            attrs["user"] = user
            return attrs
        raise serializers.ValidationError(self.validation_error_message)

    def create(self, validated_data):
        lookup_kwargs = {}
        for key in ["email", "phone_number"]:
            if key in validated_data:
                lookup_kwargs[key] = validated_data.get(key)

        user = get_user_model().objects.get(**lookup_kwargs)
        otp = models.OTP.generate_new_otp(
            user=user, channel="email" if "email" in validated_data else "phone_number"
        )
        return otp


class VerifyOTPSerializer(SendOTPSerializer):
    validation_error_message = "Email or Phone number must be provided to verify OTP"
    code = serializers.CharField()

    class Meta:
        model = models.OTP
        fields = ["email", "phone_number", "code"]

    def validate(self, attrs):
        super().validate(attrs)
        lookup_kwargs = {}
        for key in ["email", "phone_number"]:
            if key in attrs:
                lookup_kwargs[key] = attrs.get(key)

        user = get_user_model().objects.get(**lookup_kwargs)
        otp = user.get_active_otp

        if attrs.get("code") != otp.code:
            raise serializers.ValidationError("Invalid Code, Please cross check.")

        attrs["user"] = user
        attrs["otp"] = otp
        return attrs

    def create(self, validated_data):
        otp = validated_data.pop("otp")
        otp.expired = False
        otp.save()

        user = validated_data.pop("user")
        user.is_active = True
        user.save()
        return user
