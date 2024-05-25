class Player:
    def __init__(self):
        self.user_name = '?'
        self.score = 0

    def __init__(self, name=None, score=None):
        if name is not None and score is not None:
            self.user_name = name
            self.score = score
        else:
            self.user_name = '?'
            self.score = 0

    def __repr__(self):
        return f"name= {self.user_name}, score= {self.score})"

    def increment_stats(self):
        self.score += 1

    def set_name(self):
        self.user_name = input('enter your name: ')
