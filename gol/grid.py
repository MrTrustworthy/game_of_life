__author__ = 'MrTrustworthy'

from gol.x_utils import Position


class Field:
    def __init__(self, position, passable, cost, objects):
        self.passable = passable
        self.cost = cost if passable else None

        if not isinstance(position, Position):
            raise ValueError("position must be a Position-object")
        if not isinstance(objects, list):
            raise ValueError("Objects must be a list")

        self.objects = objects if isinstance(objects, list) else [objects]
        self.position = position


class Grid:
    def __init__(self, fields):
        self.fields = fields

    def get(self, *args):
        """
        Returns a given field based on a X-Y value or tuple
        :return:
        """
        if len(args) == 1:
            x, y = args[0]
        else:
            x, y = (args[0], args[1])
        return self.fields[x][y]

    def get_path(self, pos_a, pos_b):
        """
        Calculates a passable path between the two given positions
        :param pos_a:
        :param pos_b:
        :return:
        """

        class FieldInfo:
            def __init__(self, fld, c, h, parent):
                self.fld = fld
                self.pos = fld.position
                self.c = c
                self.h = h
                self.total = self.c + self.h
                self.parent = parent

            def __eq__(self, other):
                return self.pos == other.pos

        current_field = FieldInfo(self.get(pos_a.tuple), 0, pos_a.distance_to(pos_b), None)
        path = [current_field]
        already_checked = []

        while current_field.pos != pos_b:

            for field in self._get_neighbours(current_field.pos):
                # calculate the values of each field
                cost = current_field.pos.distance_to(field.position)
                h = field.position.distance_to(pos_b)
                fld = FieldInfo(field, cost, h, current_field)

                # dont want duplicates
                if fld not in path and fld not in already_checked:
                    already_checked.append(fld)

            already_checked.sort(key=lambda x: x.total)
            current_field = already_checked[0]
            already_checked.remove(current_field)
            path.append(current_field)

        ordered_path = []
        while current_field is not None:
            ordered_path.append(current_field.fld)
            current_field = current_field.parent
        ordered_path.reverse()
        return ordered_path

    def _get_neighbours(self, position):
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
