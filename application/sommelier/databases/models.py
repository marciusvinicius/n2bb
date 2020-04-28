from .db import db


class Country(db.Document):
    name = db.StringField(required=True, unique=True)


class Wine(db.Document):
    title = db.StringField(required=True, unique=True)
    description = db.StringField(index=True)
    country = db.ReferenceField(Country)

    points = db.IntField()
    price = db.DecimalField()
    variant = db.StringField(required=False)