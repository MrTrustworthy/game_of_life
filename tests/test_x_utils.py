__author__ = 'MrTrustworthy'

import unittest
from gol.x_utils import Gender, Position
from math import sqrt


class TestXUtils(unittest.TestCase):
    def test_gender(self):
        g = Gender(Gender.FEMALE)
        self.assertTrue(isinstance(g, Gender))
        self.assertTrue(g == Gender.FEMALE)
        self.assertFalse(g == Gender.MALE)

    def test_position(self):
        p = Position(20, 35)
        self.assertTrue(p.x == 20 and p.y == 35, "Position init doesn't work")
        self.assertTrue(p.tuple == (20, 35), "Position init doesn't work")

        p = Position(20, 0)
        self.assertTrue(p.x == 20 and p.y == 0, "Position init doesn't work")
        self.assertTrue(p.tuple == (20, 0), "Position init doesn't work")

        p = Position((20, 0))
        self.assertTrue(p.x == 20 and p.y == 0, "Position init doesn't work")
        self.assertTrue(p.tuple == (20, 0), "Position init doesn't work")

        p = Position((20, 35))
        self.assertTrue(p.x == 20 and p.y == 35, "Position init doesn't work")
        self.assertTrue(p.tuple == (20, 35), "Position init doesn't work")

        with self.assertRaises(TypeError):
            p2 = Position()

    def test_position_distance(self):
        p1 = Position(0, 0)
        p2 = Position(10, 0)
        p3 = Position(10, 10)
        self.assertEqual(p1.distance_to(p2), 10, "Position.distance_to not working as expected")
        self.assertEqual(p2.distance_to(p1), 10, "Position.distance_to not working as expected")
        self.assertAlmostEqual(p1.distance_to(p3), sqrt(200), 5, "Position.distance_to not working as expected")

        with self.assertRaises(TypeError):
            p1.distance_to("nothing")

    def test_position_range(self):
        p1 = Position(0, 0)
        p2 = Position(10, 0)
        p3 = Position(10, 10)
        self.assertTrue(p1.in_range(p2, 20), "Position.in_range function not working")
        self.assertTrue(p1.in_range(p2, 10), "Position.in_range function not working")
        self.assertFalse(p1.in_range(p2, 9.9999), "Position.in_range function not working")
        self.assertFalse(p1.in_range(p2, 0), "Position.in_range function not working")
        self.assertTrue(p1.in_range(p3, 14.15), "Position.in_range function not working")
        self.assertFalse(p1.in_range(p3, 14), "Position.in_range function not working")

        with self.assertRaises(TypeError):
            p1.in_range(p2)

    def test_equal(self):
        self.assertEqual(Position(32, 44), Position(32, 44), "Position equality doesn't behave as expected")
