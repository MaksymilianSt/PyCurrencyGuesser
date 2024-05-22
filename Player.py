class Player:
    def __init__(self):
        self.userName = '?'
        self.score = 0
        self.rounds = 0

    def incrementStats(self):
        self.score += 1
        self.rounds += 1
