from django.test import Client, TestCase


class APIClient(Client):
    def get(
        self,
        path,
        **kwargs,
    ):
        return super().get(path, **kwargs, content_type="application/json")

    def post(
        self,
        path,
        data,
        **kwargs,
    ):
        return super().post(path, data, **kwargs, content_type="application/json")

    def patch(
        self,
        path,
        data,
        **kwargs,
    ):
        return super().patch(path, data, **kwargs, content_type="application/json")

    def put(
        self,
        path,
        data,
        **kwargs,
    ):
        return super().put(path, data, **kwargs, content_type="application/json")

    def delete(
        self,
        path,
        **kwargs,
    ):
        return super().delete(path, **kwargs, content_type="application/json")


class BaseTestCase(TestCase):
    client_class = APIClient
