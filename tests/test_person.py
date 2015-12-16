__author__ = 'MrTrustworthy'

import unittest
from gol.person import Person
from gol.stat import Stat
from gol.x_utils import Position, Gender
import uuid


class TestPerson(unittest.TestCase):

    def setUp(self):
        self.person = Person((1, 3), 2, Gender.MALE, 1)

    def test_init(self):

        with self.assertRaises(TypeError):
            Person()

        with self.assertRaises(TypeError):
            Person(1, 3, 2, Gender.MALE, 1)

        self.assertTrue(isinstance(self.person.id, uuid.UUID), "ID is not a uuid")
        self.assertTrue(isinstance(self.person.gender, Gender), "Gender is not valid!" + str(self.person.gender))
        self.assertTrue(isinstance(self.person.age, int), "Age not an int")
        self.assertTrue(isinstance(self.person.level, int), "Level not an int")

        self.assertTrue(isinstance(self.person.position, Position), "Position is not a Position-Object")
        self.assertTrue(self.person.position.x == 1 and self.person.position.y == 3, "Position init went wrong")

        self.assertTrue(isinstance(self.person.experience, Stat), "experience is not a stat")
        self.assertTrue(self.person.experience.val == 0, "experience is wrong initialized")

        self.assertTrue(isinstance(self.person.health, Stat), "Health is not a stat")
        self.assertTrue(self.person.health.val == self.person.level*10, "Health is wrong initialized")

        self.assertTrue(isinstance(self.person.stamina, Stat), "Stamina is not a stat")
        self.assertTrue(self.person.stamina.val == self.person.level*10, "Stamina is wrong initialized")

        self.assertTrue(isinstance(self.person.satiation, Stat), "Satiation is not a stat")
        self.assertTrue(self.person.satiation.val == self.person.level*10, "Satiation is wrong initialized")

        self.assertTrue(isinstance(self.person.hydration, Stat), "Hydration is not a stat")
        self.assertTrue(self.person.hydration.val == self.person.level*10, "Hydration is wrong initialized")

