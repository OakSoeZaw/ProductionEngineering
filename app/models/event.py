from peewee import CharField, DateTimeField, ForeignKeyField, AutoField
from datetime import datetime
from playhouse.postgres_ext import JSONField

from app.database import BaseModel
from app.models.url import Url
from app.models.user import User

class Event(BaseModel):
    id = AutoField()
    url = ForeignKeyField(Url, backref="events")
    user = ForeignKeyField(User, backref="events")
    event_type = CharField()
    timestamp = DateTimeField(default = datetime.now)
    details = JSONField()