from modeles.score import Score
from modeles.config import Config
from datetime import datetime


print(Score.chargerScores())

score = Score("Shawn2", 10, datetime.now)
score.sauvegarder()

print(Score.chargerScores())