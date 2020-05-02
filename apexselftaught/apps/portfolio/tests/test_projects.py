import pytest
import random
from apexselftaught.apps.portfolio.tests.factories import ProjectFactory


@pytest.mark.django_db
def test_user_can_create_project(authorized_client, base_url):
    project = {
        "project": {
            "name": "My Project",
            "link": "http://myproject.com",
            "description": "New project"
        }
    }
    response = authorized_client.post(f'{base_url}projects', project, format='json')
    assert response.status_code == 201


@pytest.mark.django_db
def test_user_can_edit_existing_project(authorized_client, user, base_url):
    project = ProjectFactory(user=user)
    edit_data = {
        "project": {
            "name": "My Project Update",
            "link": "http://myproject.com",
            "description": "New project"
        }
    }
    response = authorized_client.put(f'{base_url}projects/{project.id}', edit_data, format='json')
    assert response.data.get('name') == edit_data['project']['name']
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_can_get_all_projects(authorized_client, base_url):
    batch = 5
    ProjectFactory.create_batch(batch)
    response = authorized_client.get(f'{base_url}projects', format='json')
    assert response.status_code == 200
    assert len(response.data.get('results')) == batch


@pytest.mark.django_db
def test_user_can_get_a_single_project(authorized_client, base_url):
    project = ProjectFactory()
    response = authorized_client.get(f'{base_url}projects/{project.id}')
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_can_delete_project(authorized_client, base_url, user):
    projects = [ProjectFactory(user=user) for _ in range(0, 3)]
    random_project = random.choice(projects)
    response = authorized_client.delete(f'{base_url}projects/{random_project.id}')
    assert response.status_code == 200
    response2 = authorized_client.get(f'{base_url}projects/{random_project.id}')
    assert response2.status_code == 404
