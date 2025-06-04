from common.api.tests.base import BaseTestCase
from django.urls import reverse_lazy
from accounts.tests import factories
from rest_framework import status
from accounts import models


class SignUpTestCase(BaseTestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.user = factories.UserFactory()

    def test_create_user(self):
        response = self.client.post(
            reverse_lazy("signup-list"),
            {
                "email": "email@test.com",
                "first_name": "Waqar",
                "last_name": "Ali",
                "phone_number": "+92333 8693455",
                "profile": {"office_number": "+92333 8693455"},
                "organization": {"name": "Test", "address": "Test Address"},
            },
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_send_otp(self):
        response = self.client.post(
            reverse_lazy("signup-send-otp"), data={"email": self.user.email}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_verify_otp(self):
        otp = models.OTP.generate_new_otp(self.user, "email")
        response = self.client.post(
            reverse_lazy("signup-verify-otp"),
            data={"email": self.user.email, "code": otp.code},
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
