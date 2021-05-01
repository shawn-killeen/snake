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

        self._logique = Logique(self)

        self.title("Snake - Shawn Killeen")
        #self.resizable(width=False, height=False)
        self._demarrerVue()
        
    ####################################
    ##          CONTROLEUR            ##
    ####################################
    
    def _demarrerVue(self):
        partie = Partie(self, self)
        partie.mainloop()
    
    ####################################
    ##            ACTIONS             ##
    ####################################
    # Callbacks des boutons de l'interface
    
    def actionDemarrer(self):
        self._logique.demarrerLoop()
    
    def actionOptions(self):
        pass
    
    def actionQuitter(self):
       self._logique.arreterLoop()
       self.quit()