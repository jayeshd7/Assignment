

from starlette.testclient import TestClient
from h11 import Response


from .db.models import UserDetails
from .main import app, create_new_user


async def mock_create_user():
    user_details=UserDetails(user_id =1, user_name = 'Jayesh', address = 'pune', email = 'jayesh@gmail.com')
    response = Response(status=True, data=user_details)
    return response

# using dependency overrides to mock the function get_user_name
app.dependency_overrides[create_new_user] = mock_create_user

client = TestClient(app)


def test_read_root():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Fast API in Python'}




def test_create_user():
    response = client.post(
        "/user",
        headers={"X-Token": "coneofsilence"},
        json={
    "user_id": 1,
    "user_name": "Jayesh",
    "address": "pune",
    "email": "jayesh@gmail.com"
  },
    )
    assert response.status_code == 201

def test_get_user():
    response = client.get('/user/2')
    assert response.status_code == 200
    assert len(response.json()) != 0

def test_get_user_not_exist():
    response = client.get('/user/3')
    assert response.status_code == 404


