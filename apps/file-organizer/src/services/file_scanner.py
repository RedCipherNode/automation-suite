from pathlib import Path

from src.models.file_info import FileInfo


class FileScanner:

    @staticmethod
    def scan(directory: Path) -> list[FileInfo]:

        files: list[FileInfo] = []

        for item in directory.iterdir():

            if not item.is_file():
                continue

            files.append(
                FileInfo(
                    name=item.stem,
                    extension=item.suffix.lower(),
                    size=item.stat().st_size,
                    path=item
                )
            )

        return files