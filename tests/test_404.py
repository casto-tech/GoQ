def test_404_route(test_client):
    """Tests the 404 error route."""
    response = test_client.get('/nonexistent-route')
    assert response.status_code == 404
