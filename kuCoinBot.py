import config
from kucoin.client import Client
import pandas as pd
import datetime
import time
client = Client(config.API_KU, config.API_KU_SCRT, config.API_PS)

# or connect to Sandbox
# client = Client(api_key, api_secret, api_passphrase, sandbox=True)

# get currencies

def generarInforme(mes,año):

    fecha = datetime.date(año,mes,1)
    if mes != 12:
        fecha2 = datetime.date(año, (mes+1), 1)
    else:
        fecha2 = datetime.date((año+1), 1, 1)
    ts = time.mktime(datetime.datetime.strptime(str(fecha), "%Y-%m-%d").timetuple()) * 1000
    ts2 = time.mktime(datetime.datetime.strptime(str(fecha2), "%Y-%m-%d").timetuple()) * 1000
    dep = client.get_deposits(currency='USDT')
    df = pd.DataFrame(dep['items'],
                          columns=['currency','status','address', 'amount', 'walletTxId','createdAt'])
    df = df[(df['createdAt'] > ts)&(df['createdAt']<ts2)]
    df['createdAt'] = pd.to_datetime(df['createdAt'], unit='ms')

    kline = client.get_kline_data("ETH-USDT",'1hour',int(ts/1000),int(ts2/1000))
    print(kline)
    df.to_excel('informe.xlsx', index=False)

generarInforme(4,2021)
# get market depth
#depth = client.get_order_book('KCS-BTC')

# get symbol klines
#klines = client.get_kline_data('KCS-BTC')


#orders = client.get_active_orders('KCS-BTC')