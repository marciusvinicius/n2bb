from .db import db


#TODO: Better way to filter, maybe using RestFilter
possible_filters = [
    "price",
    "price__gte",
    "price__gt",
    "price__lte",
    "price__lt",
    "points",
    "points__lt",
    "points__lte",
    "points__gt",
    "points__gte",
    "title",
    "title__contains",
    "variety",
    "variety__contains",
    "description",
    "description__contains",
    "country",
    "country__contains",
]


class Wine(db.Document):
    title = db.StringField(required=True, unique=True, index=True)
    description = db.StringField(index=True)
    country = db.StringField(index=True)
    points = db.IntField()
    price = db.DecimalField()
    variety = db.StringField(index=True)