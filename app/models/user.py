from peewee import CharField, DateTimeField, IntegerField

from app.database import BaseModel

class User(BaseModel):
    id = IntegerField()
    username = CharField()
    email = CharField()
    created_at = DateTimeField()