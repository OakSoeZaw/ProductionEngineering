from peewee import PostgresqlDatabase
from app.database import db

#add the model you want to create a table for
# from app.models.user import User for example
from app.models.user import User

db.initialize(PostgresqlDatabase("hackathon_db"))
db.connect()
db.drop_tables([User])
db.create_tables([User])