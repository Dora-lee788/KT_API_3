from base_request import base_request


print('GET INVENTORY')

inventory = base_request.get(
    'store/inventory'
)

print(inventory)


print('CREATE ORDER')

order_data = {
    'id': 5,
    'petId': 1,
    'quantity': 1,
    'shipDate': '2026-10-02T13:00:00.000Z',
    'status': 'placed',
    'complete': True
}

order = base_request.post(
    'store/order',
    body=order_data
)

print(order)


print('GET ORDER')

order_info = base_request.get(
    'store/order',
    5
)

print(order_info)


print('DELETE ORDER')

deleted_order = base_request.delete(
    'store/order',
    5
)

print(deleted_order)