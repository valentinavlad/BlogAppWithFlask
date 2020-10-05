def test_index(client):
    response = client.get('/', follow_redirects=True)
    assert response.status_code == 200
    assert '<h1>Angular</h1>' in response.get_data(as_text=True)
    assert '<h1>Php</h1>' in response.get_data(as_text=True)
    assert b'Check our latest posts in web technologies!' in response.data
    assert b'Add a post' in response.data

def test_view_post(client):
    response = client.get('/posts/5')
    assert '<h3>Angular</h3>' in response.get_data(as_text=True)
    assert b'V.W. Craig' in response.data
    assert response.status_code == 200

def test_post_create(client):
    response = client.get('/posts/new')
    assert response.status_code == 200
    assert b'Owner' in response.data
    assert b'Content' in response.data

    data = {'title': 'KOKO', 'contents':'hello'}

    response_post = client.post('/posts/new', data=data, follow_redirects=True)
    assert response_post.status_code == 200
    assert b'Check our latest posts in web technologies!' in response_post.data
    assert 'KOKO' in response_post.get_data(as_text=True)

def test_update_post(client):
    response = client.get('/posts/2')
    assert response.status_code == 200
    assert b'Edit your post' in response.data

    data = {'title': 'updated PHP', 'owner': 'update'}
    response_post = client.post('/posts/2/edit', data=data, follow_redirects=True)
    assert response_post.status_code == 200
    assert b'Edit your post' in response_post.data
    assert 'updated PHP' in response_post.get_data(as_text=True)

def test_delete_post(client):
    #at id 4 is Javascript
    res = client.get('/posts/4')
    assert res.status_code == 200
    assert b'Delete your post' in res.data

    response = client.post('/posts/4/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Javascript' not in response.data
    assert '<h1>Angular</h1>' in response.get_data(as_text=True)
    assert '<h1>Php</h1>' in response.get_data(as_text=True)
        