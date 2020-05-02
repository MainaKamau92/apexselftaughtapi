import pytest
from apexselftaught.apps.core.utils import jwt_decode


@pytest.mark.django_db
def test_jwt_decode_util(authorized_client, user):
    payload = jwt_decode(user.token)
    assert payload.get('user') == user.username


@pytest.mark.django_db
def test_jwt_decode_rejects_empty_token_field(authorized_client, user):
    payload = jwt_decode()
    assert payload is None
