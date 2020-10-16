def test_login(client_is_config):
    response = client_is_config.get('/auth/login')
    assert response.status_code == 200
    assert b'Name' in response.data
    assert b'Email' in response.data    
    assert b'Password' in response.data
    data = {'name': 'tia', 'email':'tia@gmail.com', 'password':'123'}

    response_post = client_is_config.post('/auth/login', data=data, follow_redirects=True)
    assert response_post.status_code == 200
    assert b'Check our latest posts in web technologies!' in response_post.data
