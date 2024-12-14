from .BasePage import BasePage
from tkinter import ttk
import tkinter as tk


class HomePage(BasePage):
    def __init__(self, master, inventory_manager):
        super().__init__(master, inventory_manager)

        # Styling for the page
        self.configure(bg="#f4f4f9")

        # Page Title
        tk.Label(self, text="Welcome to Light Logistics Systems", font=("Arial", 28, "bold"),
                 bg="#f4f4f9", fg="#2e3f4f").pack(pady=20)

        # Cards Container
        cards_frame = tk.Frame(self, bg="#f4f4f9", padx=20, pady=10)
        cards_frame.pack(fill="both", expand=True)

        # Add three cards
        self.create_card(cards_frame, "Browse Items", "Browse and add items to your cart.",
                         lambda: self.master.show_page("BrowseItemsPage"))
        self.create_card(cards_frame, "Manage Inventory", "Manage stock and add new inventory.",
                         lambda: self.master.show_page("ManageInventoryPage"))
        self.create_card(cards_frame, "Order History", "View the history of your orders.",
                         lambda: self.master.show_page("OrderHistoryPage"))

    def create_card(self, container, title, description, command):
        card = tk.Frame(container, bg="white", bd=2, relief="groove", padx=20, pady=20)
        card.pack(side="left", expand=True, fill="both", padx=10, pady=10)

        card.configure(
            # bg="linear-gradient(to bottom, #f8f9fa, #e0e0e0)",
            highlightbackground="#cccccc",
            highlightthickness=1
        )
        card.pack_propagate(False)  # Prevent shrinking

        # Card Content
        tk.Label(card, text=title, font=("Arial", 18, "bold"), fg="#2e3f4f", bg="white").pack(pady=10)
        tk.Label(card, text=description, font=("Arial", 12), fg="#555555", wraplength=200, bg="white").pack(pady=10)

        ttk.Button(card, text="Go", command=command).pack(pady=10)

