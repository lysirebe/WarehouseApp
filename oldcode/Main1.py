# import tkinter as tk
# from tkinter import messagebox, ttk

# from InventoryManagement1 import InventoryManager
# from Sections1 import InventorySection
# from RegularItems1 import RegularItem, PerishableItem

# class WarehouseApp(tk.Tk):

#     def __init__(self, inventory_manager):
#         super().__init__()
#         self.inventory_manager = inventory_manager
#         self.title("Warehouse Management System")
#         self.geometry("900x700")
#         self.configure(bg="#f4f4f9")

#         self.current_frame = None
#         self.show_home_page()

#     def show_home_page(self):
#         if self.current_frame:
#             self.current_frame.destroy()
#         self.current_frame = HomePage(self, self.inventory_manager)
#         self.current_frame.pack(fill="both", expand=True)

#     def show_browse_items(self):
#         if self.current_frame:
#             self.current_frame.destroy()
#         self.current_frame = BrowseItemsPage(self, self.inventory_manager)
#         self.current_frame.pack(fill="both", expand=True)

#     def show_manage_inventory(self):
#         if self.current_frame:
#             self.current_frame.destroy()
#         self.current_frame = ManageInventoryPage(self, self.inventory_manager)
#         self.current_frame.pack(fill="both", expand=True)

#     def show_order_history(self):
#         if self.current_frame:
#             self.current_frame.destroy()
#         self.current_frame = OrderHistoryPage(self, self.inventory_manager)
#         self.current_frame.pack(fill="both", expand=True)

#     def show_order_page(self, cart_items):
#         if self.current_frame:
#             self.current_frame.destroy()
#         self.current_frame = OrderPage(self, self.inventory_manager, cart_items)
#         self.current_frame.pack(fill="both", expand=True)

# class HomePage(tk.Frame):
#     def __init__(self, master, inventory_manager):
#         super().__init__(master)
#         self.master = master
#         self.inventory_manager = inventory_manager
#         self.configure(bg="#f4f4f9")

#         title_label = tk.Label(self, text="Welcome to Light Logistics Systems", font=("Arial", 24, "bold"),
#                                bg="#f4f4f9", fg="#2e3f4f", pady=10)
#         title_label.pack(pady=20)

#         browse_button = ttk.Button(self, text="Browse Items and Add to Cart", command=self.master.show_browse_items)
#         browse_button.pack(pady=10)

#         manage_button = ttk.Button(self, text="Manage Inventory", command=self.master.show_manage_inventory)
#         manage_button.pack(pady=10)

#         history_button = ttk.Button(self, text="Order History", command=self.master.show_order_history)
#         history_button.pack(pady=10)

# class BrowseItemsPage(tk.Frame):
#     def __init__(self, master, inventory_manager):
#         super().__init__(master)
#         self.master = master
#         self.inventory_manager = inventory_manager
#         self.cart = []
#         self.configure(bg="#f4f4f9")

#         title_label = tk.Label(self, text="Browse Items", font=("Arial", 24, "bold"),
#                                bg="#f4f4f9", fg="#2e3f4f", pady=10)
#         title_label.pack(pady=20)

#         self.items_frame = tk.Frame(self, bg="white", bd=2, relief="groove", padx=10, pady=10)
#         self.items_frame.pack(pady=10, fill="both", expand=True, padx=20)

#         self.update_items()

#         cart_button = ttk.Button(self, text="Go to Cart", command=self.go_to_cart)
#         cart_button.pack(pady=10)

#         back_button = ttk.Button(self, text="Back to Home", command=self.master.show_home_page)
#         back_button.pack(pady=10)

#     def update_items(self):
#         for widget in self.items_frame.winfo_children():
#             widget.destroy()

#         for section_name, section in self.inventory_manager.sections.items():
#             section_label = tk.Label(self.items_frame, text=section_name, font=("Arial", 14, "bold"), bg="white")
#             section_label.pack(anchor="w", pady=5)

#             for item in section.items.values():
#                 item_frame = tk.Frame(self.items_frame, bg="white")
#                 item_frame.pack(fill="x", pady=2)

