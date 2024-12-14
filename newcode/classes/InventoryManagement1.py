from classes.Sections1 import InventorySection

class InventorySection:
    """Represents a section in the warehouse with its items."""
    def __init__(self, name):
        self.name = name
        self.items = {}  # Stores items in the form {item_name: Item}

    def add_item(self, item):
        if item.name in self.items:
            raise ValueError(f"Item '{item.name}' already exists in section '{self.name}'.")
        self.items[item.name] = item


class Item:
    """Represents an item in a section."""
    def __init__(self, name, quantity, section):
        self.name = name
        self.quantity = quantity
        self.section = section  # New attribute

    def __str__(self):
        return f"{self.name} - Quantity: {self.quantity}"


class InventoryManager:
    """Manages all sections and items in the warehouse."""

    def __init__(self):
        self.sections = {}  # Stores sections in the form {section_name: InventorySection}
        self.order_history = []  # List of completed orders

    def add_section(self, section_name):
        """Adds a new section to the warehouse."""
        if section_name in self.sections:
            raise ValueError(f"Section '{section_name}' already exists.")
        self.sections[section_name] = InventorySection(section_name)


    def add_stock(self, section_name, item_name, quantity):
        """Adds stock to a specific section."""
        if section_name not in self.sections:
            raise ValueError(f"Section '{section_name}' does not exist.")

        section = self.sections[section_name]
        if item_name in section.items:
            # Update existing item's quantity
            section.items[item_name].quantity += quantity
        else:
            # Add a new item to the section
            section.add_item(Item(item_name, quantity, section_name))


    def remove_stock(self, section_name, item_name, quantity):
        """Removes stock from a specific section."""
        if section_name not in self.sections:
            raise ValueError(f"Section '{section_name}' does not exist.")

        section = self.sections[section_name]
        if item_name not in section.items:
            raise ValueError(f"Item '{item_name}' does not exist in section '{section_name}'.")

        item = section.items[item_name]
        if item.quantity < quantity:
            raise ValueError(f"Not enough stock for '{item.name}'. Available: {item.quantity}")

        # Deduct the quantity but do not delete the item
        item.quantity -= quantity



    def add_order_history(self, item, quantity, destination,order_number):
        """
        Adds an order to the order history.

        Args:
            item_name (str): The name of the ordered item.
            quantity (int): The quantity ordered.
            destination (str): The destination of the order.
            order_number (int): The unique order number.
        """
        order = {
            "item": item,
            "quantity": quantity,
            "destination": destination,
            "order_number": order_number
        }
        self.order_history.append(order)

    def get_sections(self):
        """Returns all section names."""
        return list(self.sections.keys())

    def get_section_items(self, section_name):
        """Returns all items in a section."""
        if section_name not in self.sections:
            raise ValueError(f"Section '{section_name}' does not exist.")
        return self.sections[section_name].items
