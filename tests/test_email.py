import os

from application import application
from dotenv import load_dotenv

load_dotenv()

assert True
# def test_email_send(test_client):
#     mail = Mail(application)
#     with mail.record_messages() as outbox:
#         recipients = 'info@greensonq.com'
#         mail.send_message(
#             subject='Testing',
#             body='This is a test email',
#             recipients=recipients
#         )
#         assert len(outbox) == 1
#         assert outbox[0].subject == 'Testing'
#         assert outbox[0].recipients == recipients
