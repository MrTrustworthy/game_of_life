__author__ = 'MrTrustworthy'

import unittest

from gol.mtAntenna import Antenna


class TestAntenna(unittest.TestCase):
    def test_add_listener(self):
        a1 = Antenna()
        test_key = "test_1"

        def callback(one):
            print("test 1 complete")

        a1.add_listener(test_key, callback)
        self.assertTrue(callback in a1.listeners[test_key])

    def test_add_bad_listener(self):
        a1 = Antenna()

        def callback():
            pass

        with self.assertRaises(TypeError):
            a1.add_listener("something", callback)

    def test_dispatch(self):
        a1 = Antenna()
        check_obj = {"checked": False}
        test_key = "test_2"

        def callback(one):
            check_obj["checked"] = True

        a1.add_listener(test_key, callback)
        a1.dispatch_message(test_key, None)

        self.assertTrue(check_obj)

    def test_dispatch_non_existing(self):
        a1 = Antenna()
        with self.assertRaises(KeyError):
            a1.dispatch_message("not_a_valid_key", fail_when_empty=True)
        a1.dispatch_message("also_not_a_valid_key")

    def test_dispatch_multiple(self):
        a1 = Antenna()
        check_obj = {"checked": False}
        test_key = "test_2"

        def callback(one):
            check_obj["checked"] = True

        a1.add_listener(test_key, callback)
        a1.dispatch_message(test_key, None)
        self.assertTrue(check_obj)

        check_obj["checked"] = False
        a1.add_listener(test_key, callback)
        a1.dispatch_message(test_key, None)
        self.assertTrue(check_obj)

    def test_execute_object_check(self):
        a1 = Antenna()
        key = "test_6"
        check_obj = "random_text"
        info = {"some": "thing"}

        def callback(info_obj):
            nonlocal check_obj
            check_obj = info_obj

        a1.add_listener(key, callback)
        a1.dispatch_message(key, info)

        self.assertEqual(check_obj, info)

    def test_remove_listener(self):
        a1 = Antenna()

        def callback(one):
            pass

        key = "test_7"

        a1.add_listener(key, callback)
        self.assertEqual(a1.listeners[key][0], callback)

        a1.remove_listener(key, callback)
        # should delete the whole list object
        self.assertTrue(key not in a1.listeners.keys())

    def test_remove_multiple(self):
        a1 = Antenna()

        def callback(one):
            pass

        def callback2(one):
            pass

        key = "test_7"

        a1.add_listener(key, callback)
        self.assertEqual(a1.listeners[key][0], callback)

        a1.add_listener(key, callback2)
        self.assertEqual(a1.listeners[key][1], callback2)

        a1.remove_listener(key, callback)
        self.assertTrue(callback not in a1.listeners[key])

        a1.remove_listener(key, callback2)
        # should delete the whole list object
        self.assertTrue(key not in a1.listeners.keys())
