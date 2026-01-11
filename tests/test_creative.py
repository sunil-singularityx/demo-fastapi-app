import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_creative_message():
    response = client.get("/creative")
    assert response.status_code == 200
    assert response.json() == {"message": "Code is poetry, written in the language of logic."}
