import pytest
import random
from apexselftaught.apps.profiles.tests.factories import ProfileFactory


@pytest.mark.django_db
def test_user_can_update_profile(authorized_client, user):
    ProfileFactory(id=1, user=user)
    edit_data = {
        "profile": {
            "first_name": "Anton",
            "last_name": "LaVey"
        }
    }
    response = authorized_client.put('/api/v1/profiles/1', edit_data, format='json')
    assert response.data["first_name"] == edit_data["profile"]["first_name"]
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_can_get_all_profiles(authorized_client):
    profiles = 10
    ProfileFactory.create_batch(profiles)
    response = authorized_client.get('/api/v1/profiles', format='json')
    assert len(response.data.get('results')) == profiles
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_can_get_single_profile(authorized_client):
    profile_batch = ProfileFactory.create_batch(10)
    profile = random.choice([i for i in profile_batch])
    response = authorized_client.get(f'/api/v1/profiles/{profile.id}', format='json')
    assert response.data.get('id') == profile.id
    assert response.status_code == 200
