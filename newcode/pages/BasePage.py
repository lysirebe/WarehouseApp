import tkinter as tk

class BasePage(tk.Frame):
    def __init__(self, master, inventory_manager):
        super().__init__(master)
        self.master = master
        self.inventory_manager = inventory_manager
        self.configure(bg="#f4f4f9")
