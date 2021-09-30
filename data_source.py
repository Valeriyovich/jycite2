import websocket
import json
import requests
from datetime import datetime
from sqlalchemy import create_engine
from config import Config
from portfolio.utils import get_close_price
try:
    import thread
except ImportError:
    import _thread as thread
from datetime import datetime
db = create_engine(Config.SQLALCHEMY_DATABASE_URI)


def update_symbols():
    symbols = db.execute('SELECT symbol FROM tickers_data;')
    global symbols_string
    global symbols_date
    symbols_string = ''
    symbols_date = int(datetime.now().timestamp())
    for symbol in symbols.fetchall():
        symbols_string += symbol[0] + ','


def on_message(wsapp, message):
    if int(datetime.now().timestamp()) - symbols_date > 10:
        update_symbols()
        wsapp.send('{"action": "reset"}')
        wsapp.send('{"action": "subscribe","params": {"symbols": "%s"}}' % symbols_string)

    msg = json.loads(message)
    if msg['event'] == 'price':
        now_ts = int(datetime.now().timestamp())
        date_changed = db.execute('SELECT close_price_updated FROM tickers_data WHERE symbol="%s"' % msg['symbol'])
        date_changed = date_changed.first()[0]
        req = ''
        close_price = get_close_price(msg['symbol'])
        if not date_changed or now_ts - date_changed > 86400:
            req = ', close_price="%s", close_price_updated="%s"' % (close_price, now_ts)
        db.execute('UPDATE tickers_data SET last_price="%s", date_changed="%s" %s '
                   'WHERE symbol = "%s";' % (msg['price'], now_ts, req, msg['symbol']))
        path_symbol = msg['symbol'].replace('/', '_')
        requests.get('http://127.0.0.1:5000/test_2/%s' % path_symbol)


def on_open(wsapp):
    def run():
        update_symbols()
        wsapp.send('{"action": "subscribe","params": {"symbols": "%s"}}' % symbols_string)
    thread.start_new_thread(run, ())


while True:
    wsapp = websocket.WebSocketApp("wss://ws.twelvedata.com/v1/quotes/price?apikey=49e355ddf97e440aa449ec7bab6233bc",
            on_message=on_message)
    wsapp.on_open = on_open
    print("start")
    wsapp.run_forever(ping_interval=65, ping_timeout=60)
    print("close")
