import os
from application import application


def test_config_loads_from_env(test_client):
    assert os.getenv("SERVICE_ACCOUNT_FILE") == 'sa-key.json'
    assert os.getenv("USER_TO_IMPERSONATE") == 'info@greensonq.com'
    assert os.getenv("SCOPES") == 'https://www.googleapis.com/auth/gmail.send'
    assert os.getenv("TO") == 'joey@greensonq.com'
    assert os.getenv("SENDER") == 'info@greensonq.com'
