import csv
from peewee import chunked
from app.database import db
from io import StringIO
from typing import IO

from app.models.product import Product
from app.models.user import User


def import_users_from_file(file_stream: IO) -> int:
    row = parse_csv_rows(file_stream)
    count = len(row)
    
    with db.atomic():
        for batch in chunked(row, 100):
            User.insert_many(batch).execute()
    return count

def parse_csv_rows(file_stream: IO) -> list:
    file_content = file_stream.read().decode('utf-8')
    csv_file = StringIO(file_content)
    reader = csv.DictReader(csv_file)

    return list(reader)