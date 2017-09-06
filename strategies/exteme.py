import pandas as pd
import pybacktest as pbt
import ema as e
import tema as t
import macd as m
import rsi as r
import numpy as np
from collections import OrderedDict as od
# nifty_data = pbt.load_from_yahoo('^nsei', start = '2014' , adjust_close= True)

def crossover(ms, ml):
    buy = (ms > ml) & (ms.shift() < ml.shift())
    return buy

def crossunder(ms, ml):
    sell = (ms < ml) & (ms.shift() > ml.shift())
    return sell
def datas(symbols):
    return {symbol: pbt.load_from_yahoo(symbol+'.ns', start='2014') for symbol in symbols}
##########
def sma_cross(ohlc, period_small = 5, period_long = 10):
    ms = pd.rolling_mean(ohlc.C, period_small)
    ml = pd.rolling_mean(ohlc.C, period_long)
    buy = cover =(ms > ml) & (ms.shift() < ml.shift())
    sell = short =(ms < ml) & (ms.shift() > ml.shift())
    # bt = pbt.Backtest(locals(), "Sma Crossover")
    return locals()

def ema_cross(ohlc, period_small = 5, period_long = 10):
    ms = e.expon_moving_avg(ohlc.C, period_small)
    ml = e.expon_moving_avg(ohlc.C, period_long)
    buy = cover =(ms > ml) & (ms.shift() < ml.shift())
    sell = short =(ms < ml) & (ms.shift() > ml.shift())
    return locals()

def wma_ccross(ohlc, period_small = 5, period_long = 10):
    import wma as w
    ms = w.weighted_moving_average(ohlc.C, period_small)
    ml = w.weighted_moving_average(ohlc.C, period_long)
    buy = cover =(ms > ml) & (ms.shift() < ml.shift())
    sell = short =(ms < ml) & (ms.shift() > ml.shift())
    return locals()

def dema_cross(ohlc, period_small = 5, period_long = 10):
    import dema as d
    ms = d.double_exponential_moving_average(ohlc.C, period_small)
    ml = d.double_exponential_moving_average(ohlc.C, period_long)
    buy = cover =(ms > ml) & (ms.shift() < ml.shift())
    sell = short =(ms < ml) & (ms.shift() > ml.shift())
    # bt = pbt.Backtest(locals(), "Dema Crossover")
    return locals()

def tema_cross(ohlc, period_small = 5, period_long = 10):

    ms = t.expon_moving_avg(ohlc.C, period_small)
    ml = t.expon_moving_avg(ohlc.C, period_long)
    buy = cover =(ms > ml) & (ms.shift() < ml.shift())
    sell = short =(ms < ml) & (ms.shift() > ml.shift())
    # bt = pbt.Backtest(locals(), "Dema Crossover")
    return locals()

def supertrand(ohlc, period_small = 5, multiplier = 3):
    import supertrand as s
    moving_small = s.supertrand(ohlc, period_small, multiplier)
    buy = cover = (ohlc.C > moving_small) & (ohlc.C.shift() < moving_small.shift())
    sell = short = (ohlc.C < moving_small) & (ohlc.C.shift() > moving_small.shift())
    # bt = pbt.Backtest(locals(),"Supertrand")
    return locals()

def chandevidya(ohlc, period = 9):
    import chande_vidya as cv
    moving_small = cv.chande_vidya(ohlc.C, period)
    buy = cover = (ohlc.C > moving_small) & (ohlc.C.shift() < moving_small.shift())
    sell = short = (ohlc.C < moving_small) & (ohlc.C.shift() > moving_small.shift())
    # bt = pbt.Backtest(locals(), "Chande Vidya")
    return locals()

def trix(ohlc, trix_period = 10, avg_period = 9):
    import trix as t
    ms = t.trix(ohlc.C, trix_period)
    ml = pd.rolling_mean(ms, avg_period)
    buy = cover =(ms > ml) & (ms.shift() < ml.shift())
    sell = short =(ms < ml) & (ms.shift() > ml.shift())
    # bt = pbt.Backtest(locals(), "Trix Crossover")
    return locals()

def macd(ohlc, small_ema = 12, long_ema = 24, avg_period = 9):
    ms = m.macd(ohlc.C, small_ema, long_ema)
    ml = pd.rolling_mean(ms, avg_period)
    buy = cover =(ms > ml) & (ms.shift() < ml.shift())
    sell = short =(ms < ml) & (ms.shift() > ml.shift())
    # bt = pbt.Backtest(locals(), "MACD Crossover")
    return locals()

def rsi_cross(ohlc, rsi_period = 14, avg_period = 9):
    ms = r.rsi(ohlc.C, rsi_period)
    ml = pd.rolling_mean(ms, avg_period)
    buy = cover =(ms > ml) & (ms.shift() < ml.shift())
    sell = short =(ms < ml) & (ms.shift() > ml.shift())
    # bt = pbt.Backtest(locals(), "RSI Crossover")
    return locals()

def macd_rsi(ohlc, small_ema = 50, long_ema = 100, avg_period = 9, rsi_period = 14):
    macd = m.macd(ohlc.C, small_ema, long_ema)
    rsi = r.rsi(ohlc.C, rsi_period)



strategies = [sma_cross, ema_cross, wma_ccross, dema_cross, tema_cross, supertrand, chandevidya,trix, macd, rsi_cross]
# def apply(strategies = strategies):
#     final_dict = {}
#     nifty_all = pd.read_csv('/home/sigmasoft6/Desktop/indicator/nifty_all.csv')
#     data = dict(zip(nifty_all['Symbol'], nifty_all['Company']))
#     all_scripts = datas(data.keys())
#     for strategy in strategies:
#         final_dict.update({strategy.__name__: [{scrip:strategy(all_scripts[scrip]).report['performance']['profit']} for scrip in all_scripts]})
#     return final_dict
#
# def sort_by_scripts(strategies):
#     final_dict = {}
#     nifty_all = pd.read_csv('/home/sigmasoft6/Desktop/indicator/nifty_all.csv')
#     data = dict(zip(nifty_all['Symbol'], nifty_all['Company']))
#     all_scripts = datas(data.keys()[12:25])
#     for script in all_scripts:
#         final_dict.update({script:[{stgy.__name__: stgy(all_scripts[script]).report['performance']['profit']} for stgy in strategies]})
#     return final_dict
#########################

# nifty_all = pd.read_csv('/home/sigmasoft6/Desktop/indicator/nifty_all.csv')
# data = dict(zip(nifty_all['Symbol'], nifty_all['Company']))
# all_scripts = datas(data.keys()[9:10])
# bt = pbt.Backtest(ema_cross(all_scripts['KOTAKBANK']), 'ema cross')
# # print bt.report
# # print all_scripts
# if 'performance' in bt.report:
#    print bt.report['performance']
# else:
#     print "none"
a = [1,2,3,4,5]
print map(lambda x: x, a)