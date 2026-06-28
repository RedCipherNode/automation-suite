from app.services.folder_service import FolderService


class MainController:

    def __init__(self, view):

        self.view = view

    def browse_folder(self) -> None:

        folder = FolderService.select_folder()

        if folder is None:
            return

        self.view.set_folder(str(folder))