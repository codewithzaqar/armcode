import customtkinter as ctk

class Toolbar(ctk.CTkFrame):
    def __init__(self, parent, file_callback):
        super().__init__(parent)

        self.file_callback = file_callback

        # Buttons
        btn_new = ctk.CTkButton(self, text="New", command=lambda: self.file_callback("new"))
        btn_new.pack(side="left", padx=5, pady=5)

        btn_open = ctk.CTkButton(self, text="Open", command=lambda: self.file_callback("openn"))
        btn_open.pack(side="left", padx=5)

        btn_save = ctk.CTkButton(self, text="Save", command=lambda: self.file_callback("save"))
        btn_save.pack(side="left", padx=5)