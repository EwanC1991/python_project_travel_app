import unittest
from models.sights import Sight

class TestSight(unittest.TestCase):
    def setUp(self):
        self.sight_1 =  Sight("Nou Camp", "Barcelona", True)
        self.sight_2 = Sight("Bernabeu Stadium", "Madrid")

    def test_sight_has_name(self):
        self.assertEqual("Nou Camp", self.sight_1.name)

    def test_sight_has_a_city(self):
        self.assertEqual("Barcelona", self.sight_1.city)

    def test_sight_has_True_visited(self):
        self.assertEqual(True, self.sight_1.visited)

    def test_sight_has_False_visited(self):
        self.assertEqual(False, self.sight_2.visited)
    
    def test_sight_has_id(self):
        self.assertEqual(None, self.sight_1.id)
