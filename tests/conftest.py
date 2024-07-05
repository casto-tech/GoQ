import pytest  # type: ignore
from application import application


@pytest.fixture
def test_client():
    application.config['TESTING'] = True
    with application.test_client() as client:
        yield client
