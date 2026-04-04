from peewee import CharField, DateTimeField, IntegerField, AutoField
from datetime import datetime

from app.database import BaseModel

class User(BaseModel):
    id = AutoField()
    username = CharField()
    email = CharField()
    created_at = DateTimeField(default = datetime.now)