__author__ = 'MrTrustworthy'

from gol.grid import Field, Grid
import unittest
from gol.gameobject import GameObject
from gol.x_utils import Position


class TestGrid(unittest.TestCase):
    def test_field(self):
        g = GameObject((1, 2))

        f = Field(Position(1, 2), True, 2, [])
        self.assertTrue(f.passable, "Field should be passable")
        self.assertTrue(f.passing_cost == 2, "Field movement cost should be 2")
        self.assertTrue(len(f.objects) == 0, "Field should contain no objects")
        self.assertTrue(isinstance(f.position, Position), "Field has no Position")

        f2 = Field(Position(3, 4), False, 100, [g])
        self.assertTrue(not f2.passable, "Field should notbe passable")
        self.assertTrue(f2.passing_cost is None, "Field movement cost should be NONE if not passable")
        self.assertTrue(len(f2.objects) == 1, "Field should contain an objects")
        self.assertTrue(f2.objects[0] is g, "Field contains the wrong object")
        self.assertTrue(isinstance(f2.position, Position), "Field has no Position")

        with self.assertRaises(ValueError):
            Field(Position(0, 0), False, 100, g)

    def test_grid(self):
        fields = [list([Field(Position(i, s), True, 1, []) for s in range(20)]) for i in range(20)]
        self.assertTrue(isinstance(fields, list) and isinstance(fields[0], list), "Something went wrong with lists")
        g = Grid(fields)

        # make sure the index-values of the fields match their position
        for i, field_list in enumerate(g.fields):
            for j, field in enumerate(field_list):
                self.assertEqual(field.position, Position(i, j))

        return g

    def test_get(self):
        g = self.test_grid()

        f = g.get(3, 6)
        self.assertTrue(f is g.fields[3][6], "Grid.GET returns wrong values")
        self.assertTrue(f.position == Position(3, 6), "Grid.GET returns wrong values")

        f = g.get((4, 5))
        self.assertTrue(f is g.fields[4][5], "Grid.GET returns wrong values")
        self.assertTrue(f.position == Position(4, 5), "Grid.GET returns wrong values")

        f = g.get(Position(4, 5))
        self.assertTrue(f is g.fields[4][5], "Grid.GET returns wrong values")
        self.assertTrue(f.position == Position(4, 5), "Grid.GET returns wrong values")

    def test_neighbours(self):
        g = self.test_grid()

        n1 = g._get_neighbours(Position(0, 0))
        self.assertTrue(len(n1) == 3, "Calculating neighbours failed")
        self.assertTrue(g.get(0, 1) in n1, "Calculating neighbours failed")
        self.assertTrue(g.get(1, 1) in n1, "Calculating neighbours failed")
        self.assertTrue(g.get(1, 0) in n1, "Calculating neighbours failed")

    def test_neighbours2(self):
        g = self.test_grid()
        n2 = g._get_neighbours(Position(7, 7))
        self.assertTrue(len(n2) == 8, "Calculating neighbours failed")
        self.assertTrue(g.get(6, 6) in n2, "Calculating neighbours failed")
        self.assertTrue(g.get(6, 7) in n2, "Calculating neighbours failed")
        self.assertTrue(g.get(6, 8) in n2, "Calculating neighbours failed")
        self.assertTrue(g.get(7, 6) in n2, "Calculating neighbours failed")
        self.assertTrue(g.get(7, 8) in n2, "Calculating neighbours failed")
        self.assertTrue(g.get(8, 6) in n2, "Calculating neighbours failed")
        self.assertTrue(g.get(8, 7) in n2, "Calculating neighbours failed")
        self.assertTrue(g.get(8, 8) in n2, "Calculating neighbours failed")

    def test_pathfinding(self):
        g = self.test_grid()
        path = g.get_path(Position(0, 0), Position(10, 0))

        self.assertTrue(path[0].position == Position(0, 0), "Pathfinding error")
        self.assertTrue(path[1].position == Position(1, 0), "Pathfinding error")
        self.assertTrue(path[2].position == Position(2, 0), "Pathfinding error")
        self.assertTrue(path[3].position == Position(3, 0), "Pathfinding error")
        self.assertTrue(path[4].position == Position(4, 0), "Pathfinding error")
        self.assertTrue(path[5].position == Position(5, 0), "Pathfinding error")
        self.assertTrue(path[6].position == Position(6, 0), "Pathfinding error")
        self.assertTrue(path[7].position == Position(7, 0), "Pathfinding error")
        self.assertTrue(path[8].position == Position(8, 0), "Pathfinding error")
        self.assertTrue(path[9].position == Position(9, 0), "Pathfinding error")
        self.assertTrue(path[10].position == Position(10, 0), "Pathfinding error")

    def test_pathfinding2(self):
        g = self.test_grid()
        path = g.get_path(Position(0, 0), Position(10, 10))
        self.assertTrue(path[0].position == Position(0, 0), "Pathfinding error")
        self.assertTrue(path[1].position == Position(1, 1), "Pathfinding error")
        self.assertTrue(path[2].position == Position(2, 2), "Pathfinding error")
        self.assertTrue(path[3].position == Position(3, 3), "Pathfinding error")
        self.assertTrue(path[4].position == Position(4, 4), "Pathfinding error")
        self.assertTrue(path[5].position == Position(5, 5), "Pathfinding error")
        self.assertTrue(path[6].position == Position(6, 6), "Pathfinding error")
        self.assertTrue(path[7].position == Position(7, 7), "Pathfinding error")
        self.assertTrue(path[8].position == Position(8, 8), "Pathfinding error")
        self.assertTrue(path[9].position == Position(9, 9), "Pathfinding error")
        self.assertTrue(path[10].position == Position(10, 10), "Pathfinding error")

    def test_pathfinding3(self):
        g = self.test_grid()
        path = g.get_path(Position(0, 0), Position(1, 2))
        self.assertTrue(path[0].position == Position(0, 0), "Pathfinding error")
        self.assertTrue(path[1].position == Position(1, 1) or path[1].position == Position(0, 1), "Pathfinding error")
        self.assertTrue(path[2].position == Position(1, 2), "Pathfinding error")

    def test_pathfinding4(self):
        g = self.test_grid()
        g.get(Position(0, 1)).passable = False
        path = g.get_path(Position(0, 0), Position(0, 2))
        self.assertTrue(path[0].position == Position(0, 0), "Pathfinding error")
        self.assertTrue(path[1].position == Position(1, 1), "Pathfinding error")
        self.assertTrue(path[2].position == Position(0, 2), "Pathfinding error")
