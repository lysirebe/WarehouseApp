from oldcode.RegularItems import RegularItem, PerishableItem

class InventorySection:
    """
    Class to manage a collection of inventory items within a specific section of the warehouse.
    """
    def __init__(self, name):
        """
        Initializes the section with a name and an empty dictionary to hold inventory items.
        
        Args:
            name (str): The name of the section.
        """
        self.name = name
        self.items = {}

    def add_item(self, item):
        """
        Adds an inventory item to the section.

        Args:
            item (InventoryItem): The item object to add.
        """
        self.items[item.name] = item

    def get_item(self, name):
        """
        Retrieves an inventory item by its name.

        Args:
            name (str): The name of the item to retrieve.

        Returns:
            InventoryItem or None: Returns the item object if found, otherwise None.
        """
        return self.items.get(name)

    def add_stock(self, name, amount, misc_info=None, expiry_date=None):
        """
        Adds stock to an existing item or creates a new item if it doesn't exist.

        Args:
            name (str): The name of the item.
            amount (int): The amount of stock to add.
            misc_info (str, optional): Optional flag for item type ('p' for perishable items).
            expiry_date (str, optional): Expiry date for perishable items.

        Raises:
            ValueError: If the stock amount is invalid.
        """
        if amount <= 0:
            raise ValueError("Stock amount must be positive")

        item = self.get_item(name)
        if item:
            item.add_stock(amount)
        else:
            if misc_info == 'p':  # Create a perishable item
                item = PerishableItem(name, amount, expiry_date)
            else:  # Create a regular item
                item = RegularItem(name, amount)
            self.add_item(item)

    def remove_stock(self, name, amount):
        """
        Removes stock from an existing item.

        Args:
            name (str): The name of the item.
            amount (int): The amount of stock to remove.

        Raises:
            ValueError: If the item does not exist or stock is insufficient.
        """
        item = self.get_item(name)
        if item:
            item.remove_stock(amount)
        else:
            raise ValueError("Item not found")

    def __str__(self):
        """
        Returns a string representation of the section.

        Returns:
            str: A string in the format 'Section: SectionName'.
        """
        return f"Section: {self.name}"
