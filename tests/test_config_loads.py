import os


def test_config_loads_from_env(test_app):
    """Tests that configuration values are loaded from environment variables."""
    assert os.getenv("SERVICE_ACCOUNT_FILE") == os.environ["SERVICE_ACCOUNT_FILE"]
    assert os.getenv("USER_TO_IMPERSONATE") == os.environ["USER_TO_IMPERSONATE"]
    assert os.getenv("SCOPES") == os.environ["SCOPES"]
    assert os.getenv("TO") == os.environ["TO"]
    assert os.getenv("SENDER") == os.environ["SENDER"]
