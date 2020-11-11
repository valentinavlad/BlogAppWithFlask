def login(client_is_config, name, password):
    return client_is_config.post('/auth/login', data=dict(
        name=name,
        password=password
    ), follow_redirects=True)

def logout(client_is_config):
    return client_is_config.get('/auth/logout', follow_redirects=True)

def test_index(client_is_config):
    response = client_is_config.get('/posts/', follow_redirects=True)
    assert response.status_code == 200
    assert '<h1>Angular</h1>' in response.get_data(as_text=True)
    assert b'<p>By maia on March 13, 2020 <small>Post Id is 5</small></p>' in response.data
    assert '<h1>C++</h1>' in response.get_data(as_text=True)
    assert b'<p>By tia on March 13, 2020 <small>Post Id is 6</small></p>' in response.data
    assert b'Check our latest posts in web technologies!' in response.data

def test_view_post(client_is_config):
    response = client_is_config.get('/posts/5')
    assert '<h3>Angular</h3>' in response.get_data(as_text=True)
    assert response.status_code == 200

def test_post_create_by_owner(client_is_config):
    log = login(client_is_config, 'tia', '123')
    assert b'Hello Tia' in log.data
    response = client_is_config.get('/posts/new')
    assert response.status_code == 200
    assert b'Owner' in response.data
    assert b'Content' in response.data
    data = {'title': 'KOKO', 'contents':'hello'}

    response_post = client_is_config.post('/posts/new', data=data, follow_redirects=True)
    assert response_post.status_code == 200
    assert b'Check our latest posts in web technologies!' in response_post.data
    assert 'KOKO' in response_post.get_data(as_text=True)
    logout(client_is_config)

def test_post_create_by_admin(client_is_config):
    log = login(client_is_config, 'admin', '123')
    assert b'Hello Admin' in log.data
    response = client_is_config.get('/posts/new')
    assert response.status_code == 200
    assert b'Owner' in response.data
    assert b'Content' in response.data
    data = {'title': 'KOKO', 'contents':'hello'}

    response_post = client_is_config.post('/posts/new', data=data, follow_redirects=True)
    assert response_post.status_code == 200
    assert b'Check our latest posts in web technologies!' in response_post.data
    assert 'KOKO' in response_post.get_data(as_text=True)
    logout(client_is_config)

def test_cannot_create_post_if_not_logged(client_is_config):
    response = client_is_config.get('/posts/new', follow_redirects=True)
    assert response.status_code == 200
    assert b'Email' in response.data
    assert b'Password' in response.data
    assert b'Login' in response.data
#C++
def test_update_post_by_owner(client_is_config):
    log = login(client_is_config, 'tia', '123')
    with client_is_config.session_transaction() as sess:
        sess['user_id'] = '1'
    assert b'Hello Tia' in log.data
    response = client_is_config.get('/posts/6')
    assert response.status_code == 200
    assert b'View your post' in response.data

    data = {'title': 'updated C++', 'owner': 'update', 'contents': 'updated content'}
    response_post = client_is_config.post('/posts/6/edit', data=data, follow_redirects=True)
    assert response_post.status_code == 200
    assert b'View your post' in response_post.data
    assert 'updated C++' in response_post.get_data(as_text=True)
    logout(client_is_config)
    sess.clear()
#php
def test_update_post_by_admin(client_is_config):
    log = login(client_is_config, 'admin', '123')
    with client_is_config.session_transaction() as sess:
        sess['user_id'] = '3'
    assert b'Hello Admin' in log.data
    response = client_is_config.get('/posts/2')
    assert response.status_code == 200
    assert b'View your post' in response.data

    data = {'title': 'updated PHP', 'owner': 'update', 'contents': 'úpdated Php content'}
    response_post = client_is_config.post('/posts/2/edit', data=data, follow_redirects=True)
    assert response_post.status_code == 200
    assert b'View your post' in response_post.data
    assert 'updated PHP' in response_post.get_data(as_text=True)

#Laravel
def test_update_post_by_other_wont_work(client_is_config):
    log = login(client_is_config, 'tia', '123')
    assert b'Hello Tia' in log.data
    with client_is_config.session_transaction() as sess:
        sess['user_id'] = '1'
    response = client_is_config.get('/posts/8')
    assert response.status_code == 200
    assert b'View your post' in response.data

    data = {'title': 'updated Laravel', 'owner': 'update', 'contents': 'úpdated Laravel content'}
    resp = client_is_config.post('/posts/8/edit', data=data)

    assert resp.status == '403 FORBIDDEN'
    assert '<h1>Forbidden</h1>' in resp.get_data(as_text=True)
    assert "<h1>User tia doesn't have rights to alter this page.</h1>"\
       in resp.get_data(as_text=True)

def test_update_not_logged_user(client_is_config):
    response = client_is_config.get('/posts/8/edit', follow_redirects=True)
    assert response.status_code == 200
    assert b'Email' in response.data
    assert b'Password' in response.data
    assert b'Login' in response.data

