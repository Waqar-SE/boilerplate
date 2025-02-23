from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class User(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def save(self, *args, **kwargs):
        created = not self.pk
        if created:
            self.username = self.email
        super().save(*args, **kwargs)


class Profile(models.Model):
    """A Profile model to support multiple profiles for user.

    The user key can be changed as needed to
    """

    user = models.ForeignKey(
        get_user_model(), related_name="profiles", on_delete=models.CASCADE
    )
    mobile = models.CharField(max_length=24)
