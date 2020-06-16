import keyboard as _k


class GKeyboard:
    def __init__(self, **settings):
        """Sets self keyboard."""
        self._keyboard = _k
        
        """Gets self configuration settings from given settings."""
        self._configs = settings
        
        """Sets all settings for keyboard operation."""
        # No settings
    
    def type(self, *keys):
        """Joins all sent keys into one"""
        action = "".join(keys)
        
        self._keyboard.write(action)
    
    def shortcut(self, *keys):
        """Joins keys together into one"""
        shortcut = "".join(keys)
        
        self._keyboard.press_and_release(shortcut)
        