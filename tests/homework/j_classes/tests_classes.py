import unittest

from src.homework.j_classes.class_a import *

class TestConfig(unittest.TestCase):
    values = [1,2,3,4,5,6]

    def test_roll_1(self):
        die1 = Die()
        die1.roll()
        self.assertIn(die1.get_rolled_value(), self.values)

    def test_roll_2(self):
        die2 = Die()
        die2.roll()
        self.assertIn(die2.get_rolled_value(), self.values)

    def test_roll_3(self):
        die3 = Die()
        die3.roll()
        self.assertIn(die3.get_rolled_value(), self.values)
        