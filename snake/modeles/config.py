# Shawn Killeen - Travail Pratique Synthese
# College Montmorency - H2021 4B5 - S. Deschenes

import json
import os

class Config:

    FICHIER_CONFIG = "./stockage/config.json"
    
    ####################################
    ##            DUNDERS             ##
    ####################################
    
    def __init__(self, grosseurGrille=8, tickRate=1, longeurDebut=3, typeInput="clavier"):
        self._grosseurGrille = grosseurGrille
        self._tickRate = tickRate
        self._longeurDebut = longeurDebut
        self._typeInput = typeInput
        
    def __repr__(self):
        affichage = "%s %s %s" %  (str(self.getGrosseurGrille()), str(self.getTickRate()), str(self.getLongeurDebut()))
        return affichage
    
    ####################################
    ##            GETTERS             ##
    ####################################
    
    def getGrosseurGrille(self): 
        return self._grosseurGrille
    
    def getTickRate(self): 
        return self._tickRate
    
    def getLongeurDebut(self): 
        return self._longeurDebut
    
    def getTypeInput(self):
        return self._typeInput
    
    ####################################
    ##            SETTERS             ##
    ####################################
    
    def setGrosseurGrille(self, valeur): self._grosseurGrille = int(valeur)
    
    def setTickRate(self, valeur): self._tickRate = int(valeur)
    
    def setLongeurDebut(self, valeur): self._longeurDebut = int(valeur)
    
    def setTypeInput(self, valeur): self._typeInput = str(valeur)
    
    ####################################
    ##            DONNEES             ##
    ####################################
    
    # Chargement du fichier de configuration en json Si le fichier 
    # n'existe pas, le programme charge le constructeur defaut
    @classmethod
    def charger(cls):
        
        try:
            with open(cls.FICHIER_CONFIG, "r", encoding='utf-8') as fichier:
            
                donnees = json.load(fichier)
                return Config(grosseurGrille=donnees["grosseurGrille"], 
                              tickRate=donnees["tickRate"], 
                              longeurDebut=donnees["longeurDebut"], 
                              typeInput=donnees["input"])
        except:
            print("Json ne peut pas etre charger")
            return Config()
    
    # Sauvegarde de la configuration en json, le contenu du fichier est ecraser
    def sauvegarder(self):
        try:
            with open(self.FICHIER_CONFIG, "w", encoding='utf-8') as fichier:
                
                donnees = {"grosseurGrille": self.getGrosseurGrille(),
                            "tickRate": self.getTickRate(),
                            "longeurDebut": self.getLongeurDebut(),
                            "input": self.getTypeInput()}
            
                json.dump(donnees, fichier, indent=2, ensure_ascii=False)
                
                fichier.truncate() # Efface l'exces
        except IOError as erreur:
            print("Erreur de ecriture json: " + erreur)
            