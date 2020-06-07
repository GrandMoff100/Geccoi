import keyboard as k
import mouse as m
import os, json


class Controller:
    def __init__(self):
        with open(os.getcwd() + "\\settings.json", "r") as settings:
            self._settings = json.load(settings)


