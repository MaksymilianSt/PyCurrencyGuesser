from forex_python.converter import CurrencyCodes

class UserInputService:
    def __init__(self):
        pass

    def get_user_input(self, question_message):
        userChoise = int(input(question_message))
        while userChoise > 2 or userChoise < 1:
            print('podana zla wartosc wybierz 1 lub 2')
            userChoise = int(input(question_message))
        return userChoise

    def create_question(self, first_currency, sec_currency):
        first_currency_info = self.create_currency_label(first_currency[0])
        sec_currency_info = self.create_currency_label(sec_currency[0])

        main_label = "press: '1' to select: " +first_currency_info + "\t\t\t vs \t\t\t" + "press: '2' to select: " + sec_currency_info
        return  main_label + "\n" + ':'

    def create_currency_label(self, currency):
        symbol = CurrencyCodes().get_symbol(currency) if (CurrencyCodes().get_symbol(currency)) is not None else '?'
        name = CurrencyCodes().get_currency_name(currency)  if CurrencyCodes().get_currency_name(currency) is not None else '?'
        return '[ ' + currency + ', ' + symbol + ',' + name + ']'