#                 item_label = tk.Label(item_frame, text=str(item), font=("Arial", 12), bg="white")
#                 item_label.pack(side="left", padx=5)

#                 add_button = ttk.Button(item_frame, text="Add to Cart", command=lambda i=item: self.add_to_cart(i))
#                 add_button.pack(side="right", padx=5)

#     def add_to_cart(self, item):
#         self.cart.append(item)
#         messagebox.showinfo("Added to Cart", f"Added {item.name} to cart.")

#     def go_to_cart(self):
#         self.master.show_order_page(self.cart)

# class ManageInventoryPage(tk.Frame):
#     def __init__(self, master, inventory_manager):
#         super().__init__(master)
#         self.master = master
#         self.inventory_manager = inventory_manager
#         self.configure(bg="#f4f4f9")

#         title_label = tk.Label(self, text="Manage Inventory", font=("Arial", 24, "bold"),
#                                bg="#f4f4f9", fg="#2e3f4f", pady=10)
#         title_label.pack(pady=20)

#         self.inventory_frame = tk.Frame(self, bg="white", bd=2, relief="groove", padx=10, pady=10)
#         self.inventory_frame.pack(pady=10, fill="both", expand=True, padx=20)

#         self.update_inventory()

#         add_button = ttk.Button(self, text="Add New Item", command=self.add_new_item)
#         add_button.pack(pady=10)

#         back_button = ttk.Button(self, text="Back to Home", command=self.master.show_home_page)
#         back_button.pack(pady=10)

#     def update_inventory(self):
#         for widget in self.inventory_frame.winfo_children():
#             widget.destroy()

#         for section_name, section in self.inventory_manager.sections.items():
#             section_label = tk.Label(self.inventory_frame, text=section_name, font=("Arial", 14, "bold"), bg="white")
#             section_label.pack(anchor="w", pady=5)

#             for item in section.items.values():
#                 item_frame = tk.Frame(self.inventory_frame, bg="white")
#                 item_frame.pack(fill="x", pady=2)

#                 item_label = tk.Label(item_frame, text=str(item), font=("Arial", 12), bg="white")
#                 item_label.pack(side="left", padx=5)

#                 update_button = ttk.Button(item_frame, text="Update Stock", command=lambda i=item: self.update_stock(i))
#                 update_button.pack(side="right", padx=5)

#     def add_new_item(self):
#         AddItemWindow(self.master, self.inventory_manager, self.update_inventory)

#     def update_stock(self, item):
#         UpdateStockWindow(self.master, self.inventory_manager, item, self.update_inventory)

# class OrderHistoryPage(tk.Frame):
#     def __init__(self, master, inventory_manager):
#         super().__init__(master)
#         self.master = master
#         self.inventory_manager = inventory_manager
#         self.configure(bg="#f4f4f9")

#         title_label = tk.Label(self, text="Order History", font=("Arial", 24, "bold"),
#                                bg="#f4f4f9", fg="#2e3f4f", pady=10)
#         title_label.pack(pady=20)

#         self.history_frame = tk.Frame(self, bg="white", bd=2, relief="groove", padx=10, pady=10)
#         self.history_frame.pack(pady=10, fill="both", expand=True, padx=20)

#         self.update_history()

#         back_button = ttk.Button(self, text="Back to Home", command=self.master.show_home_page)
#         back_button.pack(pady=10)

#     def update_history(self):
#         for widget in self.history_frame.winfo_children():
#             widget.destroy()

#         for order in self.inventory_manager.order_history:
#             order_label = tk.Label(self.history_frame, text=str(order), font=("Arial", 12), bg="white")
#             order_label.pack(anchor="w", pady=2)

# class OrderPage(tk.Frame):
#     def __init__(self, master, inventory_manager, cart_items):
#         super().__init__(master)
#         self.master = master
#         self.inventory_manager = inventory_manager
#         self.cart_items = cart_items
#         self.configure(bg="#f4f4f9")

#         title_label = tk.Label(self, text="Order Page", font=("Arial", 24, "bold"),
#                                bg="#f4f4f9", fg="#2e3f4f", pady=10)
#         title_label.pack(pady=20)

