import mouse as _m


class GMouse:
    def __init__(self, **settings):
        """Sets self mouse module."""
        self._mouse = _m
        
        """Gets self configuration settings from given settings."""
        self._configs = settings
        
        """Sets all settings for mouse operation."""
        self._sensitivity = self._configs.get("mouse").get("sensitivity")
        self._inversed = self._configs.get("mouse").get("inverse")
        
    def move(self, delta_x, delta_y):
        delta_x = round(delta_x)
        delta_y = round(delta_y)
        
        if self._inversed:
            delta_x *= -1
            delta_y *= -1
        
        delta_x *= self._sensitivity
        delta_y *= self._sensitivity

        self._mouse.move(delta_x, delta_y)
        
    def set_left_state(self, state):
        if state == "up":
            # set mouse left click released
            pass
        elif state == "down":
            # set mouse left click down
            pass
        
    def set_right_state(self, state):
        if state == "up":
            # set mouse right click released
            pass
        elif state == "down":
            # set mouse right click down
            pass
    
    def set_middle_state(self, state):
        if state == "up":
            # set mouse middle click released
            pass
        elif state == "down":
            # set mouse middle click down
            pass
