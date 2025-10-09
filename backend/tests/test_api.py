from fastapi import status
from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_healthz():
    r = client.get("/healthz")
    assert r.status_code == status.HTTP_200_OK
    assert r.json()["status"] == "ok"

def test_todos_flow():
    r = client.get("/api/todos"); assert r.status_code == 200; assert r.json() == []
    r = client.post("/api/todos", json={"title": "first"}); assert r.status_code == 201
    r = client.get("/api/todos"); assert r.status_code == 200; assert len(r.json()) == 1

def test_root_ok():
    r = client.get("/")
    assert r.status_code == 200
    j = r.json()
    assert j["status"] == "ok"

def test_readyz_ok():
    r = client.get("/readyz")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"
