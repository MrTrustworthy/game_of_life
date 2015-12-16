__author__ = 'MrTrustworthy'

import unittest

from gol.stat import Stat


class TestStats(unittest.TestCase):
    def test_stat_init(self):
        s = Stat(0, 50, 40)
        self.assertTrue(s.min == 0)
        self.assertTrue(s.max == 50)
        self.assertTrue(s.val == 40)

    def test_stat_init_2(self):
        s = Stat(0, 50)
        self.assertTrue(s.min == 0)
        self.assertTrue(s.max == 50)
        self.assertTrue(s.val == 50)

    def test_stat_init_3(self):
        s = Stat(50)
        self.assertTrue(s.min == 0)
        self.assertTrue(s.max == 50)
        self.assertTrue(s.val == 50)

    def test_stat_sub(self):
        s = Stat(50)
        s.sub(10)
        self.assertTrue(s.min == 0)
        self.assertTrue(s.max == 50)
        self.assertTrue(s.val == 40)

    def test_stat_sub_negative(self):
        s = Stat(50)
        s.sub(60)
        self.assertTrue(s.min == 0)
        self.assertTrue(s.max == 50)
        self.assertTrue(s.val == -10)

    def test_stat_sub_negative_2(self):
        s = Stat(50)
        with self.assertRaises(ValueError):
            s.sub(60, strict=True)

    def test_stat_add(self):
        s = Stat(50)
        s.sub(20)
        s.add(15)
        self.assertTrue(s.min == 0)
        self.assertTrue(s.max == 50)
        self.assertTrue(s.val == 45)

    def test_stat_add_over(self):
        s = Stat(50)
        s.add(20)
        self.assertTrue(s.min == 0)
        self.assertTrue(s.max == 50)
        self.assertTrue(s.val == 50)

    def test_stat_add_over2(self):
        s = Stat(50)
        s.add(10, force=True)
        self.assertTrue(s.min == 0)
        self.assertTrue(s.max == 50)
        self.assertTrue(s.val == 60)

    def test_stat_is_below(self):
        s = Stat(50)
        s.sub(70)
        self.assertTrue(s.is_below())
        s.add(20)
        self.assertFalse(s.is_below())
