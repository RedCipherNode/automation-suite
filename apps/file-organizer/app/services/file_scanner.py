from pathlib import Path


class FileScanner:

    @staticmethod
    def scan(directory: Path) -> list[Path]:
        return [
            item
            for item in directory.iterdir()
            if item.is_file()
        ]