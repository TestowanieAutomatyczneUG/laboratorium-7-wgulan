import unittest
from sample.Hamming import *
from parameterized import parameterized, parameterized_class


class HammingParametrizedPackage(unittest.TestCase):

    def setUp(self):
        self.temp = Hamming()

    @parameterized.expand([
        ("", "", 0),
        ("A", "A", 0),
        ("G", "T", 1),
        ("GGACTGAAATCTG", "GGACTGAAATCTG", 0),
        ("GGACGGATTCTG", "AGGACGGATTCT", 9),
    ])
    def test_distance_parametrized(self, gene1, gene2, expected):
        self.assertEqual(self.temp.distance(gene1, gene2), expected)


@parameterized_class(('gene1', 'gene2', 'expected'), [
    ("", "", 0),
    ("A", "A", 0),
    ("G", "T", 1),
    ("GGACTGAAATCTG", "GGACTGAAATCTG", 0),
    ("GGACGGATTCTG", "AGGACGGATTCT", 9),
    ("GGACGGATTCTG", "AAGACGGATTCT", 10),
    ("GACT", "GGA", "Genes have to have same lenghts"),
    (123, "ATT", "Genes have to be strings"),
    (False, 432, "Genes have to be strings"),

])
class HammingParametrizedPackage2(unittest.TestCase):

    def setUp(self):
        self.temp = Hamming()

    def test_distance_parametrized(self):
        self.assertEqual(self.temp.distance(self.gene1, self.gene2), self.expected)


if __name__ == "__main__":
    unittest.main()
