"""
Settings Manager API for the GUI
controller.py uses this to access the settings.

By @GrandMoff100
"""

import json, sys, os


def get_settings_file():
    """Retrieves the settings from settings.json in the package folder."""
    settings_path = sys.executable + "\\lib\\site-packages\\geccoi\\settings.json"

    try:
        with open(settings_path, "r") as settings:
            return json.load(settings)
    except FileNotFoundError:
        with open(settings_path, "w") as settings:
            json.dump({}, settings)

        return {}


def get_settings(*setting_names):
    """Returns setting values by given names."""
    settings_path = sys.executable + "\\lib\\site-packages\\geccoi\\settings.json"

    aquired_settings = {}

    settings = get_settings_file()

    for key in setting_names:
        try:
            aquired_settings[key] = settings[key]
        except KeyError:
            change_setting(key, None)

    return aquired_settings


def create_settings_file():
    settings_path = sys.executable + "\\lib\\site-packages\\geccoi\\settings.json"

    if not settings_exists():
        with open(settings_path, "w") as j:
            json.dump(
                {
                    "general": {
                        "theme": "DarkBlue",
                        "run-in-background": False,
                        "on-startup": False
                    },

                    "keyboard": {

                    },

                    "mouse": {
                        "sensitivity": 50,
                        "inversed": False
                    }

                },
                j)


def settings_exists():
    return True if os.path.exists(sys.executable + "\\lib\\site-packages\\geccoi\\settings.json") else False
