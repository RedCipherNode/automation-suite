from pathlib import Path
from tkinter import filedialog


class FolderService:

    @staticmethod
    def select_folder() -> Path | None:

        folder = filedialog.askdirectory()

        if not folder:
            return None

        return Path(folder)