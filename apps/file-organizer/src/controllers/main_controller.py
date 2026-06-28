from src.services.folder_service import FolderService
from src.services.file_scanner import FileScanner
from pathlib import Path

class MainController:

    def __init__(self, view):

        self.view = view

        self.current_folder: Path | None = None

    def browse_folder(self) -> None:

        folder = FolderService.select_folder()

        if folder is None:
            return

        self.view.set_folder(str(folder))

        self.current_folder = folder
    
    def scan_folder(self) -> None:

        if self.current_folder is None:
            return

        files = FileScanner.scan(self.current_folder)

        self.view.show_files(files)