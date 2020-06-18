"""
Settings Manager API for the GUI
app.py uses this to access the settings.

By @GrandMoff100
"""

import json, sys, os


def get_settings_file():
    """Retrieves the settings from settings.json in the current working directory."""
    settings_path = os.getcwd() + "\\settings.json"

    create_settings_file()

    with open(settings_path, "r") as settings:
        return json.load(settings)



def create_settings_file():

    settings_path = os.getcwd() + "\\settings.json"
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

                },
                j)


def settings_exists():
    return True if os.path.isfile(os.getcwd() + "\\settings.json") else False

def change_setting(key, category, new_setting):
    settings_path = os.getcwd() + "\\settings.json"

    with open(settings_path, "r") as file:
        settings = json.load(file)

    settings[category][key] = new_setting

    with open(settings_path, "w") as file:
        json.dump(settings, file)