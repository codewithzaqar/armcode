import customtkinter as ctk
from gui.editor import CodeEditor
from gui.toolbar import Toolbar

class IDEApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("ArmCode")
        self.geometry("800x600")

        # Layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Components
        self.toolbar = Toolbar(self, self.handle_file_operation)
        self.toolbar.grid(row=0, column=0, sticky="ew")

        self.editor = CodeEditor(self)
        self.editor.grid(row=1, column=0, sticky="nsew")

    def handle_file_operation(self, operation):
        print(f"File operation: {operation}")  # Placeholder