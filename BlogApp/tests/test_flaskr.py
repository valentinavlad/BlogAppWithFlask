def test_index(app_test, client):
    res = client.get('/')
    assert res.status_code == 200
    assert '<title>Blog posts</title>' in res.get_data(as_text=True)

def test_view_post(app_test, client):
    res = client.get('/posts/1')
    assert res.status_code == 200
