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
        try:
            aquired_settings[key] = settings[key]
        except KeyError:
            change_setting(key, None)
    
    return aquired_settings

def change_setting(setting_name, new_setting):
    settings_path = sys.executable + "\\lib\site-packages\geccoi\settings.json"

    with open(settings_path, "r") as existing:
        existing_settings = json.load(existing)
    
    with open(settings_path, "w") as new_settings:
        existing_settings[setting_name] = new_setting
        json.dump(existing_settings, new_settings)

    return {setting_name: new_setting}        
