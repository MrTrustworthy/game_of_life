__author__ = 'MrTrustworthy'

from gol.gameobject import GameObject
from uuid import UUID
import unittest
from gol.x_utils import Position


class TestGameObject(unittest.TestCase):
    def test_init(self):
        with self.assertRaises(TypeError):
            GameObject()

        with self.assertRaises(TypeError):
            GameObject(1, 2)

        g = GameObject((8, 9))

        self.assertTrue(isinstance(g.id, UUID), "ID is not a uuid")
        self.assertTrue(isinstance(g.position, Position), "Position is not a Position-Object")
        self.assertTrue(g.position.x == 8 and g.position.y == 9, "Position is setup wrong")
