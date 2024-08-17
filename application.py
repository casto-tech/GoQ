import os
import base64
from flask import Flask, render_template, request, flash, redirect, url_for  # type: ignore
from flask_mail import Mail, Message  # type: ignore
from dotenv import load_dotenv  # type: ignore
from google.oauth2 import service_account
from googleapiclient.discovery import build
from email.mime.text import MIMEText
from email_handler import create_message, send_message

load_dotenv()
application = Flask(__name__)
mail = Mail(application)

application.secret_key = os.getenv("SECRET_KEY")
application.config['MAIL_SERVER'] = os.getenv("SERVER")
application.config['MAIL_PORT'] = os.getenv("PORT")
application.config['MAIL_USE_TLS'] = os.getenv("TLS")
application.config['MAIL_USE_SSL'] = os.getenv("SSL")
application.config['MAIL_USERNAME'] = os.getenv("USERNAME")
application.config['MAIL_PASSWORD'] = os.getenv("PASSWORD")
application.config['MAIL_DEBUG'] = os.getenv("DEBUG")

SERVICE_ACCOUNT_FILE = os.getenv("SERVICE_ACCOUNT_FILE")
USER_TO_IMPERSONATE = os.getenv("USER_TO_IMPERSONATE")
SCOPES = ['https://www.googleapis.com/auth/gmail.send']


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
        credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)

        delegated_credentials = credentials.with_subject(USER_TO_IMPERSONATE)

        service = build('gmail', 'v1', credentials=delegated_credentials)

        sender = 'info@greensonq.com'
        to = 'joey@greensonq.com'
        subject = f'New Inquiry from: {name}'
        message_text = f'NAME: {name}<br> EMAIL: {email}/n PHONE: {phone}/n/n MESSAGE: {message}'

        msg= create_message(sender, to, subject, message_text)
        send_message(service, 'me', msg)
        # name = request.form.get('name')
        # email = request.form.get('email')
        # phone = request.form.get('phone')
        # message = request.form.get('message')
        # sender = os.getenv("USERNAME")
        # to = os.getenv("USERNAME")
        # subject = f'New Inquiry from {name}'
        # message_text = message

        # email_message = create_message(sender, to, subject, message_text)
        # send_message(service, 'me', email_message)

        # msg = Message(
        #     subject=f"New Contact Form Submission: {name}",
        #     sender=os.getenv("SENDER"),
        #     recipients=[os.getenv("USERNAME")])
        # msg.body = f"""
        #     {name}
        #     {email}
        #     {phone}
        #     {message}
        #     """
    #     try:
    #         mail.send(msg)
    #         flash('We will get back to you soon.', 'success')
    #     except Exception as e:
    #         print(f"Error sending email: {e}")
    #         flash('An error occurred. Please try again later.', 'error')
    #         return render_template('500.html')
    #     return redirect(url_for('home'))
    # return render_template('base.html')


@application.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@application.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    application.run()
