from actions import UIC


class Other(UIC):
    def __init__(self, parent=None):
        super().__init__()
        # Other menu
        self.action_clear_text.triggered.connect(self.textEdit.clear)
