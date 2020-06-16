import cv2

from .settingsapi import get_settings_file
from .ic import GKeyboard, GMouse
from .gui import GeccoiInterface


class Controller:
    def __init__(self):
        self._settings = get_settings_file()

        self._mouse = GMouse(**self._settings.get("mouse"))
        self._keyboard = GKeyboard(**self._settings.get("keyboard"))

        self._gui = GeccoiInterface()
        self._gui.start_event_loop()

        if not cv2.VideoCapture(0).read()[0]:
            self._gui.sg.popup("GeCCOI requires a camera to operate. \n No camera's were found.")
        

    


