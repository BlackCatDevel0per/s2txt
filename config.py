import configparser
import os


class Config:
    def __init__(self):
        self.app_path = os.getcwd()
        self.app_name = "SpeechApp"
        self.app_version = "Alpha 1.0"
        self.config = configparser.ConfigParser()  # создаём объекта парсера
        self.conf = os.path.join(self.app_path, 'src', 'data', 'config.ini')

    def get(self, args: str):
        self.config.read(self.conf)  # читаем конфиг

        inputmic_index = str(self.config["AUDIO"]["input"])
        lang = str(self.config["AUDIO"]["rlang"])
        rtimeout = str(self.config["AUDIO"]["rtimeout"])
        rclear_voice = str(self.config["AUDIO"]["rclear_voice"])
        rphrase_timeout = str(self.config["AUDIO"]["rphrase_timeout"])

        if args == "mic":  # in python 3.10 will be updated to switch case
            args = int(inputmic_index)
        elif args == "lang":
            args = str(lang)
        elif args == "rtimeout":
            args = int(rtimeout)
        elif args == "rclear_voice":
            args = eval(rclear_voice)
        elif args == "rphrase_timeout":
            args = int(rphrase_timeout)

        return args

    def get_langs_list(self):
        langs = ["en", "ru", "uz"]

        return langs

    def set_index4input(self, index: int):
        self.config.read(self.conf)
        self.config.set("AUDIO", "input", str(index))
        self.config.write(open(self.conf, "w"))

    def set_language(self, language: str):
        self.config.read(self.conf)
        self.config.set("AUDIO", "rlang", language)
        self.config.write(open(self.conf, "w"))

    def set_mic_timeout(self, timeout: int):
        self.config.read(self.conf)
        self.config.set("AUDIO", "rtimeout", timeout)
        self.config.write(open(self.conf, "w"))

    def set_mic_phrase_timeout(self, phrase_timeout: int):
        self.config.read(self.conf)
        self.config.set("AUDIO", "rphrase_timeout", str(phrase_timeout))
        self.config.write(open(self.conf, "w"))

    def set_clear_voice(self, state: bool):
        self.config.read(self.conf)
        self.config.set("AUDIO", "rclear_voice", str(state))
        self.config.write(open(self.conf, "w"))
    #inputmic_index = 8
    #lang = "ru"
    #ltimeout = 2
