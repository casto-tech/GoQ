from google.oauth2 import service_account
from googleapiclient.discovery import build
from email.mime.text import MIMEText
import base64

# Set up the service account credentials
SERVICE_ACCOUNT_FILE = 'sa-key.json'
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

# Email of the user you want to impersonate (only needed for domain-wide delegation)
USER_TO_IMPERSONATE = 'info@greensonq.com'

# Create credentials using the service account file
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# If using domain-wide delegation, impersonate a user
delegated_credentials = credentials.with_subject(USER_TO_IMPERSONATE)

# Build the Gmail service
service = build('gmail', 'v1', credentials=delegated_credentials)

# Create the email content
def create_message(sender, to, subject, message_text):
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

# Send the email
def send_message(service, user_id, message):
    try:
        message = service.users().messages().send(userId=user_id, body=message).execute()
        print(f'Message Id: {message["id"]}')
        return message
    except Exception as error:
        print(f'An error occurred: {error}')
        return None

# Define the email details
sender = 'info@greensonq.com'
to = 'joey@greensonq.com'
subject = 'Test Email'
message_text = 'This is a test email sent using the Gmail API and a service account.'

# Create and send the email
message = create_message(sender, to, subject, message_text)
send_message(service, 'me', message)