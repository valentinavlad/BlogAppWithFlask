def test_login(client_is_config):
    response = client_is_config.get('/auth/login')

    assert response.status_code == 200
    assert b'Email' in response.data
    assert b'Password' in response.data
    data = {'name': 'tia', 'email':'tia@gmail.com', 'password':'123'}

    response_post = client_is_config.post('/auth/login', data=data, follow_redirects=True)
    assert response_post.status_code == 200
    assert b'Check our latest posts in web technologies!' in response_post.data
    assert '<h1>Angular</h1>' in response_post.get_data(as_text=True)
    assert '<h1>Php</h1>' in response_post.get_data(as_text=True)
    assert b'Hello Tia !' in response_post.data
    assert b'Log Out' in response_post.data

def test_logout(client_is_config):
    response = client_is_config.get('/auth/logout', follow_redirects=True)
    assert not b'Log Out' in response.data
    assert b'Login' in response.data

def test_login_invalid_user(client_is_config):
    response = client_is_config.get('/auth/login')

    assert response.status_code == 200
    assert b'Email' in response.data
    assert b'Password' in response.data
    data = {'email':'dummy@gmail.com', 'password':'123'}

    response_post = client_is_config.post('/auth/login', data=data)
    assert response_post.status_code == 200
    assert b'Email' in response_post.data
    assert b'Password' in response_post.data
    assert b'This user is not registered' in response_post.data
 