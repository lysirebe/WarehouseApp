from classes.RegularItems1 import RegularItem, PerishableItem

class InventorySection:
    def __init__(self, name):
        self.name = name
        self.items = {}

    def add_item(self, item):
        item.section = self.name  # Set the section attribute
        self.items[item.name] = item

    def get_item(self, name):
        return self.items.get(name)

    def add_stock(self, name, amount, misc_info=None, expiry_date=None):
        if amount <= 0:
            raise ValueError("Stock amount must be positive")

        item = self.get_item(name)
        if item:
            item.add_stock(amount)
        else:
            if misc_info == 'p':
                item = PerishableItem(name, amount, expiry_date, self.name)
            else:
                item = RegularItem(name, amount, self.name)
            self.add_item(item)

    def remove_stock(self, name, amount):
        item = self.get_item(name)
        if item:
            item.remove_stock(amount)
        else:
            raise ValueError("Item not found")

    def __str__(self):
        return f"Section: {self.name}"