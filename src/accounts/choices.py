from django.db.models import TextChoices


class OTPChannelChannel(TextChoices):
    SMS = "S"
    EMAIL = "E"
