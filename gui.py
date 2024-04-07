import tkinter as tk
from tkinter import filedialog, messagebox

class AppGUI:
    def __init__(self, root, main_app):
        self.root = root
        self.main_app = main_app  # Reference to the main application class
        self.setup_ui()

    def setup_ui(self):
        self.root.title("UNH Scripting w/Python Project")
        self.root.geometry('600x400')

        # Main label
        tk.Label(self.root, text="UNH Scripting w/Python", font=("Arial", 16)).pack(pady=10)