import customtkinter as ctk
from pathlib import Path
from src.models.file_info import FileInfo
from src.controllers.main_controller import MainController


class MainWindow:
    WIDTH = 1000
    HEIGHT = 700

    def __init__(self) -> None:
        ctk.set_appearance_mode("Dark")

        self.root = ctk.CTk()

        self.configure_window()

        self.controller = MainController(self)

        # Folder Entry
        self.folder_entry = ctk.CTkEntry(
            self.root,
            width=600
        )

        self.folder_entry.pack(
            pady=(20, 10)
        )

        # Browse Button
        browse_button = ctk.CTkButton(
            self.root,
            text="Browse",
            command=self.controller.browse_folder
        )

        browse_button.pack(
            pady=(0, 10)
        )

        # Scan Button
        scan_button = ctk.CTkButton(
            self.root,
            text="Scan",
            command=self.controller.scan_folder
        )

        scan_button.pack(
            pady=(0, 20)
        )

        # File List
        self.file_list = ctk.CTkTextbox(
            self.root,
            width=800,
            height=400
        )

        self.file_list.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )

    def configure_window(self) -> None:
        self.root.title("File Organizer")

        self.root.geometry(
            f"{self.WIDTH}x{self.HEIGHT}"
        )

        self.root.minsize(
            800,
            600
        )

    def set_folder(self, folder: str) -> None:
        self.folder_entry.delete(0, "end")
        self.folder_entry.insert(0, folder)

    def show_files(self, files: list[Path]) -> None:
        self.file_list.delete("1.0", "end")

        for file in files:
            self.file_list.insert(
                "end",
                f"{file.name}\n"
            )

    def run(self) -> None:
        self.root.mainloop()

    def show_files(self, files: list[FileInfo]) -> None:

        self.file_list.delete("1.0", "end")

        for file in files:

            self.file_list.insert(
                "end",
                f"{file.name}{file.extension}\n"
            )