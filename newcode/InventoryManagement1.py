from Sections1 import InventorySection

class InventoryManager:
    """
    Manages warehouse sections and their inventory items.
    Acts as the central controller for inventory operations.
    """

    def __init__(self):
        """
        Initializes the InventoryManager with an empty dictionary for sections.
        """
        self.sections = {}
        self.order_history = []

    def add_section(self, section):
        """
        Adds a new section to the warehouse.

        Args:
            section (InventorySection): An InventorySection object to add.
        """
        self.sections[section.name] = section

    def get_section(self, name):
        """
        Retrieves a section by its name.

        Args:
            name (str): Name of the section.

        Returns:
            InventorySection or None: Returns the section object if found, otherwise None.
        """
        return self.sections.get(name)

    def add_item_to_section(self, section_name, item):
        """
        Adds an item to a specific section.

        Args:
            section_name (str): Name of the section.
            item (InventoryItem): The item to be added.

        Raises:
            ValueError: If the section does not exist.
        """
        section = self.get_section(section_name)
        if section:
            section.add_item(item)
        else:
            raise ValueError(f"Section '{section_name}' does not exist.")

    def add_stock(self, section_name, item_name, amount, misc_info=None, expiry_date=None):
        """
        Adds stock to an item in a section. Creates the item if it doesn't exist.

        Args:
            section_name (str): Name of the section.
            item_name (str): Name of the item.
            amount (int): Amount of stock to add.
            misc_info (str, optional): Flag for item type ('p' for perishable items).
            expiry_date (str, optional): Expiry date for perishable items.

        Raises:
            ValueError: If the section does not exist or stock amount is invalid.
        """
        section = self.get_section(section_name)
        if section:
            section.add_stock(item_name, amount, misc_info, expiry_date)
        else:
            raise ValueError(f"Section '{section_name}' does not exist.")

    def remove_stock(self, section_name, item_name, amount):
        """
        Removes stock from an item in a section.

        Args:
            section_name (str): Name of the section.
            item_name (str): Name of the item.
            amount (int): Amount of stock to remove.

        Raises:
            ValueError: If the section or item does not exist, or if stock is insufficient.
        """
        section = self.get_section(section_name)
        if section:
            section.remove_stock(item_name, amount)
        else:
            raise ValueError(f"Section '{section_name}' does not exist.")

    def move_stock(self, from_section_name, to_section_name, item_name, amount):
        """
        Moves stock from one section to another.

        Args:
            from_section_name (str): Source section name.
            to_section_name (str): Destination section name.
            item_name (str): Name of the item to move.
            amount (int): Amount of stock to move.

        Raises:
            ValueError: If either section does not exist, or stock movement fails.
        """
        from_section = self.get_section(from_section_name)
        to_section = self.get_section(to_section_name)

        if not from_section:
            raise ValueError(f"Source section '{from_section_name}' does not exist.")
        if not to_section:
            raise ValueError(f"Destination section '{to_section_name}' does not exist.")

        # Get item and remove stock from the source
        item = from_section.get_item(item_name)
        if item:
            from_section.remove_stock(item_name, amount)
            # Add stock to the destination section
            to_section.add_stock(item_name, amount, "p" if hasattr(item, "expiry_date") else None, 
                                 getattr(item, "expiry_date", None))
        else:
            raise ValueError(f"Item '{item_name}' not found in section '{from_section_name}'.")

    def get_inventory(self):
        """
        Retrieves an overview of all sections and their items.

        Returns:
            list: A list of formatted strings representing each section and its items.
        """
        inventory = []
        for section_name, section in self.sections.items():
            inventory.append(str(section))  # Section header
            for item in section.items.values():
                inventory.append(f"  {item}")  # Indented item details
        return inventory

    def get_items_in_section(self, section_name):
        """
        Retrieves all items in a specific section.

        Args:
            section_name (str): Name of the section.

        Returns:
            list: A list of item details from the specified section.

        Raises:
            ValueError: If the section does not exist.
        """
        section = self.get_section(section_name)
        if section:
            return [str(item) for item in section.items.values()]
        else:
            raise ValueError(f"Section '{section_name}' does not exist.")

    # def add_order_history(self, item, destination):
    #     """
    #     Adds an order to the order history.

    #     Args:
    #         item (InventoryItem): The item that was ordered.
    #         destination (str): The destination of the order.
    #     """
    #     order = {
    #         "item": item.name,
    #         "quantity": item.quantity,
    #         "destination": destination
    #     }
    #     self.order_history.append(order)

    
    def add_order_history(self, item, quantity, destination):
        """
        Adds an order to the order history.

        Args:
            item_name (str): The name of the ordered item.
            quantity (int): The quantity ordered.
            destination (str): The destination of the order.
        """
        order = {
            "item": item,
            "quantity": quantity,
            "destination": destination
        }
        self.order_history.append(order)

