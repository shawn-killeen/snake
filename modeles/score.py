from datetime import datetime

class Score:
    
    def __init__(self, nom, score, date=None, rang=-1):
        self._nom = nom
        self._score = score
        self._rang = rang
        
        if date is None: 
            self._date = datetime.now
        else: 
            self._date = date
            
    def getNom(self):
        return self._nom
    
    def getScore(self):
        return self._score        
    
    def getDate(self):
        return self._date
    
    def getRang(self):
        return self._rang
    
    def __repr__(self):
        affichage = "%s %s %s %s" %  (str(self.getRang()), str(self.getScore()), str(self.getNom()), str(self.getDate()))
        return affichage
    
    