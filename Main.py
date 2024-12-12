import tkinter as tk
from tkinter import messagebox, ttk

# Uncomment these imports once the modules are available
from InventoryManagement import InventoryManager
from Sections import InventorySection
from RegularItems import RegularItem, PerishableItem

class WarehouseApp(tk.Tk):
    """
    GUI Application for Warehouse Management System using Tkinter.
    """
    def __init__(self, inventory_manager):
        super().__init__()
        self.inventory_manager = inventory_manager
        self.title("Warehouse Management System")
        self.geometry("900x700")
        self.configure(bg="#f4f4f9")  # Light background for a clean look

        self.create_widgets()
        self.update_inventory()

    def create_widgets(self):
        # Title Label
        title_label = tk.Label(self, text="Warehouse Management System", font=("Arial", 24, "bold"),
                               bg="#f4f4f9", fg="#2e3f4f", pady=10)
        title_label.pack()

        # Input Frame
        input_frame = tk.Frame(self, bg="white", bd=2, relief="groove", padx=10, pady=10)
        input_frame.pack(pady=10, fill="x", padx=20)

        # Section Selection
        tk.Label(input_frame, text="Select Section:", font=("Arial", 12), bg="white").grid(row=0, column=0, padx=5, pady=5)
        self.section_var = tk.StringVar(self)
        self.section_menu = ttk.OptionMenu(input_frame, self.section_var, "Select Section", *self.inventory_manager.sections.keys())
        self.section_menu.grid(row=0, column=1, padx=5, pady=5)

        # Item Fields
        tk.Label(input_frame, text="Item Name:", font=("Arial", 12), bg="white").grid(row=0, column=2, padx=5, pady=5)
        self.add_item_name = ttk.Entry(input_frame)
        self.add_item_name.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(input_frame, text="Quantity:", font=("Arial", 12), bg="white").grid(row=1, column=0, padx=5, pady=5)
        self.add_item_quantity = ttk.Entry(input_frame)
        self.add_item_quantity.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Expiry Date (Optional):", font=("Arial", 12), bg="white").grid(row=1, column=2, padx=5, pady=5)
        self.add_item_expiry = ttk.Entry(input_frame)
        self.add_item_expiry.grid(row=1, column=3, padx=5, pady=5)

        # Add Item Button
        self.add_item_button = ttk.Button(input_frame, text="Add Item", command=self.add_item)
        self.add_item_button.grid(row=2, column=1, columnspan=2, pady=10)

        # Inventory Display
        tk.Label(self, text="Inventory Overview", font=("Arial", 14, "bold"), bg="#f4f4f9").pack()
        self.inventory_text = tk.Text(self, height=15, width=90, font=("Arial", 12), bg="#ffffff", fg="#333333")
        self.inventory_text.pack(pady=10)

        # Update Inventory Button
        self.update_button = ttk.Button(self, text="Refresh Inventory", command=self.update_inventory)
        self.update_button.pack(pady=5)

    def add_item(self):
        """
        Adds an item to the inventory section.
        """
        section_name = self.section_var.get()
        name = self.add_item_name.get()
        quantity = self.add_item_quantity.get()
        expiry = self.add_item_expiry.get()

        if section_name and name and quantity.isdigit():
            quantity = int(quantity)
            if expiry:
                item = PerishableItem(name, quantity, expiry)
            else:
                item = RegularItem(name, quantity)
            self.inventory_manager.get_section(section_name).add_item(item)
            self.update_inventory()
            messagebox.showinfo("Success", f"Item '{name}' added to section '{section_name}'.")
        else:
            messagebox.showerror("Error", "Please fill out all fields correctly.")

    def update_inventory(self):
        """
        Updates the inventory display with the current inventory.
        """
        self.inventory_text.delete(1.0, tk.END)
        inventory = self.inventory_manager.get_inventory()
        for item in inventory:
            self.inventory_text.insert(tk.END, item + '\n')


# Main application entry point
if __name__ == "__main__":
    from InventoryManagement import InventoryManager
    from Sections import InventorySection

    # Create inventory manager
    inventory_manager = InventoryManager()

    # Add initial sections
    inventory_manager.add_section(InventorySection("Electronics"))
    inventory_manager.add_section(InventorySection("Automotive"))
    inventory_manager.add_section(InventorySection("Clothes"))
    inventory_manager.add_section(InventorySection("Food"))
    inventory_manager.add_section(InventorySection("Animals"))




    # Run the application
    app = WarehouseApp(inventory_manager)
    app.mainloop()