#         self.order_frame = tk.Frame(self, bg="white", bd=2, relief="groove", padx=10, pady=10)
#         self.order_frame.pack(pady=10, fill="both", expand=True, padx=20)

#         self.update_order()

#         tk.Label(self.order_frame, text="Select Destination:", font=("Arial", 12), bg="white").pack(pady=5)
#         self.destination_var = tk.StringVar(self)
#         self.destination_menu = ttk.OptionMenu(self.order_frame, self.destination_var, "Select Destination", "Warehouse 1", "Warehouse 2")
#         self.destination_menu.pack(pady=5)

#         send_button = ttk.Button(self.order_frame, text="Send Order", command=self.send_order)
#         send_button.pack(pady=10)

#         back_button = ttk.Button(self, text="Back to Home", command=self.master.show_home_page)
#         back_button.pack(pady=10)

#     def update_order(self):
#         for widget in self.order_frame.winfo_children():
#             widget.destroy()

#         for item in self.cart_items:
#             item_label = tk.Label(self.order_frame, text=str(item), font=("Arial", 12), bg="white")
#             item_label.pack(anchor="w", pady=2)

#     def send_order(self):
#         destination = self.destination_var.get()
#         if destination == "Select Destination":
#             messagebox.showerror("Error", "Please select a destination.")
#             return

#         for item in self.cart_items:
#             try:
#                 self.inventory_manager.remove_stock(item.section, item.name, item.quantity)
#                 self.inventory_manager.add_order_history(item, destination)
#             except ValueError as e:
#                 messagebox.showerror("Error", str(e))
#                 return

#         messagebox.showinfo("Success", "Order successful.")
#         self.master.show_home_page()

# class AddItemWindow(tk.Toplevel):
#     def __init__(self, master, inventory_manager, update_callback):
#         super().__init__(master)
#         self.inventory_manager = inventory_manager
#         self.update_callback = update_callback
#         self.title("Add New Item")
#         self.geometry("400x300")
#         self.configure(bg="#f4f4f9")

#         tk.Label(self, text="Section:", font=("Arial", 12), bg="#f4f4f9").pack(pady=5)
#         self.section_var = tk.StringVar(self)
#         self.section_menu = ttk.OptionMenu(self, self.section_var, "Select Section", *self.inventory_manager.sections.keys())
#         self.section_menu.pack(pady=5)

#         tk.Label(self, text="Item Name:", font=("Arial", 12), bg="#f4f4f9").pack(pady=5)
#         self.item_name_entry = ttk.Entry(self, width=30)
#         self.item_name_entry.pack(pady=5)

#         tk.Label(self, text="Quantity:", font=("Arial", 12), bg="#f4f4f9").pack(pady=5)
#         self.quantity_entry = ttk.Entry(self, width=30)
#         self.quantity_entry.pack(pady=5)

#         tk.Label(self, text="Expiry Date (Optional):", font=("Arial", 12), bg="#f4f4f9").pack(pady=5)
#         self.expiry_entry = ttk.Entry(self, width=30)
#         self.expiry_entry.pack(pady=5)

#         add_button = ttk.Button(self, text="Add Item", command=self.add_item)
#         add_button.pack(pady=10)

#     def add_item(self):
#         section_name = self.section_var.get()
#         item_name = self.item_name_entry.get()
#         quantity = self.quantity_entry.get()
#         expiry_date = self.expiry_entry.get()

#         if section_name == "Select Section" or not item_name or not quantity.isdigit():
#             messagebox.showerror("Error", "Please fill in all required fields.")
#             return

#         try:
#             self.inventory_manager.add_stock(section_name, item_name, int(quantity), 'p' if expiry_date else None, expiry_date)
#             messagebox.showinfo("Success", f"Added {item_name} to {section_name}.")
#             self.update_callback()
#             self.destroy()
#         except ValueError as e:
#             messagebox.showerror("Error", str(e))

