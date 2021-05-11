from vues.partie import Partie
from modeles.config import Config
from modeles.caseSerpent import CaseSerpent
from threading import Thread
from time import sleep
import math

class Logique:
    
    ####################################
    ##            DUNDERS             ##
    ####################################
    
    def __init__(self, controleur, config, vue):
        self._controlleur = controleur
        self._config = config
        self._vue = vue
        
        self.stopBoucle = False 
        self.estDemarrer = False
        self.demarrerLoop()
    
    ####################################
    ##          CONTROLEUR            ##
    ####################################
    
    def demarrer(self):
        
        if self.estDemarrer:
            self._grille.generer()
        
        self._direction = "up"
        self._tick = 1/self._config.getTickRate()
        self._grille = self._vue.getGrille()
        self._creerSerpent()
        self.estDemarrer = True
    
    def demarrerLoop(self):
        # boucle
        
        self.stopBoucle = False
        thread = Thread(target = self._gameLoop)
        thread.start()
        
    def arreterLoop(self):
        self.stopBoucle = True
        
    ####################################
    ##             SNAKE              ##
    ####################################    

    def _gameLoop(self):
        
        count = 0
        while(not self.stopBoucle):
            
            if(self.estDemarrer):
                # On modifie les objets du jeu
                self._serpent.initierBouger(self._direction)
                
                # On affiche le jeu
                self._grille.dessinerSerpent(self._serpent)
                
                # Deroulement du jeu
                sleep(self._tick)
                
                count = count+1
                
                if count == 3:
                    self._direction = 'left' 
                elif count == 6:
                    self._direction = 'down'
                elif count == 9:
                    self._direction = 'right'
                elif count == 12:
                    self._direction = 'up'
                    CaseSerpent.allongerAuTick = True
                    count = 0
            else:
                sleep(1)
            
    def _creerSerpent(self):
        initiale = math.floor(self._config.getGrosseurGrille()/2)
        self._serpent =  CaseSerpent(self._config.getGrosseurGrille(), x=initiale, y=initiale, parent=None, enfant=None )
    
    