import sys
from pathlib import Path
import io
import pytest


project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

def test_post_users_bulk_valid(client):
    csv_data = "username,email\nalice,alice@example.com\nbob,bob@example.com"
    data = {
        "file": (io.BytesIO(csv_data.encode("utf-8")), "users.csv")
    }
    response = client.post("/users/bulk", content_type="multipart/form-data", data=data)

    assert response.status_code == 201
    result = response.get_json()
    assert result["imported"] == 2