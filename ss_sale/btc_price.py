import requests
import json



headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36', 
        }
def get_btc_price():
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,CNY')
    data = json.loads(r.text)
    return data

if __name__ == '__main__':
    my = get_btc_price()
    print(my)
