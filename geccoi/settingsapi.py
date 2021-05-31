"""
Settings Manager API for the GUI
app.py uses this to access the settings.

By @GrandMoff100
"""

import json
import os


settings_path = os.path.join(
    os.getcwd(),
    "settings.json"
)


def get_settings_file():
    """Retrieves the settings from settings.json in the current working directory."""
    create_settings_file()
    with open(settings_path, "r") as settings:
        return json.load(settings)


def create_settings_file():
    if not settings_exists():
        with open(settings_path, "w") as j:
            json.dump(
                {
                    "general": {
                        "theme": "Geccoi"
                    },

                    "keyboard": {
                        "typing-language": "English - en"
                    },

                    "mouse": {
                        "sensitivity": 50,
                        "inversed": False
                    }

                }, j, indent=4
            )


def settings_exists():
    return True if os.path.isfile(settings_path) else False


def change_setting(key, category, new_setting):
    with open(settings_path, "r") as file:
        settings = json.load(file)
    settings[category][key] = new_setting
    with open(settings_path, "w") as file:
        json.dump(settings, file)
