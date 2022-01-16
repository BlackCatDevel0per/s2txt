from .uic4load import UIC

from .menubar import FileMenu
from .menubar import Record
from .menubar import Options
from .menubar import Other
from .window import WindowActions
from .buttons import Buttons
from .buttons import Shortcuts


class Actions(WindowActions, FileMenu, Record, Options, Other, Buttons, Shortcuts):
    pass
