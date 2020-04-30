import unittest
import helpers


# class FiltersTestCase(unittest.TestCase):

#     def test_filter_number(self):
#         request = "money___gte=20&money__lte=200"
#         filters = helpers.filters(request)
#         expected = {
#             'money': {"$gte": 20, "$lte": 200}
#         }
#         self.assertDictEqual(expected, filters)