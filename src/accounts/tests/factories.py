import factory
from django.contrib.auth import get_user_model
from accounts import models


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Faker("email")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")

    phone_number = factory.Faker("bothify", text="+##############")
    is_active = True

    @factory.post_generation
    def password(self, created, extracted, **kwargs):
        self.set_password("change_me")
        self.save()

    class Meta:
        model = get_user_model()


class OrganizationFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("name")
    address = factory.Faker("address")

    class Meta:
        model = models.Organization


class ProfileFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory("accounts.tests.factories.UserFactory")
    organization = factory.SubFactory("accounts.tests.factories.OrganizationFactory")

    office_number = factory.Faker("bothify", text="+##############")

    class Meta:
        model = models.Profile
