import json
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
    response = client_is_config.post('/api-posts/login',
                                     data=json.dumps(dict(
                                         username='tia',
                                         password='123')),
                                     content_type='application/json')

    data = json.loads(response.data.decode())
    assert data['status'] == 'success'
    assert data['message'] == 'Successfully logged in.'
    assert data['auth_token']
    assert response.status_code == 200

def test_login_with_invalid_credentials_return_401(client_is_config):
    response = client_is_config.post(
        '/api-posts/login',
        data=json.dumps(dict(
            username='dummy',
            password='111'
        )),
        content_type='application/json')

    assert response.status_code == 401
    assert b'Credentials invalid!' in response.data

def test_delete_post_by_logged_user(client_is_config):
    #POstgres id 12
    response = client_is_config.post(
        '/api-posts/login',
        data=json.dumps(dict(
            username='ben',
            password='123'
        )),
        content_type='application/json')
    data = json.loads(response.data.decode())
    assert data['status'] == 'success'
    assert data['message'] == 'Successfully logged in.'
    assert data['auth_token']
    assert response.status_code == 200

    headers = {
        'Authorization' : 'Bearer ' + data['auth_token']
    }
    response_delete = client_is_config.delete('/api-posts/12',
                                              content_type='application/json',
                                              headers=headers,
                                              follow_redirects=True)
    delete_data = json.loads(response_delete.data.decode())
    assert response_delete.status_code == 200
    assert delete_data['message'] == 'Post deleted!'

def test_delete_post_by_logged_user_with_invalid_post_id(client_is_config):
    response = client_is_config.post('/api-posts/login',
                                     data=json.dumps(dict(
                                         username='ben',
                                         password='123')),
                                     content_type='application/json')
    data = json.loads(response.data.decode())
    assert data['message'] == 'Successfully logged in.'

    headers = {
        'Authorization' : 'Bearer ' + data['auth_token']
    }
    response_delete = client_is_config.delete('/api-posts/158',
                                              content_type='application/json',
                                              headers=headers,
                                              follow_redirects=True)
    delete_data = response_delete.json
    assert response_delete.status_code == 404
    assert delete_data['error'] == 'Post not found'

def test_delete_other_user_post_by_logged_user_403(client_is_config):
    response = client_is_config.post('/api-posts/login',
                                     data=json.dumps(dict(
                                         username='ben',
                                         password='123')),
                                     content_type='application/json')
    data = json.loads(response.data.decode())
    assert data['message'] == 'Successfully logged in.'
    headers = {
        'Authorization' : 'Bearer ' + data['auth_token']
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
        'Authorization' : ""
    }
    response_delete = client_is_config.delete('/api-posts/5',
                                              content_type='application/json',
                                              headers=headers,
                                              follow_redirects=True)
    delete_data = response_delete.json
    assert response_delete.status_code == 401
    assert delete_data['message'] == 'Token is missing'

def test_logout(client_is_config):
    response = client_is_config.post('/api-posts/logout',
                                     content_type='application/json', follow_redirects=True)
    data = json.loads(response.data.decode())
    assert data['message'] == 'Successfully logged out.'
    assert response.status_code == 200

def test_set_credentials_should_set_pass(client_is_config):
    response = client_is_config.post('/api-posts/login',
                                     data=json.dumps(dict(
                                         username='oli',
                                         password='')),
                                     content_type='application/json',
                                     follow_redirects=True)
    data = json.loads(response.data.decode())
    assert data['message'] == 'Accepted'
    assert response.status_code == 202
    response_set_cred = client_is_config.post('/api-posts/9/set_credentials',
                                              data=json.dumps(dict(
                                                  email='oli@jds.com',
                                                  password='123',
                                                  cf_password='123')),
                                              content_type='application/json',
                                              follow_redirects=True)
    data = json.loads(response_set_cred.data.decode())
    assert data['email'] == 'oli@jds.com'
    assert data['name'] == 'oli'

def test_set_credentials_user_with_pass_should_return_403(client_is_config):
    response_set_cred = client_is_config.post('/api-posts/8/set_credentials',
                                              data=json.dumps(dict(
                                                  email='marc@gmail.com',
                                                  password='123',
                                                  cf_password='123')),
                                              content_type='application/json',
                                              follow_redirects=True)
    data = json.loads(response_set_cred.data.decode())
    assert data['error'] == 'Forbidden!'
    assert response_set_cred.status_code == 403
