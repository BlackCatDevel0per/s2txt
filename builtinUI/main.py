from PyQt5.QtWidgets import QMessageBox


class UIS:
    def WarningUi(self, warning: str, title=None):
        QMessageBox.warning(self, title, warning, buttons=QMessageBox.Ok)

    def InformationUi(self, information: str, title=None):
        QMessageBox.information(
            self, title, information, buttons=QMessageBox.Ok)

    def CriticalUi(self, critical: str, title=None):
        QMessageBox.critical(self, title, critical, buttons=QMessageBox.Ok)

    def QuestionUi(self, question: str, title=None):
        self.qui = QMessageBox.question(
            self, title, question, buttons=QMessageBox.Ok | QMessageBox.Cancel)
