import tkinter as tk
from tkinter import ttk

class ManageInventoryPage(tk.Frame):
    def __init__(self, master, inventory_manager):
        super().__init__(master)
        self.master = master
        self.inventory_manager = inventory_manager
        self.configure(bg="#f4f4f9")

        title_label = tk.Label(self, text="Manage Inventory", font=("Arial", 24, "bold"),
                               bg="#f4f4f9", fg="#2e3f4f", pady=10)
        title_label.pack(pady=20)

        self.inventory_frame = tk.Frame(self, bg="white", bd=2, relief="groove", padx=10, pady=10)
        self.inventory_frame.pack(pady=10, fill="both", expand=True, padx=20)

        self.update_inventory()

        add_button = ttk.Button(self, text="Add New Item", command=self.add_new_item)
        add_button.pack(pady=10)

        back_button = ttk.Button(self, text="Back to Home", command=self.master.show_home_page)
        back_button.pack(pady=10)

    def update_inventory(self):
        for widget in self.inventory_frame.winfo_children():
            widget.destroy()

        for section_name, section in self.inventory_manager.sections.items():
            section_label = tk.Label(self.inventory_frame, text=section_name, font=("Arial", 14, "bold"), bg="white")
            section_label.pack(anchor="w", pady=5)

            for item in section.items.values():
                item_frame = tk.Frame(self.inventory_frame, bg="white")
                item_frame.pack(fill="x", pady=2)

                item_label = tk.Label(item_frame, text=str(item), font=("Arial", 12), bg="white")
                item_label.pack(side="left", padx=5)

                update_button = ttk.Button(item_frame, text="Update Stock", command=lambda i=item: self.update_stock(i))
                update_button.pack(side="right", padx=5)

    def add_new_item(self):
        AddItemWindow(self.master, self.inventory_manager, self.update_inventory)

    def update_stock(self, item):
        UpdateStockWindow(self.master, self.inventory_manager, item, self.update_inventory)