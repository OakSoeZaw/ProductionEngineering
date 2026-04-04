from peewee import PostgresqlDatabase
from app.database import db

#add the model you want to create a table for
# from app.models.user import User for example
# from app.models.user import User
from app.models.url import Url

db.initialize(PostgresqlDatabase("hackathon_db"))
db.connect()
db.drop_tables([Url])
db.create_tables([Url])