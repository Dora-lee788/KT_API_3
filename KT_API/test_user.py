
from base_request import base_request


def test_create_user():
    user_data = {
        "id": 1001,
        "username": "test_user_1001",
        "firstName": "Test",
        "lastName": "User",
        "email": "test@example.com",
        "password": "123456",
        "phone": "1234567890",
        "userStatus": 1
    }

    response = base_request.post(
        "user",
        body=user_data
    )

    assert response["code"] == 200
    assert response["type"] == "unknown"


def test_get_user():
    response = base_request.get(
        "user",
        "test_user_1001"
    )

    assert response["username"] == "test_user_1001"
    assert response["id"] == 1001


def test_update_user():
    updated_user_data = {
        "id": 1001,
        "username": "test_user_1001",
        "firstName": "Updated",
        "lastName": "User",
        "email": "updated@example.com",
        "password": "654321",
        "phone": "9876543210",
        "userStatus": 1
    }

    response = base_request.put(
        "user",
        "test_user_1001",
        updated_user_data
    )

    assert response["code"] == 200
    assert response["type"] == "unknown"

    user_info = base_request.get(
        "user",
        "test_user_1001"
    )

    assert user_info["firstName"] == "Updated"
    assert user_info["email"] == "updated@example.com"


def test_delete_user():
    response = base_request.delete(
        "user",
        "test_user_1001"
    )

    assert response["code"] == 200
    assert response["type"] == "unknown"

    user_info = base_request.get(
        "user",
        "test_user_1001",
        expected_error=True
    )

    assert "message" in user_info

