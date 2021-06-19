
class BandNameGenerator(object):
    print("Welcome to the Band Name Generator")


    def generate_band_name(self):
        """
        This function generates a band name from 2 user inputs and returns it
        :return:
        band_name(str)
        """
        city_name = input("What's the name of the city you grew up in?: ")
        pet_name = input("What's your pets name?: ")
        band_name = city_name+" "+pet_name
        return band_name

c = BandNameGenerator()
band_name = c.generate_band_name()
print(f"Your band name could be {band_name}")

