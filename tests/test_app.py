# import pytest
# from app import app

# def test_submit_post_success(test_client, monkeypatch):
#   # Test successful form submission with mocked mail sending
#   data = {
#     'name': 'Test User',
#     'email': 'test@example.com',
#     'phone': '123-456-7890',
#     'message': 'This is a test message'
#   }
#   # Mock mail sending function to prevent actual emails
#   monkeypatch.patch('app.mail.send')
#   response = app.post('/submit', data=data)
#   assert response.status_code == 302  # Redirect on success
#   assert 'Thank you for your message' in response.session['flash'].get('success')

# def test_submit_post_error(test_client, monkeypatch):
#   # Test form submission error with mocked mail sending
#   data = {
#     'name': 'Test User',
#     'email': 'test@example.com',
#     'phone': '123-456-7890',
#     'message': 'This is a test message'
#   }
#   # Mock mail sending function to raise exception
#   monkeypatch.patch('app.mail.send', side_effect=Exception('Test exception'))
#   response = app.post('/submit', data=data)
#   assert response.status_code == 200  # Render error template
#   assert 'An error occurred' in response.session['flash'].get('error')