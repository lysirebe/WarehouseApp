import tkinter as tk
from classes.InventoryManagement1 import InventoryManager
from classes.Sections1 import InventorySection
from pages.HomePage import HomePage
from pages.BrowsePage import BrowseItemsPage
from pages.ManageInventoryPage import ManageInventoryPage
from pages.OrderHistoryPage import OrderHistoryPage
from pages.OrderPage import OrderPage


class WarehouseApp(tk.Tk):
    def __init__(self, inventory_manager):
        super().__init__()
        self.inventory_manager = inventory_manager
        self.title("Warehouse Management System")
        self.geometry("900x700")
        self.configure(bg="#f4f4f9")

        self.current_frame = None
        self.pages = {}  # Store page instances

        # Define the mapping between page names and page classes
        self.page_classes = {
            "HomePage": HomePage,
            "BrowseItemsPage": BrowseItemsPage,
            "ManageInventoryPage": ManageInventoryPage,
            "OrderHistoryPage": OrderHistoryPage,
            "OrderPage": OrderPage,
        }

        # Show the Home Page initially
        self.show_page("HomePage")

    def show_page(self, page_name, *args):
        """Dynamically resolve and show pages by their name."""
        if self.current_frame:
            self.current_frame.destroy()

        # Resolve the page class from the string name
        PageClass = self.page_classes[page_name]

        # Create an instance of the resolved class
        self.pages[page_name] = PageClass(self, self.inventory_manager, *args)

        self.current_frame = self.pages[page_name]
        self.current_frame.pack(fill="both", expand=True)


if __name__ == "__main__":
    manager = InventoryManager()
    # Ensure sections are added before adding stock
    manager.add_section("Electronics")
    manager.add_section("Perishables")

    # Now add stock to existing sections
    manager.add_stock("Electronics", "Laptop", 10)
    manager.add_stock("Perishables", "Milk", 20)

    app = WarehouseApp(manager)
    app.mainloop()