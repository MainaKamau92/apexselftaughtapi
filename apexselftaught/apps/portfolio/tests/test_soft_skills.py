import pytest

from apexselftaught.apps.portfolio.tests.factories import SoftSkillFactory


@pytest.mark.django_db
def test_user_can_create_soft_skill_proficiency(authorized_client, base_url):
    soft_skill = {
        "soft_skill": {
            "team_work": 7,
            "logic_reason": 9,
            "communication_proficiency": 5
        }
    }
    response = authorized_client.post(f'{base_url}soft-skills', soft_skill, format='json')
    assert response.status_code == 201


@pytest.mark.django_db
def test_user_can_edit_soft_skill_proficiency(authorized_client, base_url, user):
    soft_skill = SoftSkillFactory(user=user)
    edit_data = {
        "soft_skill": {
            "team_work": 8,
        }
    }
    response = authorized_client.put(f'{base_url}soft-skills/{soft_skill.id}', edit_data, format='json')
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_can_get_all_soft_skill_proficiencies(authorized_client, base_url):
    batch = 3
    SoftSkillFactory.create_batch(batch)
    response = authorized_client.get(f'{base_url}soft-skills', format='json')
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_can_get_single_soft_skill_proficiency(authorized_client, base_url):
    soft_skill = SoftSkillFactory()
    response = authorized_client.get(f'{base_url}soft-skills/{soft_skill.id}')
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_can_delete_soft_skill_proficiency(authorized_client, base_url, user):
    soft_skill_proficiencies = [SoftSkillFactory(user=user) for _ in range(0, 3)]
    soft_skill_proficiency = soft_skill_proficiencies[0]
    response = authorized_client.delete(f'{base_url}soft-skills/{soft_skill_proficiency.id}', format='json')
    assert response.status_code == 200
    response2 = authorized_client.get(f'{base_url}soft-skills/{soft_skill_proficiency.id}', format='json')
    assert response2.status_code == 404
