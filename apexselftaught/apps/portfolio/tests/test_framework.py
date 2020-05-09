import pytest
from apexselftaught.apps.portfolio.tests.factories import FrameworkFactory, ProgrammingLanguageFactory


@pytest.mark.django_db
def test_user_can_create_framework(authorized_client, base_url):
    language = ProgrammingLanguageFactory()
    framework = {
        "framework": {
            "language": language.id,
            "name": "New Framework",
            "proficiency": 8,
            "is_primary": True
        }
    }
    response = authorized_client.post(f'{base_url}frameworks', framework, format='json')
    assert response.status_code == 201


@pytest.mark.django_db
def test_user_can_edit_existing_framework(authorized_client, base_url, user):
    framework = FrameworkFactory(user=user)
    edit_data = {
        "framework": {
            "language": framework.language.id,
            "name": "New Framework",
            "proficiency": 8,
            "is_primary": True
        }
    }
    response = authorized_client.put(f'{base_url}frameworks/{framework.id}', edit_data, format='json')
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_can_get_all_frameworks(authorized_client, base_url):
    batch = 3
    FrameworkFactory.create_batch(batch)
    response = authorized_client.get(f'{base_url}frameworks', format='json')
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_can_get_single_framework(authorized_client, base_url):
    framework = FrameworkFactory()
    response = authorized_client.get(f'{base_url}frameworks/{framework.id}')
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_can_delete_framework(authorized_client, base_url, user):
    frameworks = [FrameworkFactory(user=user) for _ in range(0, 3)]
    framework = frameworks[0]
    response = authorized_client.delete(f'{base_url}frameworks/{framework.id}', format='json')
    assert response.status_code == 200
    response2 = authorized_client.get(f'{base_url}frameworks/{framework.id}', format='json')
    assert response2.status_code == 404
