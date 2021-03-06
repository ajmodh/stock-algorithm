import sys
import ema as e
sys.setrecursionlimit(10000)

def smoothing_const(days):
     return (2.0 / (days + 1))

def expon_moving_avg(list_close, period):
    ema = e.expon_moving_avg(list_close, period)
    ema_of_ema = e.expon_moving_avg(ema, period)
    ema_of_ema_of_ema = e.expon_moving_avg(ema_of_ema, period)
    tema = (3 * ema) - (3 * ema_of_ema) + ema_of_ema_of_ema
    return tema

