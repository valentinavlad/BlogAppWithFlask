from flask import url_for

def test_index(client):
    res = client.get('/', follow_redirects=True)
    assert res.status_code == 200
    assert '<h1>Angular</h1>' in res.get_data(as_text=True)
    assert '<h1>Php</h1>' in res.get_data(as_text=True)
    assert b'Check our latest posts in web technologies!' in res.data
    assert b'Add a post' in res.data

def test_view_post(client):
    res = client.get('/posts/5')
    assert '<h3>Angular</h3>' in res.get_data(as_text=True)
    assert b'V.W. Craig' in res.data
    assert res.status_code == 200

def test_all_posts(client):
    res = client.get('/posts')
    assert res.status_code == 308

def test_post_create(client):
    res = client.get('/posts/new')
    assert res.status_code == 200
    assert b'Owner' in res.data
    assert b'Content' in res.data

    content_header = {'Content-Type': 'text/html'}
    data = {'title': 'KOKO', 'contents':'hello'}
    with client as c:
        r = client.post('/posts/new',data=data, follow_redirects=True)
        assert r.status_code == 200
        assert b'Check our latest posts in web technologies!' in r.data
        assert 'KOKO' in r.get_data(as_text=True)
  
def test_update_post(client):
    r1 = client.get('/posts/2')
    assert r1.status_code == 200
    assert b'Edit your post' in r1.data
   
    data={'title': 'updated PHP', 'owner': 'update'}
    with client as c:
        r = client.post('/posts/2/edit', data=data, follow_redirects=True)
        assert r.status_code == 200
        assert b'Edit your post' in r.data
        assert 'updated PHP' in r.get_data(as_text=True)
   
def test_delete_post(client):
    r1 = client.get('/posts/4')
    assert r1.status_code == 200
    assert b'Delete post' in r1.data
    with client as c:
        r = client.post('/posts/4', data=data, follow_redirects=True)
        assert r.status_code == 302
        