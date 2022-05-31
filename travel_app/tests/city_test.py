import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def setUp(self):
        self.city_1 =  City("Seville", "Spain", False)
        self.city_2 = City("Paris", "France", True)

    def test_city_has_name(self):
        self.assertEqual("Seville", self.city_1.name)

    def test_city_has_a_country(self):
        self.assertEqual("Spain", self.city_1.country)

    def test_city_has_False_visited(self):
        self.assertEqual(False, self.city_1.visited)

    def test_city_has_True_visited(self):
        self.assertEqual(True, self.city_2.visited)
    
    def test_city_has_id(self):
        self.assertEqual(None, self.city_1.id)
