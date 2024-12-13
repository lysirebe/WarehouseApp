import tkinter as tk
from tkinter import ttk

class HomePage(tk.Frame):
    def __init__(self, master, inventory_manager):
        super().__init__(master)
        self.master = master
        self.inventory_manager = inventory_manager
        self.configure(bg="#f4f4f9")

        title_label = tk.Label(self, text="Welcome to Light Logistics Systems", font=("Arial", 24, "bold"),
                               bg="#f4f4f9", fg="#2e3f4f", pady=10)
        title_label.pack(pady=20)

        browse_button = ttk.Button(self, text="Browse Items and Add to Cart", command=self.master.show_browse_items)
        browse_button.pack(pady=10)

        manage_button = ttk.Button(self, text="Manage Inventory", command=self.master.show_manage_inventory)
        manage_button.pack(pady=10)

        history_button = ttk.Button(self, text="Order History", command=self.master.show_order_history)
        history_button.pack(pady=10)