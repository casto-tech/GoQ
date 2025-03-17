import pytest
from unittest.mock import MagicMock, patch
from flask import Flask
from flask.testing import FlaskClient
from bs4 import BeautifulSoup
from contact_form import ContactForm


# Mock the Gmail API
def mock_build(service, version, credentials=None):
    """Mocks the googleapiclient.discovery.build function."""
    return MagicMock()


def mock_send_message(service, user_id, message):
    """Mocks the application.send_message function."""
    pass


@pytest.fixture
def client(test_app: Flask) -> FlaskClient:
    """Fixture to create a Flask test client with mocked Gmail API."""
    with test_app.test_client() as client:
        with patch('googleapiclient.discovery.build', side_effect=mock_build):
            with patch('application.send_message', side_effect=mock_send_message):
                form = ContactForm
                response = client.get('/')
                soup = BeautifulSoup(response.data, 'html.parser')
                csrf_token = soup.find('input', {'id': 'csrf_token'})['value']
                client.csrf_token = csrf_token
                print(client.csrf_token)
                yield client


def test_submit_form_success(client: FlaskClient):
    """Tests successful form submission to the '/submit' route."""
    response = client.post('/submit', data={
        'name': 'Test User',
        'email': 'test@example.com',
        'phone': '123-456-7890',
        'message': 'This is a test message',
        'csrf_token': client.csrf_token
    }, follow_redirects=True)
    assert response.status_code == 200
