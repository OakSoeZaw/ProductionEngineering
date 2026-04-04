from peewee import CharField,BooleanField, DateTimeField, AutoField, ForeignKeyField
from datetime import datetime

from app.database import BaseModel
from app.models.user import User

class Url(BaseModel):
    id = AutoField()
    user = ForeignKeyField(User, backref="urls")
    short_code = CharField()
    original_url = CharField()
    title = CharField()
    is_active = BooleanField()
    created_at = DateTimeField(default = datetime.now)
    updated_at = DateTimeField(default = datetime.now)