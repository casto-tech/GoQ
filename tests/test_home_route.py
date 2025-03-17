def test_home_route(test_client):
    """Tests the home route ('/')."""
    response = test_client.get('/')
    assert response.status_code == 200
