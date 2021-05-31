import keyboard as _k
from translate import Translator


class GKeyboard:
    def __init__(self, **settings):
        """Sets self keyboard."""
        self._keyboard = _k

        """Gets self configuration settings from given settings."""
        self._configs = settings

        """Sets all settings for keyboard operation."""
        lang = self._configs.get("typing-language")
        self._language = lang if lang is not None else "en"
        self._translator = Translator(to_lang=self._language[-2:])

    def type(self, *keys):
        """Joins all sent keys into one"""
        keys = [self._translator.translate(key) for key in keys]
        action = "".join(keys)
        self._keyboard.write(action)

    def shortcut(self, *keys):
        """Joins keys together into one"""
        shortcut = "".join(keys)
        self._keyboard.press_and_release(shortcut)
