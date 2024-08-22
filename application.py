import os
from flask import Flask, render_template, request
from dotenv import load_dotenv  # type: ignore
from google.oauth2 import service_account
from googleapiclient.discovery import build
from email_handler import create_message, send_message

load_dotenv()

application = Flask(__name__)

application.secret_key = os.getenv("SECRET_KEY")
SERVICE_ACCOUNT_FILE = os.getenv("SERVICE_ACCOUNT_FILE")
USER_TO_IMPERSONATE = os.getenv("USER_TO_IMPERSONATE")
SCOPES = [os.getenv("SCOPES")]


@application.route('/')
def home():
    return render_template('base.html')


@application.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    message = request.form.get('message')

    if request.method == 'POST':
        try:
            credentials = service_account.Credentials.from_service_account_file(
                SERVICE_ACCOUNT_FILE, scopes=SCOPES)

            delegated_credentials = credentials.with_subject(USER_TO_IMPERSONATE)

            service = build('gmail', 'v1', credentials=delegated_credentials)

            sender = os.getenv("SENDER")
            to = os.getenv("TO")
            subject = f"New Contact Form Submission: {name}"
            message_text = f" NAME: {name}\n EMAIL: {email}\n PHONE: {phone}\n\n MESSAGE: {message}"

            msg = create_message(sender, to, subject, message_text)
            send_message(service, 'me', msg)
            return render_template('success.html')

        except Exception as error:
            print(f'An error occurred: {error}')
            return render_template('500.html', success=False)


@application.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@application.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    application.run()
