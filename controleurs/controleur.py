from vues.partie import Partie
from controleurs.logique import Logique
from modeles.config import Config
from tkinter import Tk
from threading import Thread
from time import sleep

class Controleur(Tk):
    
    
    ####################################
    ##            DUNDERS             ##
    ####################################
    
    def __init__(self):
        super().__init__()

        self._config = Config.charger()

        self.title("Snake - Shawn Killeen")
        self._partie = Partie(self, self, config=self._config)

        self._logique = Logique(controleur=self, config=self._config , vue=self._partie)
    
        self._partie.mainloop()
        
    ####################################
    ##          CONTROLEUR            ##
    ####################################
    
    ####################################
    ##            ACTIONS             ##
    ####################################
    # Callbacks des boutons de l'interface
    
    def actionDemarrer(self):
        self._logique.demarrer()
    
    def actionOptions(self):
        pass
    
    def actionQuitter(self):
       self._logique.arreterLoop()
       self.quit()