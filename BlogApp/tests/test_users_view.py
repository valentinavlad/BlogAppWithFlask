def login(client_is_config, email, password):
    return client_is_config.post('/auth/login', data=dict(
        email=email,
        password=password
    ), follow_redirects=True)

def test_see_all_users_by_admin(client_is_config):
    log = login(client_is_config, 'admin@gmail.com', '123')
    assert b'Hello Admin' in log.data
    response = client_is_config.get('/users/')
    assert response.status_code == 200
    assert b'Kolo' in response.data
    assert b'Bobby' in response.data

def test_create_user_by_admin(client_is_config):
    log = login(client_is_config, 'admin@gmail.com', '123')
    assert b'Hello Admin' in log.data
    response = client_is_config.get('/users/new')
    assert response.status_code == 200
    assert b'Name' in response.data
    assert b'Email' in response.data

    data = {'name': 'bob', 'email':'bob@gmail.com', 'password': '123'}

    response_post = client_is_config.post('/users/new', data=data, follow_redirects=True)
    assert response_post.status_code == 200
    assert b'bob' in response_post.data
    assert b'Kolo' in response_post.data
    assert b'Bobby' in response_post.data

def test_create_user_by_non_logged_user(client_is_config):
    response = client_is_config.get('/users/new', follow_redirects=True)
    assert response.status_code == 200
    assert b'Email' in response.data
    assert b'Password' in response.data
    assert b'Login' in response.data
def test_create_user_by_logged_user_not_work(client_is_config):
    log = login(client_is_config, 'ben@gmail.com', '123')
    response = client_is_config.get('/users/new', follow_redirects=True)
    assert response.status == '403 FORBIDDEN'
    assert '<h1>Forbidden</h1>' in response.get_data(as_text=True)
    assert "<h1>User Ben doesn't have rights to alter this page.</h1>" in response.get_data(as_text=True)
def test_update_user_by_admin(client_is_config):
    log = login(client_is_config, 'admin@gmail.com', '123')
    assert b'Hello Admin' in log.data
    response = client_is_config.get('/users/2')
    assert response.status_code == 200
    assert 'Name' in response.get_data(as_text=True)

    data = {'name': 'maia_update'}
    response_post = client_is_config.post('/users/2/edit', data=data, follow_redirects=True)
    assert response_post.status_code == 200
    assert b'User data' in response_post.data
    assert b'maia_update' in response_post.data
    assert 'Update' in response_post.get_data(as_text=True)

def test_update_user_by_owner(client_is_config):
    log = login(client_is_config, 'kolo@gmail.com', '123')
    assert b'Hello Kolo' in log.data
    
    response =  client_is_config.get('/users/5')
    assert b'Name: Kolo' in response.data
    assert 'User data' in response.get_data(as_text=True)
    data = {'name': 'kolo_update', 'email': 'kolo@gmail.com', 'password': '123'}
    response_post = client_is_config.post('/users/5/edit', data=data, follow_redirects=True)
    assert response_post.status_code == 200
    assert b'Name: kolo_update' in response_post.data

def test_update_user_by_not_logged_user(client_is_config):
    response = client_is_config.get('/users/2/edit', follow_redirects=True)
    assert response.status_code == 200
    #redirects to login
    assert b'Email' in response.data
    assert b'Password' in response.data

def test_delete_user_by_admin(client_is_config):
    #at id 1 is Tia
    log = login(client_is_config, 'admin@gmail.com', '123')
    assert b'Hello Admin' in log.data
    res = client_is_config.get('/users/1')
    assert res.status_code == 200
    assert b'Delete' in res.data

    response = client_is_config.post('/users/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Tia' not in response.data

def test_delete_user_by_other_should_not_work(client_is_config):
    log = login(client_is_config, 'bobby@gmail.com', '123')
    assert b'Hello Bobby' in log.data
    response = client_is_config.post('/users/1/delete', follow_redirects=True)
    assert response.status == '403 FORBIDDEN'
    assert '<h1>Forbidden</h1>' in response.get_data(as_text=True)
    assert "<h1>User Bobby doesn't have rights to alter this page.</h1>" in response.get_data(as_text=True)

def test_delete_user_by_non_logged_user(client_is_config):
    response = client_is_config.get('/users/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Email' in response.data
    assert b'Password' in response.data
    assert b'Login' in response.data

def test_see_all_users_redirect_setup(client_is_not_config):
    response = client_is_not_config.get('/auth/login', follow_redirects=True)
    assert response.status_code == 200
    assert '<h1>Your database is not configured</h1>' in response.get_data(as_text=True)
    assert b'Database name' in response.data
    assert b'User' in response.data
    assert b'Password' in response.data

def test_create_user_redirect_setup(client_is_not_config):
    response = client_is_not_config.get('/users/new', follow_redirects=True)
    assert response.status_code == 200
    assert '<h1>Your database is not configured</h1>' in response.get_data(as_text=True)
    assert b'Database name' in response.data
    assert b'User' in response.data
    assert b'Password' in response.data

def test_update_user_redirect_setup(client_is_not_config):
    response = client_is_not_config.get('/users/2', follow_redirects=True)
    assert response.status_code == 200
    assert '<h1>Your database is not configured</h1>' in response.get_data(as_text=True)
    assert b'Database name' in response.data
    assert b'User' in response.data
    assert b'Password' in response.data

def test_delete_user_redirect_setup(client_is_not_config):
    response = client_is_not_config.get('/users/2', follow_redirects=True)
    assert response.status_code == 200
    assert '<h1>Your database is not configured</h1>' in response.get_data(as_text=True)
    assert b'Database name' in response.data
    assert b'User' in response.data
    assert b'Password' in response.data
