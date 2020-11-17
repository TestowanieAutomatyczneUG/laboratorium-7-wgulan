import unittest
from sample.Hamming import *
from parameterized import parameterized, parameterized_class

class HammingParametrizedPackage(unittest.TestCase):

    def setUp(self):
        self.temp = Hamming()

    @parameterized.expand([
        ("", "",  0),
        ("A", "A", 0),
        ("G", "T", 1),
        ("GGACTGAAATCTG", "GGACTGAAATCTG", 0),
        ("GGACGGATTCTG", "AGGACGGATTCT", 9),
    ])
    def test_distance_parametrized(self, gene1, gene2, expected):
        self.assertEqual(self.temp.distance(gene1, gene2), expected)

if __name__ == "__main__":
    unittest.main()