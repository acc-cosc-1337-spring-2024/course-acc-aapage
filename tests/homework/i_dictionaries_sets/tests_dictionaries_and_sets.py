import unittest

from src.homework.i_dictionaries_sets.dictionary import *
from src.homework.i_dictionaries_sets.sets import *

class Test_Config(unittest.TestCase):

    #dictionaries
    def test_add_inventory_1(self):
        add_inventory(dictionary, "Widget1", 10)
        self.assertEqual(dictionary, {"Widget1":10})

    def test_add_inventory_2(self):
        add_inventory(dictionary, "Widget1", 25)
        self.assertEqual(dictionary, {"Widget1":35})

    def test_add_inventory_3(self):
        add_inventory(dictionary, "Widget1", -10)
        self.assertEqual(dictionary, {"Widget1": 25})

    def test_remove_inventory(self):
        add_inventory(dictionary, "Widget2", 11)
        remove_inventory_widget(dictionary, "Widget1")
        self.assertEqual(len(dictionary), 1)
        self.assertEqual(dictionary, {"Widget2": 11})
        remove_inventory_widget(dictionary, "Widget2")
        

    #sets
    def test_get_students_who_took_prog1_and_prog2(self):
        self.assertEqual(get_students_who_took_prog1_and_prog2(prog1, prog2), {"Student3"})

    def test_get_students_who_took_prog1_or_prog2(self):
        self.assertEqual(get_students_who_took_prog1_or_prog2(prog1, prog2), {"Student1", "Student2", "Student3", "Student4", "Student5"})

    def test_get_students_who_took_prog1_not_prog_2(self):
        self.assertEqual(get_students_who_took_prog1_not_prog_2(prog1, prog2), {"Student1", "Student2"})
    
    def test_get_students_who_took_prog2_not_prog_1(self):
        self.assertEqual(get_students_who_took_prog2_not_prog_1(prog1, prog2), {"Student4", "Student5"})