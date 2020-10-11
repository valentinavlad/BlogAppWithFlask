from unittest.mock import Mock
from setup.config import Config

def test_index_redirect_setup(client):
     config = Mock(Config)  
     config.db_is_configured = False
     ff = config.db_is_configured
     response = client.get('/posts/', follow_redirects=True)
     assert response.status_code == 200
     assert '<h1>Your database is not configured</h1>' in response.get_data(as_text=True)
     assert b'Database name' in response.data
     assert b'User' in response.data
     assert b'Password' in response.data

def test_view_post_redirect_setup(client):
     config = Mock(Config)  
     config.db_is_configured = False
     ff = config.db_is_configured
     response = client.get('/posts/5', follow_redirects=True)
     assert response.status_code == 200
     assert '<h1>Your database is not configured</h1>' in response.get_data(as_text=True)
     assert b'Database name' in response.data
     assert b'User' in response.data
     assert b'Password' in response.data

def test_post_create_redirect_setup(client):
     config = Mock(Config)  
     config.db_is_configured = False
     ff = config.db_is_configured
     response = client.get('/posts/new', follow_redirects=True)
     assert response.status_code == 200
     assert '<h1>Your database is not configured</h1>' in response.get_data(as_text=True)
     assert b'Database name' in response.data
     assert b'User' in response.data
     assert b'Password' in response.data

def test_post_create_redirect_setup2(client):
     config = Mock(Config)  
     config.db_is_configured = True
     ff = config.db_is_configured
     response = client.get('/posts/new')
     assert response.status_code == 200
     assert b'Owner' in response.data
     assert b'Content' in response.data

   