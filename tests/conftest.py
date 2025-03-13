import pytest  # type: ignore
from application import application
from dotenv import load_dotenv


@pytest.fixture(scope="session")
def test_app():
    """Fixture to create a Flask application instance for testing."""
    load_dotenv()
    application.config['TESTING'] = True
    application.config['MAIL_DEBUG'] = True
    application.config['MAIL_SUPPRESS_SEND'] = True
    yield application


@pytest.fixture
def test_client(test_app):
    """Fixture to create a Flask test client."""
    with test_app.test_client() as client:
        yield client
