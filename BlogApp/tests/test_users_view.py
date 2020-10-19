def login(client_is_config, email, password):
    return client_is_config.post('/auth/login', data=dict(
        email=email,
        password=password
    ), follow_redirects=True)
#individual trec, in grup nu
def test_see_all_users(client_is_config):
    log = login(client_is_config, 'admin@gmail.com', '123')
    assert b'Hello Admin' in log.data
    response = client_is_config.get('/users/')
    assert response.status_code == 200
    assert b'Maia' in response.data
    assert b'Tia' in response.data

def test_create_user(client_is_config):
    log = login(client_is_config, 'admin@gmail.com', '123')
    assert b'Hello Admin' in log.data
    response = client_is_config.get('/users/new')
    assert response.status_code == 200
    assert b'Name' in response.data
    assert b'Email' in response.data

    data = {'name': 'bob', 'email':'bob@gmail.com', 'password': '123'}

    response_post = client_is_config.post('/users/new', data=data, follow_redirects=True)
    assert response_post.status_code == 200
    assert b'Maia' in response_post.data
    assert 'Tia' in response_post.get_data(as_text=True)

def test_update_user(client_is_config):
    log = login(client_is_config, 'admin@gmail.com', '123')
    assert b'Hello Admin' in log.data
    response = client_is_config.get('/users/2')
    assert response.status_code == 200
    assert 'Name' in response.get_data(as_text=True)

    data = {'name': 'bob', 'email':'bob@gmail.com', 'password': '123'}
    response_post = client_is_config.post('/users/2/edit', data=data, follow_redirects=True)
    assert response_post.status_code == 200
    assert b'User data' in response_post.data
    assert 'Update' in response_post.get_data(as_text=True)
