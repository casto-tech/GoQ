import base64
from flask import flash, render_template, redirect, url_for
from email.mime.text import MIMEText


def create_message(sender, to, subject, message_text):
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}


def send_message(service, user_id, message):
    try:
        message = service.users().messages().send(userId=user_id, body=message).execute() # type: ignore
        print(f'Message Id: {message["id"]}')
        flash('We will get back to you soon.', 'success')
        return message
    except Exception as error:
        print(f'An error occurred: {error}')
        flash('An error occurred. Please try again later.', 'error')
        return render_template('500.html')
    return redirect(url_for('home'))
