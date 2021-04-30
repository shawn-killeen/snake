from modeles.score import Score
from modeles.config import Config
from datetime import datetime


print(Score.chargerScores())

score = Score("Shawn", 10, datetime.now)

print(Config.charger())
Config(1, 2, 3).sauvegarder()