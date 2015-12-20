__author__ = 'MrTrustworthy'

from gol.x_utils import Position
from typing import List, Union


class Field:
    def __init__(self, position: Position, passable: bool, passing_cost: Union[int, None], objects):
        self.passable = passable
        self.passing_cost = passing_cost if passable else None

        if not isinstance(position, Position):
            raise ValueError("position must be a Position-object")
        if not isinstance(objects, list):
            raise ValueError("Objects must be a list")

        self.objects = objects if isinstance(objects, list) else [objects]
        self.position = position


class Grid:
    def __init__(self, fields: List[List[Field]]) -> None:
        self.fields = fields

    def get(self, *args: List[Union[Position, tuple, int]]) -> Field:
        """
        Returns a given field based on a X-Y value or tuple
        :return:
        """

        if len(args) == 1:
            if isinstance(args[0], Position):
                x, y = args[0].tuple
            else:
                x, y = args[0]
        else:
            x, y = (args[0], args[1])
        return self.fields[x][y]

    def get_path(self, pos_a: Position, pos_b: Position) -> List[Field]:
        """
        Calculates a passable path between the two given positions
        :param pos_a:
        :param pos_b:
        :return:
        """

        class Node:
            def __init__(self, node, cost, expected, parent):
                self.node = node
                 # same position reference that Field-Object has
                self.pos = node.position
                self.cost = cost
                self.expected = expected
                self.total = self.cost + self.expected
                self.parent = parent

            def __eq__(self, other):
                return self.pos == other.pos

        current_field = Node(self.get(pos_a.tuple), 0, pos_a.distance_to(pos_b), None)
        path = [current_field]
        already_checked = []

        while current_field.pos != pos_b:

            valid_neighbours = filter(
                lambda x: x.passable,
                self._get_neighbours(current_field.pos)
            )

            for field in valid_neighbours:

                # calculate the values of each field
                cost = current_field.pos.distance_to(field.position)

                h = field.position.distance_to(pos_b)

                node = Node(field, cost, h, current_field)

                # dont want duplicates
                if node not in path and node not in already_checked:
                    already_checked.append(node)

            already_checked.sort(key=lambda x: x.total)
            current_field = already_checked[0]
            already_checked.remove(current_field)
            path.append(current_field)

        ordered_path = []
        while current_field is not None:
            ordered_path.append(current_field.node)
            current_field = current_field.parent
        ordered_path.reverse()
        return ordered_path

    def _get_neighbours(self, position: Position) -> List[Field]:
        """
        Calculates and returns a list of all Fields right next to the given position
        :param position:
        :return: List(Field) List of neighbouring fields
        """
        x, y = (position.x, position.y)
        neighbours = []
        for i in [x - 1, x, x + 1]:
            for j in [y - 1, y, y + 1]:
                if i < 0 or j < 0:
                    continue
                if i == x and j == y:
                    continue
                else:
                    neighbours.append(self.get(i, j))
        return neighbours
