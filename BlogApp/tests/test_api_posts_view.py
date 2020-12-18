import base64
def login(client_is_config, name, password):
    return client_is_config.post('/auth/login', data=dict(
        name=name,
        password=password
    ), follow_redirects=True)

def test_existing_post(client_is_config):
    response = client_is_config.get('/api-posts/2')
    data = response.json
    assert response.status_code == 200
    assert data["title"] == "Php"
    assert data["owner"] == "1"
    assert data["name"] == "tia"
    assert data["img_id"] == "id2"

def test_unexisting_post(client_is_config):
    response = client_is_config.get('/api-posts/289')
    data = response.json
    assert response.status_code == 404
    assert data["error"] == "post not found"

def test_login_return_token(client_is_config):
    valid_credentials = base64.b64encode(b'tia:123').decode('utf-8')
    response = client_is_config.post(
        '/api-posts/login',
        content_type='application/json',
        headers={'Authorization': 'Basic ' + valid_credentials}
    )
    data = response.json
    assert response.status_code == 200
    token_header = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9'
    token_payload = '.eyJ1c2VyX2lkIjoxfQ'
    token_signature = '.wI1ScMWwJ779IJRumXR9T_6JPjxxSaaMzGqN8zFv6ys'
    token = token_header + token_payload + token_signature
    assert data['token'] == token


def test_login_with_invalid_credentials_return_401(client_is_config):
    invalid_credentials = base64.b64encode(b'tipa:123').decode('utf-8')
    response = client_is_config.post(
        '/api-posts/login',
        content_type='application/json',
        headers={'Authorization': 'Basic ' + invalid_credentials}
    )

    assert response.status_code == 401
    assert b'Could not verify' in response.data

def test_delete_post_by_logged_user(client_is_config):
    #POstgres id 12
    valid_credentials = base64.b64encode(b'ben:123').decode('utf-8')
    response = client_is_config.post(
        '/api-posts/login',
        content_type='application/json',
        headers={'Authorization': 'Basic ' + valid_credentials}
    )
    data = response.json
    assert response.status_code == 200
    token_header = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9'
    token_payload = '.eyJ1c2VyX2lkIjo2fQ'
    token_signature = '.KGZWLrK0r65CXAMElUhsS8yMWq2MfDIFjgY6TgUPxvY'
    token = token_header + token_payload + token_signature
    assert data['token'] == token

    token = data['token']
    headers = {
        'x-access-token' : token
    }
    response_delete = client_is_config.delete('/api-posts/12',
                                              content_type='application/json',
                                              headers=headers,
                                              follow_redirects=True)
    delete_data = response_delete.json
    assert response_delete.status_code == 200
    assert delete_data['message'] == 'Post deleted!'

def test_delete_post_by_logged_user_with_invalid_post_id(client_is_config):
    valid_credentials = base64.b64encode(b'ben:123').decode('utf-8')
    response = client_is_config.post(
        '/api-posts/login',
        content_type='application/json',
        headers={'Authorization': 'Basic ' + valid_credentials}
    )
    data = response.json
    assert response.status_code == 200
    token_header = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9'
    token_payload = '.eyJ1c2VyX2lkIjo2fQ'
    token_signature = '.KGZWLrK0r65CXAMElUhsS8yMWq2MfDIFjgY6TgUPxvY'
    token = token_header + token_payload + token_signature
    assert data['token'] == token

    token = data['token']
    headers = {
        'x-access-token' : token
    }
    response_delete = client_is_config.delete('/api-posts/158',
                                              content_type='application/json',
                                              headers=headers,
                                              follow_redirects=True)
    delete_data = response_delete.json
    assert response_delete.status_code == 404
    assert delete_data['error'] == 'post not found'

def test_delete_other_user_post_by_logged_user_403(client_is_config):
    valid_credentials = base64.b64encode(b'ben:123').decode('utf-8')
    response = client_is_config.post(
        '/api-posts/login',
        content_type='application/json',
        headers={'Authorization': 'Basic ' + valid_credentials}
    )
    data = response.json
    assert response.status_code == 200
    token_header = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9'
    token_payload = '.eyJ1c2VyX2lkIjo2fQ'
    token_signature = '.KGZWLrK0r65CXAMElUhsS8yMWq2MfDIFjgY6TgUPxvY'
    token = token_header + token_payload + token_signature
    assert data['token'] == token

    token = data['token']
    headers = {
        'x-access-token' : token
    }
    response_delete = client_is_config.delete('/api-posts/5',
                                              content_type='application/json',
                                              headers=headers,
                                              follow_redirects=True)
    delete_data = response_delete.json
    assert response_delete.status_code == 403
    assert delete_data['error'] == 'Forbidden'

def test_delete_post_by_unlogged_user_401(client_is_config):
    headers = {
        'x-access-token' : ""
    }
    response_delete = client_is_config.delete('/api-posts/5',
                                              content_type='application/json',
                                              headers=headers,
                                              follow_redirects=True)
    delete_data = response_delete.json
    assert response_delete.status_code == 401
    assert delete_data['message'] == 'Token is missing'