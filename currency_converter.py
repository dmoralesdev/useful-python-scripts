import requests

def convert_currency(amount, from_currency, to_currency):
    API_KEY = "your_api_key_here"
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"

    response = requests.get(url)
    data = response.json()
    exchange_rate = data["rates"][to_currency]

    return exchange_rate * amount

amount = float(input("Enter the amount to convert: "))
from_currency = input("Enter the currency to convert from: ").upper()
to_currency = input("Enter the currency to convert to: ").upper()

converted_amount = convert_currency(amount, from_currency, to_currency)
print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")
