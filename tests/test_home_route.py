from application import application


def test_home_route(test_client):
    response = application.test_client().get('/')
    assert response.status_code == 200
    assert response.status_code != 404
    assert response.status_code != 500
