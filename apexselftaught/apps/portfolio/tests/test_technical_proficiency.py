import pytest

from apexselftaught.apps.portfolio.tests.factories import TechnicalSkillsFactory


@pytest.mark.django_db
def test_user_can_create_technical_proficiency(authorized_client, base_url):
    technical = {
        "technical": {
            "algorithms_proficiency": 7,
            "backend_testing_proficiency": 9,
            "frontend_testing_proficiency": 5,
            "design_patterns_proficiency": 3,
            "data_structure_proficiency": 5,
            "object_oriented_programming_proficiency": 7,
            "ui_ux_proficiency": 9,
            "git_proficiency": 2,
            "databases_proficiency": 5
        }
    }
    response = authorized_client.post(f'{base_url}technical-skills', technical, format='json')
    assert response.status_code == 201


@pytest.mark.django_db
def test_user_can_update_technical_proficiency(authorized_client, base_url, user):
    technical = TechnicalSkillsFactory(user=user)
    edit_data = {
        "technical": {
            "algorithms_proficiency": 7
        }
    }
    response = authorized_client.put(f'{base_url}technical-skills/{technical.id}', edit_data, format='json')
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_can_get_all_technical_proficiencies(authorized_client, base_url):
    batch = 3
    TechnicalSkillsFactory.create_batch(batch)
    response = authorized_client.get(f'{base_url}technical-skills', format='json')
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_can_get_single_technical_proficiency(authorized_client, base_url):
    technical = TechnicalSkillsFactory()
    response = authorized_client.get(f'{base_url}technical-skills/{technical.id}')
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_can_delete_technical_proficiency(authorized_client, base_url, user):
    technical_proficiencies = [TechnicalSkillsFactory(user=user) for _ in range(0, 3)]
    technical_proficiency = technical_proficiencies[0]
    response = authorized_client.delete(f'{base_url}technical-skills/{technical_proficiency.id}', format='json')
    assert response.status_code == 200
    response2 = authorized_client.get(f'{base_url}technical-skills/{technical_proficiency.id}', format='json')
    assert response2.status_code == 404
