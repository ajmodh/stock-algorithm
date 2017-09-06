import sys
import pandas
import pybacktest
#script = sys.argv[1]
script = 'siemens.ns'

ohlc = pybacktest.load_from_yahoo(script, adjust_close=True)

lips_sma_period = 5
teeth_sma_period = 8
jaw_sma_period = 13

hl_diff = (ohlc.H+ ohlc.L)/ 2

ml1 = pandas.rolling_mean(hl_diff, lips_sma_period)
mt1 = pandas.rolling_mean(hl_diff, teeth_sma_period)
mj1 = pandas.rolling_mean(hl_diff, jaw_sma_period)

ml = ml1.shift(2)
mt = mt1.shift(4)
mj = mj1.shift(7)

buy = cover = (ml > mt) & (mt > mj) & ((ml.shift() < mt.shift()) | (mt.shift() < mj.shift()))
sell = short = (ml < mt) & (mt < mj) & ((ml.shift() > mt.shift()) | (mt.shift() > mj.shift()))

del cover
del short


bt = pybacktest.Backtest(locals(), 'alligator')
# df = pandas.DataFrame()
# df['ml'] = ml
# df['mt'] = mt
# df['mj'] = mj

# location = '/home/sigmasoft6/Desktop/alligator_test.xlsx'
# df = ohlc.copy()
# df['ml'] = ml
# df['mt'] = mt
# df['mj'] = mj
# df['buy'] = bt.signals['Buy']
# df['sell'] = bt.signals['Sell']
# df.to_excel(location,sheet_name='testing',index=True)

#print bt.signals.tail()
import json
json.dump(bt.report, open(script + '-output.json', 'w'))
import matplotlib.pyplot as plt
figure = plt.figure()
bt.plot_equity()
figure.savefig(script+"-output.png")