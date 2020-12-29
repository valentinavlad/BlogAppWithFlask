import io
from flask import json

def login(client_is_config, name, password):
    return client_is_config.post(
        '/api-posts/login',
        data=json.dumps(dict(
            username=name,
            password=password
        )),
        content_type='application/json'
    )

def logout(client_is_config):
    return client_is_config.get('/auth/logout', follow_redirects=True)

def test_index(client_is_config):
    response = client_is_config.get('/posts/', follow_redirects=True)
    assert response.status_code == 200
    assert '<h1>Angular</h1>' in response.get_data(as_text=True)
    assert b'<p>By maia on 13 March 2020 <small>Post Id is 5</small></p>' in response.data
    assert '<h1>C++</h1>' in response.get_data(as_text=True)
    assert b'<p>By tia on 13 March 2020 <small>Post Id is 6</small></p>' in response.data
    assert b'Check our latest posts in web technologies!' in response.data

def test_view_post_user_not_logged_in(client_is_config):
    response = client_is_config.get('/posts/5')
    assert 'var id = 5;' in response.get_data(as_text=True)
    assert b'let session_logged = false;' in response.data
    assert b'let session_name = "";' in response.data
    assert response.status_code == 200

def test_view_post_user_logged_in(client_is_config):
    res = client_is_config.get('/auth/login')
    assert b'<h3>Login</h3>' in res.data
    assert b'<input type="text" class="form-control" placeholder="Name" name="name" id="name">' in res.data
    assert b'<input type="password" class="form-control" placeholder="Password" name="password" id="password">' in res.data
    assert b'<input type="submit" value="Login" class="btn float-right login_btn" onclick="submit_login()">' in res.data

    response = login(client_is_config, 'tia', '123')
    data = json.loads(response.data.decode())
    assert data['status'] == 'success'
    assert data['message'] == 'Successfully logged in.'
    assert data['auth_token']
    assert response.content_type == 'application/json'
    assert response.status_code == 200

    response2 = client_is_config.get('/posts/5')
    assert b'Hello Tia' in response2.data
    assert 'var id = 5;' in response2.get_data(as_text=True)
    assert b'let session_logged = true;' in response2.data
    assert b'let session_name = "tia";' in response2.data
    assert response2.status_code == 200

def test_post_create_by_owner(client_is_config):
    response = login(client_is_config, 'tia', '123')
    data = json.loads(response.data.decode())
    assert data['status'] == 'success'
    assert data['message'] == 'Successfully logged in.'
    assert data['auth_token']
    assert response.content_type == 'application/json'
    assert response.status_code == 200

    response2 = client_is_config.get('/posts/new')
    assert b'Hello Tia' in response2.data
    assert response2.status_code == 200
    assert b'<label for="title">Title</label>' in response2.data
    assert b'Content' in response2.data

    file_name = "1.png"
    data = {
        'title': 'KOKO', 'contents':'hello',
        'file': (io.BytesIO(b"some random data"), file_name)
    }
    response_post = client_is_config.post('/posts/new', data=data, follow_redirects=True)
    assert response_post.status_code == 200
    assert b'Check our latest posts in web technologies!' in response_post.data
    assert b'"data:image/png;base64,c29tZSByYW5kb20gZGF0YQ=="'\
       in response_post.data
    assert 'KOKO' in response_post.get_data(as_text=True)
    logout(client_is_config)

def test_post_create_by_admin(client_is_config):
    response = login(client_is_config, 'admin', '123')
    data = json.loads(response.data.decode())
    assert data['status'] == 'success'
    assert data['message'] == 'Successfully logged in.'
    assert data['auth_token']
    assert response.content_type == 'application/json'
    assert response.status_code == 200

    response2 = client_is_config.get('/posts/new')
    assert b'Hello Admin' in response2.data
    assert response2.status_code == 200
    assert b'<label for="title">Title</label>' in response2.data
    assert b'Content' in response2.data
    file_name = "1.PNG"
    data = {
        'title': 'KOKO', 'contents':'hello',
        'file': (io.BytesIO(b"some random data"), file_name)
    }

    response_post = client_is_config.post('/posts/new', data=data, follow_redirects=True)
    assert response_post.status_code == 200
    assert b'Check our latest posts in web technologies!' in response_post.data
    assert b'"data:image/png;base64,c29tZSByYW5kb20gZGF0YQ=="' in response_post.data
    assert 'KOKO' in response_post.get_data(as_text=True)

    logout(client_is_config)

