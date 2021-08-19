class Furniture:
    style = 'Classic'

    def __init__(self):
        raise NotImplemented()

    def __repr__(self):
        result = ""
        result += str(self.__class__) + "\n"
        for x in dir(self):
            if not x.startswith('__'):
                result += "{} - {}\n".format(x, getattr(self, x))
        return result


class Chair(Furniture):  # Base product
    arm_rests = None

    def __init__(self, arm_rests):
        self.arm_rests = arm_rests


class VictorianChair(Chair):  # Concrete product
    style = 'Victorian'


class ModernChair(Chair):  # Concrete product
    style = 'Modern'


class Table(Furniture):  # Base Product
    table_top_material = None

    def __init__(self, table_top):
        self.table_top_material = table_top


class VictorianTable(Table):  # Concrete product
    style = 'Victorian'


class ModernTable(Table):  # Concrete product
    style = 'Modern'


class FurnitureFactory:  # Base factory
    def create_table(self, table_top):
        raise NotImplemented()

    def create_chair(self):
        raise NotImplemented()


class ClassicFurnitureFactory(FurnitureFactory):  # Concrete factory
    def create_table(self, table_top):
        return Table(table_top=table_top)

    def create_chair(self):
        return Chair(arm_rests=True)


class VictorianFurnitureFactory(FurnitureFactory):  # Concrete factory
    def create_table(self, *args):
        return VictorianTable(table_top='Wood')

    def create_chair(self):
        return VictorianChair(arm_rests=True)


class ModernFurnitureFactory(FurnitureFactory):  # Concrete factory
    def create_table(self, table_top):
        return ModernTable(table_top=table_top)

    def create_chair(self):
        return ModernChair(arm_rests=False)


if __name__ == '__main__':
    classic_factory = ClassicFurnitureFactory()
    victorian_factory = VictorianFurnitureFactory()
    modern_factory = ModernFurnitureFactory()

    chairs = []
    tables = []

    # Creating them all together for the sake of example.
    chairs.extend([classic_factory.create_chair(), victorian_factory.create_chair(), modern_factory.create_chair()])
    tables.extend([classic_factory.create_table('Glass'), victorian_factory.create_table(), modern_factory.create_table('Marble')])

    for chair in chairs:
        print(chair)

    for table in tables:
        print(table)