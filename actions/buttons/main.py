from actions import UIC


class Buttons(UIC):
    def __init__(self, parent=None):
        super().__init__()
        # Buttons
        self.recordButton.clicked.connect(self.Record)
#		self.recordButton.setCheckable(True) # Делает кнопку выделяемой
