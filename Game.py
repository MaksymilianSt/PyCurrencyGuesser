from forex_python.converter import CurrencyCodes

from UserInputService import UserInputService


class Game:
    def __init__(self, currencyService):
        self.currencyService = currencyService
        self.userInputService = UserInputService()

    def play(self, player):
        print('fight' + player.user_name)
        failed = False
        while not failed:
            failed = self.play_round(player.score)
            if not failed:
                player.increment_stats()
        print(f'\n\t\t\t\t\t* {player.user_name} : failed with score: {player.score} *')

    def play_round(self, round_counter):
        print(f'\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t*ROUND* : {round_counter}\n\n')
        currencies = self.currencyService.get_two_random_currencies()
        (currency1, rate1), (currency2, rate2) = currencies.items()

        selected_currency = self.choose_currency((currency1, rate1), (currency2, rate2))

        return self.get_more_valuable_currency(rate1, rate2) == selected_currency[1]


    def choose_currency(self, first_cur_pair, second_cur_pair):
        userChoice = self.userInputService.get_user_input(
            self.userInputService.create_question(first_cur_pair, second_cur_pair))
        print(userChoice)
        return first_cur_pair if userChoice == 1 else second_cur_pair

    def get_more_valuable_currency(self, first, sec):
        return first if first < sec else sec


