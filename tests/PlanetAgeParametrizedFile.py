import unittest
from sample.PlanetAge import *

class FizzBuzzParameterizedFile(unittest.TestCase):

    def test_from_file(self):
      fileTest = open("data/planet_age_data_test")
      tmpPlanetAge = PlanetAge()
      for line in fileTest:
        if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
            continue
        else:
            data = line.split(" ")
            planet, seconds, result = data[0], int(data[1]), float(data[2].strip("\n"))
            self.assertEqual(tmpPlanetAge.calculate_age(planet, seconds), result)
      fileTest.close()


if __name__ == '__main__':
    unittest.main()