from threading import Thread
import keyboard
from gpiozero import *
from time import sleep

class Output:
    
    ####################################
    ##            DUNDERS             ##
    ####################################
    
    def __init__(self):
        # Au cas ou on roule le jeu en dehor s du Raspberry pi
        try: 
            self.graphique = LEDBarGraph(22,6,13,26,16,12,5,25,24,23, initial_value=0, pwm=True)
            self.buzzer = Buzzer(19)
        except GPIOZeroError as erreur:
            self.graphique = None
            self.buzzer = None
            print("pas de gpio")
    
    ####################################
    ##              OUTPUT            ##
    ####################################
    
    
    def setPoints(self, value):
        if self.graphique is not None:
            self.graphique.value = min(value/10, 1)
    
    
    def sonner(self, nbr=1):
        if self.buzzer is not None:
            self.buzzer.beep(on_time=0.25, off_time=0.25, n=nbr)
