import pytest

from apexselftaught.apps.portfolio.tests.factories import CertificationFactory


@pytest.mark.django_db
def test_user_can_create_certification(authorized_client, base_url):
    certificate = {
        "certificate": {
            "title": "GCP",
            "institution": "Google Cloud",
            "date_issued": "2020-01-01",
            "expiration_date": "2022-01-01"
        }
    }
    response = authorized_client.post(f'{base_url}certificates', certificate, format='json')
    assert response.status_code == 201


@pytest.mark.django_db
def test_user_can_edit_certificate(authorized_client, base_url, user):
    # import pdb;
    # pdb.set_trace()
    certificate = CertificationFactory(user=user)
    edit_data = {
        "certificate": {
            "title": "GCP",
        }
    }
    response = authorized_client.put(f'{base_url}certificates/{certificate.id}', edit_data, format='json')
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_can_get_all_certificates(authorized_client, base_url):
    batch = 3
    CertificationFactory.create_batch(batch)
    response = authorized_client.get(f'{base_url}certificates', format='json')
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_can_get_single_certificate(authorized_client, base_url):
    certificate = CertificationFactory()
    response = authorized_client.get(f'{base_url}certificates/{certificate.id}')
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_can_delete_a_certificate(authorized_client, base_url, user):
    certificates = [CertificationFactory(user=user) for _ in range(0, 3)]
    certificate = certificates[0]
    response = authorized_client.delete(f'{base_url}certificates/{certificate.id}', format='json')
    assert response.status_code == 200
    response2 = authorized_client.get(f'{base_url}certificates/{certificate.id}', format='json')
    assert response2.status_code == 404
