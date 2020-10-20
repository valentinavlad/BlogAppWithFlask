def test_setup_is_not_config(client_is_not_config):
    response = client_is_not_config.get('/setup', follow_redirects=True)
    assert response.status_code == 200
    assert '<h1>Your database is not configured</h1>' in response.get_data(as_text=True)
    assert b'Database name' in response.data
    assert b'User' in response.data
    assert b'Password' in response.data

def test_setup_is_config(client_is_config):
    response = client_is_config.get('/setup', follow_redirects=True)
    assert response.status_code == 200
    assert '<h1>Angular</h1>' in response.get_data(as_text=True)
    assert '<h1>Php</h1>' in response.get_data(as_text=True)
    assert b'Check our latest posts in web technologies!' in response.data
