import sys
from pathlib import Path
import pytest


project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from app.models.user import User

def test_post_url_valid(client, db):
    user = User.create(username="alice", email="alice@example.com")
    
    response = client.post("/urls", json={
        "user_id": user.id,
        "original_url": "https://example.com",
        "title": "Test URL"
    })
    
    assert response.status_code == 201
    data = response.get_json()
    assert data["original_url"] == "https://example.com"
    assert data["user_id"] == user.id