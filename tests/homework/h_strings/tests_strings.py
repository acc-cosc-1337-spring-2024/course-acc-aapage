import unittest
from src.homework.h_strings.strings import get_dna_compliment, get_hamming_distance

class Test_Config(unittest.TestCase):

    def test_get_hamming_distance1(self):
        self.assertEqual(get_hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT"), 7)

    def test_get_dna_compliment(self):
        self.assertEqual(get_dna_compliment("AAAACCCGGT"), "ACCGGGTTTT")