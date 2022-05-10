import config
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import pandas as pd


def informe():
    client = Client(config.API_KEY, config.API_SECRET)
    dphistory = client.get_deposit_history(coin="ETH")
    df = pd.DataFrame(dphistory,
                      columns=['amount', 'coin', 'network', 'status', 'address', 'addressTag', 'txId', 'insertTime',
                               'transferType', 'unlockConfirm'])
    #df.insertTime = df.insertTime.apply(lambda x: pd.to_datetime(x, utc=True, unit='ms'))
    df['insertTime'] = pd.to_datetime(df['insertTime'], unit='ms')
    df.columns = ['Monto', 'Moneda','Red', 'Estado', 'Direccion','Addr Tag','txId','Tiempo','Transferencia','ConfLock']
    del df['Transferencia']
    del df['Addr Tag']
    del df['Estado']
    del df['ConfLock']
    df.to_excel('informe.xlsx', index=False)

def saliente():
    client = Client(config.API_KEY, config.API_SECRET)
    dp = client.get_withdraw_history()
    print(dp)
saliente()