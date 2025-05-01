from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from common.models import BaseModel
from accounts import choices
from django.core.exceptions import ValidationError
import random
import string
from django.utils import timezone
from django.conf import settings


class User(AbstractUser):
    email = models.EmailField(unique=True)
    # TODO: Add validation here.
    phone_number = models.CharField(max_length=24, unique=True)
    profile_picture = models.FileField(upload_to="profiles", null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def save(self, *args, **kwargs):
        created = not self.pk
        if created:
            self.username = self.email
        super().save(*args, **kwargs)

    @property
    def get_active_otp(self):
        try:
            otp = self.otps.get(expired=False)
        except OTP.DoesNotExist:
            ValidationError("A valid OTP does not exist, please request a new one.")
        else:
            return otp


class OTP(BaseModel):
    user = models.ForeignKey(
        get_user_model(), related_name="otps", on_delete=models.CASCADE
    )
    channel = models.CharField(
        choices=choices.OTPChannelChannel.choices,
        max_length=1,
        default=choices.OTPChannelChannel.EMAIL,
    )
    code = models.CharField(max_length=6)
    expired = models.BooleanField()

    @property
    def is_expired(self):
        return timezone.now() - self.created_at <= settings.OTP_EXPIRY_MS

    class Meta(BaseModel.Meta):
        constraints = [
            models.UniqueConstraint(
                fields=["user", "expired"],
                name="unique_active_otp",
                condition=models.Q(expired=True),
                violation_error_message="User already has a valid OTP.",
            )
        ]

    @classmethod
    def generate_new_otp(cls, user, channel):
        cls.objects.filter(user=user).update(expired=True)
        return cls.objects.create(
            user=user,
            channel=channel,
            code="".join(random.choices(string.digits, k=6)),
            expired=False,
        )


class Organization(BaseModel):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=255)


class Profile(BaseModel):
    """A Profile model to support multiple profiles for a user.
    MUST BE CHANGED in case user should only one profile."""

    # The user key can be changed as needed to match project needs
    user = models.ForeignKey(
        get_user_model(), related_name="profiles", on_delete=models.CASCADE
    )
    organization = models.ForeignKey(
        "Organization", related_name="profiles", on_delete=models.CASCADE
    )
    office_number = models.CharField(max_length=25)
