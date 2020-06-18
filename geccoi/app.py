import cv2

from .settingsapi import get_settings_file
from .ic import GKeyboard, GMouse
from .gui import GeccoiInterface


class GeccoiApp:
    def __init__(self):

        self._settings = get_settings_file()

        self._mouse = GMouse(**self._settings.get("mouse"))
        self._keyboard = GKeyboard(**self._settings.get("keyboard"))

        self._gui = None

        self._model = None


    @property
    def gui(self):
        return self._gui

    def start_gui(self, debug=False):
        self._gui = GeccoiInterface(**self._settings, debug=debug)

        if not cv2.VideoCapture(0).read()[0]:
            self._gui.sg.popup("GeCCOI requires a camera to operate. \n No camera's could be found.",
                               font="Courier 28 bold")

        self._gui.window.finalize()
        self._gui.window["warning"](" " * 4 + "Warning: No Cameras Found", visible=True)
        self._gui.start_event_loop()

    def stop_gui(self):
        self._gui.window.close()
        self._gui = None
