import customtkinter as ctk
from gui.app import IDEApp

def main():
    ctk.set_appearance_mode("dark")  # Set theme
    ctk.set_default_color_theme("blue")  # Set color theme
    app = IDEApp()
    app.mainloop()

if __name__ == "__main__":
    main()