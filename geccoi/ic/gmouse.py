import mouse as _m


class GMouse:
    def __init__(self, **settings):
        """Sets self mouse module."""
        self._mouse = _m
        
        """Gets self configuration settings from given settings."""
        self._configs = settings
        
        """Sets all settings for mouse operation."""
        self._sensitivity = self._configs.get("sensitivity")
        self._inverted = self._configs.get("inverted")
        
    def move(self, delta_x, delta_y):
        delta_x = round(delta_x)
        delta_y = round(delta_y)
        
        if self._inverted:
            delta_x *= -1
            delta_y *= -1
        
        delta_x *= self._sensitivity
        delta_y *= self._sensitivity

        x = self._mouse.get_position()[0]
        y = self._mouse.get_position()[1]

        self._mouse.move(x + delta_x, y + delta_y)
        
    def set_left_state(self, state):
        if state == "up":
            # set mouse left click released
            self._mouse.release("left")
        elif state == "down":
            # set mouse left click down
            self._mouse.press("left")
        
    def set_right_state(self, state):
        if state == "up":
            # set mouse right click released
            self._mouse.release("right")
        elif state == "down":
            # set mouse right click down
            self._mouse.press("right")
    
    def set_middle_state(self, state):
        if state == "up":
            # set mouse middle click released
            self._mouse.release("left")
        elif state == "down":
            # set mouse middle click down
            self._mouse.press("left")
