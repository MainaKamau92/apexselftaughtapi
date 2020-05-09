import pytest
from apexselftaught.apps.portfolio.tests.factories import ProgrammingLanguageFactory


@pytest.mark.django_db
def test_user_can_get_all_programming_languages(authorized_client, base_url):
    batch = 3
    ProgrammingLanguageFactory.create_batch(batch)
    response = authorized_client.get(f'{base_url}languages', format='json')
    assert response.status_code == 200
    assert len(response.data.get('results')) == batch


@pytest.mark.django_db
def test_user_can_get_single_language(authorized_client, base_url):
    batch = 3
    languages = ProgrammingLanguageFactory.create_batch(batch)
    response = authorized_client.get(f'{base_url}languages/{languages[0].id}')
    assert response.status_code == 200
