import sys
from PyQt5.QtWidgets import QApplication
# icons from my MX-Linux xfce - Papirus gtk2 like
# home path from - os.path.expanduser("~")
import asyncio
from asyncqt import QEventLoop

from editor import Editor

from builtinUI import UIS

# UI Actions
from actions import Actions
from utils import Utils

# Инициализация главного окна


class App(Utils, Actions, UIS, Editor):
    pass
    # Nothing =D


def run():

    app = QApplication(sys.argv)
    app.setStyle('gtk2')  # set default gtk2 style
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    window = App(loop)
    # app.aboutToQuit.connect(window.quit_accept)
    window.show()
    with loop:
        loop.run_forever()


if __name__ == "__main__":
    run()
