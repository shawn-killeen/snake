from vues.partie import Partie
from modeles.config import Config
from threading import Thread
from time import sleep

class Logique:
    
    ####################################
    ##            DUNDERS             ##
    ####################################
    
    def __init__(self, controleur):
        self._controlleur = controleur
    
    ####################################
    ##          CONTROLEUR            ##
    ####################################
    
    def demarrerLoop(self):
        self.stopBoucle = False
        thread = Thread(target = self._gameLoop)
        thread.start()
        
    def arreterLoop(self):
        self.stopBoucle = True
        
    ####################################
    ##             SNAKE              ##
    ####################################    

    def _gameLoop(self):
        while(True):
            print("Boucle")
            sleep(1)
            if self.stopBoucle: break