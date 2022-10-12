import pytest
from django.forms import model_to_dict


@pytest.mark.django_db
def test_get_organization(auth_client, enterprise):
    response = auth_client.get(f"/organization/{enterprise.id}/")
    assert response.status_code == 200

    data = response.data

    assert dict(data)['id'] == model_to_dict(enterprise)['id']
    assert dict(data)['title'] == model_to_dict(enterprise)['title']
    assert dict(data)['description'] == model_to_dict(enterprise)['description']
    assert dict(data)['enterprise_network'] == model_to_dict(enterprise)['enterprise_network']\



@pytest.mark.django_db
def test_get_organization_fail(client, enterprise):
    response = client.get(f"/organization/{enterprise.id}/")
    assert response.status_code == 401


@pytest.mark.django_db
def test_get_organizations(auth_client, enterprise):
    district_id = enterprise.district.all()[0].id
    response = auth_client.get(f"/organizations/{district_id}/")

    assert response.status_code == 200
    assert len(response.data) == enterprise.district.all().count()


@pytest.mark.django_db
def test_get_organizations_fail(client, enterprise):
    district_id = enterprise.district.all()[0].id
    response = client.get(f"/organizations/{district_id}/")

    assert response.status_code == 401
