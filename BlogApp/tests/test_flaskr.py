def test_index(app_test, client):
    res = client.get('/')
    assert res.status_code == 200
    assert '<title>Blog posts</title>' in res.get_data(as_text=True)

def test_view_post(app_test, client):
    res = client.get('/posts/1')
    assert res.status_code == 200

def test_all_posts(app_test,client):
    res = client.get('/posts')
    assert res.status_code == 308

def test_empty_db(db_inmemmory,client):
    """Start with a blank database."""

    rv_client = client.get('/')
    assert b'No entries here so far' in rv_client.data
