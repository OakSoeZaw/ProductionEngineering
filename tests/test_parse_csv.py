
import io
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from app.services.csv_import import parse_csv_rows


def test_parse_csv_rows_valid():
    csv_data = "username,email\nalice,alice@example.com\nbob,bob@example.com"
    file_stream = io.BytesIO(csv_data.encode("utf-8"))

    row = parse_csv_rows(file_stream)

    assert len(row) == 2
    assert set(row[0].keys()) == {"username", "email"}

def test_parse_csv_rows_empty():
    csv_data = ""
    file_stream = io.BytesIO(csv_data.encode("utf-8"))

    row = parse_csv_rows(file_stream)

    assert len(row) == 0

def test_parse_csv_rows_invalid():
    csv_data = "username,email,age\nalice,alice@example.com,32\nbob,bob@example.com,40"
    file_stream = io.BytesIO(csv_data.encode("utf-8"))

    row = parse_csv_rows(file_stream)

    assert len(row) == 2
    assert "age" in row[0]
    
