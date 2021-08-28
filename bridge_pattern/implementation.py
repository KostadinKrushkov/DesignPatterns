from abc import ABCMeta, abstractmethod


class Plane:  # Abstraction
    __metaclass__ = ABCMeta
    carrier = None

    def __init__(self, Carrier):
        self.carrier = Carrier()

    @abstractmethod
    def show(self):
        raise NotImplemented()


class CommercialPlane(Plane):  # ConcreteAbstraction
    load = None

    def __init__(self, Carrier, load):
        super().__init__(Carrier)
        self.load = load

    def show(self):
        print(self.carrier.carry_commerical(self.load))


class MilitaryPlane(Plane):  # ConcreteAbstraction
    load = None

    def __init__(self, Carrier, load):
        super().__init__(Carrier)
        self.load = load

    def show(self):
        print(self.carrier.carry_military(self.load))


class Carrier:  # Abstract Implementor / Resource
    def carry_military(self, items):
        pass

    def carry_commerical(self, items):
        pass


class CargoCarrier(Carrier):  # Concrete Implementor / Resource
    def carry_military(self, items):
        return "The plane is carrying {} military items.".format(items)

    def carry_commerical(self, items):
        return "The plane is carrying {} commercial goods.".format(items)


class PassengerCarrier(Carrier):  # Concrete Implementor / Resource
    def carry_military(self, items):
        return "The plane is carrying {} military personnel.".format(items)

    def carry_commerical(self, items):
        return "The plane is carrying {} commercial passengers.".format(items)


# Client
if __name__ == "__main__":
    plane = MilitaryPlane(CargoCarrier, 100)
    plane.show()

    plane = CommercialPlane(PassengerCarrier, 50)
    plane.show()
