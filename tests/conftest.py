import sys
from pathlib import Path
import pytest

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


from app.database import db as database
from app.models.user import User
from app.models.url import Url
from app.models.event import Event
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["Testing"] = True
    with app.test_client() as client:
        yield client

@pytest.fixture(autouse=True, scope="function")
def db():
    app = create_app()
    with app.app_context():
        database.create_tables([User, Url, Event], safe=True)
        database.begin()
        yield database
        database.rollback()


