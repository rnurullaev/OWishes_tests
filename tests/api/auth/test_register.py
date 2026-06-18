def test_register(auth_client, user_data):

    response = auth_client.register(user_data)
    assert response.status_code == 201
