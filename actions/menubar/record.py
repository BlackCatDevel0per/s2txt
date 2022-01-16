from actions import UIC


class Record(UIC):
    def __init__(self, parent=None):
        super().__init__()
        # Record menu
        self.action_r_start.triggered.connect(
            lambda: self.recordButton.click())  # click button programmatically
        self.action_r_stop.triggered.connect(
            lambda: self.recordButton.click())  # click button programmatically
        self.action_r_stop.setEnabled(False)
