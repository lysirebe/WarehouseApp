from .BasePage import BasePage
import tkinter as tk
from tkinter import ttk, messagebox


class OrderPage(BasePage):
    def __init__(self, master, inventory_manager, cart_items):
        super().__init__(master, inventory_manager)
        self.cart_items = cart_items

        tk.Label(self, text="Order Confirmation", font=("Arial", 24, "bold"), bg="#f4f4f9", fg="#2e3f4f").pack(pady=20)

        self.order_frame = tk.Frame(self, bg="white", padx=10, pady=10)
        self.order_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.update_order_summary()

        # Destination selection
        tk.Label(self, text="Select Destination:", font=("Arial", 14), bg="#f4f4f9").pack(pady=5)
        self.destination_var = tk.StringVar(self)
        self.destination_var.set("Select Destination")
        destinations = ["Warehouse 1", "Warehouse 2"]

        destination_menu = ttk.OptionMenu(self, self.destination_var, *destinations)
        destination_menu.pack(pady=5)

        # Action buttons
        ttk.Button(self, text="Place Order", command=self.place_order).pack(pady=10)
        ttk.Button(self, text="Back to Home", command=lambda: master.show_page("HomePage")).pack(pady=10)

    def update_order_summary(self):
        """Display items in the cart."""
        for widget in self.order_frame.winfo_children():
            widget.destroy()

        if not self.cart_items:
            tk.Label(self.order_frame, text="Your cart is empty.", font=("Arial", 12), bg="white").pack()
            return

        for item_name, quantity, section in self.cart_items:
            tk.Label(
                self.order_frame,
                text=f"Item: {item_name}, Quantity: {quantity}",
                font=("Arial", 12),
                bg="white"
            ).pack(anchor="w", pady=2)

    def place_order(self):
        """Handle order placement."""
        destination = self.destination_var.get()
        if destination == "Select Destination":
            messagebox.showerror("Error", "Please select a destination.")
            return
        
        import random
        order_number = f"ORD-{random.randint(1000, 9999)}"


        for item_name, quantity, section in self.cart_items:
            try:
                self.inventory_manager.remove_stock(section, item_name, quantity)
                self.inventory_manager.add_order_history(item_name, quantity,destination,order_number)
            except ValueError as e:
                messagebox.showerror("Error", str(e))
                return

        messagebox.showinfo("Success", "Order placed successfully.")
        self.cart_items.clear()
        self.master.show_page("HomePage")
        
