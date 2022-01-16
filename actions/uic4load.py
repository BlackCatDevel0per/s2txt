from PyQt5.QtWidgets import QMainWindow, QApplication

from PyQt5 import uic

from config import Config

import os


class UIC(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.app_path = Config().app_path
        uic.loadUi(os.path.join(self.app_path, 'src', 'uis', 'main.ui'), self)
