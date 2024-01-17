class Stat:
    def __init__(self):
        self.prevRoundsScore = 0
        self.lastRoundScore = 0
    def setLastScore(self, Score:int):
        self.lastRoundScore = Score

    def doTurn(self):
        self.prevRoundsScore += self.lastRoundScore
        self.lastRoundScore = 0
