from playsound import playsound


class SoundService:
    def __init__(self):
        pass

    def play_welcome_sound(self):
        playsound('sounds/welcome.mp3')

    def play_end_sound(self):
        playsound('sounds/end.mp3')

    def play_winner_sound(self):
        playsound('sounds/win.mp3')

    def play_lose_sound(self):
        playsound('sounds/fail.mp3')