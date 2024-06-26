import os
from app import app


def test_config_loads_from_env(test_client):
    assert os.getenv("SERVER") == app.config['MAIL_SERVER']
    assert os.getenv("PORT") == app.config['MAIL_PORT'] 
    assert os.getenv("USERNAME") == app.config['MAIL_USERNAME']
    assert os.getenv("PASSWORD") == app.config['MAIL_PASSWORD']
    assert os.getenv("TLS") == app.config['MAIL_USE_TLS']
    assert os.getenv("SSL") == app.config['MAIL_USE_SSL']
