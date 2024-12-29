import json
from fastapi import FastAPI

def test_create_user(client):
    data = {'email': 'testuser@goofbar.com', 'password': 'test_password'}
    assert type(client.app) is FastAPI
    response = client.post("/", json=data)
    assert response.status_code == 201
    assert response.json()['email'] == data['email']
    assert response.json()['is_active'] == True