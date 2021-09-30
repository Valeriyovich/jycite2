from requests import get
from config import Config


def get_quotes(symbols):
    url = 'https://api.twelvedata.com/'
    quote = 'quote?'
    price = 'price?'
    apikey = '&apikey=' + Config.TWELVEDATA_API_KEY
    symbols = 'symbol=%s' % symbols

    quote_url = url + quote + symbols + apikey
    price_url = url + price + symbols + apikey

    quotes = get(quote_url).json()
    price = get(price_url).json()

    return [quotes, price]


def get_close_price(symbol):
    url = 'https://api.twelvedata.com/'
    quote = 'quote?'
    apikey = '&apikey=' + Config.TWELVEDATA_API_KEY
    symbols = 'symbol=%s' % symbol

    url = url + quote + symbols + apikey

    quote = get(url).json()

    return quote['close']
