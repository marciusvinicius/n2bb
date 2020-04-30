import unittest
import json

from app import app
from sommelier.databases.db import db

#TODO: Mock mongodb 
class BasicWineTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.db = db.get_db()

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
