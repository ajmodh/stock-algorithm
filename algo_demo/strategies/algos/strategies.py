import pandas as pd
from . import ema
from . import wma
from . import dema
from . import tema
from . import supertrend
from . import chande_vidya
from . import trix
from . import macd
from . import rsi

def crossover(ms, ml):
    buy = (ms > ml) & (ms.shift() < ml.shift())
    return buy

def crossunder(ms, ml):
    sell = (ms < ml) & (ms.shift() > ml.shift())
    return sell

def sma_cross(ohlc, period_small = 5, period_long = 10):
    ms = pd.rolling_mean(ohlc.C, period_small)
    ml = pd.rolling_mean(ohlc.C, period_long)
    buy = cover = crossover(ms, ml)
    sell = short = crossunder(ms, ml)
    return locals()

def ema_cross(ohlc, period_small = 5, period_long = 10):
    ms = ema.expon_moving_avg(ohlc.C, period_small)
    ml = ema.expon_moving_avg(ohlc.C, period_long)
    buy = cover = crossover(ms, ml)
    sell = short = crossunder(ms, ml)
    return locals()

def wma_cross(ohlc, period_small = 5, period_long = 10):
    ms = wma.weighted_moving_average(ohlc.C, period_small)
    ml = wma.weighted_moving_average(ohlc.C, period_long)
    buy = cover = crossover(ms, ml)
    sell = short = crossunder(ms, ml)
    return locals()

def dema_cross(ohlc, period_small = 5, period_long = 10):
    ms = dema.double_exponential_moving_average(ohlc.C, period_small)
    ml = dema.double_exponential_moving_average(ohlc.C, period_long)
    buy = cover = crossover(ms, ml)
    sell = short = crossunder(ms, ml)
    return locals()

def tema_cross(ohlc, period_small = 5, period_long = 10):
    ms = tema.expon_moving_avg(ohlc.C, period_small)
    ml = tema.expon_moving_avg(ohlc.C, period_long)
    buy = cover = crossover(ms, ml)
    sell = short = crossunder(ms, ml)
    return locals()

def supertrend_cross(ohlc, period_small = 5, multiplier = 3):
    ml = supertrend.supertrand(ohlc, period_small, multiplier)
    buy = cover = crossover(ohlc.C, ml)
    sell = short = crossunder(ohlc.C, ml)
    return locals()

def chandevidya(ohlc, period = 9):
    ml = chande_vidya.chande_vidya(ohlc.C, period)
    buy = cover = crossover(ohlc.C, ml)
    sell = short = crossunder(ohlc.C, ml)
    return locals()

def trix_cross(ohlc, trix_period = 10, avg_period = 9):
    ms = trix.trix(ohlc.C, trix_period)
    ml = pd.rolling_mean(ms, avg_period)
    buy = cover = crossover(ms, ml)
    sell = short = crossunder(ms, ml)
    return locals()

def macd_cross(ohlc, small_ema = 12, long_ema = 24, avg_period = 9):
    ms = macd.macd(ohlc.C, small_ema, long_ema)
    ml = pd.rolling_mean(ms, avg_period)
    buy = cover = crossover(ms, ml)
    sell = short = crossunder(ms, ml)
    return locals()

def rsi_cross(ohlc, rsi_period = 14, avg_period = 9):
    ms = rsi.rsi(ohlc.C, rsi_period)
    ml = pd.rolling_mean(ms, avg_period)
    buy = cover = crossover(ms, ml)
    sell = short = crossunder(ms, ml)
    return locals()
