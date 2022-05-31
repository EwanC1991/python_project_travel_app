import unittest
from models.continent import Continent

class TestContinent(unittest.TestCase):
    def setUp(self):
        self.continent_1 =  Continent("Europe")

    def test_continent_has_name(self):
        self.assertEqual("Europe", self.continent_1.name)
