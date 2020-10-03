
def test_index(client):
    res = client.get('/')
    assert res.status_code == 200
    assert '<h2>Check our latest posts in web technologies!</h2>' in res.get_data(as_text=True)
    assert '<h1>Angular</h1>' in res.get_data(as_text=True)

def test_view_post(client):
    res = client.get('/posts/5')
    assert '<h3>Angular</h3>' in res.get_data(as_text=True)
    assert res.status_code == 200

def test_all_posts(client):
    res = client.get('/posts')
    assert res.status_code == 308

def test_post_create(client):
    content_header = {'Content-Type': 'text/html'}
    data = {'title': 'test-file', 'contents':'hello'}
    r = client.post('/posts/new', headers=content_header, json=data)
    assert r.status_code == 302
