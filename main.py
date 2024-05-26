
from CurrencyAPIService import CurrencyAPIService
from Game import Game
from Player import Player
from ScoreService import ScoreService
from SoundService import SoundService
from UserInputService import UserInputService

SPACE_LABEL = '\n-------------------------------------------------------------------\n'

user_input_service = UserInputService()

def start():
    sound_service = SoundService()
    currency_service = CurrencyAPIService()
    game = Game(currency_service)
    scoresService = ScoreService()
    sound_service.play_welcome_sound()
    while True:
        choice = user_input_service.get_main_user_choice()
        if choice == 'q':
            print("Quitting...")
            sound_service.play_end_sound()
            break
        else:
            if choice == 1:
                print(SPACE_LABEL)
                new_player = Player()
                new_player.set_name()
                game.play(new_player)
                scoresService.add_player(new_player)
                print(SPACE_LABEL)

            if choice == 2:
                print(SPACE_LABEL)
                print('first player')
                player1 = Player()
                player1.set_name()
                print('second player')
                player2 = Player()
                player2.set_name()
                winner = game.pvp(player1, player2)
                scoresService.add_player(winner)
                sound_service.play_winner_sound()

            if choice == 3:
                print(SPACE_LABEL)
                print('\t\t\t\t\t **SCORES**\n')
                for index, score in enumerate(scoresService.get_scores()):
                    print(f'\t\t{index} : {score}')
                print(SPACE_LABEL)

start()