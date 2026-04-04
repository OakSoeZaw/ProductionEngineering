import csv
from peewee import chunked
from app.database import db
from io import StringIO

from app.models.product import Product

def load_csv(filepath):
    with open(filepath, newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    with db.atomic():
        for batch in chunked(rows, 100):
            Product.insert_many(batch).execute()

def import_users_from_file(file_stream: IO) -> int:
    file_content = file_stream.read().decode('utf-8')

    csv_file = StringIO(file_content)

    reader = csv.DictReader(csv_file)
    count = 0
    for row in reader:
        count = count + 1
    return count