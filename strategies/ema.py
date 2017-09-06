import sys
sys.setrecursionlimit(10000)
import pandas

def smoothing_const(days):
     return (2.0 / (days + 1))

def expon_mov_value(price, ema, index, period):
    if index <= len(price) -1:
        ema[int(index)] = smoothing_const(period) * (price[index] - ema[index - 1]) + ema[index - 1]
        expon_mov_value(price, ema, index + 1, period)
    return ema

def expon_moving_avg(price, period):
    ema = pandas.rolling_mean(price, period)
    count = price.isnull().sum()
    ema = expon_mov_value(price, ema, count + period, period)
    return ema