def test_post_create_by_owner_wrong_extension_file_error(client_is_config):
    response = login(client_is_config, 'tia', '123')
    data = json.loads(response.data.decode())
    assert data['status'] == 'success'
    assert data['message'] == 'Successfully logged in.'
    assert data['auth_token']
    assert response.content_type == 'application/json'
    assert response.status_code == 200

    response2 = client_is_config.get('/posts/new')
    assert b'Hello Tia' in response2.data
    assert response2.status_code == 200
    assert b'<label for="title">Title</label>' in response2.data
    assert b'Content' in response2.data
    file_name = "1.txt"
    data = {
        'title': 'KOKO', 'contents':'hello',
        'file': (io.BytesIO(b"some random data"), file_name)
    }

    response_post = client_is_config.post('/posts/new', data=data, follow_redirects=True)
    assert response_post.status_code == 200
    assert b'This format file is not supported!' in response_post.data
    assert b'<form method="POST" action="" enctype="multipart/form-data">' in response_post.data
    logout(client_is_config)

def test_post_create_by_owner_extension_file_upper(client_is_config):
    response = login(client_is_config, 'tia', '123')
    data = json.loads(response.data.decode())
    assert data['status'] == 'success'
    assert data['message'] == 'Successfully logged in.'
    assert data['auth_token']
    assert response.content_type == 'application/json'
    assert response.status_code == 200
   
    response2 = client_is_config.get('/posts/new')
    assert response2.status_code == 200
    assert b'<label for="title">Title</label>' in response2.data
    assert b'Content' in response2.data
    file_name = "1.PNG"
    data = {
        'title': 'KOKO', 'contents':'hello',
        'file': (io.BytesIO(b"some random data"), file_name)
    }
    response_post = client_is_config.post('/posts/new', data=data, follow_redirects=True)
    assert response_post.status_code == 200
    assert b'Check our latest posts in web technologies!' in response_post.data
    assert b'"data:image/png;base64,c29tZSByYW5kb20gZGF0YQ=="' in response_post.data
    assert 'KOKO' in response_post.get_data(as_text=True)

    logout(client_is_config)

def test_cannot_create_post_if_not_logged(client_is_config):
    response = client_is_config.get('/posts/new', follow_redirects=True)
    assert response.status_code == 200
    assert b'Password' in response.data
    assert b'Login' in response.data

def test_update_post_by_owner(client_is_config):
    res = client_is_config.get('/auth/login')
    assert b'<h3>Login</h3>' in res.data
    assert b'<input type="text" class="form-control" placeholder="Name" name="name" id="name">' in res.data
    assert b'<input type="password" class="form-control" placeholder="Password" name="password" id="password">' in res.data
    assert b'<input type="submit" value="Login" class="btn float-right login_btn" onclick="submit_login()">' in res.data

    response = login(client_is_config, 'tia', '123')
    data = json.loads(response.data.decode())
    assert data['status'] == 'success'
    assert data['message'] == 'Successfully logged in.'
    assert data['auth_token']
    assert response.content_type == 'application/json'
    assert response.status_code == 200

    response2 = client_is_config.get('/posts/6')
    assert response2.status_code == 200
    assert b'var id = 6;' in response2.data
    assert b'let session_logged = true;' in response2.data
    assert b'let session_name = "tia";' in response2.data
    assert b'Hello Tia' in response2.data

def test_update_post_by_admin(client_is_config):
    response = login(client_is_config, 'admin', '123')
    data = json.loads(response.data.decode())
    assert data['status'] == 'success'
    assert data['message'] == 'Successfully logged in.'
    assert data['auth_token']
    assert response.content_type == 'application/json'
    assert response.status_code == 200
    response2 = client_is_config.get('/posts/2')
    assert b'Hello Admin' in response2.data
    assert response2.status_code == 200
    assert b'View your post' in response2.data
    assert b'var id = 2;' in response2.data
    assert b'let session_logged = true;' in response2.data
    assert b'let session_name = "admin";' in response2.data

#Laravel
def test_update_post_by_other_wont_work(client_is_config):
    res = client_is_config.get('/auth/login')
    assert b'<h3>Login</h3>' in res.data
    assert b'<input type="text" class="form-control" placeholder="Name" name="name" id="name">' in res.data
    assert b'<input type="password" class="form-control" placeholder="Password" name="password" id="password">' in res.data
    assert b'<input type="submit" value="Login" class="btn float-right login_btn" onclick="submit_login()">' in res.data

    response = login(client_is_config, 'tia', '123')
    data = json.loads(response.data.decode())
    assert data['status'] == 'success'
    assert data['message'] == 'Successfully logged in.'
    assert data['auth_token']
    assert response.content_type == 'application/json'
    assert response.status_code == 200
  
    response2 = client_is_config.get('/posts/8')
    assert response2.status_code == 200
    assert b'View your post' in response2.data

    data = {'title': 'updated Laravel', 'owner': 'update', 'contents': 'úpdated Laravel content'}
    resp = client_is_config.post('/posts/8/edit', data=data)

    assert resp.status == '403 FORBIDDEN'
    assert '<h1>Forbidden</h1>' in resp.get_data(as_text=True)
    assert "<h1>User tia doesn't have rights to alter this page.</h1>"\
       in resp.get_data(as_text=True)

