import os
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog

from config import Config

from s2txt import AppAPI as api

# Инициализация главного окна
class SetMic(QDialog):

    def __init__(self):
        super(SetMic, self).__init__()
        uic.loadUi(os.path.join('src', 'uis', 'SetDevice.ui'), self)
        self.label_lang.setText(Config().get("lang"))
        d = api.get_device_index("name&index")  # Получаем словарь
        self.select_device_box.addItems(d) # Добавляем данные словаря в ComboBox
        self.select_device_box.setCurrentIndex(Config().get("mic")) # Ставим текущий микрофон в ComboBox

        langs = Config().get_langs_list()  # Список с языками распознавания речи
        # Удаляем из списка текущий язык и записываем его в переменную lang
        lang = langs.pop(langs.index(Config().get("lang")))
        langs.insert(0, lang)  # Добавляем текущий язык в начало списка
        self.select_language_box.addItems(langs)
        # Ставим текущий таймаут в spinBox
        self.spinBox.setValue(Config().get("rtimeout"))
        # ...
        self.spinBox_2.setValue(Config().get("rphrase_timeout"))
        # ...
        ##########

        self.buttonBox.accepted.connect(self.save_config)
        self.buttonBox.rejected.connect(lambda: self.close())
        cstate = Config().get("rclear_voice")
        if cstate is True:
            cstate = 2
        elif cstate is False:
            cstate = 0
        self.checkBox_clear_voice.setCheckState(cstate)
        self.exec_()

    def save_config(self):
        Config().set_index4input(self.select_device_box.currentIndex())
        Config().set_language(self.select_language_box.currentText())
        Config().set_mic_timeout(str(self.spinBox.value()))
        chbox = self.checkBox_clear_voice.checkState()  # return 0 - False or 2 - True
        state = None
        if chbox == 2:
            state = True
        elif chbox == 0:
            state = False
        Config().set_clear_voice(state)
        Config().set_mic_phrase_timeout(self.spinBox_2.value())

        self.close()
