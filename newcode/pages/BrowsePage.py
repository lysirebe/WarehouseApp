# from .BasePage import BasePage
# from tkinter import ttk, messagebox
# import tkinter as tk


# class BrowseItemsPage(BasePage):
#     def __init__(self, master, inventory_manager):
#         super().__init__(master, inventory_manager)
#         self.cart = []

#         # Page Title
#         tk.Label(self, text="Browse Items", font=("Arial", 28, "bold"), bg="#f4f4f9", fg="#2e3f4f").pack(pady=20)

#         # Items Container
#         self.items_frame = tk.Frame(self, bg="white", padx=20, pady=10)
#         self.items_frame.pack(fill="both", expand=True, padx=20, pady=10)

#         self.update_items()

#         # Buttons - Positioned side by side
#         buttons_frame = tk.Frame(self, bg="#f4f4f9", pady=10)
#         buttons_frame.pack(pady=10)

#         ttk.Button(buttons_frame, text="Go to Cart", command=lambda: self.master.show_page("OrderPage", self.cart)).pack(side="left", padx=10)
#         ttk.Button(buttons_frame, text="Back to Home", command=lambda: self.master.show_page("HomePage")).pack(side="left", padx=10)

#     def update_items(self):
#         for widget in self.items_frame.winfo_children():
#             widget.destroy()

#         for section_name, section in self.inventory_manager.sections.items():
#             section_frame = tk.Frame(self.items_frame, bg="#f8f8f8", bd=1, relief="solid", padx=10, pady=10)
#             section_frame.pack(fill="x", pady=10)

#             tk.Label(section_frame, text=section_name, font=("Arial", 16, "bold"), bg="#f8f8f8").pack(anchor="w")

#             for item in section.items.values():
#                 self.add_item_row(section_frame, item)

#     def add_item_row(self, container, item):
#         row = tk.Frame(container, bg="#f8f8f8")
#         row.pack(fill="x", pady=5)

#         tk.Label(row, text=f"{item.name} (Stock: {item.quantity})", bg="#f8f8f8").pack(side="left", padx=10)
#         quantity_entry = ttk.Entry(row, width=5)
#         quantity_entry.pack(side="left", padx=5)
#         ttk.Button(row, text="Add to Cart", command=lambda: self.add_to_cart(item, quantity_entry)).pack(side="right")

#     def add_to_cart(self, item, quantity_entry):
#         quantity = quantity_entry.get()
#         if not quantity.isdigit() or int(quantity) <= 0:
#             messagebox.showerror("Error", "Please enter a valid quantity.")
#             return
        
#         if int(quantity) > item.quantity:
#             messagebox.showerror("Error", f"Not enough stock. Please enter a value equal to or less than {item.quantity}.")
#             return
        
#         self.cart.append((item.name, int(quantity), item.section))
#         messagebox.showinfo("Success", f"{quantity} of {item.name} added to cart.")

from .BasePage import BasePage
from tkinter import ttk, messagebox
import tkinter as tk


class BrowseItemsPage(BasePage):
    def __init__(self, master, inventory_manager):
        super().__init__(master, inventory_manager)
        self.cart = []

        # Page Title
        tk.Label(self, text="Browse Items", font=("Arial", 28, "bold"), bg="#f4f4f9", fg="#2e3f4f").pack(pady=20)

        # Items Container
        self.items_frame = tk.Frame(self, bg="white", padx=20, pady=10)
        self.items_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.update_items()

        # Buttons - Positioned side by side
        buttons_frame = tk.Frame(self, bg="#f4f4f9", pady=10)
        buttons_frame.pack(pady=10)

        ttk.Button(buttons_frame, text="Go to Cart", command=lambda: self.master.show_page("OrderPage", self.cart)).pack(side="left", padx=10)
        ttk.Button(buttons_frame, text="Back to Home", command=lambda: self.master.show_page("HomePage")).pack(side="left", padx=10)

    def update_items(self):
        """Display all items including those with 0 stock."""
        for widget in self.items_frame.winfo_children():
            widget.destroy()

        for section_name, section in self.inventory_manager.sections.items():
            # Section title
            section_frame = tk.Frame(self.items_frame, bg="#f8f8f8", bd=1, relief="solid", padx=10, pady=10)
            section_frame.pack(fill="x", pady=10)

            tk.Label(section_frame, text=section_name, font=("Arial", 16, "bold"), bg="#f8f8f8").pack(anchor="w", pady=5)

            for item in section.items.values():
                self.add_item_row(section_frame, item)

    def add_item_row(self, container, item):
        """Add a row for each item, showing quantity even if it's zero."""
        row = tk.Frame(container, bg="#f8f8f8")
        row.pack(fill="x", pady=5)

        # Show item name and quantity
        quantity_text = "Out of Stock" if item.quantity == 0 else f"Stock: {item.quantity}"
        tk.Label(row, text=f"{item.name} ({quantity_text})", bg="#f8f8f8", font=("Arial", 12)).pack(side="left", padx=10)

        # Quantity input and Add to Cart button
        quantity_entry = ttk.Entry(row, width=5)
        quantity_entry.pack(side="left", padx=5)

        ttk.Button(
            row, text="Add to Cart", 
            command=lambda: self.add_to_cart(item, quantity_entry)
        ).pack(side="right", padx=10)

    def add_to_cart(self, item, quantity_entry):
        """Add items to cart, ensure stock validation."""
        quantity = quantity_entry.get()
        if not quantity.isdigit() or int(quantity) <= 0:
            messagebox.showerror("Error", "Invalid quantity.")
            return

        quantity = int(quantity)
        if quantity > item.quantity:
            messagebox.showerror("Error", f"Not enough stock. Available: {item.quantity}")
            return

        # Add item to cart and show success message
        self.cart.append((item.name, quantity, item.section))
        messagebox.showinfo("Success", f"{quantity} of '{item.name}' added to cart.")
