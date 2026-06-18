def test_login(auth_client, user_data):

    auth_client.register(user_data)
    response = auth_client.login(user_data["email"], user_data["password"])
    assert response.status_code == 200
