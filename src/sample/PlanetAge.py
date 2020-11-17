class PlanetAge:
    def calculate_age(self, planet, age_in_sec):
        earth_age = 31557600
        planets = {
            "Ziemia": 1,
            "Merkury": 0.2408467,
            "Wenus": 0.61519726,
            "Mars": 1.8808158,
            "Jowisz": 11.862615,
            "Saturn": 29.447498,
            "Uran": 84.016846,
            "Neptun": 164.79132
        }

        if type(age_in_sec) == int and type(planet) == str:
            if planet in planets and age_in_sec > 0:
                age = age_in_sec / planets[planet] / earth_age
                return round(age, 2)
            else:
                raise Exception("Error")
        else:
            raise Exception("Error")



if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={'pAge': PlanetAge()})