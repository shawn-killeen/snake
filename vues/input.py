from threading import Thread
import keyboard

class Input:
    
    ####################################
    ##            DUNDERS             ##
    ####################################
    
    def __init__(self, config):
        self._config = config
        self.direction = "up"
        
        if self._config.getTypeInput() == "clavier":
            self.inputClavier()
        elif self._config.getTypeInput() == "gpio":
            self.inputGPIO()
    
    ####################################
    ##        SETTERS/GETTERS         ##
    ####################################
    
    def getDirection(self):
        return self.direction
    
    def setDirection(self, value):
        self.direction = value
    
    ####################################
    ##             INPUT              ##
    ####################################
    
    def inputClavier(self):
            keyboard.add_hotkey('w', lambda: self.setDirection("up"))
            keyboard.add_hotkey('a', lambda: self.setDirection("left"))
            keyboard.add_hotkey('s', lambda: self.setDirection("down"))
            keyboard.add_hotkey('d', lambda: self.setDirection("right"))
            
    def inputGPIO(self):
        pass