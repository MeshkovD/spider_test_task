import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from enterprise.models import Product, ProductCategory, EnterpriseNetwork, Enterprise, Commodity


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def user():
    user = User(
        username="TestUser1",
        email="testuser1@mail.com",
    )
    user.set_password("complex_password")
    user.save()
    return user


@pytest.fixture
def superuser():
    user = User(
        username="TestUser1",
        email="testuser1@mail.com",
        is_staff=True,
        is_superuser=True,
    )
    user.set_password("complex_password")
    user.save()
    return user


@pytest.fixture
def auth_client(superuser, client):
    client.post("/auth/token/login/", dict(username=superuser.username, password="complex_password"))
    client.credentials(HTTP_AUTHORIZATION=f'Token {superuser.auth_token}')
    return client


@pytest.fixture
def enterprise_network():
    return EnterpriseNetwork.objects.create(
        title="EnterpriseNetwork1"
    )


@pytest.fixture
def product_category():
    return ProductCategory.objects.create(
        title="Category1"
    )


@pytest.fixture
def product(product_category):
    return Product.objects.create(
        title="Product1",
        category=product_category,
    )


@pytest.fixture
def enterprise(enterprise_network):
    enterprise = Enterprise.objects.create(
        title="Enterprise1",
        description="Description1",
        enterprise_network=enterprise_network,
    )
    enterprise.district.create(title='District1')
    return enterprise


@pytest.fixture
def commodity(enterprise, product):
    return Commodity.objects.create(
        enterprise=enterprise,
        product=product,
        price=113.00,
    )
