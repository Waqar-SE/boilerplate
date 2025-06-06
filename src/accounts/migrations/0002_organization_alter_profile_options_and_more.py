# Generated by Django 5.1.6 on 2025-05-01 20:34

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Organization",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=200)),
                ("address", models.CharField(max_length=255)),
            ],
            options={
                "ordering": ["-id"],
                "abstract": False,
            },
        ),
        migrations.AlterModelOptions(
            name="profile",
            options={"ordering": ["-id"]},
        ),
        migrations.RemoveField(
            model_name="profile",
            name="mobile",
        ),
        migrations.AddField(
            model_name="profile",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=datetime.datetime(
                    2025, 5, 1, 20, 34, 6, 481290, tzinfo=datetime.timezone.utc
                ),
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="profile",
            name="office_number",
            field=models.CharField(default="", max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="profile",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="user",
            name="phone_number",
            field=models.CharField(default="", max_length=24, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="user",
            name="profile_picture",
            field=models.FileField(blank=True, null=True, upload_to="profiles"),
        ),
        migrations.AddField(
            model_name="profile",
            name="organization",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="profiles",
                to="accounts.organization",
            ),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name="OTP",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "channel",
                    models.CharField(
                        choices=[("S", "Sms"), ("E", "Email")],
                        default="E",
                        max_length=1,
                    ),
                ),
                ("code", models.CharField(max_length=6)),
                ("expired", models.BooleanField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="otps",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-id"],
                "abstract": False,
                "constraints": [
                    models.UniqueConstraint(
                        condition=models.Q(("expired", True)),
                        fields=("user", "expired"),
                        name="unique_active_otp",
                        violation_error_message="User already has a valid OTP.",
                    )
                ],
            },
        ),
    ]
