import unittest
from models.country import Country

class TestCountry(unittest.TestCase):
    def setUp(self):
        self.country_1 =  Country("Spain", "Europe", False)
        self.country_2 = Country("France", "Europe", True)

    def test_country_has_name(self):
        self.assertEqual("Spain", self.country_1.name)

    def test_country_has_a_continent(self):
        self.assertEqual("Europe", self.country_1.continent)

    def test_country_has_False_visited(self):
        self.assertEqual(False, self.country_1.visited)

    def test_country_has_True_visited(self):
        self.assertEqual(True, self.country_2.visited)
    
    def test_country_has_id(self):
        self.assertEqual(None, self.country_1.id)