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

    def get_main_user_choice(self):
        while True:
            print("Choose an option:")
            print("1: to play a game")
            print("2: pvp")
            print("3: to see score")
            print("q: Quit")
            choice = input("Enter your choice: ")

            if choice == 'q':
                return choice
            elif choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= 3:
                    return choice
                else:
                    print("Invalid choice, please enter a number between 1 and 3.")
            else:
                print("Invalid input, please enter a number or 'q' to quit.")