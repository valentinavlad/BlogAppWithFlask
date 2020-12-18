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
    #MySql id 11
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
    response_delete = client_is_config.delete('/api-posts/11',
                                              content_type='application/json',
                                              headers=headers)
    assert response_delete == 200
   # response_delete = client_is_config.
