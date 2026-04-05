import sys
from pathlib import Path
import pytest

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from app.services.generateShortCode import generate_random_code

def test_generate_code_valid():
    length = 7
    result = generate_random_code(length)

    assert len(result) == length

def test_generate_code_invalid():
    length = -1
    with pytest.raises(ValueError):
        generate_random_code(length)

def test_generate_code_long_invalid():
    length = 30
    with pytest.raises(ValueError):
        generate_random_code(length)

def test_generate_code_typeInvalid():
    length = "helo"
    with pytest.raises(ValueError):
        generate_random_code(length)