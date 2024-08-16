import os
from flask_mail import Mail, Message
from application import application
from dotenv import load_dotenv

load_dotenv()


def test_email_send(test_client):
    mail = Mail(application)
    with mail.record_messages() as outbox:
        recipients = 'info@greensonq.com'
        mail.send_message(
            subject='Testing',
            body='This is a test email',
            recipients=recipients
        )
        assert len(outbox) == 1
        assert outbox[0].subject == 'Testing'
        assert outbox[0].recipients == recipients
# def test_email_send_empty_subject(test_client):
#     mail = Mail(application)
#     with mail.record_messages() as outbox:
#         mail.send_message(
#             subject='',
#             body='This is a test email',
#             recipients=[os.getenv("USERNAME")]
#         )
#         assert len(outbox) == 1
#         assert outbox[0].subject == ''

# def test_email_send_empty_body(test_client):
#     mail = Mail(application)
#     with mail.record_messages() as outbox:
#         mail.send_message(
#             subject='Testing',
#             body='',
#             recipients=[os.getenv("USERNAME")]
#         )
#         assert len(outbox) == 1
#         assert outbox[0].subject == 'Testing'
#         assert outbox[0].body == ''

# def test_email_send_html_body(test_client):
#     mail = Mail(application)
#     with mail.record_messages() as outbox:
#         html_body = '<html><body><h1>Test Email</h1></body></html>'
#         mail.send_message(
#             subject='Testing',
#             html=html_body,
#             recipients=[os.getenv("USERNAME")]
#         )
#         assert len(outbox) == 1
#         assert outbox[0].subject == 'Testing'
#         assert outbox[0].html == html_body

