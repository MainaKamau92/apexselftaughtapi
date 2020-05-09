import pytest
import factory
from django.db.models import signals
from apexselftaught.apps.authentication.tests.factories import UserFactory


@factory.django.mute_signals(signals.post_save)
@pytest.mark.django_db
def test_user_can_register(client):
    user_data = {
        "user": {
            "email": "user@apexselftaught.com",
            "username": "user",
            "password": "User1234",
            "mobile_number": "2540710123456",
        }
    }
    response = client.post('/api/v1/users', user_data, format='json')
    assert response.data["email"] == user_data["user"]["email"]
    assert response.status_code == 201


@pytest.mark.django_db
def test_user_cannot_register_with_invalid_credentials(client):
    user_data = {
        "user": {
            "email": "userapexselftaught.com",
            "username": "user",
            "password": "User1234",
        }
    }
    response = client.post('/api/v1/users', user_data, format='json')
    assert response.status_code == 400


@pytest.mark.django_db
def test_user_can_login(client):
    UserFactory(
        email="user@apexselftaught.com",
        password="User1234",
        is_verified=True
    )
    user_data = {
        "user": {
            "email": "user@apexselftaught.com",
            "password": "User1234"
        }
    }
    response = client.post('/api/v1/login/', user_data, format='json')
    assert response.data["email"] == user_data["user"]["email"]
    assert response.data["token"]
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_cannot_login_with_invalid_credentials(client):
    UserFactory()
    user_data = {
        "user": {
            "email": "jake@jenga-hr.com",
            "password": "Jake1234"
        }
    }
    response = client.post('/api/v1/login/', user_data, format='json')
    assert response.status_code == 400


@pytest.mark.django_db
def test_user_can_reset_password(client, user):
    password_payload = {
        "user": {
            "password": "Lewiikamaa8"
        }
    }
    response = client.patch(f'/api/v1/password-reset/{user.token}', password_payload, format='json')
    assert response.status_code == 200
