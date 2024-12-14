import tkinter as tk
import unittest

class TestUI(unittest.TestCase):

    def setUp(self):
        """Set up the Tkinter UI environment."""
        self.root = tk.Tk()
        self.root.geometry("400x300")
        self.cart_button = tk.Button(self.root, text="Add to Cart", command=self.add_to_cart)
        self.cart_button.pack()
        
        self.error_label = tk.Label(self.root, text="", fg="red")
        self.error_label.pack()

    def add_to_cart(self):
        """Simulate adding an item to the cart."""
        self.error_label.config(text="Item added to cart!")

    def test_ui_elements(self):
        """Test UI elements are properly displayed."""
        self.assertIsInstance(self.cart_button, tk.Button)
        self.assertIsInstance(self.error_label, tk.Label)

    def test_button_click(self):
        """Test button action triggers."""
        self.cart_button.invoke()
        self.assertEqual(self.error_label.cget("text"), "Item added to cart!")

if __name__ == "__main__":
    unittest.main()
