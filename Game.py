from forex_python.converter import CurrencyCodes


class Game:
    def __init__(self, currencyService):
        self.currencyService = currencyService

    def play(self, player):
        print('fight' + player.userName)
        failed = False
        while not failed:
            failed = self.playRound()
            player.incrementStats()

    def playRound(self):

        currencies = self.currencyService.get_two_random_currencies()
        (currency1, rate1), (currency2, rate2) = currencies.items()

        self.guessCurrency((currency1, rate1), (currency2, rate2))
        return True

    def guessCurrency(self,first_cur_pair, second_cur_pair ):

        print('userInput')
        print(self.getUserInput(self.createQuestion(first_cur_pair, second_cur_pair)))


    def getUserInput(self, question_message):
        userChoise = int(input(question_message))
        while userChoise > 2 or userChoise < 1:
            print('podana zla wartosc wybierz 1 lub 2')
            userChoise = int(input(question_message))
        return userChoise

    def createQuestion(self, first_currency, sec_currency):
        first_currency_info = self.create_currency_label(first_currency[0])
        sec_currency_info = self.create_currency_label(sec_currency[0])
        round = "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t*ROUND*\n\n"
        main_label = "press: '1' to select: " +first_currency_info + "\t\t\t vs \t\t\t" + "press: '2' to select: " + sec_currency_info
        return  round + main_label + "\n" + ':'

    def create_currency_label(self, currency):
        return ('[ ' + currency + ', ' + CurrencyCodes().get_symbol(currency)) + ',' + CurrencyCodes().get_currency_name(currency) + ']'

#         print(CurrencyCodes().get_currency_name('EUR'))
# print(CurrencyCodes().get_symbol('EUR'))
# print(CurrencyCodes().get_currency_code_from_symbol('zł'))
# Game(api).play(Player())
