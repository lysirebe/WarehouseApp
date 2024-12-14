from .BasePage import BasePage
import tkinter as tk
from tkinter import ttk, messagebox
from windows.AddItem import AddItemWindow
from windows.UpdateItem import UpdateStockWindow




class ManageInventoryPage(BasePage):
    def __init__(self, master, inventory_manager):
        super().__init__(master, inventory_manager)

        # Page Title
        tk.Label(self, text="Manage Inventory", font=("Arial", 24, "bold"), bg="#f4f4f9", fg="#2e3f4f").pack(pady=20)

        # Inventory frame
        self.inventory_frame = tk.Frame(self, bg="white")
        self.inventory_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Add New Item button
        ttk.Button(self, text="Add New Item", command=self.add_new_item).pack(pady=10)
        
        # Back to Home button
        ttk.Button(self, text="Back to Home", command=lambda: master.show_page("HomePage")).pack(pady=10)

        # Update the inventory display
        self.update_inventory()



    def update_inventory(self):
        """Display inventory with update functionality"""
        for widget in self.inventory_frame.winfo_children():
            widget.destroy()

        for section_name, section in self.inventory_manager.sections.items():
            section_label = tk.Label(self.inventory_frame, text=section_name, bg="white")
            section_label.pack(anchor="w", pady=5)

            for item in section.items.values():
                self.add_item_row(item)

    def add_item_row(self, item):
        """Helper to add each row for an item"""
        item_frame = tk.Frame(self.inventory_frame, bg="white")
        item_frame.pack(fill="x", pady=5)

        tk.Label(item_frame, text=f"{item.name} - {item.quantity}", bg="white").pack(side="left", padx=5)

        # Update Stock button
        update_button = ttk.Button(item_frame, text="Update Stock", command=lambda i=item: self.update_stock(i))
        update_button.pack(side="right", padx=5)

        

    def add_new_item(self):
        """Opens Add New Item window"""
        AddItemWindow(self.master, self.inventory_manager, self.update_inventory)

    def update_stock(self, item):
        """Opens Update Stock window"""
        UpdateStockWindow(self.master, self.inventory_manager, item, self.update_inventory)
