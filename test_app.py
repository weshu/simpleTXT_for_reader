import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page_get(client):
    """Test that the home page loads correctly."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Simple Text Reader' in response.data

def test_home_page_post(client):
    """Test that the home page handles POST requests correctly."""
    response = client.post('/', data={'new_content': 'Test content'})
    assert response.status_code == 200
    assert b'Test content' in response.data 