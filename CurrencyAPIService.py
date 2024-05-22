import requests
import random

class CurrencyAPIService:
    def __init__(self):
        self.base_url = "https://open.er-api.com/v6/latest/USD"
        self.rates = {}
        self.fetch_data()

    def fetch_data(self):
        try:
            response = requests.get(self.base_url)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            data = response.json()
            if data.get("result") == "success":
                self.rates = data.get("rates", {})
            else:
                print("Failed to fetch data: ", data.get("error-type", "Unknown error"))
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            self.rates = {}

    def get_all_rates(self):
        return self.rates

    def get_two_random_currencies(self):
        if len(self.rates) < 2:
            print("Not enough currencies to select from.")
            return None

        selected_currencies = random.sample(list(self.rates.items()), 2)
        return dict(selected_currencies)