
from base_request import base_request


def test_get_inventory():
    response = base_request.get("store/inventory")

    assert isinstance(response, dict)
    assert len(response) > 0


def test_create_order():
    order_data = {
        "id": 5,
        "petId": 1,
        "quantity": 1,
        "shipDate": "2026-10-02T13:00:00.000Z",
        "status": "placed",
        "complete": True
    }

    response = base_request.post(
        "store/order",
        body=order_data
    )

    assert response["id"] == 5
    assert response["petId"] == 1
    assert response["quantity"] == 1
    assert response["status"] == "placed"


def test_get_order():
    response = base_request.get("store/order", 5)

    assert response["id"] == 5
    assert response["status"] == "placed"


def test_delete_order():
    base_request.delete("store/order", 5)

    response = base_request.get(
        "store/order",
        5,
        expected_error=True
    )

    assert "message" in response
