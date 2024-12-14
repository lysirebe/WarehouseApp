import tkinter as tk
from tkinter import messagebox, ttk

# Import necessary modules
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
        self.configure(bg="#f4f4f9")  # Light gray background for a clean look

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
        self.add_item_name = ttk.Entry(input_frame, width=20)
        self.add_item_name.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(input_frame, text="Quantity:", font=("Arial", 12), bg="white").grid(row=1, column=0, padx=5, pady=5)
        self.add_item_quantity = ttk.Entry(input_frame, width=20)
        self.add_item_quantity.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Expiry Date (Optional):", font=("Arial", 12), bg="white").grid(row=1, column=2, padx=5, pady=5)
        self.add_item_expiry = ttk.Entry(input_frame, width=20)
        self.add_item_expiry.grid(row=1, column=3, padx=5, pady=5)

        self.add_item_button = ttk.Button(input_frame, text="Add Item", command=self.add_item)
        self.add_item_button.grid(row=2, column=1, columnspan=2, pady=10)

        # Stock Management Section
        stock_frame = tk.Frame(self, bg="white", bd=2, relief="groove", padx=10, pady=10)
        stock_frame.pack(pady=10, fill="x", padx=20)

        tk.Label(stock_frame, text="Stock Amount:", font=("Arial", 12), bg="white").grid(row=0, column=0, padx=5, pady=5)
        self.stock_amount = ttk.Entry(stock_frame, width=20)
        self.stock_amount.grid(row=0, column=1, padx=5, pady=5)

        self.add_stock_button = ttk.Button(stock_frame, text="Add Stock", command=self.add_stock)
        self.add_stock_button.grid(row=0, column=2, padx=10)

        self.remove_stock_button = ttk.Button(stock_frame, text="Remove Stock", command=self.remove_stock)
        self.remove_stock_button.grid(row=0, column=3, padx=10)

        # Moving Stock Section
        move_frame = tk.Frame(self, bg="white", bd=2, relief="groove", padx=10, pady=10)
        move_frame.pack(pady=10, fill="x", padx=20)

        tk.Label(move_frame, text="Move Stock to Section:", font=("Arial", 12), bg="white").grid(row=0, column=0, padx=5, pady=5)
        self.move_to_var = tk.StringVar(self)
        self.move_to_section = ttk.OptionMenu(move_frame, self.move_to_var, "Select Section", *self.inventory_manager.sections.keys())
        self.move_to_section.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(move_frame, text="Item Name:", font=("Arial", 12), bg="white").grid(row=1, column=0, padx=5, pady=5)
        self.move_item_name = ttk.Entry(move_frame, width=20)
        self.move_item_name.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(move_frame, text="Quantity to Move:", font=("Arial", 12), bg="white").grid(row=1, column=2, padx=5, pady=5)
        self.move_quantity = ttk.Entry(move_frame, width=20)
        self.move_quantity.grid(row=1, column=3, padx=5, pady=5)

        self.move_stock_button = ttk.Button(move_frame, text="Move Stock", command=self.move_stock)
        self.move_stock_button.grid(row=2, column=1, columnspan=2, pady=10)

        # Inventory Display Section
        display_frame = tk.Frame(self, bg="white", bd=2, relief="groove", padx=10, pady=10)
        display_frame.pack(pady=10, fill="both", expand=True, padx=20)

        tk.Label(display_frame, text="Inventory Overview", font=("Arial", 14, "bold"), bg="white").pack()
        self.inventory_text = tk.Text(display_frame, height=15, width=90, font=("Arial", 12), bg="#f9f9f9", fg="#333333")
        self.inventory_text.pack(padx=5, pady=5)

        # Status Bar
        self.status_label = tk.Label(self, text="Status: Ready", anchor="w", bg="#2e3f4f", fg="white", font=("Arial", 10))
        self.status_label.pack(fill="x", side="bottom")

    def add_item(self):
        section_name = self.section_var.get()
        name = self.add_item_name.get()
        quantity = self.add_item_quantity.get()
        expiry = self.add_item_expiry.get()

        if section_name and name and quantity.isdigit():
            section = self.inventory_manager.get_section(section_name)
            if expiry:
                item = PerishableItem(name, int(quantity), expiry)
            else:
                item = RegularItem(name, int(quantity))
            section.add_item(item)
            self.update_inventory()
            self.status_label.config(text=f"Status: Added '{name}' to section '{section_name}'.", fg="green")
        else:
            messagebox.showerror("Error", "Invalid input fields.")

    def add_stock(self):
        self.modify_stock("add")

    def remove_stock(self):
        self.modify_stock("remove")

    def modify_stock(self, action):
        section_name = self.section_var.get()
        item_name = self.add_item_name.get()
        amount = self.stock_amount.get()

        if section_name and item_name and amount.isdigit():
            section = self.inventory_manager.get_section(section_name)
            if section:
                try:
                    if action == "add":
                        section.add_stock(item_name, int(amount))
                        self.status_label.config(text=f"Status: Added stock for '{item_name}'.", fg="green")
                    else:
                        section.remove_stock(item_name, int(amount))
                        self.status_label.config(text=f"Status: Removed stock for '{item_name}'.", fg="green")
                    self.update_inventory()
                except ValueError as e:
                    messagebox.showerror("Error", str(e))
            else:
                messagebox.showerror("Error", f"Section '{section_name}' not found.")
        else:
            messagebox.showerror("Error", "Invalid input fields.")

    def move_stock(self):
        from_section = self.section_var.get()
        to_section = self.move_to_var.get()
        item_name = self.move_item_name.get()
        quantity = self.move_quantity.get()

        if from_section and to_section and item_name and quantity.isdigit():
            try:
                self.inventory_manager.move_stock(from_section, to_section, item_name, int(quantity))
                self.update_inventory()
                self.status_label.config(text=f"Status: Moved '{item_name}' from '{from_section}' to '{to_section}'.", fg="green")
            except ValueError as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Invalid input fields.")

    def update_inventory(self):
        self.inventory_text.delete(1.0, tk.END)
        for line in self.inventory_manager.get_inventory():
            self.inventory_text.insert(tk.END, line + "\n")

if __name__ == "__main__":
    manager = InventoryManager()
    manager.add_section(InventorySection("Electronics"))
    manager.add_section(InventorySection("Automotive"))
    manager.add_section(InventorySection("Perishables"))

    manager.add_stock("Electronics", "Laptop", 10)
    manager.add_stock("Automotive", "Car Tire", 15)
    manager.add_stock("Perishables", "Milk", 20, misc_info="p", expiry_date="12/12/2024")

    app = WarehouseApp(manager)
    app.mainloop()
