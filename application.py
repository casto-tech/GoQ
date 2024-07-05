import os
from flask import Flask, render_template, request, flash, redirect, url_for  # type: ignore
from flask_mail import Mail, Message  # type: ignore
from dotenv import load_dotenv  # type: ignore
import ssl
# from projects import projects

load_dotenv()
application = Flask(__name__)


context = ssl.create_default_context()
context.options &= ~ssl.OP_NO_SSLv2
MAIL_CONTEXT = context


application.secret_key = os.getenv("SECRET_KEY")
application.config['MAIL_SERVER'] = os.getenv("SERVER")
application.config['MAIL_PORT'] = os.getenv("PORT")
application.config['MAIL_USERNAME'] = os.getenv("USERNAME")
application.config['MAIL_PASSWORD'] = os.getenv("PASSWORD")
application.config['MAIL_USE_TLS'] = os.getenv("TLS")
application.config['MAIL_USE_SSL'] = os.getenv("SSL")

mail = Mail(application)


@application.route('/')
def home():
    return render_template('base.html')


# projects = projects


# @application.route('/projects')
# def projects_page():
#     return render_template('projects.html', projects=projects)


@application.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        try:
            msg = Message(subject=f"New Contact Form Submission: {name}",
                          sender=os.getenv("USERNAME"),
                          recipients=[os.getenv("USERNAME")])
            msg.body = (f"Name: {name},\nEmail: {email}\nPhone: {phone}"
                        f"\n\nMessage: {message}")
            mail.send(msg)
            flash('We will get back to you soon.', 'success')
            return redirect(url_for('home'))
        except Exception as e:
            print(f"Error sending email: {e}")
            flash('An error occurred. Please try again later.', 'error')
            return render_template('500.html')

    return render_template('base.html')


@application.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@application.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    application.run()
