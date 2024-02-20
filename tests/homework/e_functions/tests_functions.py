import unittest
from src.homework.e_functions.value_return import get_hour, get_minutes, get_seconds

class Test_Config(unittest.TestCase):

    #testing get_hour
    def test_get_hour_1(self):
        self.assertEqual(get_hour(3800), 1) #3800
    def test_get_hour_2(self):
        self.assertEqual(get_hour(3600), 1) #3600

    #testing get_minutes
    def test_get_minutes_1(self):
        self.assertEqual(get_minutes(3800), 3) #3800
    def test_get_minutes_2(self):
        self.assertEqual(get_minutes(3600), 0) #3600

    #testing get_seconds
    def test_get_seconds_1(self):
        self.assertEqual(get_seconds(3800), 20) #3800
    def test_get_seconds_2(self):
        self.assertEqual(get_seconds(3600), 0) #3600