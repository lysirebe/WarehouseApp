from tkinter import ttk, messagebox
import tkinter as tk


class UpdateStockWindow(tk.Toplevel):
    def __init__(self, master, inventory_manager, item, update_callback):
        super().__init__(master)

        self.inventory_manager = inventory_manager
        self.item = item
        self.update_callback = update_callback
        self.title("Update Stock")
        self.geometry("400x200")
        self.configure(bg="#f4f4f9")

        # Title and quantity field
        tk.Label(self, text=f"Update Stock for {item.name}", font=("Arial", 12), bg="#f4f4f9").pack(pady=5)

        tk.Label(self, text="Quantity:", font=("Arial", 12), bg="#f4f4f9").pack(pady=5)
        self.quantity_entry = ttk.Entry(self, width=30)
        self.quantity_entry.pack(pady=5)

        # Update Stock Button
        add_button = ttk.Button(self, text="Update Stock", command=self.update_stock)
        add_button.pack(pady=10)

    def update_stock(self):
        """Validates and updates the stock"""
        quantity = self.quantity_entry.get()

        if not quantity.isdigit():
            messagebox.showerror("Error", "Please enter a valid quantity.")
            return

        try:
            self.inventory_manager.add_stock(self.item.section, self.item.name, int(quantity))
            messagebox.showinfo("Success", f"Updated stock for {self.item.name}.")
            self.update_callback()  # Update the inventory list
            self.destroy()
        except ValueError as e:
            messagebox.showerror("Error", str(e))
