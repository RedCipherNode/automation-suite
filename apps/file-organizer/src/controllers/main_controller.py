from src.services.folder_service import FolderService
from src.services.file_scanner import FileScanner
from src.models.file_info import FileInfo
from pathlib import Path


class MainController:
    def __init__(self, view):

        self.view = view

        self.current_folder: Path | None = None

        self.files: list[FileInfo] = []

        self.scanned_files: list[FileInfo] = []

    def browse_folder(self) -> None:

        folder = FolderService.select_folder()

        if folder is None:
            self.view.set_status("Folder selection cancelled.")

            return

        self.current_folder = folder

        self.view.set_folder(str(folder))

        self.view.set_status(f"Selected: {folder.name}")

    def scan_folder(self) -> None:

        if self.current_folder is None:
            self.view.set_status("Please select a folder first.")

            return

        self.scanned_files = FileScanner.scan(self.current_folder)

        self.view.show_files(self.scanned_files)

        self.view.set_status(f"Found {len(self.scanned_files)} files.")

    def search_files(self, event) -> None:

        keyword = self.view.get_search_text().strip().lower()

        if keyword == "":
            self.view.show_files(self.scanned_files)

            self.view.set_status(f"Found {len(self.scanned_files)} files.")

            return

        filtered_files = [
            file for file in self.scanned_files if keyword in file.name.lower()
        ]

        self.view.show_files(filtered_files)

        self.view.set_status(f"Found {len(filtered_files)} matching files.")
