import pytest
import requests
from time import sleep
from Utils.api_client import APIclient


@pytest.fixture(scope='module')
def client():
    return APIclient()


def test_get(client):
    response = client.get('posts/1')
    print(response.status_code, ':', response.text)
    assert response.status_code == 200


def test_post(client, loaduser_data):
    response = client.post('posts', loaduser_data)
    print(response.status_code, ':', response.json())
    assert response.status_code == 201
    id = response.json()['userId']

    get_response = client.get(f'posts/{id}')
    print(get_response.status_code, ';', get_response.text)
    assert get_response.status_code == 200


def test_put(client, loaduser_data):
    userdata = {
        "userId": 3,
        "id": 1,
        "title": "Guntur Karam mahesh",
        "body": "Super star Mahesh Babu Full Mass and Ammo Sentiments, emotional"
    }
    response = client.put('posts/1', userdata)
    print(response.text, ':', response.status_code)
    assert response.status_code == 200 and response.json()['title'] == 'Guntur Karam mahesh'


def test_delete(client):
    response = client.delete('posts/1')
    print(response.status_code,';-->',response.text)
    assert response.status_code == 200
