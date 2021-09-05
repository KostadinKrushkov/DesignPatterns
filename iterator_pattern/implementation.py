class Inventory:  # Iterable
    def get_inventory_iterator(self):
        pass


class InventoryIterator:  # Iterator
    def has_next(self):
        pass

    def next(self):
        pass

    def current(self):
        pass


class HandHeldInventory(Inventory):  # Concrete Iterable
    left_hand = None
    right_hand = None

    def __init__(self, left, right):
        self.left_hand = left
        self.right_hand = right

    def get_right(self):
        return self.right_hand

    def _set_right(self, right):
        self.right_hand = right

    def get_left(self):
        return self.left_hand

    def _set_left(self, left):
        self.left_hand = left

    def get_inventory_iterator(self):
        return HandHeldInventoryIterator(self)


class HandHeldInventoryIterator(InventoryIterator):  # Concrete Iterator
    handheld_inventory = None
    index = 0

    def __init__(self, iterable):
        self.handheld_inventory = iterable

    def has_next(self):
        return self.index < 2

    def next(self):
        self.index += 1

    def current(self):
        if self.index == 0:
            return self.handheld_inventory.get_right()
        elif self.index == 1:
            return self.handheld_inventory.get_left()
        else:
            return None


class Item:
    name = None

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Item name: \"{}\"".format(self.name)


if __name__ == "__main__":  # Client
    item1, item2 = Item("Torch"), Item("Sword")
    inventory = HandHeldInventory(item1, item2)
    iterator = inventory.get_inventory_iterator()

    while iterator.has_next():
        print("Element part of inventory is: {}".format(iterator.current()))
        iterator.next()
