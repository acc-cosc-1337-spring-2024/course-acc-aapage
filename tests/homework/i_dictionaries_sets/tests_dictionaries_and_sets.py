import unittest

from src.homework.i_dictionaries_sets.dictionary import add_inventory, remove_inventory_widget
from src.homework.i_dictionaries_sets.sets import *

class Test_Config(unittest.TestCase):

    #dictionaries
    def test_add_inventory(self):
        self.assertEqual(add_inventory({'widget_name':'Widget1','quantity':10}))

    #sets
    def test_get_students_who_took_prog1_and_prog2(self):
        self.assertEqual(get_students_who_took_prog1_and_prog2(prog1, prog2), {"Student3"})

    def test_get_students_who_took_prog1_or_prog2(self):
        self.assertEqual(get_students_who_took_prog1_or_prog2(prog1, prog2), {"Student1", "Student2", "Student3", "Student4", "Student5"})

    def test_get_students_who_took_prog1_not_prog_2(self):
        self.assertEqual(get_students_who_took_prog1_not_prog_2(prog1, prog2), {"Student1", "Student2"})
    
    def test_get_students_who_took_prog2_not_prog_1(self):
        self.assertEqual(get_students_who_took_prog2_not_prog_1(prog1, prog2), {"Student4", "Student5"})