# class UpdateStockWindow(tk.Toplevel):
#     def __init__(self, master, inventory_manager, item, update_callback):
#         super().__init__(master)
#         self.inventory_manager = inventory_manager
#         self.item = item
#         self.update_callback = update_callback
#         self.title("Update Stock")
#         self.geometry("400x200")
#         self.configure(bg="#f4f4f9")

#         tk.Label(self, text=f"Update Stock for {item.name}", font=("Arial", 12), bg="#f4f4f9").pack(pady=5)

#         tk.Label(self, text="Quantity:", font=("Arial", 12), bg="#f4f4f9").pack(pady=5)
#         self.quantity_entry = ttk.Entry(self, width=30)
#         self.quantity_entry.pack(pady=5)

#         add_button = ttk.Button(self, text="Update Stock", command=self.update_stock)
#         add_button.pack(pady=10)

#     def update_stock(self):
#         quantity = self.quantity_entry.get()

#         if not quantity.isdigit():
#             messagebox.showerror("Error", "Please enter a valid quantity.")
#             return

#         try:
#             self.inventory_manager.add_stock(self.item.section, self.item.name, int(quantity))
#             messagebox.showinfo("Success", f"Updated stock for {self.item.name}.")
#             self.update_callback()
#             self.destroy()
#         except ValueError as e:
#             messagebox.showerror("Error", str(e))

# if __name__ == "__main__":
#     manager = InventoryManager()
#     manager.add_section(InventorySection("Electronics"))
#     manager.add_section(InventorySection("Perishables"))
#     manager.add_stock("Electronics", "Laptop", 10)
#     manager.add_stock("Perishables", "Milk", 20)

#     app = WarehouseApp(manager)
#     app.mainloop()




import tkinter as tk
from tkinter import messagebox, ttk

from InventoryManagement1 import InventoryManager
from Sections1 import InventorySection
from RegularItems1 import RegularItem, PerishableItem

class WarehouseApp(tk.Tk):

    def __init__(self, inventory_manager):
        super().__init__()
        self.inventory_manager = inventory_manager
        self.title("Warehouse Management System")
        self.geometry("900x700")
        self.configure(bg="#f4f4f9")

        self.current_frame = None
        self.show_home_page()

    def show_home_page(self):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = HomePage(self, self.inventory_manager)
        self.current_frame.pack(fill="both", expand=True)

    def show_browse_items(self):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = BrowseItemsPage(self, self.inventory_manager)
        self.current_frame.pack(fill="both", expand=True)

    def show_manage_inventory(self):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = ManageInventoryPage(self, self.inventory_manager)
        self.current_frame.pack(fill="both", expand=True)

    def show_order_history(self):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = OrderHistoryPage(self, self.inventory_manager)
        self.current_frame.pack(fill="both", expand=True)

    def show_order_page(self, cart_items):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = OrderPage(self, self.inventory_manager, cart_items)
        self.current_frame.pack(fill="both", expand=True)

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

