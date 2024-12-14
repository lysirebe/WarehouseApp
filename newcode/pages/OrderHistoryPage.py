from .BasePage import BasePage
import tkinter as tk
from tkinter import ttk


class OrderHistoryPage(BasePage):
    def __init__(self, master, inventory_manager):
        super().__init__(master, inventory_manager)

        tk.Label(self, text="Order History", font=("Arial", 28, "bold"), bg="#f4f4f9", fg="#2e3f4f").pack(pady=20)

        self.history_frame = tk.Frame(self, bg="white", padx=20, pady=10)
        self.history_frame.pack(fill="both", expand=True, padx=20, pady=10)

        ttk.Button(self, text="Back to Home", command=lambda: master.show_page("HomePage")).pack(pady=10)

        self.update_history()

    def update_history(self):
        for widget in self.history_frame.winfo_children():
            widget.destroy()

        if not self.inventory_manager.order_history:
            tk.Label(self.history_frame, text="No orders placed yet.", font=("Arial", 14), bg="white").pack()
            return

        for order in self.inventory_manager.order_history:
            tk.Label(self.history_frame, text=f"Order Number: {order['order_number']}", font=("Arial", 16, "bold"), bg="white").pack(anchor="w", pady=5)
            tk.Label(self.history_frame, text=f"Item: {order['item']}, Quantity: {order['quantity']}, Destination: {order['destination']}",
                     font=("Arial", 12), bg="white").pack(anchor="w", padx=10, pady=2)
