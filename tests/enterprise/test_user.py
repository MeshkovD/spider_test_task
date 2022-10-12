import pytest


@pytest.mark.django_db
def test_register_user(client):
    payload = dict(
        username="TestUser1",
        email="testuser1@mail.com",
        password="complex_password",
    )
    response = client.post("/api/v1/auth/users/", payload)
    data = response.data

    assert data["username"] == payload["username"]
    assert data["email"] == payload["email"]
    assert "password" not in data


@pytest.mark.django_db
def test_login_user(user, client):
    response = client.post("/auth/token/login/", dict(username="TestUser1", password="complex_password"))

    assert response.status_code == 200
    assert response.data['auth_token'] == user.auth_token.key


@pytest.mark.django_db
def test_login_user_fail(client):
    response = client.post("/auth/token/login/", dict(username="Stranger", password="StrangersPassword"))
    data = response.data

    assert response.status_code == 400
    assert "auth_token" not in data
