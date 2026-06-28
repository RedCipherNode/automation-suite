import customtkinter as ctk
from app.controllers.main_controller import MainController

class MainWindow:
    WIDTH = 1000
    HEIGHT = 700

    def __init__(self) -> None:
        ctk.set_appearance_mode("Dark")

        self.root = ctk.CTk()

        self.configure_window()

        self.controller = MainController(self)

        self.folder_entry = ctk.CTkEntry(

        self.root,
            width=600
        )

        self.folder_entry.pack(pady=20)

        browse_button = ctk.CTkButton(
            self.root,
            text="Browse",
            command=self.controller.browse_folder
        )

        browse_button.pack()

    def configure_window(self) -> None:
        self.root.title("File Organizer")

        self.root.geometry(
            f"{self.WIDTH}x{self.HEIGHT}"
        )

        self.root.minsize(800, 600)

    def run(self) -> None:
        self.root.mainloop()

    def set_folder(self, folder: str) -> None:

        self.folder_entry.delete(0, "end")
        self.folder_entry.insert(0, folder)    
        