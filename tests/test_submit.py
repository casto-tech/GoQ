import pytest
import os
from unittest.mock import Mock, patch
from application import application
from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError


# Mock the Gmail API
def mock_build(service, version, credentials=None):
    return MagicMock()


def mock_send_message(service, user_id, message):
    pass


os.environ["SENDER"] = os.getenv("SENDER")
os.environ["TO"] = os.getenv("TO")


@pytest.fixture
def client():
    application.config['TESTING'] = True
    client = application.test_client()
    return client


def test_submit_form_success(client):
    with patch('googleapiclient.discovery.build', side_effect=mock_build):
        with patch('application.send_message', side_effect=mock_send_message):
            response = client.post('/submit', data={
                'name': 'Test User',
                'email': 'test@example.com',
                'phone': '123-456-7890',
                'message': 'This is a test message'
            })

            assert response.status_code == 200
