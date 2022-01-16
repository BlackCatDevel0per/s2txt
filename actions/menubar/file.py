from actions import UIC


class FileMenu(UIC):
    def __init__(self, parent=None):
        super().__init__()
        # File menu
        self.action_open.triggered.connect(self.open_text)
        self.action_save_as.triggered.connect(self.save_text_as)
        self.action_save.triggered.connect(self.save_current_text)
        self.action_docx_im.triggered.connect(self.import_docx_text)
        self.action_docx_ex.triggered.connect(self.export_docx_text)
        self.action_quit.triggered.connect(self.quit_accept)
        self.action_close.triggered.connect(self.file_close)
        self.action_close.setEnabled(False)
