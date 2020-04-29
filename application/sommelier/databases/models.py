from .db import db


class Wine(db.Document):
    title = db.StringField(required=True, unique=True)
    description = db.StringField()
    country = db.StringField()
    points = db.IntField()
    price = db.DecimalField()
    variety = db.StringField()