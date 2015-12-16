__author__ = 'MrTrustworthy'


from gol.stat import Stat
from gol.x_utils import Position
from gol.gameobject import GameObject


class Person(GameObject):
    def __init__(self, position, age, gender, level):

        if not isinstance(position, tuple):
            raise TypeError("Person constructor needs Tuple as Position-Argument")

        super().__init__(position)

        self.age = age
        self.gender = gender
        self.level = level
        self.experience = Stat(0, 100, 0)

        base_values = level * 10

        self.health = Stat(base_values)
        self.stamina = Stat(base_values)
        self.satiation = Stat(base_values)
        self.hydration = Stat(base_values)


