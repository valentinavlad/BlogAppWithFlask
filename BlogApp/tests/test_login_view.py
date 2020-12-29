from flask import json

def test_login(client_is_config):
    response = client_is_config.post('/api-posts/login', data=json.dumps(dict(
        username='tia',
        password='123'
    )), content_type='application/json')
    data = json.loads(response.data.decode())

    assert response.status_code == 200
    assert data['message'] == 'Successfully logged in.'
    assert data['status'] == 'success'
    assert data['auth_token']

def test_logout(client_is_config):
    response = client_is_config.get('/auth/logout', follow_redirects=True)
    assert not b'Log Out' in response.data
    assert b'Login' in response.data

def test_login_invalid_user(client_is_config):
    response = client_is_config.post('/api-posts/login', data=json.dumps(dict(
            username='dummy',
            password='222'
        )),
        content_type='application/json')
    data = json.loads(response.data.decode())
    assert response.status_code == 401
    assert data['message'] == 'Credentials invalid!' 
    assert data['status'] == 'fail' 
 