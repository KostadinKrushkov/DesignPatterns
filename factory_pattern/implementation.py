import random


class SodaProduct:  # Base product
    size = None

    def __init__(self, size):
        self.size = size

    def __repr__(self):
        result = ""
        result += str(self.__class__) + "\n"
        for x in dir(self):
            if not x.startswith('__'):
                result += "{} - {}\n".format(x, getattr(self, x))
        return result


class FantaProduct(SodaProduct):  # Concrete product
    taste = None

    def __init__(self, size, taste):
        SodaProduct.__init__(self, size)
        self.taste = taste


class ColaProduct(SodaProduct):
    bottle = None

    def __init__(self, size, bottle):
        SodaProduct.__init__(self, size)
        self.bottle = bottle


class SodaFactory:  # Base creator - factory
    def create_soda(self, age):
        if age < 12:
            size = 0.3
        elif age >= 12 and age <= 18:
            size = 0.5
        else:
            size = 1

        return SodaProduct(size=size)


class ColaFactory(SodaFactory): # Concrete factory
    season = None

    def __init__(self, season):
        self.season = season

    def create_soda(self, age):
        if age < 18:
            size = 0.5
        else:
            size = 1

        bottle = "glass" if self.season in ['summer', 'spring'] else "plastic"
        return ColaProduct(size, bottle)


class RandomFantaFactor(SodaFactory):
    flavors = ['Tropical', 'Classic', 'Lemon', 'Mango']

    def create_soda(self, age):
        if age < 10:
            size = 0.25
        elif 10 <= age < 18:
            size = 0.5
        else:
            size = 0.75

        flavor_num = random.randint(0, 3)
        return FantaProduct(size, self.flavors[flavor_num])


def get_random_age():
    return random.randint(1, 40)


if __name__ == "__main__":
    soda_factory = SodaFactory()
    soda = soda_factory.create_soda(get_random_age())
    print(soda)

    fanta_factory = RandomFantaFactor()
    fanta = fanta_factory.create_soda(get_random_age())
    print(fanta)

    cola_factory = ColaFactory('spring')
    cola = cola_factory.create_soda(get_random_age())
    print(cola)