class BrowseItemsPage(tk.Frame):
    def __init__(self, master, inventory_manager):
        super().__init__(master)
        self.master = master
        self.inventory_manager = inventory_manager
        self.cart = []
        self.configure(bg="#f4f4f9")

        title_label = tk.Label(self, text="Browse Items", font=("Arial", 24, "bold"),
                               bg="#f4f4f9", fg="#2e3f4f", pady=10)
        title_label.pack(pady=20)

        self.items_frame = tk.Frame(self, bg="white", bd=2, relief="groove", padx=10, pady=10)
        self.items_frame.pack(pady=10, fill="both", expand=True, padx=20)

        self.update_items()

        cart_button = ttk.Button(self, text="Go to Cart", command=self.go_to_cart)
        cart_button.pack(pady=10)

        back_button = ttk.Button(self, text="Back to Home", command=self.master.show_home_page)
        back_button.pack(pady=10)

    def update_items(self):
                for widget in self.items_frame.winfo_children():
                    widget.destroy()

                for section_name, section in self.inventory_manager.sections.items():
                    section_label = tk.Label(self.items_frame, text=section_name, font=("Arial", 14, "bold"), bg="white")
                    section_label.pack(anchor="w", pady=5)

                    for item in section.items.values():
                        item_frame = tk.Frame(self.items_frame, bg="white")
                        item_frame.pack(fill="x", pady=2)

                        item_label = tk.Label(item_frame, text=str(item), font=("Arial", 12), bg="white")
                        item_label.pack(side="left", padx=5)

                        quantity_label = tk.Label(item_frame, text="Quantity:", font=("Arial", 12), bg="white")
                        quantity_label.pack(side="left", padx=5)

                        quantity_entry = ttk.Entry(item_frame, width=5)
                        quantity_entry.pack(side="left", padx=5)

                        add_button = ttk.Button(item_frame, text="Add to Cart", command=lambda i=item, q=quantity_entry: self.add_to_cart(i, q))
                        add_button.pack(side="right", padx=5)

    def add_to_cart(self, item, quantity_entry):
        quantity = quantity_entry.get()
        
        if not quantity.isdigit() or int(quantity) <= 0:
            messagebox.showerror("Error", "Please enter a valid quantity.")
            return
        
        if int(quantity) > item.quantity:
            messagebox.showerror("Error", f"Not enough stock. Please enter a value equal to or less than {item.quantity}.")
            return

        self.cart.append((item.name, int(quantity), item.section))
        messagebox.showinfo("Added to Cart", f"Added {quantity} of {item.name} to cart.")

    def go_to_cart(self):
        self.master.show_order_page(self.cart)

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

class OrderHistoryPage(tk.Frame):
    def __init__(self, master, inventory_manager):
        super().__init__(master)
        self.master = master
        self.inventory_manager = inventory_manager
        self.configure(bg="#f4f4f9")

        title_label = tk.Label(self, text="Order History", font=("Arial", 24, "bold"),
                               bg="#f4f4f9", fg="#2e3f4f", pady=10)
        title_label.pack(pady=20)

        self.history_frame = tk.Frame(self, bg="white", bd=2, relief="groove", padx=10, pady=10)
        self.history_frame.pack(pady=10, fill="both", expand=True, padx=20)

        self.update_history()

        back_button = ttk.Button(self, text="Back to Home", command=self.master.show_home_page)
        back_button.pack(pady=10)

    def update_history(self):
        for widget in self.history_frame.winfo_children():
            widget.destroy()

        for order in self.inventory_manager.order_history:
            order_label = tk.Label(self.history_frame, text=f"Item: {order['item']}, Quantity: {order['quantity']}, Destination: {order['destination']}", font=("Arial", 12), bg="white")
            order_label.pack(anchor="w", pady=2)

class OrderPage(tk.Frame):
    def __init__(self, master, inventory_manager, cart_items):
        super().__init__(master)
        self.master = master
        self.inventory_manager = inventory_manager
        self.cart_items = cart_items
        self.configure(bg="#f4f4f9")

        title_label = tk.Label(self, text="Order Page", font=("Arial", 24, "bold"),
                               bg="#f4f4f9", fg="#2e3f4f", pady=10)
        title_label.pack(pady=20)

        self.order_frame = tk.Frame(self, bg="white", bd=2, relief="groove", padx=10, pady=10)
        self.order_frame.pack(pady=10, fill="both", expand=True, padx=20)

        self.update_order()

        tk.Label(self.order_frame, text="Select Destination:", font=("Arial", 12), bg="white").pack(pady=5)
        self.destination_var = tk.StringVar(self)
        self.destination_menu = ttk.OptionMenu(self.order_frame, self.destination_var, "Select Destination", "Warehouse 1", "Warehouse 2")
        self.destination_menu.pack(pady=5)

        send_button = ttk.Button(self.order_frame, text="Send Order", command=self.send_order)
        send_button.pack(pady=10)

        back_button = ttk.Button(self, text="Back to Home", command=self.master.show_home_page)
        back_button.pack(pady=10)

    def update_order(self):
        for widget in self.order_frame.winfo_children():
            widget.destroy()

        for item_name, quantity, section in self.cart_items:
            item_label = tk.Label(self.order_frame, text=f"{item_name}: {quantity}", font=("Arial", 12), bg="white")
            item_label.pack(anchor="w", pady=2)

    def send_order(self):
        destination = self.destination_var.get()
        if destination == "Select Destination":
            messagebox.showerror("Error", "Please select a destination.")
            return

        for item_name, quantity, section in self.cart_items:
            try:
                self.inventory_manager.remove_stock(section, item_name, quantity)
                self.inventory_manager.add_order_history(item_name, quantity, destination)
            except ValueError as e:
                messagebox.showerror("Error", str(e))
                return

        messagebox.showinfo("Success", "Order successful.")
        self.master.show_home_page()

