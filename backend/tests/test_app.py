def test_home():
    from app import app
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.json == {"message": "Welcome to Career Craft API!"}