def test_update_not_logged_user(client_is_config):
    response = client_is_config.get('/posts/8/edit', follow_redirects=True)
    assert response.status_code == 200
    assert b'Password' in response.data
    assert b'Login' in response.data

def test_update_post_by_user_not_logged_redirect_login(client_is_config):
    response = client_is_config.post('/posts/4/edit', follow_redirects=True)
    assert response.status_code == 200
    assert b'Name' in response.data
    assert b'Password' in response.data

#javascript
def test_delete_post_by_other_dont_work(client_is_config):
    #at id 4 is Javascript
    response = login(client_is_config, 'maia', '123')
    data = json.loads(response.data.decode())
    assert data['status'] == 'success'
    assert data['message'] == 'Successfully logged in.'
    assert data['auth_token']
    assert response.content_type == 'application/json'
    assert response.status_code == 200

    with client_is_config.session_transaction() as sess:
        sess['user_id'] = '2'

    res = client_is_config.get('/posts/4')
    assert b'Hello Maia' in res.data
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
    assert b'Password' in response.data

def test_delete_post_by_owner(client_is_config):
    #at id 4 is Javascript
    response = login(client_is_config, 'tia', '123')
    data = json.loads(response.data.decode())
    assert data['status'] == 'success'
    assert data['message'] == 'Successfully logged in.'
    assert data['auth_token']
    assert response.content_type == 'application/json'
    assert response.status_code == 200

    res = client_is_config.get('/posts/4')
    assert b'Hello Tia' in res.data
    assert res.status_code == 200
    assert b'Hi! View your post' in res.data
    assert b'var id = 4;' in res.data
    assert b'let session_logged = true;' in res.data
    assert b'let session_name = "tia";' in res.data

    logout(client_is_config)
#python
def test_delete_post_by_admin(client_is_config):
    response = login(client_is_config, 'admin', '123')
    data = json.loads(response.data.decode())
    assert data['status'] == 'success'
    assert data['message'] == 'Successfully logged in.'
    assert data['auth_token']
    assert response.content_type == 'application/json'
    assert response.status_code == 200

    res = client_is_config.get('/posts/1')
    assert res.status_code == 200
    assert b'var id = 1;' in res.data
    assert b'let session_logged = true;' in res.data
    assert b'let session_name = "admin";' in res.data

    logout(client_is_config)

def test_delete_not_logged_user(client_is_config):
    response = client_is_config.get('/posts/8/delete', follow_redirects=True)
    assert response.status_code == 200
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
    left = bytearray(b"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HA")
    right = bytearray(b"wCAAAAC0lEQVR42mNkMAYAADkANVKH3ScAAAAASUVORK5CYII=")

    img = left + right
    assert img in response.data
    assert b'<h1>Angular</h1>' in response.data
    assert b'<p>By maia on 13 March 2020 <small>Post Id is 5</small></p>' in response.data
    assert b'<h1>C++</h1>' in response.data
    assert b'Newer posts' not in response.data
    assert b'Older posts' in response.data

def test_see_posts_second_page(client_is_config):
    #have 3 pages
    response = client_is_config.get('/posts/?page=2')
    assert b'<h1>Laravel</h1>' in response.data
    assert b'<h1>Ajax</h1>' in response.data

    assert b'<a class="btn btn-outline-info" href="/posts/?page=1">Newer posts</a>' in response.data
    assert b'<a class="btn btn-outline-info" href="/posts/?page=3&amp;user=">Older posts</a>'\
       in response.data

def test_see_posts_third_page(client_is_config):
    #have 3 pages
    response = client_is_config.get('/posts/?page=3')

    assert b'<h1>MySql</h1>' in response.data
    assert b'Newer posts' in response.data
    assert b'Older posts' not in response.data

def test_filtering_by_name(client_is_config):
    response = client_is_config.get('/posts/?page=1')
    assert b'<h1>Angular</h1>' in response.data
    with client_is_config.session_transaction() as sess:
        sess['post_owner'] = 'tia'
        sess['post_owner_id'] = '1'
    response_two = client_is_config.get('/posts/?page=1&user="tia"')
    assert b'<h1>Angular</h1>' not in response_two.data
    assert b'<p>By maia on 13 March 2020 <small>Post Id is 5</small></p>' not in response_two.data
    assert b'C++' in response_two.data
    assert b'<p>By tia on 13 March 2020 <small>Post Id is 6</small></p>' in response_two.data
    assert b'<h1>Vue Js</h1>' in response_two.data
    assert b'By tia' in response_two.data
