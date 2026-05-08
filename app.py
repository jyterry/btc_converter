import requests

def main():
    amount, currency = get_user_input()

    rate = get_exchange_rate(currency)

    btc_price = get_btc_price()

    print(f"{convert_to_btc(amount, rate, btc_price)} BTC")

def get_user_input():
    amount, currency = input("Please enter total amounts which should be sperated by blank, e.g. 200 USD: ").split(" ")
    amount = float(amount)
    return amount, currency

def get_exchange_rate(currency):
    if currency == "USD" or currency == "usd":
        return 1
    else:
        response = requests.get("https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/" + currency + ".json").json()
        return response[currency]["usd"]

def get_btc_price():
    response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd").json()
    return response["bitcoin"]["usd"]

def convert_to_btc(amount, rate, btc_price):
    return amount * rate / btc_price

if __name__ == "__main__":
    main()
