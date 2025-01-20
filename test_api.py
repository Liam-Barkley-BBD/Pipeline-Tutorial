import pytest
from api import app

# Create test client
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Test the /date endpoint
def test_get_date(client):

    # Check for successful response and format
    response = client.get('/date')
    assert response.status_code == 200

    json_data = response.get_json()
    assert 'date' in json_data
