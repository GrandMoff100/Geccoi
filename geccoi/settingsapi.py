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


def create_settings_file():
    settings_path = sys.executable + "\\lib\\site-packages\\geccoi\\settings.json"

    if not settings_exists():
        with open(settings_path, "w") as j:
            json.dump(
                {
                    "general": {
                        "theme": "Geccoi",
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
