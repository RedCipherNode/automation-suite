from pathlib import Path
import customtkinter as ctk
import tkinter.ttk as ttk
from src.controllers.main_controller import MainController
from src.models.file_info import FileInfo
from src.state.app_state import AppState


class MainWindow:
    WIDTH = 1000
    HEIGHT = 700

    MIN_WIDTH = 800
    MIN_HEIGHT = 600

    ENTRY_WIDTH = 600

    TABLE_NAME_WIDTH = 550
    TABLE_INFO_WIDTH = 120

    # =========================================================================
    # Layout
    # =========================================================================

    WINDOW_PADDING = 20

    TOP_MARGIN = 20

    SECTION_SPACING = 15

    WIDGET_SPACING = 10

    # Lifecycle
    def __init__(self) -> None:

        ctk.set_appearance_mode("Dark")

        self.root = ctk.CTk()

        self.controller = MainController(self)

        self.state = AppState.IDLE

        self.configure_window()

        self.create_widgets()

        self.configure_widgets()

        self.configure_layout()

        self.bind_events()

    # Configuration
    def configure_window(self) -> None:

        self.root.title("File Organizer")

        self.root.geometry(f"{self.WIDTH}x{self.HEIGHT}")

        self.root.minsize(self.MIN_WIDTH, self.MIN_HEIGHT)

    def configure_widgets(self) -> None:

        self.file_table.heading("name", text="Name")

        self.file_table.heading("extension", text="Extension")

        self.file_table.heading("size", text="Size")

        self.file_table.column("name", width=self.TABLE_NAME_WIDTH)

        self.file_table.column(
            "extension", width=self.TABLE_INFO_WIDTH, anchor="center"
        )

        self.file_table.column("size", width=self.TABLE_INFO_WIDTH, anchor="e")

        self.status_frame.pack(fill="x", padx=20, pady=(10, 15))

        self.status_label.pack(anchor="w")

    # Widget Creation
    def create_widgets(self) -> None:

        self.folder_entry = ctk.CTkEntry(self.root, width=self.ENTRY_WIDTH)

        self.browse_button = ctk.CTkButton(self.root, text="Browse")

        self.scan_button = ctk.CTkButton(self.root, text="Scan")

        self.file_table = ttk.Treeview(
            self.root, columns=("name", "extension", "size"), show="headings"
        )

        # Layout Containers
        self.top_frame = ctk.CTkFrame(self.root, fg_color="transparent")

        self.action_frame = ctk.CTkFrame(self.root, fg_color="transparent")

        self.content_frame = ctk.CTkFrame(self.root, fg_color="transparent")

        self.status_frame = ctk.CTkFrame(self.root, fg_color="transparent")

        self.folder_entry = ctk.CTkEntry(self.top_frame, width=self.ENTRY_WIDTH)

        self.browse_button = ctk.CTkButton(self.action_frame, text="Browse")

        self.scan_button = ctk.CTkButton(self.action_frame, text="Scan")

        self.file_table = ttk.Treeview(
            self.content_frame, columns=("name", "extension", "size"), show="headings"
        )

        self.status_label = ctk.CTkLabel(self.status_frame, text="Ready.", anchor="w")

        # config layout

        self.top_frame.pack(
            fill="x",
            padx=self.WINDOW_PADDING,
            pady=(self.TOP_MARGIN, self.WIDGET_SPACING),
        )

        self.action_frame.pack(
            fill="x", padx=self.WINDOW_PADDING, pady=(0, self.SECTION_SPACING)
        )

        self.content_frame.pack(fill="both", expand=True, padx=self.WINDOW_PADDING)

        self.status_frame.pack(
            fill="x",
            padx=self.WINDOW_PADDING,
            pady=(self.WIDGET_SPACING, self.SECTION_SPACING),
        )

        self.folder_entry.pack(fill="x")

        # Buttons in the action
        self.browse_button.pack(side="left")

        self.scan_button.pack(side="left", padx=(10, 0))

        self.file_table.pack(fill="both", expand=True)

        self.status_label.pack(anchor="w")

    # Layout
    def configure_layout(self) -> None:

        self.folder_entry.pack(pady=(20, 10))

        self.browse_button.pack(pady=(0, 10))

        self.scan_button.pack(pady=(0, 20))

        self.file_table.pack(fill="both", expand=True, padx=20, pady=(0, 20))

    # Event Binding
    def bind_events(self) -> None:

        self.browse_button.configure(command=self.controller.browse_folder)

        self.scan_button.configure(command=self.controller.scan_folder)

    # Public API
    def run(self) -> None:

        self.root.mainloop()

    def set_folder(self, folder: str) -> None:

        self.folder_entry.delete(0, "end")

        self.folder_entry.insert(0, folder)

    def set_state(self, state: AppState) -> None:

        self.state = state

        if state == AppState.IDLE:
            self.scan_button.pack_forget()

            self.file_table.pack_forget()

            return

        if state == AppState.FOLDER_SELECTED:
            self.scan_button.pack(pady=(0, 20))

            self.file_table.pack_forget()

            return

        if state == AppState.READY:
            self.scan_button.pack(pady=(0, 20))

            self.file_table.pack(fill="both", expand=True, padx=20, pady=(0, 20))

    def show_files(self, files: list[FileInfo]) -> None:

        for row in self.file_table.get_children():
            self.file_table.delete(row)

        for file in files:
            self.file_table.insert(
                "",
                "end",
                values=(file.name, file.extension, self.format_size(file.size)),
            )

    def set_status(self, message: str) -> None:

        self.status_label.configure(text=message)

    # Helpers
    @staticmethod
    def format_size(size: int) -> str:

        units = ["B", "KB", "MB", "GB", "TB"]

        value = float(size)

        for unit in units:
            if value < 1024:
                return f"{value:.2f} {unit}"

            value /= 1024

        return f"{value:.2f} PB"
