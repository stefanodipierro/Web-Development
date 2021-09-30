## Importa pacchetti

import pandas as pd
from binance.client import Client
from datetime import datetime


# importa websocket

from binance.websockets import BinanceSocketManager
from twisted.internet import reactor


# init
api_key = 'owoQUF1z1tM7aguMmuMYtaRjVwyIGY0dLe4djVlAeBDi1xHqu3ayYHQ61b827e0o'
api_secret = '2KVvAWoLBGYg5Yjk914XCJmk7eRnpE0ZA2dkSWWw1lwcOGByRGs8Nz49NKKLFPVf'
client = Client(api_key, api_secret)

btc_price = {'error':False}
def btc_trade_history(msg):
    ''' define how to process incoming WebSocket messages '''
    if msg['e'] != 'error':

        btc_price['last'] = msg['c']

    else:
        btc_price['error'] = True


# init and start the WebSocket
bsm = BinanceSocketManager(client)
bsm.start_symbol_ticker_socket('BTCUSDT',btc_trade_history)


bsm.start()

# function to convert milliseconds string into datetime

def convert_todatetime (column):
    return column = datetime.fromtimestamp(int(column)/1000)



#list of pairs
                                                                                                                                                      ')
pairsList = ['BTCUSDT' , 'ADAUSDT' , 'BNBUSDT', 'ETHUSDT']

# as per Binance python docs
columnsList = [
    'open_time', 'open', 'high', 'low', 'close', 'volume',
    'close_time', 'quote_asset_volume', 'number_of_trades',
    'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume',
    'ignore'
]
#get historical kline data
'''pair is a string, example 'BTCUSDT'
interval is method , example Client.KLINE_INTERVAL_1MINUTE
startDate and endDate are strings, example '1 Dec, 2017' '''

def get_historical(pairsList, interval, startDate, endDate):

    for pair in pairsList:


        klines = client.get_historical_klines(pair, interval, startDate, endDate)
        globals()[f"df{pair}"] = pd.DataFrame(klines, columns = columnsList)
        globals()[f"df{pair}"]
        globals()[f"df{pair}"].set_index('close_time', drop = True, inplace = True)


        #figure out to set index to close time and convert to real date with datetime.fromtimestamp(int("1518308894652")/1000)



btc_df = pd.DataFrame(bars, columns=['date', 'open', 'high', 'low', 'close'])
btc_df.set_index('date', inplace=True)
btc_df.index
btc_df.head()


btc_df['MA 12'] = btc_df['close'].rolling(12).mean()

btc_df['close'].plot(figsize = (12,6), label = 'CLOSE' )
btc_df['MA 12'].plot( label = 'MA 12' )
plt.legend()





yearCount = 0
startingBalance = 7500
while yearCount < 365:
    startingBalance = startingBalance + (startingBalance/100)*1
    yearCount = yearCount + 1
    print(startingBalance)

 def compundInterest :
     while count < 31
     startingBalance = startingBalance + (startingBalance/ 100 )*7

     return startingBalance
