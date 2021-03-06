import sys
import pandas
import pybacktest
import ema as e

def trix(close, period):
    ema = e.expon_moving_avg(close, period)
    double_smooth = e.expon_moving_avg(ema, period)
    triple_smooth = e.expon_moving_avg(double_smooth, period)
    change =  (triple_smooth - triple_smooth.shift())/triple_smooth.shift()*100
    return change