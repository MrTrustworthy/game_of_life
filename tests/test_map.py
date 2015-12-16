__author__ = 'MrTrustworthy'

import unittest
from gol.map import Map
from gol.gameobject import GameObject
from gol.grid import Grid, Field


class TestMap(unittest.TestCase):
    def setUp(self):
        pass

    def test_init(self):
        with self.assertRaises(ValueError):
            Map()

        m = Map((200, 100))
        self.assertTrue(m.size_x == 200)
        self.assertTrue(m.size_y == 100)
        self.assertTrue(isinstance(m.objects, list))

        m = Map(200, 100)
        self.assertTrue(m.size_x == 200)
        self.assertTrue(m.size_y == 100)
        self.assertTrue(isinstance(m.objects, list))

    def test_objects(self):
        m = Map(200, 200)
        g = GameObject((1, 2))

        m.objects.append(g)
        self.assertTrue(len(m.objects) == 1 and m.objects[0] is g)

        m.objects.remove(g)
        self.assertTrue(len(m.objects) == 0)

    def test_splitting(self):
        m = Map(200, 150)

        # the sub-function first
        fields = m._split(5)

        # self.assertTrue(isinstance(fields, list) and isinstance(fields[0], list), "Should have a list of lists")

        # g = m.get_grid(5)
        # self.assertTrue(isinstance(g, Grid))
        # for field in g.fields:
        #     self.assertTrue(isinstance(field, Field))
