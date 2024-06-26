import os

def test_config_loads_from_env(client):
  # Test that configuration variables are loaded from environment variables
  assert os.getenv("SECRET_KEY") == client.application.secret_key
  assert os.getenv("SERVER") == client.application.config['MAIL_SERVER']
  # ... (repeat for other config variables)

def test_home_route(client):
  # Test the home route
  response = client.get('/')
  assert response.status_code == 200
  assert b'base.html' in response.data  # Check for template name in response

# def test_projects_route(client):
#   # Test the projects route
#   response = client.get('/projects')
#   assert response.status_code == 200
#   assert b'projects.html' in response.data  # Check for template name in response

# def test_submit_post(client, monkeypatch):
#   # Test successful form submission with mocked mail sending
#   data = {
#     'name': 'Test User',
#     'email': 'test@example.com',
#     'phone': '123-456-7890',
#     'message': 'This is a test message'
#   }
#   # Mock mail sending function to prevent actual emails
#   monkeypatch.patch('app.mail.send')
#   response = client.post('/submit', data=data)
#   assert response.status_code == 302  # Redirect on success
#   assert 'Thank you for your message' in response.session['flash'].get('success')

# def test_submit_post_error(client, monkeypatch):
#   # Test form submission error with mocked mail sending
#   data = {
#     'name': 'Test User',
#     'email': 'test@example.com',
#     'phone': '123-456-7890',
#     'message': 'This is a test message'
#   }
#   # Mock mail sending function to raise exception
#   monkeypatch.patch('app.mail.send', side_effect=Exception('Test exception'))
#   response = client.post('/submit', data=data)
#   assert response.status_code == 200  # Render error template
#   assert 'An error occurred' in response.session['flash'].get('error')

# def test_404_handler(client):
#   # Test the 404 error handler
#   response = client.get('/non-existent-page')
#   assert response.status_code == 404
#   assert b'404.html' in response.data  # Check for template name in response

# def test_500_handler(client, monkeypatch):
#   # Test the 500 error handler
#   # Simulate internal server error (replace with your error scenario)
#   monkeypatch.setattr(app, 'view_functions', {'/': lambda: 1/0})
#   response = client.get('/')
#   assert response.status_code == 500
#   assert b'500.html' in response.data  # Check for template name in response




###########################################################################
# import pytest #type: ignore
# from app import app


# @pytest.fixture

# def client():
#     response = app.test_client()


# def client():
#     # return app.test_client()
#     return app.test_client()

# def test_home_route(client):
#     response = client.get('/')
#     assert response.status_code == 200
#     assert b'base.html' in response.data

# def test_home_route_with_trailing_slash(client):
#     response = client.get('/')
#     assert response.status_code == 200
#     assert b'base.html' in response.data

# def test_home_route_with_invalid_method(client):
#     response = client.post('/')
#     assert response.status_code == 405

# def test_projects_route(client):
#     response = client.get('/projects')
#     assert response.status_code == 200
#     assert b'projects.html' in response.data

# def test_projects_route_with_trailing_slash(client):
#     response = client.get('/projects/')
#     assert response.status_code == 308

# def test_projects_route_with_invalid_method(client):
#     response = client.post('/projects')
#     assert response.status_code == 405

# def test_projects_route_with_empty_projects(client):
#     app.projects = []
#     response = client.get('/projects')
#     assert response.status_code == 200
#     assert b'No projects found' in response.data

# def test_projects_route_with_single_project(client):
#     app.projects = [{'name': 'Project 1', 'description': 'This is a test project'}]
#     response = client.get('/projects')
#     assert response.status_code == 200
#     assert b'Project 1' in response.data
#     assert b'This is a test project' in response.data

# def test_projects_route_with_multiple_projects(client):
#     app.projects = [
#         {'name': 'Project 1', 'description': 'This is a test project'},
#         {'name': 'Project 2', 'description': 'Another test project'}
#     ]
#     response = client.get('/projects')
#     assert response.status_code == 200
#     assert b'Project 1' in response.data
#     assert b'This is a test project' in response.data
#     assert b'Project 2' in response.data
#     assert response.status_code == 500
#     assert b'500.html' in response.data
#     assert b'Another test project' in response.data
    
    
# @pytest.fixture
# def test_client():
#     app.config['TESTING'] = True
#     with app.test_client() as client:
#         yield client

# def test_submit_route_get(test_client):
#     response = test_client.get('/submit')
#     assert response.status_code == 200
#     assert b'base.html' in response.data

# def test_submit_route_post_valid_data(test_client, monkeypatch):
#     monkeypatch.setenv('USERNAME', 'test@example.com')
#     data = {
#         'name': 'John Doe',
#         'email': 'john@example.com',
#         'phone': '1234567890',
#         'message': 'Hello, this is a test message.'
#     }
#     response = test_client.post('/submit', data=data, follow_redirects=True)
#     assert response.status_code == 200
#     assert b'Thank you for your message!' in response.data

# def test_submit_route_post_missing_data(test_client, monkeypatch):
#     monkeypatch.setenv('USERNAME', 'test@example.com')
#     data = {
#         'name': '',
#         'email': '',
#         'phone': '',
#         'message': ''
#     }
#     response = test_client.post('/submit', data=data, follow_redirects=True)
#     assert response.status_code == 200
#     assert b'An error occurred. Please try again later.' in response.data

# def test_submit_route_post_invalid_email(test_client, monkeypatch):
#     monkeypatch.setenv('USERNAME', 'test@example.com')
#     data = {
#         'name': 'John Doe',
#         'email': 'invalid_email',
#         'phone': '1234567890',
#         'message': 'Hello, this is a test message.'
#     }
#     response = test_client.post('/submit', data=data, follow_redirects=True)