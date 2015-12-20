__author__ = 'MrTrustworthy'

from enum import Enum
from math import pow, sqrt
from typing import List, Union


class Gender(Enum):
    MALE = 0
    FEMALE = 1


class Position:
    """
    Position is a simple helper object for 2d-positions with an x- and y-value
    """

    def __init__(self, *args: List[Union[int, tuple]]) -> None:
        """
        creates a position object either based on 2 values (x and y) or a (x, y) tuple
        :param args:
        :return:
        """

        if len(args) == 1:
            x, y = args[0]
        elif len(args) == 2:
            x, y = args
        else:
            raise TypeError("Need at least 1 parameter")

        self.x = x
        self.y = y
        self.tuple = (x, y)

    def distance_to(self, other: "Position") -> int:
        """
        calculates the line-of-sight distance between this position and another position
        :param other:
        :return:
        """

        if not other or not isinstance(other, Position):
            raise TypeError("Other value is not position:", other)

        return sqrt(pow(abs(self.x - other.x), 2) + pow(abs(self.y - other.y), 2))

    def in_range(self, other: "Position", distance: float) -> bool:
        """
        returns whether this and another given position are distanced less than the given amount of each other
        :param other:
        :param distance:
        :return:
        """
        if not other or distance is None or not isinstance(other, Position):
            raise TypeError("Position.in_range needs at least 2 arguments")

        return self.distance_to(other) <= distance

    def __eq__(self, other: "Position") -> bool:
        """
        Returns true if both this and the other Position object have the same coordinates
        :param other:
        :return:
        """
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        """
        Gives x,y coords in print statements
        :return:
        """
        return "Position Object: " + "(" + str(self.x) + ":" + str(self.y) + ")"
