import pytest
from rest_framework.test import APIClient
from apexselftaught.apps.authentication.tests.factories import UserFactory


@pytest.fixture
@pytest.mark.django_db
def client():
    client = APIClient()
    yield client


@pytest.fixture
@pytest.mark.django_db
def token():
    user = UserFactory(
        email="user@apexselftaught.com",
        password="User1234",
        is_verified=True
    )
    token = user.token
    yield f"Token {token}"


@pytest.fixture
@pytest.mark.django_db
def authorized_client(client, token):
    client.credentials(HTTP_AUTHORIZATION=token)
    yield client
