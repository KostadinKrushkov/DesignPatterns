class Washer:  # Subsystem 1
    def wash(self, clothes):
        print("Washing {}".format(','.join(clothes)))


class Dryer:  # Subsystem 2
    def dry(self, clothes):
        print("Drying {}".format(','.join(clothes)))


class Folder:  # Subsystem 3
    def fold(self, clothes):
        print("Folding {}".format(','.join(clothes)))


class CleaningMachine:  # Facade
    washer = None
    dryer = None
    folder = None

    def __init__(self, washer, dryer, folder):
        self.washer = washer
        self.dryer = dryer
        self.folder = folder

    def clean_clothes(self, clothes):  # Easy to use combining methods from subsystem
        self.washer.wash(clothes)
        self.dryer.dry(clothes)
        self.folder.fold(clothes)


if __name__ == "__main__":
    clothes = ['T-Shirt', 'Pants', 'Jeans', "Jacket"]
    washer = Washer()
    dryer = Dryer()
    folder = Folder()

    cleaner = CleaningMachine(washer=washer, dryer=dryer, folder=folder)
    cleaner.clean_clothes(clothes)
