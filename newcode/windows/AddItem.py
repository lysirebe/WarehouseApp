from tkinter import ttk, messagebox
import tkinter as tk


class AddItemWindow(tk.Toplevel):
    def __init__(self, master, inventory_manager, update_callback):
        super().__init__(master)

        self.inventory_manager = inventory_manager
        self.update_callback = update_callback
        self.title("Add New Item")
        self.geometry("400x400")
        self.configure(bg="#f4f4f9")

        # Section Selection Dropdown
        tk.Label(self, text="Select Existing Section:", font=("Arial", 12), bg="#f4f4f9").pack(pady=5)
        self.section_var = tk.StringVar(self)
        self.section_var.set("Select Section")
        section_menu = ttk.OptionMenu(self, self.section_var, *self.inventory_manager.sections.keys())
        section_menu.pack(pady=5)

        # OR New Section Input
        tk.Label(self, text="Or Create a New Section:", font=("Arial", 12), bg="#f4f4f9").pack(pady=5)
        self.new_section_entry = ttk.Entry(self, width=30)
        self.new_section_entry.pack(pady=5)

        # Item Name Input
        tk.Label(self, text="Item Name:", font=("Arial", 12), bg="#f4f4f9").pack(pady=5)
        self.item_name_entry = ttk.Entry(self, width=30)
        self.item_name_entry.pack(pady=5)

        # Quantity Input
        tk.Label(self, text="Quantity:", font=("Arial", 12), bg="#f4f4f9").pack(pady=5)
        self.quantity_entry = ttk.Entry(self, width=30)
        self.quantity_entry.pack(pady=5)

        # Add Item Button
        add_button = ttk.Button(self, text="Add Item", command=self.add_item)
        add_button.pack(pady=10)

    def add_item(self):
        """Validates inputs, creates a section if needed, and adds a new item."""
        existing_section = self.section_var.get()
        new_section = self.new_section_entry.get().strip()
        item_name = self.item_name_entry.get().strip()
        quantity = self.quantity_entry.get().strip()

        # Validation: Check if item name and quantity are provided
        if not item_name or not quantity.isdigit():
            messagebox.showerror("Error", "Please enter a valid item name and quantity.")
            return

        # Validate Section Selection
        if existing_section == "Select Section" and not new_section:
            messagebox.showerror("Error", "Please select an existing section or create a new one.")
            return

        # Create New Section if specified
        if new_section:
            if new_section in self.inventory_manager.sections:
                messagebox.showerror("Error", f"Section '{new_section}' already exists.")
                return
            self.inventory_manager.add_section(new_section)  # Add new section
            section_name = new_section
        else:
            section_name = existing_section

        # Add the item to the selected section
        try:
            self.inventory_manager.add_stock(section_name, item_name, int(quantity))
            messagebox.showinfo("Success", f"Added {item_name} to '{section_name}'.")
            self.update_callback()  # Refresh inventory
            self.destroy()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

