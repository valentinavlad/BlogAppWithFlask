def test_index(client):
    res = client.get('/')
    assert res.status_code == 200
    assert '<title>Blog posts</title>' in res.get_data(as_text=True)

def test_view_post(client):
    res = client.get('/posts/5')
    assert '<h3>Angular</h3>' in res.get_data(as_text=True)
    assert res.status_code == 200

def test_all_posts(client):
    res = client.get('/posts')
    assert res.status_code == 308