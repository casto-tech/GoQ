import os
import logging
from flask import Flask, render_template, send_from_directory, current_app, flash, redirect, url_for
from markupsafe import escape
from dotenv import load_dotenv  # type: ignore
from google.oauth2 import service_account
from googleapiclient.discovery import build
from email_handler import create_message, send_message
from contact_form import ContactForm
from flask_font_awesome import FontAwesome
from flask_wtf.csrf import CSRFProtect
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

load_dotenv()

application = Flask(__name__)
font_awesome = FontAwesome(application)

application.secret_key = os.urandom(24)
csrf = CSRFProtect(application)
limiter = Limiter(
    get_remote_address,
    app=application,
    storage_uri="memory://",
    default_limits=["5 per hour"]
)


SERVICE_ACCOUNT_FILE = os.getenv("SERVICE_ACCOUNT_FILE")
USER_TO_IMPERSONATE = os.getenv("USER_TO_IMPERSONATE")
SCOPES = [os.getenv("SCOPES")]

logging.basicConfig(filename='app.log', level=logging.ERROR)


@application.route('/robots.txt')
def robots():
    return send_from_directory(current_app.static_folder, 'robots.txt')


@application.route('/')
def home():
    form = ContactForm()
    return render_template('base.html', form=form)


@application.route('/submit', methods=['POST'])
@limiter.limit("5 per hour")
def submit():
    form = ContactForm()
    if form.validate_on_submit():
        name = escape(form.name.data)
        email = form.email.data
        phone = form.phone.data
        message = escape(form.message.data)

        try:
            credentials = service_account.Credentials.from_service_account_file(
                SERVICE_ACCOUNT_FILE, scopes=SCOPES)

            delegated_credentials = credentials.with_subject(USER_TO_IMPERSONATE)

            service = build('gmail', 'v1', credentials=delegated_credentials)

            subject = f"New Contact Form Submission: {escape(name)}"
            message_text = f"NAME: {name}\nEMAIL: {email}\nPHONE: {phone}\n\nMESSAGE: {message}"

            msg = create_message(os.getenv("SENDER"), os.getenv("TO"), subject, message_text)
            send_message(service, 'me', msg)
            flash("Message sent successfully!", 'success')
            return redirect(url_for('home'))

        except Exception as e:
            logging.exception(f'An error occurred during form submission: {e}')
            flash("An error occurred. Please try again later.", 'danger')
            return render_template('base.html'), 500
    else:
        return render_template('base.html', form=form)


@application.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@application.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500


@application.after_request
def set_security_headers(response):
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    csp = "default-src 'self'; script-src 'self' 'unsafe-inline' https://code.jquery.com https://cdn.jsdelivr.net https://cdnjs.cloudflare.com https://stackpath.bootstrapcdn.com; style-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net; img-src 'self' data: https://cdn.jsdelivr.net/*; font-src 'self' https://cdnjs.cloudflare.com;"
    response.headers['Content-Security-Policy'] = csp
    return response


if __name__ == '__main__':
    application.run()
