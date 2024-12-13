class InventoryItem:
    def __init__(self, name, quantity, section=None):
        self.name = name
        self.quantity = quantity
        self.section = section

    def add_stock(self, amount):
        raise NotImplementedError

    def remove_stock(self, amount):
        raise NotImplementedError

    def __str__(self):
        return f"{self.name}: {self.quantity}"
