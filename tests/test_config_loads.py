import os
from application import application


def test_config_loads_from_env(test_client):
    assert os.getenv("SERVER") == application.config['MAIL_SERVER']
    assert os.getenv("PORT") == application.config['MAIL_PORT']
    assert os.getenv("USERNAME") == application.config['MAIL_USERNAME']
    assert os.getenv("PASSWORD") == application.config['MAIL_PASSWORD']
    assert os.getenv("TLS") == application.config['MAIL_USE_TLS']
    assert os.getenv("SSL") == application.config['MAIL_USE_SSL']
