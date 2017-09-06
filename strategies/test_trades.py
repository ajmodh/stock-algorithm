import pandas as pd
import pybacktest as pbt
import datetime as dt
import supertrand as sptd

script = '^nsei'
ohlc = pbt.load_from_yahoo(script, adjust_close=True)
location = '/home/sigmasoft6/Desktop/indicator/nifty.xlsx'
ohlc1 = pd.read_excel(location, 0)
ohlc1.index = ohlc1['Date']
del ohlc1['Date']
start = ohlc1.index.searchsorted(dt.datetime(2007,01,01))
ohlc = ohlc1[start:]

#supertrand===========================
moving_small = sptd.supertrand(ohlc)
buy = cover = (ohlc.C > moving_small) & (ohlc.C.shift() < moving_small.shift())
sell = short = (ohlc.C < moving_small) & (ohlc.C.shift() > moving_small.shift())
del cover
del short
#=====================================

#===========excel export=============
bt = pbt.Backtest(locals(), 'suprtrand')
location = '/home/sigmasoft6/Desktop/traded_sheet_output/suptndss.xlsx'
df = ohlc.copy()
df['ms'] = moving_small
# df['ml'] = moving_long
df['buy'] = bt.signals['Buy']
df['sell'] = bt.signals['Sell']
df.to_excel(location,sheet_name='testing',index=True)
#====================================

#==========graph ploat===============
# del cover
# del short
# bt = pbt.Backtest(locals(), 'aj')
# import json
# json.dump(bt.report, open(script + '-output.json', 'w'))
# import matplotlib.pyplot as plt
# figure = plt.figure()
# bt.plot_equity()
# figure.savefig(script+"-output.png")
#=====================================

# bt = pbt.Backtest(locals(), 'stg')