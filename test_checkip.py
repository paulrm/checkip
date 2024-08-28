import pytest
from fastapi.testclient import TestClient
from checkip import app, RATE_LIMIT_SECONDS
import time

client = TestClient(app)

def test_browser_request():
    headers = {"User-Agent": "Mozilla/5.0", "X-Test-Bypass-Rate-Limit": "true"}
    response = client.get("/", headers=headers)
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert "ip" in response.json()
    assert response.json()["ip"] == "testclient"  # Adjusted for test environment

def test_curl_request():
    headers = {"User-Agent": "curl/7.68.0", "X-Test-Bypass-Rate-Limit": "true"}
    response = client.get("/", headers=headers)
    print(response.headers["content-type"])
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    #assert response.text.strip() == "testclient"  # Adjusted for test environment

def test_rate_limiting():
    headers = {"User-Agent": "Mozilla/5.0"}
    response = client.get("/", headers=headers)
    assert response.status_code == 200

    # Immediately make another request
    response = client.get("/", headers=headers)
    assert response.status_code == 429  # Expecting rate limit to be enforced

    # Wait for the rate limit to reset
    time.sleep(RATE_LIMIT_SECONDS)
    response = client.get("/", headers=headers)
    assert response.status_code == 200
