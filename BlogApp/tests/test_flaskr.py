def test_index(app, client):
    res = client.get('/')
    assert res.status_code == 200
    assert '<title>Blog posts</title>' in res.get_data(as_text=True)

def test_view_post(app, client):
    res = client.get('/posts/5')
    assert res.status_code == 200
