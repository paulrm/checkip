import pytest
from fastapi.testclient import TestClient
from checkip import app

client = TestClient(app)

def test_browser_request():
    headers = {"User-Agent": "Mozilla/5.0"}
    response = client.get("/", headers=headers)
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert "ip" in response.json()
    assert response.json()["ip"] == "testclient"  # Adjusted for test environment

def test_curl_request():
    headers = {"User-Agent": "curl/7.68.0"}
    response = client.get("/", headers=headers)
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/plain; charset=utf-8"
    assert response.text.strip() == "testclient"  # Adjusted for test environment

