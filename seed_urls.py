import csv
import json
from dotenv import load_dotenv
from app import create_app

from app.models.url import Url
from app.models.event import Event

load_dotenv()
app = create_app()

with app.app_context():
    with open("data/events.csv", "r") as f:
        reader = csv.DictReader(f)
        rows = []
        for row in reader:
            row["details"] = json.loads(row["details"])
            rows.append(row)
        Event.insert_many(rows).execute()
        print(f"Inserted {len(rows)} events")