from base_request import base_request


user_data = {
    'id': 1001,
    'username': 'test_user_1001',
    'firstName': 'Test',
    'lastName': 'User',
    'email': 'test@example.com',
    'password': '123456',
    'phone': '1234567890',
    'userStatus': 1
}


print('CREATE USER')

created_user = base_request.post(
    'user',
    body=user_data
)

print(created_user)


print('GET USER')

user_info = base_request.get(
    'user',
    'test_user_1001'
)

print(user_info)

assert user_info['username'] == user_data['username']


print('UPDATE USER')

updated_user_data = {
    'id': 1001,
    'username': 'test_user_1001',
    'firstName': 'Updated',
    'lastName': 'User',
    'email': 'updated@example.com',
    'password': '654321',
    'phone': '9876543210',
    'userStatus': 1
}

updated_user = base_request.put(
    'user',
    'test_user_1001',
    updated_user_data
)

print(updated_user)


print('DELETE USER')

deleted_user = base_request.delete(
    'user',
    'test_user_1001'
)

print(deleted_user)


print('CHECK DELETE')

user_info = base_request.get(
    'user',
    'test_user_1001',
    expected_error=True
)

print(user_info)