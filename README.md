# BTC Currency Converter 

A simple Python command-line tool that converts fiat currencies into Bitcoin using real-time exchange rates and BTC market price.

---

## Features
• Lightweight and easy to run
• Convert any supported fiat currency to USD
• Fetch real-time USD-based Bitcoin price 
• Calculate how much BTC you can buy with a given amount

## How It Works
This project uses two public APIs and a library:

1. requests library
   
2. Currency exchange rate API
   - Converts user input currency → USD
   - From [exchange rate API by fawazahmed0](https://github.com/fawazahmed0/exchange-api)

3. Bitcoin price API (CoinGecko)  
   - Gets current BTC price in USD
   - From [BTC price API](https://api.coingecko.com/api/v3/simple/price)

Then it performs the calculation:
    BTC = (amount in USD) / (BTC price in USD)

## Installation

```bash
git clone https://github.com/your-username/btc-converter.git
cd btc-converter
pip install requests
```

## Usage

```bash
python app.py
```

Examples:

```
Enter amount and currency (e.g. 200 USD): 100 CNY
```

Output:

```
0.00018434260386976885 BTC
```


## Future Improvements

The first version was released on May 8, 2026 , in the future I'll

• Add error handling for potential errors
• Display exchange rate and btc price details
• Add web UI
• Provide history search
...

### About

This is my first Python project inspired by CS50P. It is still under development and will be improved over time.
