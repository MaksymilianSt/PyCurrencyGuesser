
from CurrencyAPIService import CurrencyAPIService
from Game import Game
from Player import Player
from ScoreService import ScoreService

SPACE_LABEL = '\n-------------------------------------------------------------------\n'

def get_user_choice():
    while True:
        print("Choose an option:")
        print("1: to play a game")
        print("2: to see score")
        print("q: Quit")
        choice = input("Enter your choice: ")

        if choice == 'q':
            return choice
        elif choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= 5:
                return choice
            else:
                print("Invalid choice, please enter a number between 1 and 5.")
        else:
            print("Invalid input, please enter a number or 'q' to quit.")

def start():
    currency_service = CurrencyAPIService()
    scoresService = ScoreService()
    while True:
        choice = get_user_choice()
        if choice == 'q':
            print("Quitting...")
            break
        else:
            if choice == 1:
                print(SPACE_LABEL)
                new_player = Player()
                new_player.set_name()
                Game(currency_service).play(new_player)
                scoresService.add_player(new_player)
                print(SPACE_LABEL)
            if choice == 2:
                print(SPACE_LABEL)
                print('\t\t\t\t\t **SCORES**\n')
                for index, score in enumerate(scoresService.get_scores()):
                    print(f'\t\t{index} : {score}')
                print(SPACE_LABEL)


start()