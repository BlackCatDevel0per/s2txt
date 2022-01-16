from actions import UIC
from config import Config


class WindowActions(UIC):
    def __init__(self, parent=None):
        super().__init__()
        # Window
        self.app_title = f"{Config().app_name} {Config().app_version}"
        self.setWindowTitle(self.app_title)

        # Buttons shortcuts
        self.shortcut_btn_record = "Ctrl+Alt+R"
        self.recordButton.setShortcut(self.shortcut_btn_record)
