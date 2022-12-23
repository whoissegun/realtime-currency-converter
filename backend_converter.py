import requests
import json
    
def convert(base:str,quote,amount):
    url = 'https://api.exchangerate-api.com/v4/latest/USD' #website used for getting real time exchange rates
    data = requests.get(url)
    info = data.text
    rates = json.loads(info)

    if base != 'USD': 
        exc_rate = float(rates['rates'][base]) #getting the exchange rate of the base currency
        amt_in_usd = amount/exc_rate
        exc_rate_1 = float(rates['rates'][quote]) #getting the echange rate of the quote currency
        final_amt = exc_rate_1 * amt_in_usd
        return round(final_amt,2)
    else:
        exc_rate = float(rates['rates'][quote])
        final_amt = amount * exc_rate
        return round(final_amt,2)
    

