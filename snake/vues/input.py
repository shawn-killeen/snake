from threading import Thread
import keyboard
import gpiozero
from time import sleep

try:
    from libs.ADCDevice import *
except ImportError:
    print("pas de raspberry pi (import librarie)")

class Input:
    
    ####################################
    ##            DUNDERS             ##
    ####################################
    
    def __init__(self, config):
        self._config = config
        self.direction = "up"
        
        typeInput = self._config.getTypeInput()
        if typeInput == "clavier" or typeInput == "tout":
            try:
                self.inputClavier()
            except:
                print("erreur input clavier")
        if typeInput == "gpio" or typeInput == "tout":
            try:
                self.adc = ADS7830()
                self.inputGPIO()
            except:
                print("erreur input gpio")
    
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
        
        self.stopBoucle = False
        thread = Thread(target = self.boucleJoystick)
        thread.start()
        
    def arreterLoop(self):
        self.stopBoucle = True
    
    @staticmethod
    def clampJoystick(val):
        if(val > 200): val = 1
        elif(val < 100): val = -1
        else: val = 0
        return -val
    
    def boucleJoystick(self):
        while not self.stopBoucle:
            y = Input.clampJoystick(self.adc.analogRead(1))
            x = Input.clampJoystick(self.adc.analogRead(0))
            
            direction = None
            if x == 1 and y == 0:
                direction = "right"
            elif x == -1 and y == 0:
                direction = "left"
            elif x == 0 and y == -1:
                direction = "down"
            elif x == 0 and y == 1:
                direction = "up"
                
            if direction is not None:
                self.setDirection(direction)
                
            sleep(0.1)