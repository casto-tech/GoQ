import os
from application import application
from dotenv import load_dotenv

load_dotenv()


def test_config_loads_from_env(test_client):
    assert os.getenv("SERVICE_ACCOUNT_FILE") == os.environ["SERVICE_ACCOUNT_FILE"]
    assert os.getenv("USER_TO_IMPERSONATE") == os.environ["USER_TO_IMPERSONATE"]
    assert os.getenv("SCOPES") == os.environ["SCOPES"]
    assert os.getenv("TO") == os.environ["TO"]
    assert os.getenv("SENDER") == os.environ["SENDER"]
