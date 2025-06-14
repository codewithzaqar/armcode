import customtkinter as ctk

class CodeEditor(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.text_area = ctk.CTkTextbox(self, wrap="none", font=("Consolas", 12))
        self.text_area.pack(fill="both", expand=True, padx=5, pady=5)