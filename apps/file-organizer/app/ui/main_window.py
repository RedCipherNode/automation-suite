import customtkinter as ctk


class MainWindow:

    def __init__(self) -> None:
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()

        self.root.title("File Organizer")
        self.root.geometry("1000x700")
        self.root.minsize(800, 600)

        self.create_widgets()

    def create_widgets(self) -> None:

        # ===== Folder =====

        folder_frame = ctk.CTkFrame(self.root)

        folder_frame.pack(fill="x", padx=20, pady=(20, 10))

        self.folder_entry = ctk.CTkEntry(folder_frame)

        self.folder_entry.pack(side="left", fill="x", expand=True, padx=(10, 10), pady=10)

        browse_button = ctk.CTkButton(
            folder_frame,
            text="Browse"
        )

        browse_button.pack(side="right", padx=(0, 10), pady=10)

        # ===== File List =====

        self.file_list = ctk.CTkTextbox(self.root)

        self.file_list.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        # ===== Bottom =====

        bottom_frame = ctk.CTkFrame(self.root)

        bottom_frame.pack(fill="x", padx=20, pady=(0, 20))

        self.status_label = ctk.CTkLabel(
            bottom_frame,
            text="Ready"
        )

        self.status_label.pack(side="left", padx=10, pady=10)

        scan_button = ctk.CTkButton(
            bottom_frame,
            text="Scan"
        )

        scan_button.pack(side="right", padx=10, pady=10)

    def run(self) -> None:
        self.root.mainloop()