"""
Settings Manager API for the GUI
controller.py uses this to access the settings.

By @GrandMoff100
"""

import json, sys


def get_settings_file():
    """Retrieves the settings from settings.json in the package folder."""
    settings_path = sys.executable + "\\lib\site-packages\geccoi\settings.json"

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
        aquired_settings[key] = settings[key]
    
    return aquired_settings

        