def test_update_post_by_user_not_logged_redirect_login(client_is_config):
    response = client_is_config.post('/posts/4/edit', follow_redirects=True)
    assert response.status_code == 200
    assert b'Email' in response.data
    assert b'Password' in response.data

#javascript
def test_delete_post_by_other_dont_work(client_is_config):
    #at id 4 is Javascript
    log = login(client_is_config, 'maia', '123')
    with client_is_config.session_transaction() as sess:
        sess['user_id'] = '2'
    assert b'Hello Maia' in log.data
    res = client_is_config.get('/posts/4')
    assert res.status_code == 200
    response = client_is_config.post('/posts/4/delete')
    assert response.status == '403 FORBIDDEN'
    assert '<h1>Forbidden</h1>' in response.get_data(as_text=True)
    assert "<h1>User maia doesn't have rights to alter this page.</h1>"\
       in response.get_data(as_text=True)
    logout(client_is_config)

def test_delete_post_by_user_not_logged_redirect_login(client_is_config):
    #at id 4 is Javascript
    response = client_is_config.post('/posts/4/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Email' in response.data
    assert b'Password' in response.data

def test_delete_post_by_owner(client_is_config):
    #at id 4 is Javascript
    log = login(client_is_config, 'tia', '123')
    with client_is_config.session_transaction() as session:
        session['user_id'] = '1'
    assert b'Hello Tia' in log.data
    res = client_is_config.get('/posts/4')
    assert res.status_code == 200
    assert b'Hi! View your post' in res.data
    assert b'Javascript' in res.data
    response = client_is_config.post('/posts/4/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Javascript' not  in response.data
    assert '<h1>Vue Js</h1>' in response.get_data(as_text=True)

    logout(client_is_config)
#python
def test_delete_post_by_admin(client_is_config):
    log = login(client_is_config, 'admin', '123')
    with client_is_config.session_transaction() as sess:
        sess['user_id'] = '3'
    assert b'Hello Admin' in log.data
    res = client_is_config.get('/posts/1')
    assert res.status_code == 200
    assert b'Delete your post' in res.data

    response = client_is_config.post('/posts/1/delete', follow_redirects=True)
    assert b'Angular' in response.data
    assert response.status_code == 200
    response_two = client_is_config.get('/posts/?page=2')
    assert b'Python' not in response_two.data
    assert '<h1>Java</h1>' in response_two.get_data(as_text=True)
    logout(client_is_config)
    sess.clear()

def test_delete_not_logged_user(client_is_config):
    response = client_is_config.get('/posts/8/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Email' in response.data
    assert b'Password' in response.data
    assert b'Login' in response.data

def test_index_redirect_setup(client_is_not_config):
    response = client_is_not_config.get('/posts/', follow_redirects=True)
    assert response.status_code == 200
    assert '<h1>Your database is not configured</h1>' in response.get_data(as_text=True)
    assert b'Database name' in response.data
    assert b'User' in response.data
    assert b'Password' in response.data

def test_view_post_redirect_setup(client_is_not_config):
    response = client_is_not_config.get('/posts/5', follow_redirects=True)
    assert response.status_code == 200
    assert '<h1>Your database is not configured</h1>' in response.get_data(as_text=True)
    assert b'Database name' in response.data
    assert b'User' in response.data
    assert b'Password' in response.data

def test_post_create_redirect_setup(client_is_not_config):
    response = client_is_not_config.get('/posts/new', follow_redirects=True)
    assert response.status_code == 200
    assert '<h1>Your database is not configured</h1>' in response.get_data(as_text=True)
    assert b'Database name' in response.data
    assert b'User' in response.data
    assert b'Password' in response.data

def test_post_delete_redirect_setup(client_is_not_config):
    response = client_is_not_config.get('/posts/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert '<h1>Your database is not configured</h1>' in response.get_data(as_text=True)
    assert b'Database name' in response.data
    assert b'User' in response.data
    assert b'Password' in response.data

def test_post_update_redirect_setup(client_is_not_config):
    response = client_is_not_config.get('/posts/2/edit', follow_redirects=True)
    assert response.status_code == 200
    assert '<h1>Your database is not configured</h1>' in response.get_data(as_text=True)
    assert b'Database name' in response.data
    assert b'User' in response.data
    assert b'Password' in response.data
##TEST PAGINATION
def test_see_posts_first_page(client_is_config):
    response = client_is_config.get('/posts/?page=1')
    assert b'<h1>Angular</h1>' in response.data
    assert b'<p>By maia on March 13, 2020 <small>Post Id is 5</small></p>' in response.data

def test_see_posts_second_page(client_is_config):
    response = client_is_config.get('/posts/?page=2')
    assert b'<h1>Java</h1>' in response.data

def test_filtering_by_name(client_is_config):
    response = client_is_config.get('/posts/?page=1')
    assert b'<h1>Angular</h1>' in response.data
    response_two = client_is_config.post('/posts/', data={'user_id': '1', 'name':'tia'}, \
      follow_redirects=True)
    assert b'C++' in response_two.data
