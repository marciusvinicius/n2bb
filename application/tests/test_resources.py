import unittest
import json
from app import app
from sommelier.databases.db import db

#TODO: Mock mongodb 
class BasicWineTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.db = db.get_db()
        self.mock_result = json.dumps({
            "count": 2144,
            "current_page": 1,
            "data": [
                {
                    "_id": {
                        "$oid": "5eaae0e1ccb4473f36beb07a"
                    },
                    "country": "US",
                    "description": "This wine from the Geneseo district offers aromas of sour plums and just enough cigar box to tempt the nose. The flavors are a bit flat at first, then the acidity and tension of sour cherries emerges in the midpalate, bolstered by some black licorice.",
                    "points": 87,
                    "price": 22.0,
                    "title": "Bianchi 2011 Signature Selection Merlot (Paso Robles)",
                    "variety": "Merlot"
                },
                {
                    "_id": {
                        "$oid": "5eaae0e1ccb4473f36beb0ba"
                    },
                    "country": "US",
                    "description": "Softened tannins surround a light-bodied, lean and herbal approach to this vineyard-designate, dotted in black pepper, leather and baked cherry.",
                    "points": 86,
                    "price": 55.0,
                    "title": "Passaggio 2014 Blau Vineyards Merlot (Knights Valley)",
                    "variety": "Merlot"
                },
                {
                    "_id": {
                        "$oid": "5eaae0e1ccb4473f36beb10b"
                    },
                    "country": "US",
                    "description": "A fairly elegant expression of the variety, this wine is bright in cherry kirsch and pretty aromas of rose petal and lavender, structured to age and enjoy with food. Rector Creek Vineyard is just north of Yountville and planted in rocky alluvial soils. Drink now through 2022.",
                    "points": 91,
                    "price": 95.0,
                    "title": "Duckhorn 2012 Rector Creek Vineyard Merlot (Napa Valley)",
                    "variety": "Merlot"
                }
            ],
            "next_page": 2,
            "previous_page": None,
            "total_pages": 715
        })

    def test_successful_get_wines(self):
        response = self.app.get(
            '/wines',
            headers={"Content-Type": "application/json"}
        )
        self.assertEqual(200, response.status_code)
        data = json.loads(response.data)
        keys = [
            "previous_page",
            "current_page",
            "next_page",
            "total_pages",
            "data",
            "count"]

        self.assertListEqual(sorted(keys), sorted(list(data.keys())))

    def test_get_with_pagination(self):
        response = self.app.get(
            '/wines?page=1&per_page=1',
            headers={"Content-Type": "application/json"}
        )
        data = json.loads(response.data)
        self.assertEqual(200, response.status_code)
        self.assertEqual(data["current_page"], 1)
        self.assertEqual(len(data["data"]), 1)

    def test_get_with_filters(self):
        response = self.app.get(
            '/wines?page=2&per_page=10&title__contains=Marcius',
            headers={"Content-Type": "application/json"}
        )
        self.assertEqual(404, response.status_code)

    def test_get_with_filters2(self):
        response = self.app.get(
            '/wines?page=2&per_page=10&price__gte=200',
            headers={"Content-Type": "application/json"}
        )
        self.assertEqual(200, response.status_code)


    def tearDown(self):
        pass
        # Delete Database collections after the test is complete
        #for collection in self.db.list_collection_names():
        #    self.db.drop_collection(collection)
