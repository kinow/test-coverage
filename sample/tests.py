import unittest

from sample.app import App


class TestCase(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(3, App.sum(1, 2))

    def test_str(self):
        self.assertEquals("App", str(App()))
