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

def test_show_statistics_logged_user(client_is_config):
    log = login(client_is_config, 'tia', '123')

    res = client_is_config.get('/statistics/')
    assert res.status_code == 200
    assert b'In March 2020 you had 1 posts' in res.data
    assert b'<h5>In January 2018 you had 1 posts</h5>' in res.data
    assert b'<h5>In December 2017 you had 1 posts</h5>' in res.data
    assert b'Newer posts' not in res.data
    assert b'Older posts' not in res.data

def test_statistcs_route_logged_out_user(client_is_config):
    response = client_is_config.get('/statistics', follow_redirects=True)
    assert response.status_code == 200
    assert b'Password' in response.data
    assert b'Login' in response.data
