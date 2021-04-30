import json
import os

class Config:

    FICHIER_CONFIG = "./config.json"
    
    def __init__(self, grosseurGrille=8, tickRate=1, longeurDebut=3):
        self._grosseurGrille = grosseurGrille
        self._tickRate = tickRate
        self._longeurDebut = longeurDebut
        
    def __repr__(self):
        affichage = "%s %s %s" %  (str(self.getGrosseurGrille()), str(self.getTickRate()), str(self.getLongeurDebut()))
        return affichage
    
    def getGrosseurGrille(self): return self._grosseurGrille
    
    def getTickRate(self): return self._tickRate
    
    def getLongeurDebut(self): return self._longeurDebut
    
    def setGrosseurGrille(self, valeur): self._grosseurGrille = int(valeur)
    
    def setTickRate(self, valeur): self._tickRate = int(valeur)
    
    def setLongeurDebut(self, valeur): self._longeurDebut = int(valeur)
    
    @classmethod
    def charger(cls):
        
        try:
            with open(cls.FICHIER_CONFIG, "r", encoding='utf-8') as fichier:
            
                donnees = json.load(fichier)
                return Config(donnees["grosseurGrille"], donnees["tickRate"], donnees["longeurDebut"])
        except:
            print("Json ne peut pas etre charger")
            return Config()
    
    def sauvegarder(self):
        try:
            with open(self.FICHIER_CONFIG, "w", encoding='utf-8') as fichier:
                
                donnees = {"grosseurGrille": self.getGrosseurGrille(),
                            "tickRate": self.getTickRate(),
                            "longeurDebut": self.getLongeurDebut()}
            
                json.dump(donnees, fichier, indent=2, ensure_ascii=False)
                
                fichier.truncate() # Efface l'exces
        except IOError as erreur:
            print("Erreur de ecriture json: " + erreur)
            