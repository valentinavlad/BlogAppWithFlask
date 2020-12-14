
def login(client_is_config, name, password):
    return client_is_config.post('/auth/login', data=dict(
        name=name,
        password=password
    ), follow_redirects=True)

def test_see_all_users_by_admin(client_is_config):
    log = login(client_is_config, 'admin', '123')
    assert b'Hello Admin' in log.data
    response = client_is_config.get('/users/')
    assert response.status_code == 200
    assert b'kolo' in response.data
    assert b'bobby' in response.data

def test_create_user_by_admin(client_is_config):
    log = login(client_is_config, 'admin', '123')
    assert b'Hello Admin' in log.data
    response = client_is_config.get('/users/new')
    assert response.status_code == 200
    assert b'Name' in response.data
    assert b'Email' in response.data

    data = {'name': 'bob', 'email':'bob@gmail.com', 'password': '123'}
    response_post = client_is_config.post('/users/new', data=data, follow_redirects=True)
    assert response_post.status_code == 200
    assert b'bob' in response_post.data
    assert b'kolo' in response_post.data
    assert b'bobby' in response_post.data

def test_try_create_user_by_existing_name_by_admin(client_is_config):
    log = login(client_is_config, 'admin', '123')
    assert b'Hello Admin' in log.data
    response = client_is_config.get('/users/new')
    assert response.status_code == 200
    assert b'Name' in response.data
    assert b'Email' in response.data

    data = {'name': 'maia', 'email':'maia@gmail.com', 'password': '123'}
    response_post = client_is_config.post('/users/new', data=data)
    assert response_post.status_code == 200
    assert b'This user already exists! Use another name' in response_post.data

def test_create_user_by_non_logged_user(client_is_config):
    response = client_is_config.get('/users/new', follow_redirects=True)
    assert response.status_code == 200
    assert b'Email' in response.data
    assert b'Password' in response.data
    assert b'Login' in response.data

def test_create_user_by_logged_user_not_work(client_is_config):
    log = login(client_is_config, 'ben', '123')
    assert b'Hello Ben' in log.data
    response = client_is_config.get('/users/new', follow_redirects=True)
    assert response.status == '403 FORBIDDEN'
    assert '<h1>Forbidden</h1>' in response.get_data(as_text=True)
    assert "<h1>User ben doesn't have rights to alter this page.</h1>"\
       in response.get_data(as_text=True)

def test_update_user_by_admin(client_is_config):
    log = login(client_is_config, 'admin', '123')
    with client_is_config.session_transaction() as sess:
        sess['name'] = 'admin'
    assert b'Hello Admin' in log.data
    response = client_is_config.get('/users/2')
    assert response.status_code == 200
    assert 'Name' in response.get_data(as_text=True)

    data = {'name': 'maia_update', 'email': 'maia@gmail.com'}
    response_post = client_is_config.post('/users/2/edit', data=data, follow_redirects=True)
    assert response_post.status_code == 200
    assert b'User data' in response_post.data
    assert b'maia_update' in response_post.data
    assert 'Update' in response_post.get_data(as_text=True)

    response_two = client_is_config.get('/posts/5')

    assert b'var id = 5;' in response_two.data
    assert b'let session_logged = true;' in response_two.data
    assert b'let session_name = "admin";' in response_two.data

    response_three = client_is_config.get('/posts/?page=1')
    assert b'Angular' in response_three.data
    assert b'<p>By maia_update on 13 March 2020 <small>Post Id is 5</small></p>'\
       in response_three.data

def test_update_user_by_owner(client_is_config):
    log = login(client_is_config, 'kolo', '123')
    assert b'Hello Kolo' in log.data
    response = client_is_config.get('/users/5')
    assert b'Name: kolo' in response.data
    assert b'Email: kolo@gmail.com' in response.data
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
    log = login(client_is_config, 'admin', '123')
    assert b'Hello Admin' in log.data
    res = client_is_config.get('/users/1')
    assert res.status_code == 200
    assert b'Delete' in res.data

    response = client_is_config.post('/users/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Tia' not in response.data
    #test to see if posts by Tia are deleted
    response_two = client_is_config.get('/posts/')
    assert b'<h1>C++</h1>' not in response_two.data
    assert b'<h1>Javascript</h1>' not in response_two.data

def test_delete_user_by_other_should_not_work(client_is_config):
    log = login(client_is_config, 'bobby', '123')
    assert b'Hello Bobby' in log.data
    response = client_is_config.post('/users/1/delete', follow_redirects=True)
    assert response.status == '403 FORBIDDEN'
    assert '<h1>Forbidden</h1>' in response.get_data(as_text=True)
    assert "<h1>User bobby doesn't have rights to alter this page.</h1>"\
       in response.get_data(as_text=True)

def test_delete_user_by_non_logged_user(client_is_config):
    response = client_is_config.get('/users/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Email' in response.data
    assert b'Password' in response.data
    assert b'Login' in response.data

def test_user_first_loggin_no_pass(client_is_config):
    response = client_is_config.get('users/7/set_credentials', follow_redirects=True)
    assert b'Set login info' in response.data
    data = {'name': 'goia', 'email': 'goia@gmail.com', 'password':'123', 'cf_password':'123'}
    response_two = client_is_config.post('users/7/set_credentials',\
                                        data=data, follow_redirects=True)
    assert b'Login' in response_two.data
    assert b'Name' in response_two.data
    assert b'Email' in response_two.data

def test_access_set_credential_with_pass_forbidden(client_is_config):
    data = {'name': 'marc', 'password':'123'}
    response_post = client_is_config.post('auth/login', data=data, follow_redirects=True)
    assert '<h1>Angular</h1>' in response_post.get_data(as_text=True)
    assert b'Hello Marc !' in response_post.data
    response = client_is_config.get('users/8/set_credentials', follow_redirects=True)
    assert b'Forbidden' in response.data

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
