"""User Interface for Geccoi Management"""

import tkinter

import PySimpleGUI as sg

from geccoi.settingsapi import get_settings_file, change_setting


class GeccoiInterface:
    def __init__(self, debug=False, **settings):
        self._sg = sg
        self.debug = debug

        self.settings = settings

        self._sg.LOOK_AND_FEEL_TABLE["Geccoi"] = {
            'BACKGROUND': '#757575',
            'TEXT': '#74c93a',
            'INPUT': '#949494',
            'SCROLL': '#58ad1f',
            'TEXT_INPUT': '#8ced4a',
            'BUTTON': ('white', '#6D9F85'),
            'PROGRESS': sg.DEFAULT_PROGRESS_BAR_COLOR,
            'BORDER': 0,
            'SLIDER_DEPTH': 0,
            'PROGRESS_DEPTH': 0
        }

        self._sg.theme(get_settings_file().get("general").get("theme"))

        self._layout = [
            [self._sg.Text(" " * 100), self._sg.Button("Exit", button_color=("#e00000", self._sg.LOOK_AND_FEEL_TABLE["Geccoi"]["BACKGROUND"]), size=(6, 1))],
            [self._sg.Text("_" * 80, font="Courier 15 bold")],
            [self._sg.Text(" "), self._sg.Text("Geccoi Manager", font="Courier 30 bold")],
            [self._sg.Text("Warning:", key="warning", size=(80, 1), visible=False, font="Courier 18 bold", text_color="darkred")],
            [self._sg.Text(" " * 40), self._sg.Button("Start", font="Courier 15", button_color=("white", "#07c700"), size=(12, 1), key="-S/S-")],
            [self._sg.Text("")],
            [self._sg.Text(" " * 8), self._sg.Text('Settings', font="Courier 24 bold")],
            # Rest of the toggleable settings.
            [self._sg.Text(" " * 16), self._sg.Text("General:", font="Courier 16 bold")],
            [self._sg.Text(" " * 20), self._sg.Text("Manager Theme: ", font="Courier 12 "), self._sg.In(self.settings.get("general").get("theme"), key="Theme", size=(15, 1), background_color=self._sg.DEFAULT_BACKGROUND_COLOR)],
            [self._sg.Text(" " * 16), self._sg.Text("Keyboard:", font="Courier 16 bold")],
            [self._sg.Text(" " * 20), self._sg.Text("Typing Language", font="Courier 12"), self._sg.Listbox(["English - en", "Spanish - es", "Chinese - zh", "French - fr", "German - de"], default_values=[settings.get("keyboard").get("typing-language")], size=(15, 5))],
            [self._sg.Text(" " * 16), self._sg.Text("Mouse:", font="Courier 16 bold")],
            [self._sg.Text(" " * 20), self._sg.Text("Sensitivity: ", font="Courier 12"), self._sg.Slider((0, 100), self.settings.get("mouse").get("sensitivity"), tick_interval=50, orientation="h", key="Sensitivity")],
            [self._sg.Text(" " * 20), self._sg.Text("Inverted: ", font="Courier 12"), self._sg.Radio("No", "Invert", key="inv-set-no", default=not self.settings.get("mouse").get("inversed")), self._sg.Radio("Yes", "Invert", default=self.settings.get("mouse").get("inversed"), key="inv-set-yes")],
            [self._sg.Text("")],
            [self._sg.Text("_" * 15, font="Courier 15 bold"), self._sg.Submit("Save All", font="Courier 12 bold", key="save-settings", button_color=("white", self._sg.DEFAULT_BACKGROUND_COLOR), size=(10, 1)), self._sg.Text("_" * 15, font="Courier 15 bold")]
        ]

        self._window = self._sg.Window('Geccoi Manager', self._layout, size=(500, self._get_display_res()[1]), no_titlebar=True)

    def _get_display_res(self):
        # Get Display Resolution.
        root = tkinter.Tk()
        root.withdraw()
        return root.winfo_screenwidth(), root.winfo_screenheight()

    def start_event_loop(self):
        while True:
            event, values = self._window.read()
            if self.debug:
                print(event, values)

            if event == "-S/S-":
                if self._window["-S/S-"].get_text() == "Start":
                    self._window["-S/S-"]("Stop", button_color=("white", "red"))
                else:
                    self._window["-S/S-"]("Start", button_color=("white", "#07c700"))
            elif event == "save-settings":
                change_setting("theme", "general", values.get("Theme"))
                change_setting("typing-language", "keyboard", values.get("typing-language"))
                change_setting("sensitivity", "mouse", values.get("Sensitivity"))
                change_setting("inversed", "mouse", values.get("inv-set-yes"))

            if event in (None, "Exit"):
                break

        self._window.close()

    @property
    def sg(self):
        return self._sg

    @property
    def window(self):
        return self._window
