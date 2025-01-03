from tests.utils.blog import create_random_blog

def test_get_blog(client, db_session):
    blog = create_random_blog(db=db_session)
    response = client.get(f"blog/{blog.id}/")
    assert response.status_code == 200
    assert response.json()['title'] == blog.title