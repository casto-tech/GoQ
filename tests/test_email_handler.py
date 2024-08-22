# import base64
# from email.mime.text import MIMEText
# import pytest
# from email_handler import create_message, send_message


# # Mock service for testing
# class MockService:
#     def users(self):
#         return self

#     def messages(self):
#         return self

#     def send(self, userId, body):
#         return {'id': 'mock_message_id'}


# def test_create_message():
#     sender = 'sender@example.com'
#     to = 'recipient@example.com'
#     subject = 'Test Subject'
#     message_text = 'Hello, this is a test message.'

#     expected_raw = base64.urlsafe_b64encode(MIMEText(message_text).as_bytes()).decode()

#     result = create_message(sender, to, subject, message_text)
#     # assert result['raw'] == expected_raw
#     assert result[create_message(sender=sender, to=to, subject=subject, message_text=message_text)] == sender


# def test_send_message():
#     user_id = 'user123'
#     message = {'raw': 'mock_base64_encoded_message'}

#     # Create a mock service instance
#     mock_service = MockService()

#     # Test successful message sending
#     result = send_message(mock_service, user_id, message)
#     assert result['id'] == 'mock_message_id'

#     # Test exception handling (you can customize this part)
#     with pytest.raises(Exception):
#         send_message(mock_service, user_id, {'invalid_key': 'invalid_value'})
