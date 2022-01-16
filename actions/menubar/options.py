from actions import UIC
import setmic


class Options(UIC):
    def __init__(self, parent=None):
        super().__init__()
        # Options menu
        self.set_device.triggered.connect(setmic.SetMic)
