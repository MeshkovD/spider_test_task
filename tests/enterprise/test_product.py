import pytest
from django.forms import model_to_dict


@pytest.mark.django_db
def test_get_products(auth_client, product):
    response = auth_client.get("/products/")

    assert response.status_code == 200
    assert response.data[0]["title"] == product.title


@pytest.mark.django_db
def test_get_products_fail(client, product):
    response = client.get("/products/")

    assert response.status_code == 401


@pytest.mark.django_db
def test_get_product(auth_client, product):
    response = auth_client.get(f"/product/{product.id}/")
    assert response.status_code == 200

    data = response.data
    assert dict(data) == model_to_dict(product)


@pytest.mark.django_db
def test_get_product_fail(client, product):
    response = client.get(f"/product/{product.id}/")

    assert response.status_code == 401


@pytest.mark.django_db
def test_add_product(auth_client, product_category):
    payload = dict(
        title="NewTitle",
    )

    response = auth_client.post("/products/", payload)

    assert response.status_code == 201
    assert payload["title"] == payload["title"]


@pytest.mark.django_db
def test_add_product_fail(client, product_category):
    payload = dict(
        title="NewTitle",
    )
    response = client.post("/products/", payload)

    assert response.status_code == 401