class AddItemWindow(tk.Toplevel):
    def __init__(self, master, inventory_manager, update_callback):
        super().__init__(master)
        self.inventory_manager = inventory_manager
        self.update_callback = update_callback
        self.title("Add New Item")
        self.geometry("400x300")
        self.configure(bg="#f4f4f9")

        tk.Label(self, text="Section:", font=("Arial", 12), bg="#f4f4f9").pack(pady=5)
        self.section_var = tk.StringVar(self)
        self.section_menu = ttk.OptionMenu(self, self.section_var, "Select Section", *self.inventory_manager.sections.keys())
        self.section_menu.pack(pady=5)

        tk.Label(self, text="Item Name:", font=("Arial", 12), bg="#f4f4f9").pack(pady=5)
        self.item_name_entry = ttk.Entry(self, width=30)
        self.item_name_entry.pack(pady=5)

        tk.Label(self, text="Quantity:", font=("Arial", 12), bg="#f4f4f9").pack(pady=5)
        self.quantity_entry = ttk.Entry(self, width=30)
        self.quantity_entry.pack(pady=5)

        tk.Label(self, text="Expiry Date (Optional):", font=("Arial", 12), bg="#f4f4f9").pack(pady=5)
        self.expiry_entry = ttk.Entry(self, width=30)
        self.expiry_entry.pack(pady=5)

        add_button = ttk.Button(self, text="Add Item", command=self.add_item)
        add_button.pack(pady=10)

    def add_item(self):
        section_name = self.section_var.get()
        item_name = self.item_name_entry.get()
        quantity = self.quantity_entry.get()
        expiry_date = self.expiry_entry.get()

        if section_name == "Select Section" or not item_name or not quantity.isdigit():
            messagebox.showerror("Error", "Please fill in all required fields.")
            return

        try:
            self.inventory_manager.add_stock(section_name, item_name, int(quantity), 'p' if expiry_date else None, expiry_date)
            messagebox.showinfo("Success", f"Added {item_name} to {section_name}.")
            self.update_callback()
            self.destroy()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

class UpdateStockWindow(tk.Toplevel):
    def __init__(self, master, inventory_manager, item, update_callback):
        super().__init__(master)
        self.inventory_manager = inventory_manager
        self.item = item
        self.update_callback = update_callback
        self.title("Update Stock")
        self.geometry("400x200")
        self.configure(bg="#f4f4f9")

        tk.Label(self, text=f"Update Stock for {item.name}", font=("Arial", 12), bg="#f4f4f9").pack(pady=5)

        tk.Label(self, text="Quantity:", font=("Arial", 12), bg="#f4f4f9").pack(pady=5)
        self.quantity_entry = ttk.Entry(self, width=30)
        self.quantity_entry.pack(pady=5)

        add_button = ttk.Button(self, text="Update Stock", command=self.update_stock)
        add_button.pack(pady=10)

    def update_stock(self):
        quantity = self.quantity_entry.get()

        if not quantity.isdigit():
            messagebox.showerror("Error", "Please enter a valid quantity.")
            return

        try:
            self.inventory_manager.add_stock(self.item.section, self.item.name, int(quantity))
            messagebox.showinfo("Success", f"Updated stock for {self.item.name}.")
            self.update_callback()
            self.destroy()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    manager = InventoryManager()
    manager.add_section(InventorySection("Electronics"))
    manager.add_section(InventorySection("Perishables"))
    manager.add_stock("Electronics", "Laptop", 10)
    manager.add_stock("Perishables", "Milk", 20)

    app = WarehouseApp(manager)
    app.mainloop()

