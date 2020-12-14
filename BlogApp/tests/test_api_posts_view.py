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

