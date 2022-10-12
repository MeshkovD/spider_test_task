import pytest


@pytest.mark.django_db
def test_get_commodities(auth_client, enterprise):
    enterprise_id = enterprise.id
    response = auth_client.get(f"/commodities/{enterprise_id}/")

    assert response.status_code == 200
    assert len(response.data) == enterprise.commodities.all().count()


@pytest.mark.django_db
def test_get_commodities_fail(client, enterprise):
    enterprise_id = enterprise.id
    response = client.get(f"/commodities/{enterprise_id}/")

    assert response.status_code == 401


@pytest.mark.django_db
def test_add_commodity(auth_client, enterprise, product):
    payload = dict(
        enterprise=enterprise.id,
        product=product.id,
        price=114.00,
    )

    response = auth_client.post("/commodities/1/", payload)

    assert response.status_code == 201


@pytest.mark.django_db
def test_add_product_fail(client, enterprise, product):
    payload = dict(
        enterprise=enterprise.id,
        product=product.id,
        price=114.00,
    )
    response = client.post("/commodities/1/", payload)

    assert response.status_code == 401


@pytest.mark.django_db
def test_get_commodity(auth_client, commodity):
    response = auth_client.get(f"/commodity/{commodity.id}/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_commodity_fail(client, commodity):
    response = client.get(f"/product/{commodity.id}/")

    assert response.status_code == 401
