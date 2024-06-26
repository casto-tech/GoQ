from app import app


def test_home_route(test_client):
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.status_code != 404