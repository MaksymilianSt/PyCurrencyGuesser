from forex_python.converter import CurrencyCodes

from CurrencyAPIService import CurrencyAPIService
from Game import Game
from Player import Player
# Example usage:
if __name__ == "__main__":
    api = CurrencyAPIService()
    api.fetch_data()

    rate_to_eur = api.get_all_rates()
    if rate_to_eur:
        print(f"Exchange rate from USD to EUR: {rate_to_eur}")

    all_rates = api.get_all_rates()
    if all_rates:
        print("All exchange rates:", all_rates)

print(CurrencyCodes().get_currency_name('EUR'))
print(CurrencyCodes().get_symbol('EUR'))
print(CurrencyCodes().get_currency_code_from_symbol('zł'))
Game(api).play(Player())