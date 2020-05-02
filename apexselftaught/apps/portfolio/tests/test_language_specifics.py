import pytest

from apexselftaught.apps.portfolio.tests.factories import ProgrammingLanguageSpecificsFactory, \
    ProgrammingLanguageFactory


@pytest.mark.django_db
def test_user_can_create_language_specific(authorized_client, base_url):
    language = ProgrammingLanguageFactory()
    language_specific = {
        "language": {
            "language": language.id,
            "proficiency": 6,
            "is_primary": True
        }
    }
    response = authorized_client.post(f'{base_url}language-specifics', language_specific, format='json')
    assert response.status_code == 201


@pytest.mark.django_db
def test_user_can_update_language_specific(authorized_client, base_url, user):
    language_specific = ProgrammingLanguageSpecificsFactory(user=user)
    edit_data = {
        "language": {
            "proficiency": 10,
        }
    }
    response = authorized_client.put(f'{base_url}language-specifics/{language_specific.id}', edit_data, format='json')
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_can_get_all_language_specifics(authorized_client, base_url):
    batch = 3
    ProgrammingLanguageSpecificsFactory.create_batch(batch)
    response = authorized_client.get(f'{base_url}language-specifics', format='json')
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_can_get_single_language_specific(authorized_client, base_url):
    language_specific = ProgrammingLanguageSpecificsFactory()
    response = authorized_client.get(f'{base_url}language-specifics/{language_specific.id}')
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_can_delete_language_specific(authorized_client, base_url, user):
    language_specifics = [ProgrammingLanguageSpecificsFactory(user=user) for _ in range(0, 3)]
    language_specific = language_specifics[0]
    response = authorized_client.delete(f'{base_url}language-specifics/{language_specific.id}', format='json')
    assert response.status_code == 200
    response2 = authorized_client.get(f'{base_url}language-specifics/{language_specific.id}', format='json')
    assert response2.status_code == 404
