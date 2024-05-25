import json
import os
from Player import Player

SCORES_FILE_PATH = "score"

class ScoreService:
    def __init__(self):
        self.score = []
        self.load_from_file()


    def add_player(self, player):
        self.score.append(player)
        self.save_to_file()

    def save_to_file(self):
        data = [{"name": player.user_name, "score": player.score} for player in self.score]
        with open(SCORES_FILE_PATH, 'w') as file:
            json.dump(data, file)

    def load_from_file(self):
        if os.path.exists(SCORES_FILE_PATH):
            with open(SCORES_FILE_PATH, 'r') as file:
                data = json.load(file)
                self.score = [Player(player_data["name"], int(player_data["score"])) for player_data in data]


    def get_scores(self):
       return sorted(self.score, key=lambda player: player.score, reverse=True)

    def __repr__(self):
        return f"PlayerList(players={self.players})"