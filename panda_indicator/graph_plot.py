import sys

import pandas
import pybacktest
#script = sys.argv[1]
script = '^NSEI'

ohlc = pybacktest.load_from_yahoo(script, adjust_close=True)
short_ma = 10
long_ma = 50

ms = pandas.rolling_mean(ohlc.C, short_ma)
ml = pandas.rolling_mean(ohlc.C, long_ma)

buy = cover = (ms > ml) & (ms.shift() < ml.shift())  # ma cross up
sell = short = (ms < ml) & (ms.shift() > ml.shift())

del cover
del short


bt = pybacktest.Backtest(locals(), 'ma_cross')

# import json
# json.dump(bt.report, open(script + '-output.json', 'w'))
# import matplotlib.pyplot as plt
#
#
# figure = plt.figure()
# bt.plot_equity()
# #fig = plotter.get_figure()
# figure.savefig(script+"-output.png")

#=======================================
# def smoothing_const(days):
#      return (2.0 / (days + 1))
#
# def average_list(list):
#     return sum(list)/len(list)
#
# def expon_moving_avg(list, days):
#     ema_index = [index if index > days - 1 else None if index != (days - 1) else average_list(list[index - (days-1) : index+1]) for index in range(days)]
#     def expon_mov_value(index):
#         if index <= len(list) -1:
#             ema_value =  smoothing_const(days) * (list[index] - ema_index[index -1]) + ema_index[index -1]
#             ema_index.append(ema_value)
#             expon_mov_value(index + 1)
#     expon_mov_value(days)
#     return ema_index

#=======================================

#demil code==============================
# def expon_moving_avg(list, days_ema, days_dema):
#     ema = pandas.rolling_mean(list, days_ema)
#     def expon_mov_value(index):
#         if index < len(list):
#             ema_value =  smoothing_const(days_ema) * (list[index] - ema[index -1]) + ema[index -1]
#             ema[index] = ema_value
#             expon_mov_value(index + 1)
#     expon_mov_value(days_ema)
#     dema = pandas.rolling_mean(ema, 10)
#     def double_ema_value(index):
#         if index < len(ema):
#             dema_value = smoothing_const(days_dema) * (ema[index] - dema[index -1]) + dema[index -1]
#             dema[index] = dema_value
#             double_ema_value(index + 1)
#     double_ema_value((days_ema-1)+days_dema)
#     return ema, dema
#=========================================