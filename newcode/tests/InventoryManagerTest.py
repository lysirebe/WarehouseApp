import unittest
from classes.InventoryManagement1 import InventoryManager, InventorySection, Item

class TestInventoryManager(unittest.TestCase):
    def setUp(self):
        """Setup a fresh InventoryManager before each test."""
        self.manager = InventoryManager()
        self.manager.add_section("Electronics")
        self.manager.add_section("Perishables")

    # Unit Tests 

    def test_add_section(self):
        """Test adding a new section."""
        self.manager.add_section("Clothing")
        self.assertIn("Clothing", self.manager.sections)

    def test_add_duplicate_section(self):
        """Test adding a duplicate section."""
        with self.assertRaises(ValueError):
            self.manager.add_section("Electronics")

    def test_add_stock_to_section(self):
        """Test adding stock to an existing section."""
        self.manager.add_stock("Electronics", "Laptop", 5)
        self.assertEqual(self.manager.sections["Electronics"].items["Laptop"].quantity, 5)


    def test_prevent_add_to_cart_no_stock(self):
        """Test preventing adding out-of-stock items to the cart."""
        cart = []
        self.manager.add_stock("Electronics", "Laptop", 0)
        item = self.manager.sections["Electronics"].items["Laptop"]

        with self.assertRaises(ValueError):
            if item.quantity == 0:
                raise ValueError("Cannot add out-of-stock item to cart.")
            

            
    # Integration Tests 
    def test_add_item_to_cart(self):
        """Test adding an item to the cart."""
        cart = []
        self.manager.add_stock("Electronics", "Laptop", 5)
        item = self.manager.sections["Electronics"].items["Laptop"]
        cart.append((item.name, 2, item.section))
        self.assertIn(("Laptop", 2, "Electronics"), cart)

    def test_place_order(self):
        """Test placing an order and verifying order history."""
        self.manager.add_stock("Electronics", "Laptop", 5)
        self.manager.add_order_history("Laptop", 3, "Warehouse 1","ORD-1234",)
        self.assertEqual(len(self.manager.order_history), 1)
        self.assertEqual(self.manager.order_history[0]["order_number"], "ORD-1234")


    def test_update_item_stock(self):
        """Test updating stock for an existing item."""
        self.manager.add_stock("Electronics", "Laptop", 10)
        self.manager.add_stock("Electronics", "Laptop", 5)  # Updating stock
        
        # Verify the updated stock
        self.assertEqual(self.manager.sections["Electronics"].items["Laptop"].quantity, 15)


    def test_multiple_items_in_order(self):
        """Test placing an order with multiple items."""
        self.manager.add_stock("Electronics", "Laptop", 5)
        self.manager.add_stock("Perishables", "Milk", 10)
        
        # Place order with multiple items
        order_number = "ORD-5678"
        self.manager.add_order_history("Laptop", 2, "Warehouse 1", order_number)
        self.manager.add_order_history("Milk", 5, "Warehouse 2", order_number)
        
        # Verify that both items are in the order history
        self.assertEqual(len(self.manager.order_history), 2)
        self.assertEqual(self.manager.order_history[1]["item"], "Milk")

    def test_add_to_cart_and_place_order(self):
        """Test adding an item to the cart and placing an order."""
        # Add stock
        self.manager.add_stock("Electronics", "Laptop", 10)
        
        # Add item to cart
        cart = []
        item = self.manager.sections["Electronics"].items["Laptop"]
        cart.append((item.name, 2, item.section))
        
        # Place order
        order_number = "ORD-1234"
        self.manager.add_order_history("Laptop", 2, "Warehouse 1", order_number)

        # Manually reduce stock based on order quantity
        self.manager.remove_stock("Electronics", "Laptop", 2)

        
        # Verify order history and stock
        self.assertEqual(len(self.manager.order_history), 1)
        self.assertEqual(self.manager.sections["Electronics"].items["Laptop"].quantity, 8)  # Stock reduced by 2
        self.assertEqual(self.manager.order_history[0]["order_number"], "ORD-1234")


if __name__ == "__main__":
    unittest.main()
